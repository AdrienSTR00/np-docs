# Le fignolage

> Raccourcir le texte sans perdre un seul argument. Quatre passes, treize opérations, et des seuils
> mesurés.

## La consigne, dans les termes d'Adrien

> « Couper des mots ou des phrases qui n'apportent rien au copy, simplifier les phrases, reformuler
> pour raccourcir, couper des éléments de copy qui au final n'apportent pas une vraie plus-value.
> **L'obsession doit être de raccourcir le nombre de mots sans pour autant perdre un seul élément
> notable de la stratégie de persuasion du texte. On ne cherche pas à ce que les phrases ressemblent
> à des bullet points.** »

Deux contraintes qui tirent en sens inverse, et c'est voulu. Raccourcir est le critère de réussite.
Perdre un argument, une preuve ou un chiffre est un échec. Hacher le texte en phrases de six mots
est un échec symétrique.

**Le fignolage se fait avant la livraison, pas après la review.** Adrien ne lit que du texte déjà
raccourci.

## Les seuils

| | Cible | Échec si |
|---|---|---|
| **Mots** | −9 à −13 % | moins de −6 % (passe bâclée) ou plus de −20 % (des arguments ont sauté) |
| **Médiane de phrase** | perd au plus 1 mot | perd 2 mots ou plus : le texte a été haché |
| **Phrases de plus de 30 mots** | en baisse | en hausse |
| **Nombre de phrases** | stable ou en hausse | en forte baisse : des phrases ont été supprimées au lieu d'être raccourcies |
| **Sections intouchables** | garantie, récapitulatif d'offre, liste et valeurs des bonus, bloc d'urgence validé, chiffres d'ancrage | un seul mot modifié |

**Une cible en nombre de mots donnée par Adrien prime sur ces seuils.** Le nombre de mots prononcés
se compte sans les notes de production ni les sources.

```bash
python3 05-FUNNEL/00-METHODE/scripts/mesurer_fignolage.py avant.md apres.md
```

Si des emplacements de preuve ont été remplacés dans la même passe, les sections concernées faussent
le taux : les exclure avec `--sauf 13,15,23`.

## Les quatre passes, dans cet ordre

Le fignolage se fait seul, et les passes ne se mélangent pas : mélangées, la mesure devient
impossible.

| | Passe | Nature |
|---|---|---|
| **0** | **Nettoyage** — retirer les notes de travail | mécanique, scriptée |
| **1** | **Raccord** — le texte parle-t-il de lui-même ? | liste de contrôle |
| **2** | **Fignolage** — les treize opérations | jugement de copy |
| **3** | **Preuves** — remplacer les emplacements, sourcer les chiffres | production |

### Passe 0 — Nettoyage

```bash
python3 05-FUNNEL/00-METHODE/scripts/mesurer_fignolage.py texte.md --notes
```

Le script signale les emplacements entre crochets, les mentions de preuve, les variables de gabarit
non remplacées et les listes de preuves à produire. **Aucune ne doit survivre.**

### Passe 1 — Raccord

Cinq questions, chacune a déjà coûté une réécriture complète :

1. **La headline parle-t-elle du mécanisme de ce texte-ci ?** Une headline héritée d'une autre VSL s'est déjà retrouvée collée sur un corps de texte qui n'était pas le sien.
2. **La personne grammaticale est-elle la même du début à la fin ?** Vouvoiement ou tutoiement selon la VSL, jamais de mélange.
3. **Chaque référence renvoie-t-elle à quelque chose qui existe dans le texte ?** Une FAQ s'est déjà appuyée sur sept éléments dont aucun n'apparaissait ailleurs.
4. **Les prénoms de la FAQ correspondent-ils aux preuves du texte ?** Les questions viennent des membres déjà cités ou de gens nouveaux, jamais d'une liste héritée d'un autre texte.
5. **Le porte-parole est-il constant ?**

### Passe 2 — Les treize opérations

1. Couper les chevilles et les amorces vides.
2. Supprimer la redite.
3. Couper les mots qui n'apportent pas de preuve.
4. Supprimer une section qui refait une démonstration déjà faite.
5. Fusionner : supprimer une fausse respiration.
6. Scinder : isoler une phrase pour qu'elle frappe.
7. Remplacer un mot flou par le mot juste.
8. Réaligner le texte sur un seul verbe de promesse.
9. Passer du « nous » corporate au « je » du porte-parole.
10. Déplacer plutôt que couper.
11. Remplacer une image de copywriter par ce que la personne ressent.
12. Baisser un chiffre pour qu'il reste croyable.
13. Espacer un chiffre trop répété.

Ce qui se coupe en premier : les preuves qui font double emploi, les exemples facultatifs, les
chiffres dont la source reste fragile, et les passages qui refont une démonstration déjà faite.

### Passe 3 — Preuves et sources

Remplacer les emplacements par les preuves réelles, et construire la page des sources.

## Après le fignolage

**Repasser le contrôle avatar.** Les coupes font tomber des mots du segment, et ils se remettent en
place à ce moment-là.
