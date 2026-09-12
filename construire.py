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


def _lire(chemin):
    """Le titre, le chapô et le corps d'un fichier de contenu."""
    texte = chemin.read_text(encoding='utf-8')
    titre = 'Sans titre'
    m = re.search(r'^#\s+(.+)$', texte, re.M)
    if m:
        titre = m.group(1).strip()
        texte = texte[:m.start()] + texte[m.end():]
    chapo = ''
    m = re.search(r'^>\s+(.+)$', texte, re.M)
    if m:
        chapo = m.group(1).strip()
        texte = texte[:m.start()] + texte[m.end():]
    return titre, chapo, texte.strip()


def _section(chemin):
    """La section d'une page, déduite du dossier qui la contient."""
    rel = chemin.relative_to(CONTENU)
    return rel.parts[0] if len(rel.parts) > 1 else ''


def _lien(chemin):
    rel = chemin.relative_to(CONTENU).with_suffix('.html')
    return '/'.join(re.sub(r'^\d+[-_]', '', p) for p in rel.parts)


def _pages():
    pages = []
    for f in sorted(CONTENU.rglob('*.md')):
        titre, chapo, corps = _lire(f)
        pages.append({'fichier': f, 'titre': titre, 'chapo': chapo, 'corps': corps,
                      'lien': _lien(f), 'section': _section(f)})
    return pages


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
    """Le sommaire, groupé par section, dans l'ordre des noms de fichiers."""
    sections, ordre = {}, []
    for p in pages:
        s = p['section'] or 'Général'
        if s not in sections:
            sections[s] = []
            ordre.append(s)
        sections[s].append(p)
    out = []
    for s in ordre:
        nom = html.escape(re.sub(r'^\d+[-_]', '', s).replace('-', ' ').capitalize())
        out.append(f'<div class="groupe"><span class="groupe-nom">{nom}</span><ul>')
        for p in sections[s]:
            actif = ' class="actif"' if courante and p['lien'] == courante else ''
            out.append(f'<li><a href="{base}{p["lien"]}"{actif}>{html.escape(p["titre"])}</a></li>')
        out.append('</ul></div>')
    return '\n'.join(out)


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
        md.reset()
        corps = md.convert(p['corps'])
        cible = SORTIE / p['lien']
        cible.parent.mkdir(parents=True, exist_ok=True)
        base = _base(p)
        cible.write_text(gabarit
                         .replace('{{BASE}}', base)
                         .replace('{{TITRE}}', html.escape(p['titre']))
                         .replace('{{TITRE_SITE}}', TITRE_SITE)
                         .replace('{{CHAPO}}', html.escape(p['chapo']))
                         .replace('{{SOMMAIRE}}', _sommaire(pages, base, p['lien']))
                         .replace('{{CORPS}}', corps),
                         encoding='utf-8')
        print(f'  {p["lien"]:44} {p["titre"]}')

    # **La page d'accueil se régénère, elle ne se recopie pas.** Une copie d'une
    # page rangée dans un sous-dossier garderait ses chemins relatifs — `../` de
    # trop — et arriverait à la racine sans style et sans liens.
    a = pages[0]
    md.reset()
    (SORTIE / 'index.html').write_text(gabarit
        .replace('{{BASE}}', './')
        .replace('{{TITRE}}', html.escape(a['titre']))
        .replace('{{TITRE_SITE}}', TITRE_SITE)
        .replace('{{CHAPO}}', html.escape(a['chapo']))
        .replace('{{SOMMAIRE}}', _sommaire(pages, './', a['lien']))
        .replace('{{CORPS}}', md.convert(a['corps'])), encoding='utf-8')

    for f in MODELE.glob('*.css'):
        shutil.copy(f, SORTIE / f.name)
    # `noindex` : le site est accessible à qui a le lien, invisible des moteurs.
    (SORTIE / 'robots.txt').write_text('User-agent: *\nDisallow: /\n', encoding='utf-8')
    # GitHub Pages sert le site tel quel, sans passer par Jekyll.
    (SORTIE / '.nojekyll').write_text('', encoding='utf-8')
    print(f'\n{len(pages)} pages → {SORTIE}')


if __name__ == '__main__':
    construire()
