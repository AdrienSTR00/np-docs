# Préparation du texte

> Les sept étapes qui produisent la matière du texte de vente : mécanisme, big idea, créateur,
> offre, 50 preuves, headlines, 50 objections. Aucune ligne du texte ne s'écrit ici.

Cette étape produit la matière, pas le texte. Pas même le lead.

## Étape 0 — Créer le document

```bash
python3 05-FUNNEL/00-METHODE/scripts/creer_preparation.py "NarratiFluent" 4
```

Le script dépose dans le dossier du funnel un document « Préparation Funnel NarratiFluent (numéro) »
**à trous** : les intitulés d'étape et les questions en puces, rien d'autre. Sous chaque question,
deux lignes vides tiennent lieu d'emplacement, sans mention « à remplir ».

Chaque étape commence sur une nouvelle page. Sur un document existant qui n'en a pas :

```bash
python3 05-FUNNEL/00-METHODE/scripts/creer_preparation.py --sauts-de-page <doc_id>
```

Les réponses s'écrivent ensuite une par une, ou en lot :

```bash
python3 05-FUNNEL/00-METHODE/scripts/remplir_preparation.py <doc_id> "Quelle est la promesse" "..."
python3 05-FUNNEL/00-METHODE/scripts/remplir_preparation.py <doc_id> --lire
```

Le script refuse d'écraser une réponse déjà écrite ; `--remplacer` la réécrit. `--markdown` accepte
une réponse rédigée en markdown, ce qui est le cas des synthèses.

**Après chaque écriture, relire le document** et vérifier cinq choses : aucune phrase coupée, seules
les questions portent une puce, aucune ligne vide entre deux puces qui se suivent, une ligne vide
entre deux paragraphes, et un saut de page devant chaque titre d'étape à partir du deuxième.

## Étape 1 — Le mécanisme unique

**Sur NarratiFluent, le mécanisme du problème ne bouge pas** : la Dépendance à la Traduction. On
reprend sa formulation du texte précédent.

**Ce qui change à chaque texte, c'est le mécanisme de la solution** : le nom sous lequel la méthode
est présentée, et la scène ou la source qui l'introduit. Il se décide ici, jamais à la rédaction.

| Texte | Mécanisme de la solution |
|---|---|
| 1 | le Protocole Phoenix, document déclassifié d'une agence gouvernementale américaine |
| 2 | les Mini-Histoires Hollywoodiennes |
| 3 | la Lecture Immersive, de Kató Lomb |
| 4 | la lecture en situation, d'après l'entraînement de la Légion étrangère |

Les règles :

- un nom fort, distinct des textes déjà en ligne. « Des histoires courtes » ne suffit pas ;
- pour un avatar professionnel, un mécanisme sobre, sans sensationnalisme ;
- une big idea portée par un groupe prend un groupe que les Français connaissent et respectent ;
- le pont entre ce groupe et la méthode ne repose que sur des faits vrais et sourcés : ce que le groupe fait réellement, les éléments qui rejoignent la méthode relevés au nom du porte-parole, une phrase franche sur ce qui n'est pas leur méthode, et jamais de partenariat suggéré.

### La grille de sélection

Cinq questions. Un mécanisme qui échoue à l'une d'elles est écarté, quel que soit son panache.

| | |
|---|---|
| **Croyable sans preuve ?** | le lecteur doit pouvoir y adhérer avant qu'on lui montre une étude |
| **Nommable en deux à quatre mots ?** | « la Dépendance à la Traduction » tient ; une périphrase de douze mots ne se retient pas |
| **Absout-il le lecteur ?** | il doit dire « ce n'est pas vous, c'est la méthode » : c'est l'argument que les acheteurs citent eux-mêmes comme déclencheur |
| **Libre ?** | aucun concurrent direct ne l'emploie |
| **Donne-t-il une solution qui n'est pas juste son inverse ?** | « le problème c'est X, la solution c'est ne pas faire X » n'est pas un mécanisme |

### La promesse

Une phrase, qui intègre la promesse, le mécanisme et une dimension de temps — le temps quotidien ou
le délai de résultat. Pas de superlatif. **Demander à Adrien avant de générer :** il connaît souvent
déjà la direction, et cinq propositions sur une promesse qu'il a en tête font perdre un tour.

## Étape 2 — La big idea

C'est ici que se joue la nouveauté d'un texte à l'autre, quand le mécanisme du problème ne bouge
pas. La big idea est l'angle qui introduit le texte et lui sert de fil : une success story, un fait
scientifique, un événement, une étude de cas, un secret, un ennemi commun.

**Produire plusieurs propositions, et qu'elles s'excluent.** Cinq variantes du même angle ne sont pas
cinq propositions. Chaque proposition porte quatre choses, et la quatrième n'est pas optionnelle :

- son nom ;
- les premières lignes réelles de l'ouverture, pour qu'on entende le ton ;
- ce qu'elle fait mécaniquement, et ce qu'elle ferme ;
- **la headline qui irait avec**.

