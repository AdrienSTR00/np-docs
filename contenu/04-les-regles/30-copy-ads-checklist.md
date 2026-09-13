# Copy Ads Checklist

**Le contrôle qualité appliqué à chaque script, automatiquement, avant qu'Adrien le voie.**

Ce document est vivant. Il s'enrichit à chaque retour d'Adrien sur les scripts produits — c'est ce qui fait que la qualité monte batch après batch au lieu de stagner.

---

## Sa place dans le process

```
Rédaction du script
        ↓
COPY CHECKLIST  ←  appliquée sur contexte neuf, pour ne pas être juge et partie
        ↓
Échec sur un critère éliminatoire  →  réécriture automatique  →  nouveau passage
        ↓
Score consigné dans le bloc d'auto-contrôle du fichier
        ↓
Relecture d'Adrien
        ↓
Ses remarques  →  journal-corrections.md  →  promotion dans cette checklist
```

**Aucun script ne sort sans être passé par ici.** Ce que juge cette checklist, c'est le **métier** : est-ce bien écrit, bien ciblé, bien construit. Elle ne juge pas la performance — seul le spend le fait, voir `winners.md`.

---

## A. Contrôles automatisés

Trois scripts les exécutent, dans `.claude/skills/rediger-ads/scripts/` :

| Contrôle | Script | Ce qu'il vérifie |
|---|---|---|
| **Ancrage avatar** | `check_avatar.py` | Le vocabulaire du script correspond-il réellement aux verbatims de la matrice de son avatar ? |
| **Compliance** | *(à écrire)* | Termes interdits de `compliance-meta.md`, ligne par ligne |
| **Vocabulaire de VSL** | *(à écrire)* | Aucun mot de la liste interdite de la VSL ciblée |

### L'ancrage avatar en détail

`check_avatar.py` extrait les verbatims de la section « Points douloureux » de la matrice, ne conserve que les mots **discriminants** — présents dans cette matrice et absents des trois autres — et compte ceux qui apparaissent dans le script. L'AdCopy est exclue de l'analyse : elle est de référence, pas rédigée.

**Seuils :**

| Résultat | Verdict | Action |
|---|---|---|
| ≥ 4 marqueurs | ✅ ancrage correct | livrer |
| 2-3 marqueurs | ⚠️ faible | renforcer avant livraison |
| ≤ 1 marqueur | ❌ script avatar-agnostique | réécrire le corps |

**Exception statics et carrousels :** un visuel comporte 10 à 30 mots, contre 350 pour un script vidéo. Le seuil y descend à **2 marqueurs pour ✅**, et un seul marqueur bien choisi peut suffire s'il est repris d'un verbatim de la matrice.

---

## B. Critères éliminatoires

Un échec, une réécriture. Sans discussion.

| # | Critère | Test |
|---|---|---|
| E1 | **Compliance** | Aucun terme 🔴 de `compliance-meta.md` |
| E2 | **Vocabulaire de VSL** | Aucun mot de la liste interdite de la VSL ciblée |
| E3 | **Registre** | En (P), le produit n'est jamais nommé. En (S), il l'est. |
| E4 | **Personne grammaticale** | **Vouvoiement dans toutes les publicités**, y compris celles qui envoient vers la VSL 2. Le tutoiement reste la règle de la page de vente elle-même, pas de l'annonce. |
| E5 | **CTA** | Vend le clic et rien d'autre — sauf en (S) vers une page de vente directe, où l'offre peut être mentionnée |
| E6 | **Longueur** | **La durée de l'originale quand l'ad décline une winneuse.** Sinon, 180 à 330 mots — la fourchette réelle du compte, mesurée sur 41 publicités. Hors statics et carrousels. |
| E7 | **Format** | Personne et registre conformes à la famille de format (`formats.md`). Un script B-Rolls à la première personne est refusé. |
| E8 | **Hook demandé** | Le hook de la ligne du Suivi Crea est utilisé, ou une variation fidèle. Toute reformulation est justifiée dans l'auto-contrôle. |
| E9 | **AdCopy de référence** | L'AdCopy est celle de l'avatar, reprise à l'identique depuis `adcopy-par-avatar.md`. Jamais réécrite. |

---

## C. Critères notés

De 1 à 5. Moyenne sous 3,5, ou un seul critère à 1 ou 2 → réécriture.

### Q1 — Force du hook
**5** — les 3 premières secondes créent une tension réelle : une scène, une contradiction, un chiffre qui dérange. **3** — correct mais déjà lu. **1** — une affirmation plate ou une mise en contexte.

