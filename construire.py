# -*- coding: utf-8 -*-
"""Fabrique le site des process NarratiFluent à partir des fichiers markdown.

Le principe tient en une phrase : **la source est le markdown, le site n'en est
que l'affichage**. Si demain ce générateur disparaît, il reste des fichiers
texte lisibles, versionnés, que n'importe qui peut reprendre. C'est ce qui
rend le dispositif tenable sur la durée, et c'est la raison d'être de ce choix.

    python3 construire.py

Lit `contenu/`, écrit `site/`. Chaque fichier `.md` devient une page, et la
première ligne de titre (`# …`) donne son nom dans le sommaire. Le classement
suit le préfixe numérique du nom de fichier, qui ne s'affiche jamais.

Le site sort en **noindex** : il est accessible à qui a le lien, mais n'apparaît
dans aucun moteur de recherche.
"""
import datetime
import html
import pathlib
import re
import shutil

import markdown

RACINE = pathlib.Path(__file__).parent
CONTENU = RACINE / 'contenu'
SORTIE = RACINE / 'site'
MODELE = RACINE / 'modele'

TITRE_SITE = 'Process NarratiFluent'

# Le nom d'un dossier ne porte ni accent ni apostrophe : l'étiquette affichée se
# déclare ici quand la transformation mécanique ne suffit pas.
ETIQUETTES = {
    '05-les-regles': 'Les règles',
    '01-process': "Process création d'ads",
}

# **Le site se rafraîchit tout seul, et il le faut.** GitHub Pages envoie
# `cache-control: max-age=600` et ne laisse pas changer cet en-tête : le
# navigateur garde donc chaque page dix minutes, et un rechargement normal
# ressert la version périmée. Sur une documentation qu'on corrige plusieurs fois
# par jour, c'est intenable — Adrien voyait ses corrections « ne rien faire ».
#
# Chaque page porte donc l'empreinte de sa construction et va lire `version.txt`
# au chargement, sans cache. Si l'empreinte a changé, elle se recharge une fois.
VERSION = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')

# **Le lien de retour ne figure pas sur toutes les pages.** Il n'a de sens que
# sur une page à laquelle le process renvoie : ni l'accueil ni le process
# lui-même n'ont à proposer d'y revenir.
RETOUR = ('<p class="retour-chaine"><a href="{base}process/process-creation-d-ads.html">'
          "← Revenir au process création d'ads</a></p>")


def _retour(page, base, accueil):
    if page is accueil or page['lien'].startswith('process/'):
        return ''
    return RETOUR.format(base=base)


RAFRAICHIR = """<script>
(function(){
  var ici = "__VERSION__";
  // **On revérifie quand l'onglet revient au premier plan.** La vérification au
  // seul chargement ne couvrait pas le cas le plus fréquent : un onglet laissé
  // ouvert pendant qu'on republie. Adrien regardait une page vieille d'une heure
  // en croyant que la correction n'avait pas été faite.
  function verifier(){
    if (sessionStorage.getItem('np-recharge') === ici) return;
    fetch("__BASE__version.txt", {cache: 'no-store'})
      .then(function(r){ return r.ok ? r.text() : null; })
      .then(function(v){
        if (!v) return;
        v = v.trim();
        if (v && v !== ici) {
          sessionStorage.setItem('np-recharge', v);
          location.replace(location.pathname + '?v=' + v + location.hash);
        }
      })
      .catch(function(){});
  }
  verifier();
  document.addEventListener('visibilitychange', function(){
    if (!document.hidden) verifier();
  });
  window.addEventListener('focus', verifier);
})();
</script>"""


def _lire(chemin):
    """Le titre, le chapô et le corps d'un fichier de contenu."""
    texte = chemin.read_text(encoding='utf-8')
    titre = 'Sans titre'
    m = re.search(r'^#\s+(.+)$', texte, re.M)
    if m:
        titre = m.group(1).strip()
        texte = texte[:m.start()] + texte[m.end():]
    # **Le chapô ne se ramasse que juste sous le titre.** Une citation placée au
    # milieu d'une fiche commence elle aussi par `>` : la chercher partout
    # remontait un verbatim d'avatar en résumé de page, et le retirait du corps.
    chapo = ''
    m = re.match(r'\s*((?:>[^\n]*\n?)+)', texte)
    if m:
        chapo = ' '.join(l.lstrip('> ').strip() for l in m.group(1).splitlines()).strip()
        texte = texte[m.end():]
    return titre, chapo, texte.strip()


