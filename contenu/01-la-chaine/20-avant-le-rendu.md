# Avant le rendu : la planche des plans

Cette étape s'intercale entre le montage écrit et le premier encodage. Elle n'existait pas, et son
absence a coûté une journée entière : des cadrages ratés découverts sur des publicités finies, dans
les formats dérivés, après que la machine a tourné trente minutes pour rien.

## La consigne

Adrien, le 11 septembre 2026 : **« avant de partir sur la génération vidéo, quand il y a des cuts et
qu'il y a plusieurs plans — notamment pour les UGC AI — montre-moi tous les plans en photo avant de
faire la vidéo, pour que je voie si ce n'est pas décalé. Et ce pour tous les formats, format un fois
un et cetera. »**

## La règle

**Dès qu'une publicité a plus d'un plan, une image fixe de chaque plan part devant lui avant le
premier rendu** — une image par plan, dans les trois formats, sur une seule planche.

```bash
python3 04-PRODUCTION/scripts/planche_plans.py 131
```

Le script retrouve tout seul le plan visuel de la publicité, quel que soit le script de montage qui
le construit (`monter_ads_NNN`, `monter_ugc`, `monter_preuve`), applique à chaque plan **le même
recadrage que le montage** et sort une planche numérotée dans le dossier d'écoute.

## Ce qui s'y regarde

Le 9:16 est le format natif : il ne subit aucun recadrage et il est donc toujours bon. **C'est
exactement le format qui ne dit rien des deux autres.** Ce qui se cherche sur la planche est donc
dans les colonnes 1:1 et 16:9 :

- un **crâne coupé** ou un menton qui sort du cadre ;
- un sujet décentré parce que le recadrage a pris le milieu géométrique et pas le milieu du sujet ;
- un plan de banque dont le recadrage a mangé ce qui faisait son intérêt.

## Pourquoi c'est avant, et pas après

Un rendu complet, c'est une dizaine de minutes par format, et la machine d'Adrien est immobilisée
pendant ce temps. La planche se fabrique en quelques secondes, avant qu'une seule image ne soit
encodée. Un défaut vu sur la planche coûte une correction ; le même défaut vu sur la publicité finie
coûte trois rendus, un aller-retour, et sa patience.

C'est « un extrait avant le complet » poussé d'un cran plus tôt : **avant le rendu, pas après**.
