# -*- coding: utf-8 -*-
"""Recopie dans `contenu/` les documents de méthode du dépôt privé.

    python3 publier_socle.py

**Rien n'est publié qui ne soit nommé ici.** Le dépôt privé contient aussi les
matrices avatar, les CPA, le stock de hooks et l'infrastructure : le jour où ces
fichiers sont partis sur un site public, il a fallu supprimer le dépôt entier
pour les retirer — un historique git réécrit laisse les anciens commits
accessibles par leur empreinte. La liste blanche ci-dessous est donc le seul
mécanisme d'autorisation : un fichier absent de cette liste ne part pas.

Second garde-fou, mécanique lui aussi : **les identifiants sont masqués à la
copie**. Une voix ElevenLabs ou un avatar Argil se désigne par une clé qui pointe
dans le compte d'Adrien. Le nom du personnage et ses réglages disent tout ce
qu'il faut pour rejouer un casting ; la clé, elle, reste dans le dépôt privé.
"""
import pathlib
import re
import sys

SOURCE = pathlib.Path('/Users/adrienvaysset/Desktop/Projets Claude/process ads NarratiFluent')
CONTENU = pathlib.Path(__file__).parent / 'contenu'

# chemin dans le dépôt privé  →  destination dans le site
PUBLIABLES = {
    '00-SOCLE/production/chaine-de-production.md':        '03-les-fiches/05-chaine-technique.md',
    '00-SOCLE/anatomie-d-un-script.md':                   '03-les-fiches/10-anatomie-d-un-script.md',
    '00-SOCLE/modele-adcopy.md':                          '03-les-fiches/15-modele-adcopy.md',
    '00-SOCLE/formats.md':                                '03-les-fiches/20-formats-de-crea.md',
    '00-SOCLE/typologie-hooks.md':                        '03-les-fiches/25-typologie-des-hooks.md',
    '00-SOCLE/production/faire-sonner-une-voix-vraie.md': '03-les-fiches/30-faire-sonner-une-voix.md',
    '00-SOCLE/production/castings-valides.md':            '03-les-fiches/35-rex-casting-valide.md',
    '00-SOCLE/production/choisir-un-visage.md':           '03-les-fiches/40-choisir-un-visage.md',
    '00-SOCLE/production/format-micro-trottoir.md':       '03-les-fiches/45-micro-trottoir.md',
    '00-SOCLE/production/tournage-d-adrien.md':           '03-les-fiches/50-tournage-d-adrien.md',
    '00-SOCLE/production/avant-le-rendu.md':              '03-les-fiches/55-planche-des-plans.md',
    '00-SOCLE/production/mouvements-de-camera.md':        '03-les-fiches/60-mouvements-d-appareil.md',
    '00-SOCLE/production/dynamiser-le-montage.md':        '03-les-fiches/65-dynamiser-le-montage.md',
    '00-SOCLE/production/sous-titres.md':                 '03-les-fiches/70-sous-titres.md',
    '00-SOCLE/production/ecrans-de-fin.md':               '03-les-fiches/75-ecrans-de-fin.md',
    '00-SOCLE/production/regles-de-son-par-format.md':    '03-les-fiches/80-regles-de-son.md',
    '00-SOCLE/production/formats-de-livraison.md':        '03-les-fiches/85-formats-de-livraison.md',
    '00-SOCLE/production/avant-de-livrer.md':             '03-les-fiches/90-avant-de-livrer.md',
    '00-SOCLE/production/boucle-de-validation.md':        '05-les-regles/10-boucle-de-validation.md',
    '00-SOCLE/anti-patterns.md':                          '05-les-regles/20-anti-patterns.md',
    '00-SOCLE/copy-checklist.md':                         '05-les-regles/30-copy-ads-checklist.md',
    '00-SOCLE/compliance-meta.md':                        '05-les-regles/40-compliance-meta.md',
    '.claude/skills/rediger-ads/SKILL.md':                '06-documents-annexes/20-skill-rediger.md',
    '.claude/skills/produire-ads/SKILL.md':               '06-documents-annexes/30-skill-produire.md',
    '.claude/skills/generer-hooks/SKILL.md':              '06-documents-annexes/40-skill-hooks.md',
}

MASQUES = (
    # identifiants de voix ElevenLabs et d'avatars Argil
    (re.compile(r'\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b'), '⟨identifiant privé⟩'),
    (re.compile(r'\b(?=[A-Za-z0-9]{20}\b)(?=[A-Za-z0-9]*[a-z])(?=[A-Za-z0-9]*[A-Z])[A-Za-z0-9]{20}\b'), '⟨identifiant privé⟩'),
    # identifiants de documents Google, adresses, adresses IP
    (re.compile(r'(docs\.google\.com/[a-z]+/d/)[A-Za-z0-9_-]{20,}'), r'\1⟨privé⟩'),
    (re.compile(r'\b[\w.%-]+@[\w.-]+\.[A-Za-z]{2,}\b'), '⟨adresse privée⟩'),
    (re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b'), '⟨adresse privée⟩'),
)


def masquer(texte):
    for motif, remplacement in MASQUES:
        texte = motif.sub(remplacement, texte)
    return texte


def publier():
    masques, manquants = 0, []
    for src, dst in PUBLIABLES.items():
        f = SOURCE / src
        if not f.exists():
            manquants.append(src)
            continue
        texte = f.read_text(encoding='utf-8')
        propre = masquer(texte)
        n = sum(1 for a, b in zip(texte.split('\n'), propre.split('\n')) if a != b)
        masques += n
        cible = CONTENU / dst
        cible.parent.mkdir(parents=True, exist_ok=True)
        cible.write_text(propre, encoding='utf-8')
        print(f'  {dst:46} {"← " + str(n) + " ligne(s) masquée(s)" if n else ""}')
    if manquants:
        print('\nintrouvables : ' + ', '.join(manquants), file=sys.stderr)
    print(f'\n{len(PUBLIABLES) - len(manquants)} documents copiés, {masques} lignes masquées')
    return 1 if manquants else 0


if __name__ == '__main__':
    raise SystemExit(publier())