def _resume(page, limite=135):
    """La phrase qui accompagne une fiche sur sa carte.

    Le chapô quand il existe ; sinon la première phrase du document. Aucune
    fiche n'a donc à être annotée pour apparaître correctement dans une grille —
    c'est ce qui permet de publier le socle tel quel, sans le dédoubler.
    """
    t = page['chapo']
    if not t and not page.get('brut'):
        m = re.search(r'^(?!#|>|\||-|\*\s|\d+\.)(.+?)(?:\n\s*\n|\Z)',
                      page['corps'], re.S | re.M)
        t = ' '.join(m.group(1).split()) if m else ''
    t = re.sub(r'[*_`]', '', t)
    t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
    if len(t) > limite:
        coupe = t[:limite]
        t = coupe[:coupe.rfind(' ')] + '…' if ' ' in coupe else coupe + '…'
    return t


PLIER_AU_DELA = 90          # lignes : en dessous, la fiche se lit d'un trait
PLIER_AU_DELA_SECTIONS = 5  # ou dès qu'elle a trop de chapitres pour tenir à l'écran


def _volets(corps, plier):
    """Chaque `##` devient un volet qu'on ouvre et qu'on referme.

    **Une procédure longue ne se lit pas d'un bloc.** Adrien : « des fois les
    procédures sont longues donc il faut pouvoir les plier, déplier si on veut ».
    Le découpage suit les titres de niveau 2, qui sont déjà les chapitres du
    document — rien à baliser dans le markdown, les fiches restent du texte
    ordinaire, lisible sans le site.

    Sur une fiche courte, `plier` est faux : tout reste ouvert, et l'affichage
    ne change pas. Sur une fiche longue, seul le premier chapitre s'ouvre.
    """
    morceaux = re.split(r'(?=<h2[ >])', corps)
    if len(morceaux) < 2:
        return corps, False
    out = [morceaux[0]]
    for i, bloc in enumerate(morceaux[1:]):
        m = re.match(r'<h2([^>]*)>(.*?)</h2>(.*)', bloc, re.S)
        if not m:
            out.append(bloc)
            continue
        attrs, titre, reste = m.groups()
        ouvert = '' if (plier and i) else ' open'
        out.append(
            f'<details class="volet"{attrs}{ouvert}>'
            f'<summary><span class="volet-titre">{titre}</span></summary>'
            f'<div class="volet-corps">{reste}</div></details>')
    barre = ('<div class="volets-barre">'
             '<button type="button" class="volets-tout" data-volets>'
             f'{"Tout déplier" if plier else "Tout replier"}</button></div>')
    return barre + ''.join(out), True


def _cartes(pages, dossier, base):
    """La grille de fiches cliquables d'une section.

    C'est ce qu'Adrien appelle « le côté Notion » : une section n'est pas une
    liste de liens dans une barre latérale, c'est un jeu de fiches qu'on voit
    d'un coup d'œil, avec leur titre et ce qu'elles contiennent.
    """
    out = ['<div class="cartes">']
    for p in pages:
        if p['section'] != dossier:
            continue
        out.append(
            f'<a class="carte" href="{base}{p["lien"]}">'
            f'<span class="carte-titre">{html.escape(p["titre"])}</span>'
            f'<span class="carte-chapo">{html.escape(_resume(p))}</span></a>')
    out.append('</div>')
    return ''.join(out)


def _section(chemin):
    """La section d'une page, déduite du dossier qui la contient."""
    rel = chemin.relative_to(CONTENU)
    return rel.parts[0] if len(rel.parts) > 1 else ''


def _lien(chemin):
    rel = chemin.relative_to(CONTENU).with_suffix('.html')
    return '/'.join(re.sub(r'^\d+[-_]', '', p) for p in rel.parts)


