# Les slides de la VSL

> Transformer le texte de vente en présentation : une slide par paragraphe, la couleur de marque
> pour l'emphase, les captures et les illustrations. Puis la review à deux.

## Les specs, mesurées sur une VSL existante

Elles se relèvent sur la VSL de référence, pas sur une note de SOP : quand les deux divergent, c'est
la présentation qui a raison.

| | Valeur |
|---|---|
| Page | 10 × 5,62 pouces (16:9), fond blanc |
| Police | Arial, et rien d'autre |
| Taille | **36** sur une slide de texte seul, **23** sur une slide illustrée, **24** au-dessus d'une capture |
| Graisse | gras partout : le gras n'est pas une emphase, c'est la graisse par défaut |
| Alignement | centré horizontalement, calé au milieu verticalement |
| Boîte de texte | 8,5 pouces de large, posée à 0,75 du bord gauche |
| Longueur | médiane 98 caractères, maximum 208 |
| Couleurs | noir, la couleur de marque pour l'emphase, le rouge pour le prix et les appels à l'action |
| Emphase | **environ 17 % des mots**, sur une slide sur deux |
| Images | une slide sur trois à une slide sur quatre |

## Le découpage

**Une slide par paragraphe du Doc**, jamais par phrase : tout ce qui n'est pas séparé par une ligne
vide reste ensemble. Au-delà de 200 caractères, la coupe est **récursive** — un paragraphe de 400
caractères donne trois slides, pas deux moitiés encore trop longues. La première finit par « … », la
suivante commence par « … » et reprend sans majuscule.

**La coupe tombe sur une frontière de sens**, dans cet ordre : une fin de phrase, sinon une virgule,
un point-virgule ou un deux-points, sinon le début d'une proposition introduite par une conjonction
ou un relatif. Jamais sur une espace nue : deux mots qui vont ensemble — un adjectif et son nom, les
deux morceaux d'une locution — restent sur la même slide. Quand aucune frontière ne convient, la
slide reste longue : une slide chargée se lit, une expression coupée en deux ne se lit pas.

**Ce qui ne devient jamais une slide** : les titres de sections, les notes de production, les
indications de tournage, les didascalies des témoignages, les répliques en anglais des vidéos
avant / après, les mentions « extrait vidéo » et l'appendice des sources.

## L'emphase

**Le gras ne marque rien, la couleur marque tout.** Quand le Doc n'est pas mis en forme, c'est Claude
qui décide des mots colorés, directement dans la présentation, à une fréquence calquée sur la VSL de
référence. Adrien corrige ensuite sur pièce.

Ce que la couleur marque : un titre de bloc, une affirmation entière qui porte l'argument, ou un
fragment court au milieu d'une phrase — un chiffre, un délai, le nom du mécanisme. Jamais un mot
isolé pour faire joli. La ponctuation de fin prend la couleur de sa phrase.

**L'emphase s'ancre sur le texte de la slide, jamais sur son rang.** Une correction du découpage
décale tous les index ; la clé est donc le début du texte.

## Les images

**Une image montre ce que la slide dit, pas le thème du chapitre.** C'est la règle qui prime sur
toutes les autres. Le plan d'illustration attribue un bassin d'images à une plage de slides : il
fournit la matière, il ne fait pas le choix. Le choix se fait slide par slide, en relisant la
phrase. Quand la phrase énumère (« les plans des pièces, les notices, les appels avec le client »),
chaque image reprend un élément de l'énumération, dans l'ordre. Quand elle nomme un lieu, un objet
ou un métier précis, c'est celui-là qu'on montre, pas sa famille. Le lien n'a pas besoin d'être
littéral, mais il doit être évident en une seconde.

**Pas de photo de stock générique.** Ce qui saute : le sujet posé au centre sur fond uni, la lumière
de studio sans direction, les modèles qui sourient à l'objectif, le plan large où rien n'accroche
l'œil. Ce qu'on garde : une lumière qui vient de quelque part, un cadrage serré ou un point de vue
choisi, de la profondeur de champ, une scène qui a l'air prise et non fabriquée. En pratique, tirer
une quinzaine de candidates par thème plutôt que trois, les regarder sur une planche de contrôle, et
écarter sans regret tout ce qui ressemble à une illustration de brochure. Une requête qui décrit une
situation ramène de meilleures images qu'une requête qui nomme un concept.

**Le coin bas droit reste libre** : le porte-parole s'y incruste en vidéo pendant toute la
présentation. Une illustration s'ancre donc à gauche, dans une zone de 7,2 × 3,8 pouces posée à
0,35 du bord, et le texte monte en haut de la slide. Un mock-up, large et bas, prend 9 pouces de
large et s'arrête à 1,55 du haut. Une capture se colle à l'étiquette ou à la question qui la
précède, qui monte en haut en corps 24.

**Les cinq gabarits de slide** sont relevés sur les slides mises en page par le porte-parole, et
ils se lisent dans `06-VSL/scripts/gabarits.py` : texte seul ; une image centrée ; deux images côte
à côte ; deux images sous une phrase longue (la rangée descend donc rétrécit) ; trois images en
rangée. Dans tous les cas la dernière ligne de texte s'arrête au-dessus de la zone d'incrustation,
et au-delà de quatre lignes le cadre de texte se remonte pour y parvenir.

**Une énumération se met en puces.** Quand plusieurs slides consécutives égrènent une liste, chaque
slide porte une puce Google Slides en tête de phrase, le paragraphe passe à gauche, le texte monte
en haut en corps 29, et l'image se pose en dessous.

**Les mock-ups se posent avant les illustrations** : un mock-up appartient à la slide qui annonce son
bonus et ne peut aller ailleurs, une illustration si.

**Le casting se pilote par la requête.** Les banques d'images rendent par défaut des modèles jeunes
et internationaux, loin de l'audience. La requête porte donc l'âge et le registre — « mature
engineer reading blueprint » plutôt que « engineer » —, et le résultat se contrôle sur une planche
de six vignettes avant de généraliser.

**Les sources** : Pexels et Pixabay pour les scènes courantes, Wikimedia Commons pour ce qu'elles
n'ont pas. Les trois exigent un en-tête `User-Agent`, faute de quoi elles répondent 403, et Commons
ne répond qu'à des requêtes en anglais.

**Deux limites techniques** : une image de plus de 25 mégapixels est refusée par l'API Slides, donc
tout se redimensionne à 2 000 pixels de large ; et cent images insérées d'un bloc échouent avec
« problem retrieving the image » alors que chacune est accessible — les images se posent par lots de
huit, après le texte.

**Les images vivent dans le dossier « Visuels » de la VSL**, jamais dans le dossier de la VSL
elle-même. Elles sont partagées par lien le temps de l'insertion, puis le partage est retiré :
Slides va chercher l'image côté serveur, mais la recopie dans la présentation.

## La review à deux

Le porte-parole relit les slides et corrige lui-même ce qu'il veut. Le reste, il le dicte par numéro
de slide, et Claude l'applique pendant qu'il continue sa relecture : les deux travaillent dans la
même présentation, en même temps.

**Une fois la review commencée, le deck ne se reconstruit plus jamais en entier.** Le script de
fabrication vide la présentation avant de la réécrire : le relancer effacerait les corrections
faites à la main. Chaque demande devient une modification ciblée de la slide concernée.

Quand une correction vaut aussi pour la source — le texte, l'emphase, le plan d'illustration —, la
source se met à jour pour les VSL suivantes, mais c'est la modification ciblée qui part dans le deck
du jour.
