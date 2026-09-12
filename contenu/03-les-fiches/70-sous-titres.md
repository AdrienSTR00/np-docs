# Les sous-titres

Sur Meta, une large part de l'audience regarde sans le son. Les sous-titres ne sont donc pas un
confort : ils portent le message. Ce document fixe leur fabrication, pour qu'ils soient bons du
premier coup et dans les trois formats.

---

## Ils se calent au mot, pas à la réplique

Le minutage vient de la **reconnaissance vocale de la bande son définitive**, qui rend la position
de chaque mot. On ne le déduit jamais des durées de réplique.

La première version affichait une réplique entière d'un seul bloc — jusqu'à seize secondes de
texte figé à l'écran. Adrien : « la synchronisation entre ce qui est dit et les sous-titres n'est
pas parfaite ». C'était vrai, et la cause n'était pas un décalage mais un **découpage trop gros**.

**Le découpage :** des bribes de cinq mots au plus, trente-quatre caractères au plus, coupées de
préférence sur une ponctuation. Une virgule ne suffit pas à couper si la bribe est trop courte,
sinon un mot seul clignote à l'écran pendant deux dixièmes de seconde. Et une bribe s'efface au
plus tard quand la suivante paraît, sans quoi deux sous-titres se chevauchent.

---

## Le retour à la ligne doit être actif

Dans le fichier ASS, **`WrapStyle: 0`**. Il était à `2`, qui interdit le retour à la ligne
automatique : une longue réplique sortait alors sur une seule ligne débordant des deux côtés du
cadre. C'est le défaut qu'Adrien a vu en premier.

Les marges latérales valent 9 % de la largeur du cadre, ce qui garantit la coupure avant le bord
quel que soit le format.

---

## Ils gardent la même taille apparente dans les trois formats

Le corps se calcule sur la hauteur du cadre — 74 points pour 1920 de haut — et la marge basse
suit la même règle. Sans cela, le même sous-titre paraît énorme en carré et minuscule en seize
neuvièmes.

Style retenu : Arial gras, blanc, contour noir épais et ombre portée, centré en bas. Le contour
existe pour que le texte reste lisible sur un fond clair, une façade blanche ou un ciel.

---

## Le contrôle avant livraison

Le texte affiché doit être **le texte du script**, pas la transcription : la reconnaissance vocale
se trompe sur les homophones et perd la ponctuation. Aujourd'hui les bribes reprennent les mots
reconnus ; si un écart apparaît sur un nom propre ou un chiffre, il se corrige dans le fichier ASS
avant l'encodage définitif.
