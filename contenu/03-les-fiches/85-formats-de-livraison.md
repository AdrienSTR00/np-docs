# Les trois formats de livraison

Chaque publicité sort en **9:16, 1:1 et 16:9**. C'est la demande d'Adrien, et elle correspond aux
placements Meta.

| Format | Dimensions | Placement |
|---|---|---|
| 9:16 | 1080 × 1920 | Reels, Stories |
| 1:1 | 1080 × 1080 | fil, carré |
| 16:9 | 1920 × 1080 | placements horizontaux |

Le **9:16 est le format maître** : c'est le format natif des avatars Argil et le plus exigeant en
composition.

---

## Le carré se recadre, il ne se comble pas

**En 1:1, on garde toute la largeur du plan vertical et on coupe le haut et le bas.** Les côtés
montrent donc le décor réel, puisque c'est la même image. Adrien a comparé notre Ads 116 à son
Ads 40, montée par lui — également avec Argil : « là où toi tu as du flou sur les côtés, moi j'ai
du vrai paysage ».

Pourquoi le montage ne le faisait pas : passer d'un 1080×1920 à un 1080×1080 coûte 44 % de surface,
au-dessus du seuil de `PERTE_TOLEREE`, ce qui déclenchait le fond flou. Le seuil est donc relevé
pour ce seul cas, par le drapeau `carre_recadre` que la publicité passe à `monter()`.

Le recadrage se décale vers le haut — `HAUT_DU_CADRE = 0.28` — pour que le sommet du crâne ne soit
pas rasé : sur un plan cadré à mi-poitrine, le visage vit dans le tiers supérieur.

**Cette règle s'applique à partir de l'Ads 120.** Les publicités déjà livrées restent en l'état,
sur sa consigne explicite.

## Recadrer ou poser sur fond flou — pour le 16:9

Un plan vertical ne se recadre pas en seize neuvièmes sans perdre les deux tiers de sa hauteur : il
ne resterait qu'un visage, et tout le décor disparaîtrait.

La règle appliquée : **au-delà d'un tiers de surface perdue, on cesse de recadrer** et on pose
l'image entière sur un fond flou tiré d'elle-même. En dessous, on recadre au centre.

---

## Ce qui se recalcule à chaque format

Les sous-titres, la carte de fin et le cadrage sont recalculés pour chaque format — jamais
redimensionnés depuis le 9:16. C'est ce qui garantit que le texte reste lisible et à la même taille
apparente partout.

## Le 16:9 d'une UGC filmée au smartphone : bandes noires

Adrien, le 11 septembre 2026, capture à l'appui : **« pour le seize fois neuf, quand il y a une UGC
qui parle, un truc filmé en mode smartphone, il faut laisser le smartphone comme ça. Il faut que les
bords soient noirs et qu'il y ait juste le truc du smartphone. Parce que quand tu veux le mettre en
wide, ça fait vraiment dégueulasse. »**

**Ce n'est pas un retour au fond flou**, qui reste interdit partout. C'est l'image verticale
entière, centrée, sur du **noir franc** — la convention d'une vidéo de téléphone repostée dans un
cadre large, qui se lit comme un parti pris et non comme un défaut. Un 16:9 recadré depuis un
vertical ne garde que 32 % de la hauteur : sur quelqu'un qui parle face caméra, ça lui coupe le
crâne.

| format | UGC filmée au smartphone | tout le reste |
|---|---|---|
| **9:16** | natif | natif |
| **1:1** | **recadré** | recadré |
| **16:9** | **cadre vertical sur bandes noires** | recadré |

Le carré ne change pas : « pour le carré, c'est bien, tu gardes ce que tu as prévu de faire ».

En pratique : `monter(..., bandes_noires_16_9=True)` sur les publicités concernées. Le réglage est
porté par la publicité, pas par le montage, parce qu'il dépend de ce qui est filmé — un écran
d'ordinateur ou un plan de banque se recadrent normalement.

**À partir des publicités suivantes.** Celles qui sont livrées ne se remontent pas.
