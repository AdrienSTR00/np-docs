# Les scripts du funnel

> Les cinq commandes qui portent la chaîne, et ce que chacune attrape.

Toutes se lancent depuis la racine du dépôt.

## Créer le document de préparation

```bash
python3 05-FUNNEL/00-METHODE/scripts/creer_preparation.py "NarratiFluent" 4
```

Dépose un document de préparation **à trous** : les intitulés d'étape, les questions en puces, deux
lignes vides sous chacune, et un saut de page devant chaque titre d'étape sauf le premier.

- `--gabarit` affiche le contenu sans rien écrire.
- `--sauts-de-page <doc_id>` pose les sauts manquants sur un document existant, sans en empiler.
- `--refaire <doc_id>` repose le socle sur un document existant sans changer son URL, **et efface tout ce qui y avait été rempli**.

## Remplir la préparation

```bash
python3 05-FUNNEL/00-METHODE/scripts/remplir_preparation.py <doc_id> "Quelle est la promesse" "..."
python3 05-FUNNEL/00-METHODE/scripts/remplir_preparation.py <doc_id> --lire
```

Écrit une réponse sous sa question, en appliquant la mise en page. Le script **refuse d'écraser une
réponse déjà écrite** ; `--remplacer` la réécrit. `--markdown` accepte une réponse rédigée en
markdown et rend les titres, les puces, le gras et l'italique, en recollant les lignes repliées pour
qu'aucune phrase n'arrive coupée en deux.

## Contrôler la cohérence avec l'avatar

```bash
python3 05-FUNNEL/00-METHODE/scripts/controler_avatar.py <texte.md> <n° avatar>
```

Compare les mots du texte à ceux de la matrice de l'avatar : mots hors registre, mots interdits, et
mots du segment absents du texte. Se lance **à chaque livraison et après chaque fignolage**, sans
attendre qu'on le demande.

## Mesurer une passe de fignolage

```bash
python3 05-FUNNEL/00-METHODE/scripts/mesurer_fignolage.py avant.md apres.md
```

Donne l'écart en mots, la médiane de phrase, le nombre de phrases de plus de 30 mots et le nombre de
phrases. `--sauf 13,15,23` exclut les sections où des emplacements de preuve ont été remplacés dans
la même passe, qui fausseraient le taux.

```bash
python3 05-FUNNEL/00-METHODE/scripts/mesurer_fignolage.py texte.md --notes
```

Signale les notes de travail encore présentes : emplacements entre crochets, mentions de preuve,
variables de gabarit non remplacées, listes de preuves à produire. **Aucune ne doit survivre au
dépôt.**

## Déposer le texte dans le Google Doc

```bash
python3 05-FUNNEL/00-METHODE/scripts/deposer_texte.py <texte.md> <doc_id> --doc --remplacer
python3 05-FUNNEL/00-METHODE/scripts/deposer_texte.py <texte.md> <doc_id> --verifier
```

Avant d'écrire, le script vérifie que personne d'autre n'a modifié ni commenté le document. S'il
refuse, on applique les changements passage par passage, sans réécrire le document.

Après l'écriture, il relit le document et doit finir sur **« Dépôt conforme »** : encadré et texte
identiques au markdown, mêmes nombres de titres, de puces, de notes en jaune et de sauts de page.
`--verifier` relance ce contrôle seul et montre le premier écart.

**Pendant la finalisation à la main par Adrien, la réécriture forcée est proscrite** : elle
écraserait ses retouches.