### Q2 — Ancrage avatar
**5** — le script ne pourrait fonctionner que sur cet avatar. **3** — compatible, mais transposable tel quel à un autre. **1** — contredit la matrice.
*Ce critère n'est jamais auto-évalué à vue : il est mesuré par `check_avatar.py` et le score en découle.*

### Q3 — Spécificité
**5** — scènes précises, objets, lieux, répliques : on voit la vidéo en lisant. **1** — « une situation difficile », « des méthodes inefficaces ». Rien à filmer.

### Q4 — Syntaxe et liaisons
**5** — vrais connecteurs, progression logique. **1** — bullet points déguisés en prose.

### Q5 — Rythme et oralité
**5** — alternance de longueurs, une idée par phrase, se lit à voix haute sans trébucher. **1** — subordonnées empilées.

### Q6 — Progression
**5** — chaque bloc ajoute quelque chose. **1** — le script tourne en rond pour tenir la longueur.

### Q7 — Ordre corps → cerveau
**5** — la scène et la douleur arrivent avant le mécanisme. **1** — ouvre sur l'explication neurologique.

### Q8 — Absolution
**5** — explicite et bien placée : « ce n'était pas vous, c'était la méthode ». **1** — absente, ou le script culpabilise.

### Q9 — Sobriété
**5** — factuel, démontré, aucun superlatif. **1** — « révolutionnaire », « incroyable ». Réactive l'objection arnaque.

### Q10 — Indications de tournage
**5** — en gras, dans le flux, à l'endroit exact. Le monteur n'a aucune décision à prendre. **1** — absentes.

### Q11 — Différenciation
**5** — même angle qu'une ad existante, mais scène et formulations entièrement neuves. **1** — reprend des phrases entières d'un script existant.

---

## D. Format de restitution

Dans le bloc d'auto-contrôle de chaque fichier :

```
COPY CHECKLIST
  Automatique : avatar 6 marqueurs ✅ · compliance 🟢 · vocabulaire VSL ✓
  Éliminatoires : E1✓ E2✓ E3✓ E4✓ E5✓ E6✓ E7✓ E8✓ E9✓
  Q1 5 · Q2 5 · Q3 5 · Q4 5 · Q5 5 · Q6 4 · Q7 5 · Q8 5 · Q9 5 · Q10 5 · Q11 5
  Moyenne 4,9 — livré
```

Si une réécriture a eu lieu, le critère en cause est mentionné. Un score n'est jamais affirmé sans avoir été vérifié : c'est précisément l'erreur qui a produit la première version de ce document.

---

## E. Corrections issues des retours d'Adrien

*Cette section est le cœur vivant de la checklist. Chaque remarque d'Adrien y arrive via `journal-corrections.md`, et devient une règle permanente une fois qu'elle s'est répétée.*

### 2026-09-04 — Batch 108-114

**R1. L'AdCopy ne se rédige pas.**
Jeu fixe de 3 à 5 variantes par avatar, repris à l'identique depuis `adcopy-par-avatar.md`. L'AdCopy suit l'avatar, le script suit le format et l'angle. → devenu critère éliminatoire **E9**.

**R2. Vérifier l'ancrage avatar, ne pas l'affirmer.**
J'avais noté Q2 à 5/5 sur les sept scripts. La mesure a montré 0 à 1 marqueur discriminant sur trois d'entre eux — tous Avatar 4. → création de `check_avatar.py`, et Q2 n'est plus auto-évalué mais mesuré.

**R3. L'Avatar 4 est le plus difficile à ancrer.**
Son registre est intellectuel, pas domestique : les scènes évidentes de l'Avatar 3 — la fille qui traduit, le voyage, les petits-enfants — n'existent pas chez lui. Son vocabulaire propre est : *connaissances, partager, dégradant, à la hauteur de mes idées, avoir l'air moins bête, tout essayé, cours particuliers, soirées linguistiques, institut, mémoire, encore capable d'apprendre, épater mon fils, réunions, événements mondains, natifs*.
→ **Sur tout script Avatar 4, injecter au moins deux de ces marqueurs avant même la première relecture.**

**R4. Le registre Solution Aware autorise l'offre.**
Une ad (S) qui envoie vers une page de vente directe peut nommer le produit et mentionner l'offre — c'est le cas des Ads 43 et 54, qui sont des winneuses. La règle stricte « on vend le clic » reste valable en Problem Aware. → E5 amendé.

