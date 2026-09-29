# Le swiping et le squelette

> Comment on analyse un texte de vente existant, ce qu'on en extrait, et comment on écrit le
> nouveau texte sur ce squelette.

Écrire un texte de vente en reprenant la structure d'un texte existant : on analyse comment ses
éléments de persuasion sont agencés, on en extrait le squelette, et on remplit ce squelette avec la
matière du document de préparation.

## Ce qu'on reprend, et ce qu'on ne reprend pas

**Le squelette, ce sont les fonctions, pas les mots.** On reprend la suite des éléments de
persuasion et leur place dans l'enchaînement. Les phrases du nouveau texte s'écrivent librement et
peuvent n'avoir aucun rapport avec celles du modèle. Le nombre de phrases ne se reprend pas non
plus : trois questions en rafale dans le modèle ne donnent pas forcément trois questions ici.

**Adrien fournit le texte à swiper.** Claude ne le choisit jamais.

**À éviter : le squelette d'une VSL déjà en ligne pour le même produit.** Ces textes fournissent des
éléments — offre, urgence, closing, phrasé —, pas la structure.

### Filtrer les formules propres à la niche d'origine

Un texte make money parle à un lecteur assommé de promesses ; le professionnel qui bloque en anglais
ne l'est pas. Ce qui saute : la lassitude des promesses, la révélation annoncée, l'objection sur
l'intérêt du vendeur, la justification d'un prix bas, et les objections que personne ne formule.

