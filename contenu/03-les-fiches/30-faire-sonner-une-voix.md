# Faire sonner une voix vraie

Adrien a validé la bande son de l'Ads 116 d'un mot — « excellente » — après avoir refusé en bloc
trois castings la veille. Ce document dit ce qui sépare les deux, parce qu'il a demandé
explicitement que la recette soit écrite plutôt que reproduite de mémoire.

Le défaut qu'il entend n'est jamais un mauvais timbre. C'est **l'absence de défaut** : « toutes les
voix font très voix de podcast, trop lisse, trop parfaite ».

---

## La règle qui prime sur toutes les autres : une prise par tour de parole

**Ne jamais découper un texte en une requête de synthèse par phrase.** Tout ce qu'un même
personnage dit d'affilée part en **une seule** génération. Le découpage par réplique se fait
ensuite, en coupant la prise continue aux respirations que le modèle a lui-même posées — les
tranches se recollent au sample près, donc la bande son reste la prise d'origine.

Deux générations successives de la même voix ne partagent ni le niveau, ni le fond sonore, ni
l'intonation de sortie. Sur une seule publicité, l'écart de sonie entre répliques atteignait
**douze LUFS** et l'écart de fond sonore **vingt et un décibels**. Chaque soudure s'entend, et
l'oreille l'entend comme un trou.

Six correctifs d'assemblage ont été essayés avant de trouver la cause, et **aucun n'a suffi** :
assemblage en WAV pour supprimer les artefacts d'encodeur MP3, fondus sur chaque réplique, souffle
de salle continu, appariement de sonie au décibel près, blancs raccourcis, fondu enchaîné. Tous
sont utiles et sont restés dans le code. Aucun ne traite la cause. **La seule façon de ne pas
entendre une jointure est de ne pas en créer.**

### Le changement de personnage, lui, se recouvre

Il subsiste une jointure à chaque changement de locuteur, et elle est légitime — c'est un dialogue.
Elle se traite par un **recouvrement franc** : la voix qui relance commence pendant que la
précédente s'éteint, comme dans une vraie conversation. Un blanc net entre deux personnages
s'entend comme une coupe de montage.

### Et le garde-fou sur la troncature

ElevenLabs coupe parfois une génération longue sans rien signaler : le fichier s'arrête à plein
niveau, au milieu d'un mot. Une prise qui finit normalement décroît. Le contrôle porte donc sur le
niveau de la dernière fenêtre, et la prise se refait si elle est encore en pleine parole.

---

## Les quatre leviers, dans l'ordre d'importance

### 1. La source du clone

C'est le levier le plus lourd et le plus négligé. **Un clone hérite de la prosodie de sa source.**
Une voix clonée sur quelqu'un qui *parle* donnera toujours un personnage plus crédible qu'une voix
clonée sur quelqu'un qui *lit*.

Mis à l'écoute de cinq candidats pour un rôle d'interviewé, Adrien a désigné la seule voix du stock
issue d'une **note vocale spontanée** — et il l'a préférée alors qu'elle sonnait dix ans plus jeune
que le rôle. L'âge se rattrape, la fausseté non.

Corollaire de sourçage : viser du **format long** — podcast, interview, vlog — d'un seul locuteur,
sans musique. Dix à quinze minutes suffisent ; au-delà le clonage instantané plafonne.

### 2. Le texte dit, qui n'est pas le texte écrit

Les tics d'oral ne s'ajoutent pas au montage : **ils s'écrivent**. C'est la seule différence entre
l'Ads 116, validée, et la première version de l'Ads 118, jugée lisse.

Ce qu'on ajoute, sans jamais toucher au fond :

- **les appuis** — hein, ben, bon, voilà, en fait, du coup
- **les élisions** — « je participe pas », « il cherche pas le mot »
- **les reprises** — « c'est juste… c'est juste ce qu'il a observé »
- **les suspensions** — « mais quand il faut répondre… rien ne sort »

Une limite mesurée : **certaines élisions sont phonétiquement ambiguës et le modèle les rate.**
« Je parle à personne » est sorti « je pars à personne » sur quatre essais sur quatre, quelle que
soit la stabilité et quelle que soit la graphie. Sur ces cas-là, le « ne » se conserve — il ne
s'entend pas comme une faute, alors qu'un contresens s'entend.

### 3. La stabilité

**`eleven_v3`, stabilité 0.** C'est le réglage validé. La stabilité haute lisse exactement ce qu'on
cherche à garder.

Deux exceptions. Les **répliques courtes** repassent automatiquement en 0,5 : sous une soixantaine
de caractères, le modèle n'a pas assez de contexte et invente des mots. Et le **registre ASMR** se
tient en 0,5 : le chuchotement est déjà porté par la voix, la stabilité créative y ajoute des
ruptures de souffle qui cassent l'effet.

### 4. Le souffle se met dans la phrase, pas à son ouverture

Adrien a retenu une voix « mais sans le soufflement au début ». **Un soupir sur les premiers
instants d'une réplique se remarque comme un effet**, parce que rien ne le précède qui le
justifie — et sur un hook, il coûte la seconde qui compte le plus. Les hésitations vivent à
l'intérieur de la phrase.

---

## Le débit se règle par rôle

Un podcast n'a pas un débit unique : l'intervieweur relance, l'invité expose. Le casting porte donc
une `vitesse_role`, appliquée réplique par réplique **avant** l'assemblage — jamais sur le mixage,
qui emporterait l'ambiance avec lui.

**Une réplique de moins d'une seconde et demie ne s'accélère pas.** « Vous savez pourquoi ? » dure
une demi-seconde ; à ×1,3 la dernière syllabe se perd, et Adrien a entendu « vous savez pour ? ».

---

## Le contrôle reste obligatoire

`verifier_voix.py` réécoute chaque réplique et la compare à son texte. Rien dans la réponse de l'API
ne signale une phrase escamotée. Toutes les erreurs décrites plus haut ont été trouvées par lui, pas
par une relecture du code.

Et l'assemblage a ses propres pièges, décrits dans `dynamiser-le-montage.md` : jamais de
concaténation de MP3, et un fondu court sur chaque réplique.