### 2026-09-05 — Batch 115-119

**R5. Le hook dit son sujet en une seconde.**
Le scrolleur doit savoir de quoi on lui parle avant d'avoir décidé de rester. *« Vous cherchez le mot. Vous le trouvez. Trop tard »* ne dit rien ; *« Vous cherchez le mot **en anglais**, vous le trouvez trop tard »* dit tout, pour un mot de plus.
Ce n'est pas une consigne de répéter « anglais » — c'est une exigence de lisibilité obtenue au moindre coût. Un indice sans ambiguïté suffit : une scène de voyage à l'étranger, le nom d'un concurrent, une réplique en anglais.
→ **Contrôle automatisé : `check_hook.py`.** Il cherche un indice non ambigu — *anglais, anglaise, english, Duolingo, Babbel, iTalki, en VO, bilingue, anglophone*, ou une réplique en anglais dans le texte. Tout hook qui n'en porte aucun est refusé.

Attention aux faux amis, qui évoquent le sujet sans le nommer et ne comptent donc pas : *traduire*, *les mots*, *parler couramment*, *une question d'âge*, *les langues*. Ce sont eux qui font passer un hook pour clair alors qu'il ne l'est pas.

```bash
python3 .claude/skills/rediger-ads/scripts/check_hook.py 00-SOCLE/hooks-stock.md
```

*Mesuré plutôt qu'affirmé, comme l'ancrage avatar : au premier passage sur soixante hooks, **vingt-cinq échouaient**. La règle ne tenait pas sans outil.*

**R6. Le hook épouse la situation d'énonciation du format.**
Un format n'est pas un habillage, c'est une situation. Dans un **micro-trottoir on pose une question à un passant, on ne lui enseigne rien** : *« Pourquoi un enfant de 3 ans apprend l'anglais plus vite que vous »* sonne faux dans la bouche d'un intervieweur de rue, alors que *« Excusez-moi, une question : à votre avis, pourquoi… ? »* fonctionne. Même exigence ailleurs : une interview podcast raconte à la première personne, un B-Roll ASMR ne s'adresse pas frontalement, un static n'a pas de voix.
Deux garde-fous complètent la règle.

**En micro-trottoir, la question reste générale et ne vise pas la personne interrogée.** *« Pourquoi un enfant apprend l'anglais plus vite **qu'un adulte** »*, et non *« plus vite **que vous** »* : on n'arrête pas quelqu'un dans la rue pour le mettre en cause. La formulation impersonnelle laisse le passant — et le spectateur derrière lui — se reconnaître de lui-même. C'est aussi la position la plus sûre vis-à-vis de la règle 4 de `compliance-meta.md`, qui interdit de s'adresser au spectateur de façon accusatoire.

**Une question cohérente mais plate reste un mauvais hook.** *« Quel est votre niveau d'anglais ? »* a été écarté pour cette raison : la situation est juste, l'accroche est nulle.

→ **Contrôle : la phrase est-elle prononçable, telle quelle, par la personne que le format met à l'écran — et sans mettre en cause celle qui l'écoute ?**

