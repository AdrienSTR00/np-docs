# Anti-patterns — ce qu'il ne faut plus jamais produire

Règles stabilisées. Elles entrent dans le contexte de **chaque** génération et sont vérifiées avant sortie.

Origine : les prompts correctifs 3, 4 et 5 de l'ancien process (« Rédaction ADS Prompts ») — c'est-à-dire les erreurs qu'Adrien devait corriger à la main à chaque ad. Elles sont désormais traitées en amont.

Nouvelles règles : voir `journal-corrections.md`, consolidé ici tous les 2-3 batches.

---

## ❌ 1. Le script trop long

L'ancien prompt 3 existait pour ça. **300 à 400 mots**, ni plus ni moins, soit environ 2 minutes de vidéo. Un script de 700 mots n'est pas « plus complet », il est inutilisable.
Vérifié automatiquement : le compte de mots figure au bloc d'auto-contrôle.

## ❌ 2. Parler du prix, de l'offre ou de la garantie

L'ancien prompt 4. Une publicité **vend le clic, rien d'autre**. Jamais le prix, jamais le contenu du programme, jamais la réduction, jamais la garantie, jamais les bonus.
Le CTA invite à découvrir la présentation en ligne. Point.
*Cause racine : donner la VSL brute au générateur. C'est pour ça qu'on ne le fait jamais — seule la section INPUT des matrices est chargée.*

## ❌ 3. Les phrases en bullet points déguisés

L'ancien prompt 5. Des phrases courtes empilées sans connecteurs, qui ressemblent à des notes plutôt qu'à un texte oral :

> *« Vous comprenez l'anglais. Vous ne le parlez pas. Le problème est ailleurs. Voici pourquoi. »*

C'est du télégraphe. Il faut des mots de liaison et une vraie progression :

> *« Vous comprenez l'anglais — les séries, les mails, les articles. Mais dès qu'il faut ouvrir la bouche, plus rien ne sort. Et si le problème n'était pas du tout là où vous croyez ? »*

## ❌ 4. Les titres, préambules et commentaires

La sortie ne contient que le script et les indications de tournage. Pas de « Voici le script », pas de « Variante 1 : approche émotionnelle », pas de commentaire final sur les choix de rédaction. Le bloc d'auto-contrôle est le seul méta-texte autorisé, et il est à sa place, à la fin.

## ❌ 5. Le générique au lieu du spécifique

Premier symptôme d'un script faible.

| ❌ Générique | ✅ Spécifique |
|---|---|
| « une situation embarrassante » | « une pharmacie à Madrid, un dimanche » |
| « des méthodes qui n'ont pas marché » | « trois ans de Duolingo, tous les matins » |
| « votre famille » | « votre gendre, que vous n'avez jamais entendu parler d'autre chose que du temps qu'il fait » |
| « vous perdez du temps » | « quarante minutes sur une notice que vous devriez lire en dix » |

Les matrices sont pleines de verbatims réels. Les utiliser.

## ❌ 6. Le mécanisme avant la douleur

L'argumentaire NarratiFluent est cognitif ; la douleur du prospect est corporelle et relationnelle. **On entre par le corps ou par la scène, on sort par le cerveau.** Jamais l'inverse.

> ❌ « Votre cerveau traduit en sept étapes, ce qui crée une latence de trois secondes… »
> ✅ « Vous ne dormez pas la nuit d'avant. Et le lendemain, rien ne sort. Il y a une raison mécanique à ça. »

## ❌ 7. Mélanger les vocabulaires de VSL

Une ad qui envoie vers la VSL 2 et qui parle du Protocole Phoenix casse la continuité et fait chuter la conversion. Chaque encart de VSL a sa liste de **vocabulaire interdit** — elle est vérifiée mot à mot avant sortie.
Rappel : la VSL 2 **tutoie**, les VSL 1 et 3 **vouvoient**. Se tromper de personne est aussi grave que se tromper de mécanisme.

## ❌ 8. Nommer le produit en registre Problem Aware

Une ad (P) fait de l'éducation sur le mécanisme. Si « NarratiFluent » apparaît, ce n'est plus une ad (P). Éliminatoire.

## ❌ 9. Le ton marketing et les superlatifs

« Révolutionnaire », « incroyable », « la méthode ultime », « vous n'en reviendrez pas ». Ce marché est au stade 4-5 de sophistication : il a tout entendu et il ne croit plus rien. Les superlatifs déclenchent l'objection « encore une arnaque », qui pèse 9 % des hésitations.
Le registre juste est **factuel, sobre, démontré**.

## ❌ 10. L'avatar interchangeable

Un script qui fonctionnerait aussi bien pour les quatre avatars n'est bon pour aucun. Le vocabulaire, les situations, l'âge, les références doivent être ceux de la matrice ciblée.
Test : si on remplace l'avatar 4 par l'avatar 2 sans rien changer au texte, le script est raté.

## ❌ 11. Promettre la vitesse plutôt que la facilité

Réflexe de copywriting standard, faux sur ce marché. Les données sont explicites : ils ne veulent pas que ce soit rapide, ils veulent que ce soit **facile et agréable**. « Seulement 20 minutes par jour » est un argument faible sur des retraités qui ont du temps ; « sans effort et sans contrainte » est décisif.

## ❌ 12. Sauter l'absolution

Sur un public qui attribue ses échecs à lui-même, une ad qui ne déculpabilise pas rate l'étape la plus rentable. « Ce n'est pas vous, c'est la méthode » est l'argument que les acheteurs citent eux-mêmes comme déclencheur.

## ❌ 13. Rédiger une AdCopy neuve à chaque ad

L'AdCopy ne se rédige pas ad par ad. Chaque avatar possède un **jeu fixe de 3 à 5 AdCopy et de 3 Headlines**, repris tel quel sur toutes les publicités qui le visent. Deux ads destinées au même avatar portent exactement les mêmes AdCopy — seule la créa change.

**L'AdCopy suit l'avatar. Le script suit le format et l'angle.** La Description est commune à tout le compte.

Les jeux de référence sont dans `00-SOCLE/adcopy-par-avatar.md`. On y va chercher le jeu de l'avatar concerné et on le recopie à l'identique.

Rédiger une AdCopy neuve n'est justifié que si l'avatar n'en possède pas encore (c'est le cas des Avatars 1 et 2), ou sur demande explicite d'Adrien pour en tester de nouvelles.
