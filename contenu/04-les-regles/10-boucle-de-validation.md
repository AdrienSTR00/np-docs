# La boucle de validation

Le process de travail avec Adrien, tel qu'il l'a formulé le 11 septembre 2026 : **« dès qu'il y a un
problème, une fois que tu l'as corrigé, tu me montres rapidement un extrait de quelques secondes
pour que je valide, et ensuite seulement tu appliques ça à l'ensemble de la vidéo. »**

Et, la même journée : **« sois stratégique. Fais-moi d'abord valider tout ce qui est à valider, et
ensuite tu pars bosser pour vingt, trente minutes. »**

Les deux phrases disent la même chose vue de deux côtés : **son temps et sa machine sont la
ressource rare, pas la mienne.**

---

## Le cycle, dans l'ordre

1. **Produire tout ce qui se juge**, en une fois — extraits de quinze secondes dans les trois
   formats, planches de visages, comparatifs de voix, plans générés, maquettes d'habillage.
2. **Envoyer le lot entier**, d'un coup, avec ce qu'il y a à trancher clairement énoncé.
3. **Attendre ses réponses.** Ne rien lancer de long pendant ce temps : sa machine doit rester libre.
4. **Lancer la phase longue**, qui peut alors tourner trente minutes sans le déranger.
5. **Vérifier soi-même** — `verifier_formats.py`, la planche des trois formats, la liste de
   `avant-de-livrer.md`.
6. **Déposer au Drive** immédiatement après sa validation, sans attendre de constituer un lot.

---

## Après une correction, jamais de montage complet à l'aveugle

```bash
python3 04-PRODUCTION/scripts/monter_ads_NNN.py "9:16" "1:1" "16:9" --extrait 15
```

Moins d'une minute par format contre dix. L'extrait montre le cadrage, les sous-titres, la
synchronisation et la qualité d'image — tout ce qui se juge. L'appel à l'action y est
automatiquement désactivé, puisqu'il se pose sur les dernières secondes de la vidéo entière et
tomberait au mauvais endroit sur un extrait.

**Le montage complet ne se lance qu'après son accord sur l'extrait.** Relancer douze fichiers sur
la foi d'une correction qu'il n'a pas vue, c'est risquer dix minutes de machine et un aller-retour
de plus.

---

## La question à se poser avant tout calcul long

**Qu'est-ce qu'il restera à valider quand ça aura fini ?**

Si la réponse n'est pas « rien », c'est qu'on s'y prend à l'envers : ce qui reste à valider devait
partir avant, pas après.

---

## Ce qui se dépense se montre avant

Aucune génération payante — Argil, Veo, clonage de voix — ne se lance sans que le chiffrage et le
contenu lui aient été soumis. Sa formulation : « je compte sur toi pour, avant de générer quoi que
ce soit qui use des crédits, tu me montres tout avant ». Le découpage plan par plan se présente en
français, avec l'intention de chaque plan, et le total en euros.

---

## Et tout se consigne

« Note bien tous les process et toutes les règles qu'on devra suivre à chaque fois. » Chaque
consigne entre ici ou dans la page de format concernée, le jour où elle est donnée. Une règle qui
ne vit que dans une conversation est une règle qu'on repayera.