Sans headline, Adrien ne peut pas juger : c'est elle qui montre par où le texte entre. La big idea
retenue repart ensuite avec **trois à cinq headlines** dans sa synthèse, qu'il lit pour voir
l'éventail des possibilités. La headline définitive, elle, se fige à la rédaction.

### Le déroulé : un brainstorm, puis une synthèse sur ordre

1. **Aller chercher la matière** : les matrices avatar, les documents de données du Drive, les textes de vente précédents, et la recherche web dès qu'un chiffre peut soutenir un angle.
2. **Brainstormer à deux.** Je propose des angles avec leur headline, Adrien réagit, écarte, apporte les siens. Plusieurs tours, et rien ne s'écrit dans le document pendant ce temps.
3. **Rédiger la synthèse sur ordre, jamais d'initiative.** Lancer la synthèse avant qu'il le demande, c'est figer un angle qu'il est encore en train de faire bouger.
4. **Il la relit** et vérifie qu'elle est conforme à ce qui s'est dit.
5. **Après validation, elle entre dans le document**, et on enchaîne.

### La forme de la synthèse

Le lead se note **en éléments ordonnés, pas en prose rédigée** : des puces avec les mots-clés de ce
qui sera dit, dans l'ordre où ce sera dit. Seules les phrases à prononcer mot pour mot sont citées
telles quelles, et signalées comme telles.

Aucun commentaire de conversation n'entre dans le document. Une section dit **ce qu'on ne fait pas** :
les angles écartés, le vocabulaire interdit, les preuves qu'on n'utilisera pas. C'est ce qui évite
qu'ils reviennent à la rédaction.

Ses rubriques, dans l'ordre : le nom, le type d'angle, l'idée en une phrase, les éléments du lead,
les grands blocs, le twist, ce qu'on ne fait pas, les sources, trois à cinq headlines, les points à
trancher.

**Chaque source se vérifie une par une, et chaque lien s'ouvre.** Un modèle en invente de très
crédibles. Pour chaque source retenue : le passage qu'elle soutient, la référence complète, le lien,
et ce que la source ne dit pas quand elle est plus faible que ce qu'on voudrait lui faire dire.

## Étape 3 — Description du créateur

Une seule réponse complète, qui porte trois questions : qui est le créateur, quelles sont ses
qualités et ses réussites, et **quel est l'ennemi commun**. Les trois se répondent dans un même
récit découpé en temps, pas en trois listes.

L'ennemi commun n'est pas décoratif : c'est lui qui permet au texte d'accuser sans accuser le
lecteur. Sur NarratiFluent, c'est l'école et la façon dont elle enseigne les langues.

## Étape 4 — Promesse, offre et échelle de valeur

**Si le produit existe**, on part de l'offre réelle et on ne touche qu'à ce qui change. Inventer
vingt bonus pour un produit qui en a déjà dix fait perdre une journée.

**Si le produit est neuf**, lister une vingtaine de bonus et une dizaine d'upsells possibles, puis
n'en retenir que ce qui compose l'offre, dans l'ordre. Chaque bonus s'écrit au format **format →
objection levée → contenu**. Un bonus qui ne lève pas d'objection, n'apporte pas de bénéfice
secondaire et ne fait pas gagner de temps n'a rien à faire dans l'offre.

## Étape 5 — Les 50 preuves

Elles ont leur propre page : **Les preuves du texte**.

## Étape 6 — Les headlines

Produire un stock large, une vingtaine. Format visé : la promesse, le mécanisme nommé, la big idea
nommée, une dimension de temps, et une urgence si elle s'y prête.

**On ne choisit pas ici.** Le stock part à la rédaction, et la headline se fige avec le lead.

Contrôle avant de fermer l'étape : chaque headline nomme-t-elle le mécanisme **de ce texte-ci**, et
dans la bonne personne grammaticale ?

## Étape 7 — Les 50 objections

Trois parties, numérotées de 1 à 50 sans reprendre à 1 : **internes** (ce que le lecteur croit de
lui-même), **externes** (son environnement, le marché, les autres solutions), **produit** (la
méthode, l'offre, le prix, la garantie). Dans chaque partie, de la plus courante à la moins courante.

Le format de chaque objection :

- le nom et la popularité : « 7. « L'objection en quelques mots » — 8/10 » ;
- la citation sceptique du lecteur, en une ou deux phrases, avec ses excuses à lui ;
- **LEVÉE** : deux à trois phrases au maximum, appuyées sur une preuve de l'étape 5, citée par son numéro et son titre, ou sur un élément de l'offre, nommé.

Les règles :

- une levée ne repose jamais sur du raisonnement seul ;
- chaque objection est une phrase que l'avatar dirait, avec son vocabulaire ;
- la popularité est une estimation quand la matrice ne mesure pas les objections : le dire en tête de l'étape ;
- un élément d'offre cité existe vraiment dans l'offre de l'étape 4.

**Contrôle avant d'écrire dans le document :** chaque preuve citée existe à l'étape 5 sous ce titre
exact, et chaque objection notée 8 ou plus s'appuie sur au moins une preuve vérifiée ou à produire.