**L'urgence ne se met pas dans le lead.** Annoncer qu'on cherche quinze personnes avant d'avoir posé
le problème est trop direct dans cette niche. À cet endroit, une rareté sans compte à rebours suffit
(« cette présentation n'est pas en ligne sur mon site ») ; le bloc d'urgence complet arrive au
moment de l'offre.

## Étape 1 — Extraire et numéroter

1. Extraire le texte : `pypdf` avec `extraction_mode="layout"` pour un PDF, export `text/plain` par l'API Drive pour un Google Doc.
2. Retirer les indications de montage et les fiches produit internes : on n'analyse que ce qui est dit ou affiché au prospect.
3. Numéroter chaque paragraphe : P001, P002… Quand un paragraphe recolle deux phrases qui appartiennent à deux blocs différents, le couper : P042a, P042b.
4. Compter les mots de chaque paragraphe, symboles seuls exclus.

## Étape 2 — Découper en sections et en blocs

1. Ranger le texte dans les sections : headline et sous-titre, hook, lead, background story et crédibilité, mécanisme du problème, mécanisme de la solution et découverte, démonstration, close, FAQ. Le close se découpe en sous-parties : pourquoi il partage, pré-offre, construction de l'offre, prix, garantie, appels à l'action, après le premier appel à l'action.
2. Découper chaque section en blocs. Pour chaque bloc : un titre, le premier et le dernier paragraphe, le nombre de mots et la part du texte, la fonction, l'émotion visée.
3. Noter la part de chaque section et la comparer à la structure Hero Journey (mécanismes 35 %, close 30 %). Une section absente s'écrit « absente ».

## Étape 3 — Étiqueter chaque segment

**Un segment, c'est une phrase ou un petit groupe de phrases qui fait une seule chose.** Chaque
segment reçoit de une à quatre étiquettes, la dominante en premier, et son **rôle** en une ligne,
écrit en termes transposables à un autre produit : « le soupçon de pyramide écarté, et le principe
nommé », pas « il dit que ce n'est pas un MLM ».

Le vocabulaire est fermé : les 62 étiquettes en 8 familles de l'analyse de référence. Une étiquette
nouvelle s'ajoute à ce lexique avec sa définition.

Trois distinctions à respecter :

- **crédibilité** : ce qui rend le porte-parole digne d'être écouté (parcours, palmarès, classement) ; **preuve d'autorité** : une source extérieure reconnue qui parle ou garantit ;
- **preuve par l'expérience** : une situation que le lecteur a vécue ou observée lui-même ;
- **élément de big idea** : le fil conducteur, qui peut revenir partout, pas seulement dans le lead.

Contrôle avant de passer à la suite : chaque paragraphe est couvert par un segment et un seul, dans
l'ordre ; aucun segment n'est à cheval sur deux blocs ; aucune étiquette n'est hors du lexique.

## Étape 4 — Tracer les fils

Pour chaque fil, lister les segments où il apparaît et décrire en une ou deux phrases comment il
revient :

- la big idea, sachant qu'un texte peut en avoir deux qui se passent le relais ;
- les deux mécanismes : où ils sont posés, redits, transformés en preuve ;
- chaque type de preuve, et le moment où il arrive ;
- la curiosité et les boucles : où chacune est ouverte, relancée, fermée, ou jamais fermée ;
- l'ennemi commun et la comparaison avec les autres méthodes ;
- la promesse : combien de fois le résultat chiffré revient, et où ;
- l'offre : teasing et annonce du produit, teasing et annonce des bonus, value stacking, prix ;
- la rareté, l'urgence, la raison de partager ;
- le lecteur : objections, empathie, flatterie, appartenance, douleur.

Terminer par le poids de chaque élément : la part du texte couverte par chaque famille, puis les 20
étiquettes les plus présentes.

## Étape 5 — Livrer l'analyse de structure

Le document d'analyse compte cinq parties, avec un saut de page avant chacune sauf la première :

1. le modèle : fiche, big idea, mécanismes, structure en pourcentages ;
2. comment les fils s'emmêlent ;
3. le squelette : pour chaque bloc, sa fonction, puis ses segments avec étiquettes et rôle ;
4. le texte étiqueté : chaque segment sous ses étiquettes, couleur par famille, éléments de big idea surlignés ;
5. les étiquettes et leurs définitions.

La version du dépôt reprend les parties 1, 2, 3 et 5. **Le texte du swipe n'entre jamais dans le
dépôt.** L'analyse n'est pas soumise à Adrien avant la rédaction : on enchaîne, et elle est livrée
avec le texte.

## Étape 6 — Écrire sur le squelette

Prendre le squelette bloc par bloc, segment par segment. **Chaque segment du modèle produit un
segment du texte qui remplit la même fonction**, avec la matière du nouveau texte :

- big idea, lead et headlines : étape 2 de la préparation ;
- histoire du porte-parole : étape 3 ;
- promesse et offre, urgence comprise : étape 4 ;
- preuves : étape 5, chacune à la place indiquée dans sa fiche, avec sa formulation et ses limites ;
- objections : étape 7, levées en passant, à l'endroit où le doute apparaît.

La headline se choisit à ce moment-là, parmi celles de l'étape 2, dans le moule de la headline du
modèle.

Quand la promesse a plusieurs paliers, **chaque palier se dit séparément**, avec son délai et ce
qu'il change concrètement dans le quotidien du lecteur.

### Reprendre les textes existants du même produit

- **L'offre, les bonus, le récapitulatif de valeur, le prix, l'urgence, la garantie, l'après-clic et le closing se reprennent presque tels quels**, phrasé compris : c'est la même offre. On retire seulement ce que la préparation a écarté.
- **L'histoire du porte-parole se reprend dans le texte le plus récent et le plus affûté**, avec ses manières de parler et ses groupes de phrases.
- **Ce qui change, ce sont les arguments** : exemples, situations, bénéfices et descriptions de bonus suivent l'avatar du nouveau texte.
- **Une question déjà traitée se recopie mot pour mot**, y compris le prénom de la personne qui la pose dans la FAQ. Improviser une réponse neuve sur une question déjà résolue est une faute, même quand la nouvelle version est correcte.

### Adapter le squelette à la niche

Garder la fonction du segment, changer sa forme quand la niche l'exige. Ce qui ne se transpose pas
se remplace par l'équivalent le plus proche, au même endroit du texte, et se signale dans le compte
rendu. **Une boucle ouverte se ferme toujours**, même si le modèle la laisse ouverte.

### Ce qui ne s'écrit pas

- Rien d'inventé : un souvenir, une humiliation, un chiffre ou un témoignage absent de la préparation ne s'écrit pas. Un emplacement de preuve à venir se marque `[PRÉNOM]`, `[MÉTIER]`, avec une note.
- Tout ce que la préparation exclut : la rubrique « ce qu'on ne fait pas », la liste « à ne pas dire » de l'urgence, les limites de chaque preuve.
- Aucune démonstration de génération d'histoire en direct : on montre des histoires réelles, et la plateforme filmée depuis l'ordinateur, vers la fin du texte.
- Un testeur est présenté comme « testeur de la première version ».

### La mise en page du texte

- Une à deux phrases par ligne, chaque ligne devenant une slide.
- Les notes de production et les points à confirmer en paragraphe séparé, surligné en jaune. Chaque preuve à vérifier reçoit une note « À VÉRIFIER avant diffusion ».
- Les répliques des témoignages vidéo en violet, le nom en gras.
- Les phrases en anglais en italique.
- Les sources en fin de texte, sur une nouvelle page.

## Étape 7 — Le contrôle avatar

Le texte terminé passe au filtre de chaque avatar visé, **avant le dépôt, et sans attendre qu'Adrien
le demande**.

```bash
python3 05-FUNNEL/00-METHODE/scripts/controler_avatar.py <texte.md> <n° avatar>
```

1. Relire chaque mot hors registre et chaque mot interdit dans son contexte, et le remplacer par le mot de l'avatar. Les noms fixes de l'offre restent tels quels.
2. Donner une place aux mots du segment qui sont à zéro.
3. Rattacher chaque situation précise prêtée à l'avatar à sa source : un verbatim, une ligne du document de données, ou la matrice. **Ce qui est extrapolé se signale comme tel** dans le compte rendu à Adrien.
4. Relire le texte avec la matrice ouverte : son quotidien, ses phrases blessantes, sa transformation rêvée, ses mots. Reprendre ses situations et ses phrases là où elles remplissent la fonction du segment.