def _pages():
    """Les pages du site — markdown, plus les pages HTML servies telles quelles.

    **Une page peut être écrite directement en HTML.** Certaines vues ne se
    réduisent pas à du texte : une chaîne de production se lit mieux dépliable,
    avec un filtre par format et des étapes qu'on ouvre une à une. Le markdown
    ne sait pas faire ça, et le forcer donnerait une page moins claire. Ces
    pages-là portent leur propre mise en page et sont recopiées sans être
    touchées — le générateur ne leur ajoute que leur entrée au sommaire.
    """
    pages = []
    for f in sorted(list(CONTENU.rglob('*.md')) + list(CONTENU.rglob('*.html'))):
        if f.suffix == '.html':
            texte = f.read_text(encoding='utf-8')
            m = re.search(r'<title>(.*?)</title>', texte, re.S)
            titre = (m.group(1).strip() if m else f.stem)
            # Une page entière n'a pas de chapô markdown : elle le déclare en
            # `<meta name="resume">`, faute de quoi sa carte n'aurait qu'un titre.
            r = re.search(r'<meta name="resume" content="(.*?)"', texte, re.S)
            pages.append({'fichier': f, 'titre': titre,
                          'chapo': html.unescape(r.group(1).strip()) if r else '', 'corps': texte,
                          'lien': _lien(f), 'section': _section(f), 'brut': True})
            continue
        titre, chapo, corps = _lire(f)
        pages.append({'fichier': f, 'titre': titre, 'chapo': chapo, 'corps': corps,
                      'lien': _lien(f), 'section': _section(f), 'brut': False})
    return sorted(pages, key=lambda p: str(p['fichier']))


def _base(page):
    """Le préfixe relatif qui ramène à la racine du site.

    **Les chemins sont relatifs, et c'est délibéré.** Un chemin absolu (`/site.css`)
    suppose que le site vit à la racine du domaine — vrai sur
    `process.narratifluent.com`, faux sur `adrienstr00.github.io/np-docs/`, où
    il pointe à côté et laisse la page sans style. Des chemins relatifs
    fonctionnent aux deux endroits sans réglage, et survivront au déménagement.
    """
    return '../' * (page['lien'].count('/')) or './'


def _sommaire(pages, base, courante=None):
    """Le sommaire : les entrées principales visibles, les listes repliées.

    **Adrien ne veut pas cinquante fiches sous les yeux en permanence.** Une
    section d'une seule page — le process lui-même — s'affiche comme un lien
    direct ; une section qui en contient plusieurs devient un volet replié, qui
    ne s'ouvre que si on le demande ou si la page courante s'y trouve.
    """
    sections, ordre = {}, []
    for p in pages[1:]:
        s = p['section'] or 'Général'
        if s not in sections:
            sections[s] = []
            ordre.append(s)
        sections[s].append(p)
    out = []
    for s in ordre:
        pages_s = sections[s]
        nom = html.escape(ETIQUETTES.get(s) or
                          re.sub(r'^\d+[-_]', '', s).replace('-', ' ').capitalize())
        ici = courante and any(p['lien'] == courante for p in pages_s)
        # une seule page : elle EST la section, et son titre sert d'étiquette
        if len(pages_s) == 1:
            p0 = pages_s[0]
            actif = ' class="actif"' if courante == p0['lien'] else ''
            out.append(f'<a class="entree" href="{base}{p0["lien"]}"{actif}>'
                       f'{html.escape(p0["titre"])}</a>')
            continue
        out.append(f'<details class="groupe"{" open" if ici else ""}>'
                   f'<summary class="groupe-nom">{nom}</summary><ul>')
        for p in pages_s:
            actif = ' class="actif"' if courante and p['lien'] == courante else ''
            out.append(f'<li><a href="{base}{p["lien"]}"{actif}>'
                       f'{html.escape(p["titre"])}</a></li>')
        out.append('</ul></details>')
    return '\n'.join(out)


def _fichiers_annexes():
    for f in MODELE.glob('*.css'):
        shutil.copy(f, SORTIE / f.name)
    (SORTIE / 'version.txt').write_text(VERSION + '\n', encoding='utf-8')
    # `noindex` : le site est accessible à qui a le lien, invisible des moteurs.
    (SORTIE / 'robots.txt').write_text('User-agent: *\nDisallow: /\n', encoding='utf-8')
    # GitHub Pages sert le site tel quel, sans passer par Jekyll.
    (SORTIE / '.nojekyll').write_text('', encoding='utf-8')


