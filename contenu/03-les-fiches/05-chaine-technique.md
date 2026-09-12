# La chaîne de production, du script à la vidéo

Ce document décrit comment une publicité NarratiFluent passe du script validé aux trois fichiers
livrables. Il est le point d'entrée : les documents voisins détaillent chaque format et chaque
élément récurrent.

---

## Le principe qui gouverne tout : la voix commande, l'image suit

La bande son est produite et validée **avant** la moindre image. Ses durées deviennent ensuite
intangibles, et chaque plan est étiré ou raccourci pour tomber exactement sur sa réplique.

C'est l'inverse du montage habituel, et c'est délibéré. Cela permet de corriger une phrase sans
refaire l'image, et cela place le point de contrôle là où il ne coûte rien : quelques milliers de
caractères ElevenLabs, contre une centaine de crédits Argil pour un rendu vidéo.

---

## Les quatre étapes, dans l'ordre

### 1. Du script au dialogue

`decouper_dialogue.py` lit le script markdown et le découpe **par voix**, pas par plan. Les
didascalies entre astérisques ne sont pas jetées : elles deviennent des balises de jeu que le
modèle `eleven_v3` interprète — « *il rit, cherche* » donne un rire et une hésitation, pas une
ligne lue à voix haute.

### 2. La bande son

`produire_ad.py` lit le `casting.json` de la publicité et fabrique la bande son complète :
génération réplique par réplique, silences, calage du débit, ambiance, compression, normalisation.
Tout ce qui décide vit dans le casting ; le script ne fait qu'exécuter. Une correction d'Adrien se
traduit donc par une ligne de données modifiée, jamais par du code réécrit.

**Le contrôle obligatoire :** `verifier_voix.py` refait écouter chaque réplique par la
reconnaissance vocale et la compare à son texte. Rien dans la réponse de l'API ne signale une
phrase escamotée — c'est arrivé, « tout le temps, trop vite pour moi » était ressorti « sur le
taux, taux vite pour moi ». **Aucune maquette ne part chez Adrien sans ce contrôle au vert.**

### 3. La validation d'Adrien

Il écoute et corrige. Les corrections portent presque toujours sur le rythme, le casting ou une
formulation — jamais sur l'image, qui n'existe pas encore.

### 4. L'image et le montage

`monter_video.py` assemble un plan par réplique et sort les trois formats. Les crédits Argil ne
partent qu'ici, après validation.

---

## Le groupement : par étape, pas par publicité

**Dix maquettes audio d'un coup, validées en une seule écoute. Puis dix vidéos.** Adrien renvoie
ses corrections en un seul message à chaque palier.

L'exception : sur un **format qu'il n'a jamais vu**, garder une publicité seule en éclaireur. C'est
ce qui a permis de ne rater qu'une seule publicité sur le cadrage du micro-trottoir au lieu de dix.

---

## Ce que coûte une publicité

Relevé sur l'Ads 115, 1 min 25, format micro-trottoir :

| Poste | Crédits |
|---|---|
| Scènes d'avatar créées dans l'application Argil | 5 par scène |
| Rendu vidéo des plans d'avatar | 160 par minute d'avatar à l'image |
| Royalties d'avatar | 20 par vidéo créée |
| Voix ElevenLabs, plans de banque, ambiance, montage, sous-titres | 0 |
| **Total d'une publicité à trois avatars** | **environ 115** |

Deux postes s'évitent par construction et doivent l'être toujours. **La voix ne se paie pas si on
fournit notre propre audio** par le champ `audioUrl`. **Et seul ce qui montre un visage qui parle
passe par Argil** : sur l'Ads 115, 66 secondes sur 85 n'ont demandé aucun avatar.

---

## Les contraintes techniques à connaître avant de promettre

- **Argil ne sait pas créer un cadrage par API.** La création d'avatar réclame une vidéo de
  tournage et une vidéo de consentement. Les scènes se fabriquent dans l'application, en pilotant
  le navigateur d'Adrien.
- **Argil n'héberge aucun fichier son.** La création d'une vidéo n'accepte qu'une `audioUrl` que
  ses serveurs vont chercher : nos voix doivent être publiées temporairement, avec l'accord
  d'Adrien, dans un dossier de son Drive prévu pour être vidé ensuite.
- **`audioUrl` et `transcript` s'excluent.** Fournir l'audio interdit le texte, et c'est ce qu'on
  veut : c'est notre voix clonée qui commande, pas un texte relu par Argil.
- **Argil ne sort qu'en 9:16 et 16:9**, jamais en carré.
- **Pexels passe par Cloudflare**, qui refuse l'agent par défaut de Python avec un 403 ressemblant
  à une clé invalide. Se présenter comme un navigateur suffit.
- **Aucun endpoint ne donne le solde de crédits Argil.** Il se lit dans l'application.

---

## Les pièges de montage déjà payés

**La durée d'un plan se fixe en images, jamais en secondes.** À trente images par seconde, FFmpeg
arrondit vers le bas ; sur dix-neuf plans, l'image finissait une seconde et demie en avance sur le
son.

**Un plan d'avatar accéléré ne couvre pas le silence qui suit la réplique.** Sa dernière image se
prolonge, ce qui donne la respiration de quelqu'un qui vient de finir sa phrase.

**Le calage du débit porte sur la voix seule, jamais sur le mixage.** Accélérer après le mixage
accélérerait aussi les voitures de l'ambiance.

---

## La musique de fond — à trancher avec Adrien

Adrien veut qu'on ajoute **une musique de fond discrète, qu'on entend vraiment au fond**, sur
l'essentiel des publicités : c'est un usage général du format, et l'absence de musique s'entend.

Ce qui est acquis : les **B-Rolls**, les publicités à **avatar IA** et les **podcasts** en portent
presque toujours. Ce qui reste ouvert : le **micro-trottoir**, où l'ambiance de rue occupe déjà le
fond sonore — il hésitait lui-même. À reconfirmer avec lui avant de l'appliquer à ce format.

Deux points à régler au moment de le mettre en œuvre : la source des musiques, qui doit autoriser
l'usage publicitaire, et le niveau de mixage, qui doit rester nettement sous la voix — de l'ordre
de vingt-cinq décibels en dessous, comme l'ambiance de rue est aujourd'hui à quatorze.
