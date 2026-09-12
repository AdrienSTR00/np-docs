---
name: produire-ads
description: Fabrique les publicités NarratiFluent à partir des scripts validés — bande son avec les voix clonées, plans d'avatar Argil, plans de banque, ambiance, sous-titres, carte de fin, et livraison en 9:16, 1:1 et 16:9. Utiliser quand l'utilisateur demande de produire, monter, rendre ou fabriquer une ou plusieurs ads, de faire une maquette audio, de cloner une voix, ou de sortir les formats de livraison.
---

# Production des publicités NarratiFluent

## Le principe : la voix commande, l'image suit

La bande son se fabrique et se fait valider **avant** la moindre image. Ses durées deviennent
ensuite intangibles et chaque plan se cale dessus. Cela place le point de contrôle là où il ne
coûte rien — quelques milliers de caractères ElevenLabs — plutôt qu'après une centaine de crédits
Argil.

## Les documents de référence

Tout le détail vit dans `00-SOCLE/production/`, à lire avant de produire :

- `boucle-de-validation.md` — **à lire en premier** : l'ordre de travail avec Adrien, l'extrait
  avant le montage complet, et le regroupement des validations
- `avant-de-livrer.md` — la liste de vérification, et les trois verrous qui refusent
- `rex-11-septembre.md` — les vingt erreurs déjà payées, leurs causes et leurs garde-fous
- `chaine-de-production.md` — les quatre étapes, les coûts, les contraintes des API, les pièges de
  montage déjà payés
- `choisir-un-visage.md` — dix candidats par personnage, Adrien choisit sur planche contact
- `regles-de-son-par-format.md` — **à relire avant chaque production** : blancs, recouvrements,
  musique et ambiance, selon qu'il y a une voix ou deux
- `faire-sonner-une-voix-vraie.md` — la recette validée : source du clone, texte oral, stabilité,
  débit par rôle
- `format-micro-trottoir.md` — casting, cadrage, montage, ambiance
- `dynamiser-le-montage.md` — les leviers qui rendent un montage vivant, et le contrôle avant de
  livrer
- `formats-animes.md` — 3D stylisée, 3D scientifique, portrait illustré : état de l'outillage et
  idées en réserve
- `mouvements-de-camera.md` — les zooms lents et les coupes serrées, et qui n'y a pas droit
- `sous-titres.md` — calage au mot, retour à la ligne, taille par format
- `cartes-de-fin.md` — composition de l'écran final
- `formats-de-livraison.md` — recadrer ou poser sur fond flou

## La procédure

### 1. Découper le script
```
python3 04-PRODUCTION/scripts/decouper_dialogue.py 02-SCRIPTS/ADS-NNN/AdCopy-NNN.md
```

### 2. Écrire le casting
Un `casting.json` dans `04-PRODUCTION/medias/ADS-NNN/` : les voix par rôle, les réglages, la durée
cible, le plan d'ambiance, les corrections de texte dit. **Tout ce qui décide vit là** ; les
scripts ne font qu'exécuter, si bien qu'une correction se traduit par une ligne de données.

Les voix se prennent dans `04-PRODUCTION/catalogue-voix.json`. Une voix manquante se clone depuis
un fichier ou un lien fourni par Adrien — jamais conçue par description, cela s'entend.

### 3. Produire et contrôler la bande son
```
python3 04-PRODUCTION/scripts/produire_ad.py 04-PRODUCTION/medias/ADS-NNN 02-SCRIPTS/ADS-NNN/AdCopy-NNN.dialogue.json
python3 04-PRODUCTION/scripts/verifier_voix.py 04-PRODUCTION/medias/ADS-NNN/bande-son.json
```
**Le contrôle est obligatoire et bloquant.** Rien dans la réponse de l'API ne signale une phrase
escamotée : seule la réécoute le dit.

### 4. Faire valider
Déposer la maquette dans `04-PRODUCTION/medias/A-ECOUTER` — **un seul fichier par objet à juger,
portant son nom exact, et rien d'autre dans ce dossier** — puis l'envoyer à Adrien.

### 5. Chiffrer, puis produire l'image
```
python3 04-PRODUCTION/scripts/cout_argil.py    # avant toute dépense, et communiqué
```
Puis les scènes d'avatar si le cadrage manque, les rendus, les plans de banque, le montage.

### 6. Livrer les trois formats
```
python3 04-PRODUCTION/scripts/monter_ads_NNN.py "9:16" "1:1" "16:9"
```

## Les règles qui ne se négocient pas

- **Un plan d'avatar généré ne reste jamais fixe** — zoom lent ou coupe vers un cadrage plus serré,
  en alternance, appliqués par défaut. **Mais un tournage réel ne bouge pas** : `mouvements=False`
  dès qu'Adrien se filme lui-même. Il annonce le cas ; sa consigne prime sur le défaut.
- **Aucun personnage n'entre dans une publicité sans qu'Adrien ait vu son visage.** Dix candidats
  par personnage, en planche contact numérotée. Il répond par un numéro.
- **Le script ne se réécrit jamais pour arranger la production.** Un raccord qui s'entend se règle
  au son. La mise en bouche — élisions, appuis, hésitations — change la manière de dire, jamais ce
  qui est dit.
- **Un tour de parole part en une seule génération.** Jamais une requête de synthèse par phrase :
  deux générations successives n'ont ni le même niveau, ni le même fond, ni la même intonation, et
  chaque soudure s'entend comme un décrochage. Le découpage par plan se fait après, sur la prise
  continue. Un changement de personnage, lui, se recouvre franchement.
- **Contrôler qu'une prise n'est pas tronquée.** ElevenLabs coupe parfois une génération longue
  sans rien dire : le fichier s'arrête à plein niveau, au milieu d'un mot.
- **Jamais de concaténation de MP3.** L'assemblage se fait en WAV, avec un seul encodage final, et
  un fondu court sur chaque réplique. Une jointure de MP3 laisse un artefact d'encodeur qu'Adrien
  entend comme un « boum ».
- **Rien ne dure plus de quatre secondes sans changer.** Sur une réplique longue, couper à
  l'intérieur avec un insert de B-roll. Les didascalies du script disent où.
- **Seul ce qui montre un visage qui parle passe par Argil.** Le reste se monte en FFmpeg avec des
  plans de banque gratuits.
- **La voix ne se paie jamais chez Argil** : on fournit notre audio par `audioUrl`.
- **Chiffrer avant de dépenser**, et communiquer le chiffrage à Adrien.
- **Demander avant toute suppression de fichier.** C'est sa seule règle d'autorisation.
- **Sauvegarder les enregistrements sources avant de toucher aux voix.** Une voix se recrée, un
  enregistrement perdu ne se retrouve pas.
