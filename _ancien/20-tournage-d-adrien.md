# Quand c'est Adrien qui tourne

L'Ads 134 est la première publicité qu'Adrien filme lui-même : son écran d'ordinateur, pris au
smartphone, avec sa vraie voix par-dessus. Elle impose trois traitements qu'aucune autre chaîne du
projet ne demande, et qui se rejoueront à l'identique la prochaine fois.

## 1. Descendre sa voix sans qu'on l'entende travaillée

Sa demande : **« rendre la voix un peu plus grave, qu'on essaye de camoufler un peu »** — il ne veut
pas être reconnu. Le réglage validé, sur sa voix mesurée à **136 Hz** :

```
highpass=f=60,
asetrate=44100*0.93, aresample=44100, atempo=1.075269,   → -1,26 demi-ton, formants compris
rubberband=pitch=0.903:formant=preserved,                → -1,74 demi-ton de plus, formants gardés
equalizer=f=110:t=q:w=1.0:g=2, equalizer=f=2800:t=q:w=1.4:g=-1.5,
loudnorm=I=-16:TP=-1.5:LRA=11
```

Total : **−3 demi-tons, de 136 à 113 Hz.** Sa réaction : « la voix est top là ».

**Ce qui compte n'est pas la hauteur, c'est le corps.** Une voix qu'on se contente de descendre en
hauteur reste reconnaissable : ce sont les formants — la signature du conduit vocal — qui font qu'on
identifie quelqu'un. `rubberband` seul les préserve par construction, ce qui est parfait pour rester
naturel mais inutile pour camoufler. D'où la combinaison : un `asetrate` modéré descend les formants
d'un peu plus d'un demi-ton, `rubberband` finit le travail sur la hauteur seule. On obtient un homme
plus massif, pas un Adrien ralenti.

**Recoller sans dérive.** Le filtrage retarde le son d'environ 12 ms. On les reprend à la remise en
place (`-itsoffset -0.012`) et on vérifie par corrélation d'enveloppe, tranche de dix secondes par
tranche de dix secondes : le décalage doit rester dans les ±5 ms d'un bout à l'autre. L'image se
recopie sans être réencodée (`-c:v copy`).

## 2. Sous-titrer une prise improvisée

Adrien ne lit pas le script, il le raconte. La transcription porte donc ses « euh », ses reprises
(« lui, lui, là »), ses amorces avalées (« l'école nous a-, nous apprend »). **Un sous-titre qui
écrit « euh » donne l'air d'un rush oublié au montage.**

Le nettoyage se fait sur la liste de mots minutée, **sans toucher aux horodatages des mots gardés** :

- on retire les tics (`euh`, `heu`, `hein`, `ben`, `bah`, `enfin`) et les fragments que Scribe note
  avec un tiret final ;
- on fusionne les mots répétés à l'identique ;
- **on enlève la ponctuation qui appartenait au tic** — sinon on lit « et, pareil avec les
  applications » — mais seulement quand elle était portée par un mot outil. Après un mot plein
  (« prof d'anglais, euh, c'est un ingénieur »), la virgule sépare deux propositions et reste ;
- on rend sa majuscule à la phrase qui commençait par un tic, sinon on lit « mobiles. sauf que ».

## 3. Deux réglages d'habillage que ce tournage a révélés

**Une bribe ne se termine jamais sur un mot qui appelle le suivant.** « nous apprend l'anglais avec
de » puis « la grammaire » : l'œil bute. `sous_titres_mots(..., eviter_mots_outils=True)` reporte ces
mots sur la bribe suivante, avec deux mots de dépassement autorisés.

**La marge verticale est une fraction de la hauteur.** Une marge en pixels multipliée par l'échelle
du texte tombait à 17 % du bas en 9:16, mais à 31 % en 1:1 et à **41 % en 16:9**, où le sous-titre
finissait au milieu de l'image. Une marge donnée entre 0 et 1 est désormais lue comme une fraction :
`marge=0.16` pose le sous-titre au même endroit dans les trois formats.

## 4. Les trois formats d'un plan vertical filmé au téléphone

La source fait 720 × 1280. Le 1:1 garde toute la largeur et coupe haut et bas : sans reproche. Le
16:9 ne garde que **32 % de la hauteur** — une bande horizontale. Elle reste lisible ici parce que le
sujet (la page à l'écran et la vignette de la webcam) vit au centre du cadre, mais c'est une limite à
connaître : un tournage vertical dont le sujet occupe toute la hauteur ne se décline pas en 16:9.
Aucun flou sur les côtés dans aucun cas.

## Le montage

```
python3 04-PRODUCTION/scripts/monter_ads_134.py "9:16" "1:1" "16:9"
python3 04-PRODUCTION/scripts/verifier_formats.py 134
```
