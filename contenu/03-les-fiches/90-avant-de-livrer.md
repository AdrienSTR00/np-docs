# La liste de vérification avant de livrer

Adrien a demandé cette page après avoir reçu une publicité dont le 9:16 était bon et dont les deux
autres formats étaient inutilisables : « identifie la cause de cette erreur et mets-toi une
check-list pour vérifier à chaque fois si elle n'est pas présente. Plus jamais tu me proposes ça. »

---

## La cause, nommée

**Le 9:16 est le format natif. Il ne subit aucun recadrage, donc il est toujours bon.** Le 1:1 et le
16:9 passent, eux, par une décision de cadrage, et c'est là que les défauts se logent. En ne
regardant que le 9:16 avant de livrer, on ne les voit jamais — ils arrivent chez Adrien.

Le défaut précis : au-delà d'un tiers de surface perdue, le montage posait l'image sur un fond
flou. Le personnage devenait minuscule au milieu de l'écran et les sous-titres deux fois plus
petits que sur le 9:16. Cela n'arrivait **que** sur les deux formats dérivés.

---

## Le contrôle, mécanique

```bash
python3 04-PRODUCTION/scripts/verifier_formats.py 123 125 128 129
```

Il mesure ce qui doit être identique — durée d'image, durée de son, écart entre les deux — et
fabrique une planche où **les trois formats se regardent côte à côte, aux mêmes instants**. Cette
planche se regarde. Ce n'est pas un rapport à parcourir, c'est une image où un défaut de cadrage
saute aux yeux en une seconde.

---

## Ce qu'on vérifie, dans l'ordre

1. **Les trois formats existent**, et portent la même durée à huit centièmes près.
2. **Aucun fond flou, aucune bande noire.** Chaque format remplit l'écran.
3. **Les sous-titres ont la même taille apparente** sur les trois — ils sont recalculés par format,
   jamais redimensionnés depuis le 9:16.
4. **Aucune image figée** sur un visage : `freezedetect` ne doit rien signaler ailleurs qu'en toute
   fin de publicité.
5. **L'appel à l'action** est présent, à la bonne taille, et les chevrons clignotent.
6. **Aucun texte en double** : le sous-titre se tait pendant la fenêtre de l'appel à l'action.
7. **Aucun visage étranger** dans un plan de coupe, sur les formats qui mettent en scène une
   personne précise.
8. **Le poids** de chaque format est sous cinquante mégaoctets.

---

## Le réflexe qui manquait

**Ne jamais juger une publicité sur son 9:16.** Le format natif ne dit rien des deux autres : c'est
exactement le format sur lequel aucune décision n'est prise.

---

## Le process de montage, et les trois verrous

Adrien a exigé que ce ne soit pas une bonne intention mais un mécanisme : « si je vois que tu te
trompes encore, ça veut dire que tu ne l'as pas fait ». Trois verrous sont donc posés dans le code,
et aucun ne dépend de ma vigilance.

### 1. Un seul montage à la fois sur une publicité

`monter()` pose un verrou dans le dossier de la publicité, portant le numéro du processus. Un
second montage sur la même ad est **refusé**, avec le numéro du premier. C'est la cause du plus gros
gâchis du projet : deux chaînes lancées en parallèle écrivaient dans le même dossier, et les trois
formats livrés venaient de trois montages différents.

Le piège à connaître : `pkill` sur le script Python ne suffit pas, la boucle `bash` qui l'enveloppe
relance aussitôt l'itération suivante. **Tuer la boucle, pas le processus.**

### 2. Les trois formats se rendent d'une seule traite

```bash
python3 04-PRODUCTION/scripts/monter_ads_NNN.py "9:16" "1:1" "16:9"
```

Jamais format par format à des moments différents. Les trois fichiers doivent porter des dates à
quelques minutes les unes des autres.

### 3. La livraison refuse ce qui ne concorde pas

`livrer_ad.controler()` vérifie avant tout dépôt : les trois formats existent, leurs dates sont à
moins de vingt minutes, leurs durées sont identiques à un dixième de seconde. Sinon **rien ne part**,
ni vers le Drive, ni vers Adrien.

---

## Ce qui reste à ma charge

Regarder la planche des trois formats. Les verrous attrapent les mélanges et les écarts de durée ;
ils ne voient pas qu'un cadrage est laid ou qu'un visage est coupé. C'est la seule partie du
contrôle qui demande un œil, et c'est pour ça qu'elle vient en dernier, quand tout le reste est déjà
garanti.

---

## L'habillage se fabrique dans les trois formats, et se regarde

Cartes de fin, appels à l'action, sous-titres : **aucun ne se donne en pixels absolus.** Un 9:16
fait 1920 de haut, un 1:1 et un 16:9 n'en font que 1080 — toute mesure verticale fixe déborde, et
toute taille calculée sur la hauteur rétrécit de 44 %.

La règle, appliquée dans `carte_bouton()` et `appel_a_laction()` :

- la largeur du bouton est une fraction de la largeur du cadre, et **la taille de police se cherche**
  pour que le texte y tienne, marges comprises ;
- les positions verticales sont des fractions de la hauteur ;
- le texte se dimensionne sur le **petit côté** ;
- la carte s'arrête où commence la bande des flèches — 66 % de la hauteur, la même valeur des deux
  côtés.

**Et on les regarde avant de monter.** Une carte de fin se rend en une seconde dans les trois
formats ; il n'y a aucune raison de la découvrir à la fin d'un montage de dix minutes.