def construire():
    if SORTIE.exists():
        shutil.rmtree(SORTIE)
    SORTIE.mkdir()
    gabarit = (MODELE / 'page.html').read_text(encoding='utf-8')
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list', 'toc'])
    pages = _pages()
    if not pages:
        raise SystemExit('aucun fichier dans contenu/')

    for p in pages:
        cible = SORTIE / p['lien']
        cible.parent.mkdir(parents=True, exist_ok=True)
        base = _base(p)
        if p['brut']:
            cible.write_text(p['corps']
                             .replace('{{BASE}}', base)
                             .replace('{{VERSION}}', VERSION)
                             .replace('{{RAFRAICHIR}}', RAFRAICHIR.replace('__VERSION__', VERSION)
                                      .replace('__BASE__', base))
                             .replace('{{SOMMAIRE}}', _sommaire(pages, base, p['lien'])),
                             encoding='utf-8')
            print(f'  {p["lien"]:44} {p["titre"]}  (page entière)')
            continue
        md.reset()
        corps = md.convert(p['corps'])
        corps = re.sub(r'\{\{CARTES:([^}]+)\}\}',
                       lambda m: _cartes(pages, m.group(1), base), corps)
        lignes = p['corps'].count(chr(10))
        corps, _ = _volets(corps, lignes > PLIER_AU_DELA
                           or corps.count('<h2') > PLIER_AU_DELA_SECTIONS)
        cible.write_text(gabarit
                         .replace('{{BASE}}', base)
                         .replace('{{VERSION}}', VERSION)
                         .replace('{{RAFRAICHIR}}', RAFRAICHIR.replace('__VERSION__', VERSION)
                                  .replace('__BASE__', base))
                         .replace('{{TITRE}}', html.escape(p['titre']))
                         .replace('{{TITRE_SITE}}', TITRE_SITE)
                         .replace('{{CHAPO}}', html.escape(p['chapo']))
                         .replace('{{SOMMAIRE}}', _sommaire(pages, base, p['lien']))
                         .replace('{{RETOUR}}', _retour(p, base, pages[0]))
                         .replace('{{CORPS}}', corps),
                         encoding='utf-8')
        print(f'  {p["lien"]:44} {p["titre"]}')

    # **La page d'accueil se régénère, elle ne se recopie pas.** Une copie d'une
    # page rangée dans un sous-dossier garderait ses chemins relatifs — `../` de
    # trop — et arriverait à la racine sans style et sans liens.
    a = pages[0]
    if a['brut']:
        (SORTIE / 'index.html').write_text(a['corps']
            .replace('{{BASE}}', './')
            .replace('{{VERSION}}', VERSION)
            .replace('{{RAFRAICHIR}}', RAFRAICHIR.replace('__VERSION__', VERSION)
                     .replace('__BASE__', './'))
            .replace('{{SOMMAIRE}}', _sommaire(pages, './', a['lien'])), encoding='utf-8')
        _fichiers_annexes()
        print(f'\n{len(pages)} pages → {SORTIE}')
        return
    md.reset()
    accueil = re.sub(r'\{\{CARTES:([^}]+)\}\}',
                     lambda m: _cartes(pages, m.group(1), './'), md.convert(a['corps']))
    (SORTIE / 'index.html').write_text(gabarit
        .replace('{{BASE}}', './')
        .replace('{{VERSION}}', VERSION)
        .replace('{{RAFRAICHIR}}', RAFRAICHIR.replace('__VERSION__', VERSION)
                 .replace('__BASE__', './'))
        .replace('{{TITRE}}', html.escape(a['titre']))
        .replace('{{TITRE_SITE}}', TITRE_SITE)
        .replace('{{CHAPO}}', html.escape(a['chapo']))
        .replace('{{SOMMAIRE}}', _sommaire(pages, './', a['lien']))
        .replace('{{RETOUR}}', '')
        .replace('{{CORPS}}', accueil), encoding='utf-8')

    _fichiers_annexes()
    print(f'\n{len(pages)} pages → {SORTIE}')


if __name__ == '__main__':
    construire()
