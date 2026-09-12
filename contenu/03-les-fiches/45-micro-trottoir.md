# Le micro-trottoir

Format éprouvé sur l'Ads 115. Un journaliste arrête des passants dans la rue et leur pose une
question ; leurs réponses alternent avec une voix off qui explique. Ce document fixe tout ce qui a
été tranché, pour que la publicité suivante soit bonne du premier coup.

---

## Le casting

**L'intervieweur ne se voit jamais.** Sa formulation : « j'ai juste besoin d'avoir la main et le
micro ». À l'image, seule la main tendue tenant le micro entre dans le champ. Conséquence directe :
**il ne consomme aucun crédit d'avatar.**

**L'intervieweur et la voix off partagent la même voix.** C'est la même personne qui tend le micro
et qui raconte ensuite ; ce qui les sépare est le jeu, pas le timbre. La voix off est posée,
l'intervieweur est pris sur le vif — on lui ajoute la balise `[projecting]`.

**Les passants sont des voix clonées d'humains réels**, jamais des voix conçues par description.
Ils se castent sur l'âge entendu, noté dans le catalogue.

---

## Le cadrage, et l'erreur à ne jamais reproduire

Le face caméra fixe a été refusé : « le plan comme ça fixe, ce n'est pas ouf ». Ce qu'il faut est
le point de vue du caméraman posté sur le côté.

**Le prompt de scène Argil, éprouvé :**

```
filmed from the side in a candid street interview, three-quarter angle, looking
off-camera at the interviewer, a hand holding a black reporter microphone
entering the frame in the foreground on the right, busy American city street
behind with blurred pedestrians, handheld camera, daylight, medium close-up
```

On alterne `on the right` et `on the left` d'un passant à l'autre, pour que les plans ne soient pas
interchangeables. Sur un avatar qui a tendance au plan de vlog, ajouter
`both arms down at his sides and holding nothing` : c'est cette phrase qui empêche le bras tendu.

**L'erreur capitale :** un avatar cadré comme un selfie, bras tendu. Adrien l'a relevée
immédiatement — « s'il est interviewé, ce n'est pas lui qui filme ». Un plan de vlog détruit la
fiction du micro-trottoir, quel que soit le décor.

**Le décor est anglophone**, et c'est délibéré : la rue américaine renforce le sujet, qui est
l'apprentissage de l'anglais. Les trois passants sont dans le même genre de rue.

---

## Le montage : on ne quitte jamais la personne interrogée

C'est la correction la plus importante du format. Pendant que l'intervieweur pose sa question,
**on reste sur le passant, silencieux**, avec le micro tendu vers lui. Couper sur un plan de rue
anonyme casse l'échange : « vire-moi ces plans de rue là, c'est horrible ».

Techniquement, on ne peut pas laisser tourner le clip de l'avatar — ses lèvres bougeraient sans
qu'aucun son ne sorte. On prélève donc une image et on la fait vivre par un lent mouvement
d'appareil, ce qui donne un plan tenu et non un arrêt sur image. L'image se prend au tout début du
clip avant la question, et à la toute fin après la réponse.

**La répartition de l'image, pour un micro-trottoir :**

| Ce qu'on entend | Ce qu'on montre |
|---|---|
| La question de l'intervieweur | le passant, image arrêtée qui respire |
| La réponse du passant | le plan d'avatar |
| La voix off | les plans de banque du sujet |
| La carte finale | voir le document dédié |

---

## L'ambiance sonore

Les bruits de rue ne courent que sur les répliques tournées dehors, et se coupent net dès que la
voix off prend la parole : « quand il y a la voix off qui parle, ça doit être le silence derrière ».

L'ambiance se déduit des rôles, jamais de plages écrites à la main — une correction de casting
remet alors l'ambiance au bon endroit toute seule. Elle est mixée à −14 dB sous les voix, à partir
de deux prises alternées : une seule, répétée, laisse entendre sa boucle au deuxième tour.

---

## Le débit

Adrien juge le débit en comparant une maquette à la précédente, jamais en mots par minute. La
consigne se traduit donc en **durée cible**, et le calage se fait au montage : ElevenLabs accepte
le paramètre `speed` mais `eleven_v3` ne le suit pas.

Repère mesuré sur l'Ads 115 : il a demandé successivement ×1,3 puis ×1,2, pour atterrir à **1 min 25
et environ 250 mots par minute**. C'est le point de départ des prochains micro-trottoirs.

---

## Les points de texte propres à l'oral

Les points de suspension du script font systématiquement baisser la voix. Ils se retirent du texte
dit — l'hésitation reste, portée par la balise de jeu. De même, un point là où il faudrait une
liaison crée une respiration de deux secondes : « À l'école. Des listes » est devenu
« À l'école, avec des listes ». Le script écrit ne change pas ; seul le texte envoyé à la synthèse
est corrigé, via `corrections_texte` dans le casting.