**R7. L'angle se vérifie dans la matrice avant d'être proposé, pas au moment du script.**
La question à se poser est : *cet avatar s'interdit-il vraiment cette chose, ou sa douleur est-elle ailleurs ?*
Cas d'école, l'Avatar 3 et le voyage. Les deux lectures figurent dans la matrice, mais elles ne pèsent pas pareil. Il **raye des destinations sans se l'avouer** (« il rature une destination de sa liste chaque fois qu'il regarde une carte »), et il **part quand même, mais diminué** (« deux ou trois voyages par an, presque toujours en France ou dans des pays où on parle français », « au comptoir de l'hôtel il se met en retrait »). La couche profonde n'est pas le voyage manqué, c'est la dépendance : *« on voyage à deux au lieu de voyager à un et demi »* — verbatim de la matrice, et meilleur matériau de hook que la destination rayée.
→ **Contrôle : citer la ligne de la matrice qui porte le pain point, avant de proposer l'angle. Pas de citation, pas d'angle.**

### 2026-09-05 — Batch VSL 2

**R8. Le sujet arrive le plus tôt possible — au plus tard dans les deux ou trois premières secondes.**
C'est un gradient, pas une règle binaire, et Adrien l'a précisé lui-même : « pas forcément le placer en premier, mais qu'on comprenne très rapidement de quoi on parle. Deux, trois secondes, ça peut suffire — mais dans l'idéal, si on peut faire mieux, autant faire mieux. »

R5 exige que le sujet soit dit ; R8 exige qu'il soit dit **tôt**. Il a réécrit *« Elena rêvait de faire le tour de l'Australie avec son chien. Ce qui l'a retenue, ce n'était pas l'argent, c'était son anglais »* en *« **À cause de son anglais**, Elena n'a jamais osé partir faire le tour de l'Australie avec son chien, ce dont elle rêvait pourtant depuis des années »*. Même contenu, même longueur — mais il fallait attendre la fin de la phrase pour comprendre le sujet, et il arrive maintenant d'emblée.

Sa consigne : *« il faut que tu prennes le réflexe d'être ultra bon dans les premières secondes »*. Construire un hook comme une phrase française bien balancée, avec la chute à la fin, est une erreur de média : sur un fil qui défile, la chute est rarement atteinte.
→ **Contrôle : lire le hook à voix haute et compter. Si le sujet n'est pas posé au bout de trois secondes, réécrire. Entre une et trois secondes, chercher si on peut faire mieux sans casser la phrase.**

**R9. On ne complète jamais le témoignage d'un client réel par de l'invention.**
Les corps des mails et des WhatsApp du texte de vente sont des images. Quand seule l'identité est lisible, le hook s'arrête à ce qui est attesté et le manque est signalé — il ne se comble pas par du plausible. Un détail inventé sur une personne qui existe est un risque de compliance et une faute tout court.

### 2026-09-06 — Mesure sur le compte

**R10. La longueur cible vient des scripts réels, pas d'une convention.**
Mesure sur 41 scripts entre Ads 57 et Ads 107 : médiane **378 mots**, intervalle interquartile **286-440**, minimum 116. La moitié du compte tient entre 286 et 440 — d'où la cible **280-450** qui remplace l'ancien 300-400.

Deux nuances relevées à la mesure. Les **dix scripts les plus récents sont plus courts** — médiane autour de 250 — ce qui est soit une évolution volontaire des formats, soit une dérive à surveiller. Et les quatre scripts de plus de 700 mots sont probablement des documents contenant plusieurs variantes à la suite : la moyenne de 435 est donc surévaluée, seule la médiane est fiable.

**Et cette règle cède devant une consigne d'Adrien.** S'il demande plus court ou plus long sur une ad précise, c'est sa demande qui s'applique.

### 2026-09-06 — Le métier de l'AdCopy

*Sept règles tirées de la construction du jeu de l'Avatar 1, avec l'AdsCopy 80 comme modèle.*

**R11. L'AdCopy avance par paliers courts, et se termine toujours par un CTA.**
La charpente éprouvée, celle de l'AdsCopy 80 : une accroche qui plante une identité ou une phrase entendue → la liste des fausses méthodes → un pivot en majuscules (*On n'APPREND pas l'anglais. On l'ABSORBE.*) → l'analogie de l'enfant qui absorbe le français → le mécanisme nommé → l'annonce de la présentation → **le CTA**.
Le CTA n'est jamais facultatif, quelle que soit la longueur. Formulation standard : *« ➡️ Cliquez sur le bouton "En savoir plus" pour découvrir la présentation, disponible gratuitement aujourd'hui. »*
→ **Contrôle : une AdCopy sans CTA final est incomplète, point.**

**R12. Varier franchement les longueurs à l'intérieur d'un même jeu.**
Quinze lignes pour l'une, trois pour l'autre. C'est ce qui empêche le jeu de sonner comme quatre fois la même chose. Un jeu dont toutes les variantes font la même taille est mal construit.

**R13. Toutes les variantes ne dévoilent pas le mécanisme au même endroit.**
Certaines coupent avant — sur les trois secondes de retard, en laissant le manque entier. D'autres vont jusqu'à « absorber » sans dire comment. **L'endroit où l'on s'arrête est lui-même une variable de test**, au même titre que l'angle.

**R14. Les objections à lever sont les méthodes concurrentes, pas les peurs supposées.**
Écrire *« sans grammaire, sans exercices répétitifs, sans applications mobiles, sans séries en VO, sans professeur particulier »* — ce sont les objections réelles du corpus. Pas *« sans avoir à parler devant qui que ce soit »*, qui répond à une peur que le lecteur n'a pas encore formulée à ce stade.

