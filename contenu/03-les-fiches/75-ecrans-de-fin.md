# Les écrans de fin, format par format

Ce fichier existe parce qu'une même erreur est revenue trois fois sous des formes différentes.
Elle a toujours la même cause : **deux éléments d'habillage qui se disputent la même zone de
l'écran**, sans que rien dans le code ne les en empêche.

## Les deux manières de finir une publicité

Il n'y en a que deux, et elles s'excluent.

**L'appel à l'action incrusté** — `fin: cta-fleches`. Pas de carte : la dernière image de la vidéo
reste à l'écran, et par-dessus viennent la phrase « CLIQUEZ SUR LE LIEN CI-DESSOUS » en gros et la
double flèche qui clignote. C'est le choix des UGC — 131, 136, 137, 138, 139.

**L'écran de fin composé** — `fin: carte-bouton` ou `carte-archive`. Un écran plein qui remplace la
dernière image : un bouton « VOIR LA PRÉSENTATION », la ligne « Cliquez sur le lien ci-dessous »
sous lui, et la place réservée aux flèches en dessous. C'est le choix des preuves clients — 128,
129, 132, 135 — et de la 130, avec le carton d'archive en noir et blanc.

## La règle, et pourquoi elle est mécanique maintenant

**Un écran de fin porte déjà son appel à l'action : on n'en incruste jamais un second.** La carte
écrit le bouton et sa ligne ; l'incrustation écrivait la même phrase, en blanc, en gros, exactement
par-dessus le bouton. Adrien : *« le bouton est derrière le CTA, il devrait être en haut, écrit
au-dessus »*.

**Un écran composé ne porte pas de sous-titre.** Même raison : le sous-titre tombait sur les
chevrons clignotants. C'est la même règle que pour les écrans de question, dont la phrase est déjà
écrite en grand.

Ces deux points ne sont plus à passer en argument d'un montage à l'autre : `monter()` regarde le
**type du dernier plan** et, s'il s'agit d'une carte, supprime l'appel à l'action incrusté et fait
taire le sous-titre sur sa durée. Une consigne qu'il faut penser à repasser d'une publicité à la
suivante finit toujours par être oubliée — ce fichier documente une règle, le code l'applique.

## Ce qui se vérifie avant de livrer

Extraire **trois images des cinq dernières secondes** et regarder, dans les trois formats :

- le bouton est en haut, entier, et rien n'est écrit dessus ;
- la ligne « Cliquez sur le lien ci-dessous » est sous le bouton, pas dedans ;
- les chevrons sont sous la ligne et ne touchent ni l'une ni l'autre ;
- aucun sous-titre n'apparaît pendant la carte.

Une carte se fabrique en une seconde — il n'y a aucune raison de la découvrir à la fin d'un montage
de dix minutes, encore moins chez Adrien.
