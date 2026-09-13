---
name: rediger-ads
description: Rédige les scripts de publicités Meta NarratiFluent à partir des lignes du Suivi Crea. Produit pour chaque ad un fichier AdCopy complet — un script vidéo unique avec indications de tournage, le jeu d'AdCopy de l'avatar, ses Headlines, la Description, et un bloc d'auto-contrôle. Utiliser quand l'utilisateur demande d'écrire, produire ou générer une ou plusieurs ads, ou nomme des numéros d'ads à rédiger.
---

# Rédaction des scripts publicitaires NarratiFluent

## Entrée

Des numéros d'ads (`105`, `105-122`, `105,108,113`) ou « toutes les lignes à écrire ».

Les briefs viennent de `01-BRIEFS/suivi-crea.csv`, export du Suivi Crea. Colonnes utilisées :
`N° ad` · `Format` · `Angle (Hook)` · `Avatar` · `Itération de` · `Niveau de conscience` · `VSL cible`

Si `VSL cible` est absente pour une ligne, **s'arrêter et demander** — ne jamais deviner : c'est elle qui détermine tout le vocabulaire.
Si `Niveau de conscience` est absent, défaut = **Problem Aware**.

## Procédure

### 1. Lire et valider les briefs
`scripts/lire_briefs.py` lit le CSV, extrait les lignes demandées, valide que chaque champ obligatoire est rempli. Signaler les lignes incomplètes avant de commencer quoi que ce soit.

### 2. Composer le contexte, ad par ad
Sept blocs, assemblés par `scripts/composer_contexte.py` :

1. **Rôle et format de sortie** — voir `00-SOCLE/modele-adcopy.md`
2. **L'avatar** — le BLOC A de `00-SOCLE/avatars/matrice-avatar-{n}.md` : marché cible, points douloureux, promesse principale, solutions courantes, MUP
3. **Le registre** — la section « Niveau de conscience » de la même matrice, avec les consignes (P) ou (S) et les accroches du bon paquet
4. **La VSL** — **un seul** encart du BLOC B : MUS, porte-parole, moment de crise, preuves, ton, vocabulaire à utiliser et interdit
5. **Le brief** — format (voir `00-SOCLE/formats.md`), angle, hook, ad parente
6. **Les références** — `00-SOCLE/swipes-ads.md`, `00-SOCLE/swipes-adcopy-headline.md`, et les 3-5 entrées de `00-SOCLE/winners.md` du même avatar
7. **Les garde-fous** — `00-SOCLE/compliance-meta.md`, `00-SOCLE/anti-patterns.md`

> ⛔ **Ne jamais charger les VSL brutes dans le contexte de rédaction.** Les matrices contiennent la distillation nécessaire, et charger le texte de vente complet fait dériver vers le pitch produit.
>
> **Une exception, ciblée.** Quand un script raconte un épisode qui figure déjà dans une page de vente — l'histoire de Kató Lomb, le mécanisme du circuit narratif, un témoignage nommé — aller y chercher **le passage précis** et en reprendre les termes, plutôt que d'écrire une paraphrase. Les textes sont dans `Biz FluentMania / Marketing / Funnel NarratiFluent`, un fichier « Texte FINAL NarratiFluent (n) » par VSL. Extraire le passage, pas le document.

### 3. Générer
Par lots de 4 à 5 ads en parallèle. Pour chacune : **un seul script** de 180 à 330 mots (HOOK / STORY / OFFER, indications de tournage en gras dans le flux), puis **le jeu d'AdCopy de l'avatar repris à l'identique** depuis `00-SOCLE/adcopy-par-avatar.md`, ses headlines, et la Description commune.

**Pas de variantes A, B, C.** Ce qui varie d'une ad à l'autre, c'est le format, l'angle, le hook et l'avatar.

**Avant d'écrire, lire `00-SOCLE/anatomie-d-un-script.md`.** C'est l'analyse mesurée des vingt scripts validés : longueur de phrase, fréquence des charnières, les neuf formes de hook, la structure du corps, et la liste de ce qu'aucun script retenu ne contient.

**Chaque script d'un même batch attaque par un angle différent.** Le répertoire disponible et la raison de la règle sont dans la fiche de mémoire `varier-les-angles-d-un-script-a-l-autre`. Les données chiffrées mobilisables sont dans `00-SOCLE/data/chiffres-de-l-enjeu.md`.

### 4. Contrôler
`scripts/controle.py`, sur **contexte neuf** — ne pas être juge et partie. Trois audits :

- **Compliance** — audit rouge / orange / vert contre `00-SOCLE/compliance-meta.md`
- **Copy Checklist** — grille de `00-SOCLE/copy-checklist.md`. Tout critère éliminatoire en échec, ou une moyenne sous 3,5, déclenche une réécriture automatique avant livraison.
- **Diversité** — comparaison avec les scripts existants du même angle dans `02-SCRIPTS/` et `03-ARCHIVE/`

### 5. Écrire la sortie
`scripts/sortie_docx.py` produit `02-SCRIPTS/ADS-{n}/AdCopy-{n}.md` et `.docx`, au format de `00-SOCLE/modele-adcopy.md`, avec le bloc d'auto-contrôle complet.

Tous les fichiers sortent au statut **« à relire »**. Rien n'est jamais marqué prêt.

### 6. Rapporter
En fin de batch, un résumé court :
- les ads produites, avec leur score de rubrique
- les réécritures automatiques et leur motif
- les points 🟠 de compliance qui demandent une décision humaine
- les lignes de brief incomplètes qui ont été écartées
- ce que j'ai corrigé seul dans le socle, et ce que je propose de changer

## Après coup

Quand Adrien recadre un script — « le hook est trop mou sur la 112 », « ça fait trop pub » — consigner immédiatement dans `00-SOCLE/journal-corrections.md` : date, n° d'ad, remarque. Tous les 2-3 batches, relire le journal et proposer la promotion des remarques récurrentes dans `anti-patterns.md` ou la rubrique.

## Commandes voisines

- `/rediger-ads 112 --revoir "hook trop mou"` — régénère une seule ad avec la remarque en contexte
- Régénérer une matrice en `.docx` après modification du `.md` : voir les scripts de génération dans `03-ARCHIVE/generateurs/`
