# Modèle Fichier AdCopy — format de sortie obligatoire

C'est la structure exacte de chaque fichier produit. Un fichier par ad, nommé `AdCopy-{numéro}`.

---

```
# AdCopy {N°}

Avatar : {1-4}  ·  Format : {…}  ·  VSL cible : {1|2|3}  ·  Niveau : {Problem Aware | Solution Aware}
Angle : {…}
Hook : {…}
Itération de : {Ads N° | NEW}

---

## AD COPY
{le jeu fixe de l'avatar, repris à l'identique — voir `adcopy-par-avatar.md`. Variante a, b ou c selon la VSL ciblée.}

## TITRE / HEADLINE
{les headlines de l'avatar, variante a, b ou c selon la VSL}

## DESCRIPTION

…

## CTA
{En savoir plus | S'inscrire | …}

## DISPLAY LINK
…

---

## CREATIVE — SCRIPT VIDÉO

**Indications de format :** {rappel du format et de ses contraintes de tournage}
**Cible de durée :** {celle de l'originale si l'ad est une itération — voir R20}

**HOOK**
…

**STORY**
…

**OFFER**
{traitement du CTA nommé : carte finale, bannière, ou flèche}

---

## BLOC D'AUTO-CONTRÔLE

- Mots : … — durée estimée … s au débit du format
- Cible de durée : … s
- Compliance : {🟢 conforme | 🟠 à vérifier : … | 🔴 …}
- Vocabulaire interdit VSL {n} : {aucun | liste}
- Registre : {(P) le produit n'est pas nommé ✓ | (S) produit nommé ✓}
- Prix / offre / garantie mentionnés : {NON ✓ | OUI ⚠}
- CTA isolé : « … »
- Rubrique qualité : {score par critère}
- Différence avec {Ads N° même angle} : …
```

---

## Règles de rédaction du script

**Un seul script par ad. Pas de variantes A, B, C.** Ce qui varie d'une ad à l'autre, c'est le format, l'angle, le hook et l'avatar — pas trois versions du même script.

**Trois blocs, toujours dans cet ordre : HOOK → STORY → OFFER.**

- **HOOK** — les 3 à 5 premières secondes. Une tension, une curiosité, une affirmation qui arrête. Jamais une introduction ni une mise en contexte.
- **STORY** — le corps. C'est là que se déploient la douleur, le mécanisme et la preuve. C'est le bloc le plus long.
- **OFFER** — l'invitation au clic. **Uniquement le clic.** Jamais le prix, l'offre, la garantie, la réduction ni le contenu du programme.

**Les indications de tournage s'écrivent en gras, à l'intérieur du flux du script**, là où elles se produisent — pas regroupées en fin de document. Exemple :

> …et là je me suis rendu compte que je n'avais rien compris. **repasser en facecam** Vous savez ce que ça fait ?

Le monteur doit pouvoir travailler sans avoir à réfléchir ni à interpréter.

**Longueur cible : 300 à 400 mots**, soit environ 2 minutes de vidéo. Au-delà, le script est trop long pour Meta.

---

## Le dépôt dans le Drive

Une publicité validée donne un dossier `Ads {n}` et un document `AdsCopy {n}` dans
`Biz FluentMania / Ads / Ads Meta NarratiFluent`. Le script qui les produit est
`.claude/skills/rediger-ads/scripts/` — la création passe par l'autorisation d'Adrien, un compte de
service n'ayant pas de quota de stockage, et la mise en forme par le compte de service.

**Typographie.** Tout en **Nunito**. Le corps en demi-gras — poids 600, « Nunito SemiBold » dans
l'interface. Les intertitres — `AdCopy`, `Titre / Headline`, `Description`, `CTA`, `Display link`,
`Creative :`, `Script Vidéo` — en 13 points, gras et soulignés.

**Les indications de montage portent trois marques cumulées : gras, italique et surlignage jaune.**
Cela couvre `HOOK`, `STORY`, `OFFER` et chaque didascalie (« plan : … », « insert : … »,
« voix off », « carte finale, 10 s »). L'œil doit séparer d'un coup ce qui se tourne de ce qui se
dit. Les `**` du brouillon se convertissent en mise en forme réelle, ils ne s'effacent pas.

**Les libellés de variante sont surlignés en jaune** (`#FFFF00`) : « V1 », « V2 », « V3a », « V4b »…
Le libellé seul, jamais la phrase qui suit, et dans les deux sections où il apparaît — l'AdCopy et
le Titre / Headline.

**L'AdCopy est aérée, le script vidéo ne l'est pas.** Dans les AdCopy, chaque retour à la ligne
devient une ligne vide. Les scripts restent compacts : les aérer séparerait la didascalie de la
réplique qu'elle commande.

**Les trois déclinaisons de VSL figurent dans chaque document.** La dernière AdCopy de l'avatar —
V3 pour l'avatar 3, V4 pour les avatars 1 et 4 — nomme un mécanisme exclusif et existe donc en
trois versions : **a** Protocole Phoenix, **b** Mini-Histoires Hollywoodiennes, **c** Lecture
Immersive. Les trois vont au document, même quand la publicité ne vise qu'une seule page de vente.
Le jeu Solution Aware fait exception : il n'a pas de déclinaison.

**Ensuite**, colorier la cellule de la publicité au bleu de la légende dans le Suivi Crea
(« Script écrit, Créa à créer »), en relisant la couleur dans la colonne A de l'onglet.

Les index de l'API Docs se comptent en unités UTF-16 : les emojis des AdCopy en occupent deux, et
les mesurer avec `len()` décale toute la mise en forme à partir du premier d'entre eux.