**R15. Un verbatim doit être attribué, et il se met au présent.**
Trois citations posées sans introduction laissent le lecteur se demander qui parle. Les annoncer : *« Elles le racontent presque toutes avec les mêmes mots : »*.
Et les écrire **au présent** — *« Je suis juste tétanisée »*, pas *« j'étais tétanisée »*. Au passé, c'est un témoignage clos qui concerne quelqu'un d'autre ; au présent, la lectrice se reconnaît en train de le vivre.

**R16. Reprendre les formulations des VSL plutôt que les réinventer.**
Le mécanisme de la Dépendance à la Traduction est déjà écrit, et bien écrit, dans les textes de vente. Puiser dedans mot pour mot :
> *« Cela crée trois secondes de retard à chaque phrase. »*
> *« Ces trois secondes créent un stress qui vous paralyse : aucun mot ne sort de votre bouche. »*
> *« Pendant que vous traduisez les premiers mots dans votre tête, la phrase est déjà finie. Vous avez toujours un train de retard. »*
**Trois secondes, jamais deux** — c'est le chiffre des VSL. Une reformulation personnelle est presque toujours plus faible qu'un passage déjà éprouvé en conversion.

**R17. La liste des ❌ méthodes ne fonctionne pas sur tous les avatars.**
Elle est calibrée pour l'Avatar 4, qui a dépensé des milliers d'euros en formations premium et porte une déception de consommateur. L'Avatar 1 ne s'est pas brûlée sur dix méthodes : elle a évité pendant vingt ans. Sa matrice le dit — *« un argumentaire "voici pourquoi Babbel vous a fait échouer" lui parle beaucoup moins qu'à l'avatar cadre. Ce qui la fait s'arrêter, c'est qu'on nomme sa dépendance et sa honte. »*
→ **Contrôle : avant d'écrire une AdCopy, vérifier dans la matrice si l'avatar a payé ou s'il a évité. La démolition de concurrents ne sert que le premier cas.**

**R18. Une AdCopy qui nomme un mécanisme se décline par VSL.**
La V4 de l'Avatar 1 — *« Comment la CIA forme ses agents à parler 5 langues en 12 mois »* — est verrouillée sur la VSL 1 : la CIA fait partie de son vocabulaire exclusif. Utilisée sur une ad qui envoie vers la VSL 2 ou 3, elle casse la continuité entre l'annonce et la page, et viole le critère **E2**.

Toute AdCopy nommant un mécanisme existe donc en trois versions, suffixées **a / b / c** :

| | VSL | Mécanisme à nommer | Adresse |
|---|---|---|---|
| **a** | 1 | Protocole Phoenix, CIA, circuit narratif | vous |
| **b** | 2 | Mini-Histoires Hollywoodiennes, cerveau accro | **tu** |
| **c** | 3 | Lecture Immersive, Kató Lomb, seize langues | vous |

→ **Contrôle : avant de reprendre une AdCopy, vérifier vers quelle VSL l'ad envoie, et prendre la variante correspondante.**

**R19. Les publicités vouvoient toujours, même vers la VSL 2.**
Le problème était réel : la VSL 2 tutoie, les jeux d'AdCopy vouvoient, et une ad de l'Avatar 1 vers la VSL 2 échouait mécaniquement à E4. Adrien a tranché — *« on ne prend pas la tête avec le vouvoiement, en général tu mets du vouvoiement et c'est très bien »*.

**Le tutoiement reste une caractéristique de la page de vente, pas de l'annonce.** Une seule conséquence à surveiller : le raccord de ton entre une ad qui vouvoie et une page qui tutoie. Adrien l'assume, et ça simplifie tout le reste — un seul jeu d'AdCopy par avatar, quelle que soit la VSL visée, et seule la variante de mécanisme change.

**R20. La durée cible d'une itération est celle de l'originale.**
Mesure des fichiers vidéo du Drive : le compte tourne à **93 s de médiane**, et **les winneuses à 123 s** — Ads 19 à 199 s, Ads 23 à 195 s, Ads 26 à 140 s, Ads 28 à 175 s. Deux à sept fois plus que les médianes du marché américain.

L'explication tient au métier : NarratiFluent vend une méthode à 297 € à des gens de soixante ans qui ont besoin de comprendre un mécanisme avant de cliquer. Les publicités d'ecommerce qui tournent en dix-sept secondes ne font pas le même travail.

→ **Contrôle : avant d'écrire une itération, lire la durée de l'originale dans le Drive et caler le nombre de mots dessus.** Les repères par famille de format restent utiles pour les publicités qui n'itèrent rien, mais ils cèdent devant la mesure du compte.
