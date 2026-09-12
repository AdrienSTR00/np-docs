---
name: generer-hooks
description: Génère des hooks publicitaires neufs pour NarratiFluent, à partir des matrices avatar et de la typologie des 15 types. Utiliser quand l'utilisateur demande de créer, générer ou trouver de nouveaux hooks, de nouveaux angles, ou d'explorer un territoire créatif — par opposition à la rédaction de scripts d'ads existantes.
---

# Générer des hooks

Produit des hooks candidats pour alimenter le Suivi Crea. **Ce sont des propositions : Adrien choisit.** Le générateur ne décide jamais de la stratégie créative.

## Ce qu'il faut charger

1. `00-SOCLE/typologie-hooks.md` — les 15 types et leurs règles d'écriture
2. `00-SOCLE/avatars/matrice-avatar-{N}.md` — **uniquement le BLOC A** : marché cible, points douloureux, MUP. Jamais le BLOC B, jamais les VSL brutes.
3. `00-SOCLE/hooks-stock.md` — pour ne pas reproposer un hook existant ou écarté
4. `01-BRIEFS/suivi-crea.csv` — la colonne Angle, pour ne pas reproposer un angle déjà testé
5. `00-SOCLE/compliance-meta.md` — pour pré-qualifier chaque hook

## Invocations

```
/generer-hooks avatar 3                          → 30 hooks, tous types
/generer-hooks avatar 4 --type STOP --nombre 20  → 20 hooks d'un seul type
/generer-hooks --territoire "les chansons"       → sur un angle précis
/generer-hooks --territoires-vierges             → propose ce qui n'a jamais été testé
```

## Procédure

1. Lire le stock et les angles déjà présents dans le Suivi Crea → constituer la liste de ce qu'il ne faut pas reproposer
2. Lire le BLOC A de la matrice de l'avatar → en extraire les verbatims réels
3. Générer, en s'appuyant **sur les verbatims plutôt que sur des formulations inventées**
4. Pour chaque hook : taguer le type, l'avatar, le niveau de conscience, la VSL compatible
5. Passer chacun à la compliance → 🟢 ou 🟠 avec le motif
6. Écrire dans `hooks-stock.md` au statut `proposé`
7. Restituer la liste à Adrien, groupée par type

## Règles

- **S'appuyer sur les verbatims des matrices.** Un hook inventé de toutes pièces sonnera générique. Les matrices contiennent des centaines de phrases réelles de clients.
- **Un hook qui mentionne Kató Lomb ne vaut que pour la VSL 3.** Le Protocole Phoenix pour la VSL 1, les mini-histoires hollywoodiennes pour la VSL 2. Taguer la compatibilité.
- **Ne jamais nommer NarratiFluent dans un hook Problem Aware.**
- **Signaler les hooks 🟠** au moment de la génération, pas trois semaines plus tard.
- **Ne pas hiérarchiser les propositions.** Les présenter à égalité : c'est Adrien qui juge.
