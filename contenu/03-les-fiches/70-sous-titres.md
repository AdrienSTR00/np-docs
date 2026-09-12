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

## Le style des UGC d'Adrien : jaune, sans contour, ombre nette

Arrêté le 12 septembre 2026 sur les Ads 136, 137 et 138, après qu'Adrien a passé en revue dix
propositions : **« ces sous-titres font cheap »**.

| | |
|---|---|
| Police | **Avenir Next Heavy**, corps 112 |
| Couleur | **jaune #FFD43B** |
| Contour | aucun |
| Ombre | portée nette, 4 |
| Position | 15 % du bas |

**Ce qui a été écarté, et pourquoi.** Impact d'abord : c'est la police des mèmes des années 2010,
elle se reconnaît instantanément et c'est elle qui faisait « cheap ». Puis le contour épais, qui
produit le même effet quelle que soit la police. Puis Futura espacé — fait affiche —, le bandeau
blanc — fait sous-titre de film —, le vert citron — fait gaming — et l'italique — fait citation.

Ce qui reste marche pour une raison simple : **les publicités qui tournent sur l'Ads Library sont
en grasse géométrique, sans contour, avec une ombre.** Arial Black, Montserrat, Poppins, Anton. Ce
sont des polices de titrage, pas des polices de sous-titrage de film.

**Attention à l'italique involontaire.** Nommer une famille sans sa graisse laisse macOS choisir, et
il choisit parfois la variante penchée : trois des dix propositions sont sorties en italique sans
que rien ne le demande. Le style porte donc `italique=0` explicitement, et la police se nomme en
entier — `Avenir Next Heavy`, pas `Avenir Next`.

---

## Le hook se révèle mot à mot, et la ligne ne bouge pas

Sur les UGC, la phrase d'accroche ne s'affiche pas d'un bloc : **chaque mot apparaît à l'instant où
il est prononcé.** C'est la demande d'Adrien, et le minutage de Scribe la rend exacte à la syllabe.

Le mot qui porte la phrase est écrit **beaucoup plus gros, en capitales, dans une seconde police** —
Futura Condensed ExtraBold à 150 contre Avenir Next Heavy à 74. C'est le contraste qu'on voit dans
les publicités qu'Adrien a relevées, et il vaut mieux qu'une couleur d'accent.

**Le piège, et sa solution.** Révéler un mot en l'ajoutant à la ligne fait sauter tout le bloc à
chaque mot — c'est exactement l'effet bon marché qu'on cherche à éviter. Les mots à venir sont donc
**écrits dès le début et rendus transparents** (`{\alpha&HFF&}`) : ils réservent leur largeur, et
le texte se remplit sans que rien ne se déplace.

Le générateur ordinaire doit **sauter la fenêtre du hook** (`exclure=[(0, fin_hook)]`), sinon le
même texte s'écrit deux fois l'un par-dessus l'autre.

---

## Le contrôle avant livraison

Le texte affiché doit être **le texte du script**, pas la transcription : la reconnaissance vocale
se trompe sur les homophones et perd la ponctuation. Aujourd'hui les bribes reprennent les mots
reconnus ; si un écart apparaît sur un nom propre ou un chiffre, il se corrige dans le fichier ASS
avant l'encodage définitif.
