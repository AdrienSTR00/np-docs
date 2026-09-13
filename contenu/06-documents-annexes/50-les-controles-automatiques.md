# Les contrôles automatiques, et ce que chacun attrape

> Chacun de ces contrôles existe parce qu'une erreur est passée. Ils sont bloquants :
> ils ne préviennent pas, ils arrêtent la chaîne.

Le principe commun : **rien dans la réponse d'une API ne signale un travail raté.** Une
génération de voix qui escamote une phrase renvoie un succès. Un encodage tronqué
renvoie un fichier valide. Seule une mesure faite sur le fichier produit le dit.

## Sur la bande son

**`verifier_voix.py`** retranscrit chaque réplique de la piste finale et la compare au
texte attendu. C'est le seul moyen de voir qu'un mot a sauté, qu'une phrase a été
avalée, ou qu'un modèle a prononcé autre chose que ce qui était écrit.

Il est né d'un cas précis : une coquille corrigée dans un script, la prise régénérée, et
le modèle prononçant « vous laissez **fait** » au lieu de « vous laissez **faire** » à
vingt-quatre secondes — à un endroit qui n'avait pas été modifié, et donc pas réécouté.

**La règle qui en découle dépasse le script** : après toute modification, c'est le
livrable **entier** qui repasse dans ses contrôles, jamais seulement le morceau touché.

## Sur le montage

**`planche_plans.py`** fabrique une image fixe de chaque plan, dans les trois formats,
sur une seule planche — **avant le premier encodage**. Un rendu complet prend une
dizaine de minutes par format ; une planche se fabrique en quelques secondes. Ce qu'on y
cherche : un visage coupé, un sujet sorti du cadre, un recadrage qui a mangé l'essentiel
du plan. C'est précisément ce que le 9:16 ne montre jamais, puisqu'il est le format natif
et ne subit aucun recadrage.

**`verifier_formats.py`** relit les trois fichiers livrés et compare durées, dimensions
et débit. Il a attrapé un 9:16 encodé tronqué à 4,8 secondes alors que les deux autres
formats étaient bons.

**Le garde-fou « casting plus récent que la maquette »** refuse de monter quand le
fichier de casting a été modifié après la bande son. Une publicité est partie sans sa
musique parce que la musique avait été ajoutée au casting vingt minutes après la
génération : le montage lisait une maquette périmée sans le savoir.

**La détection d'image figée** attrape un plan d'avatar qui se prolonge après la fin de
la phrase — un défaut qu'aucune durée ne signale.

## Sur le script

**`check_avatar.py`** mesure l'ancrage avatar réel dans le texte, au lieu de le
supposer. **`check_hook.py`** contrôle le hook contre sa typologie.

La [Copy Ads Checklist](../les-regles/copy-ads-checklist.html) s'applique **automatiquement
après la rédaction et avant la relecture d'Adrien**, sur un contexte neuf pour ne pas
être juge et partie. Un échec sur un critère éliminatoire déclenche une réécriture sans
qu'Adrien ait à la demander.

## Avant la livraison

**`livrer_ad.py`** compare l'empreinte du son du fichier livré à celle de la maquette
validée. Si les dates divergent mais que les empreintes sont identiques, il laisse
passer ; si les empreintes diffèrent, il bloque — c'est le signe qu'une prise a été
régénérée depuis la validation.

## Ce que les contrôles ne remplacent pas

Aucun de ces scripts ne juge si une publicité est bonne. Ils attrapent ce qui est
**mesurable** : une phrase manquante, un cadre faux, une durée impossible, un fichier
périmé. Le jugement — le timbre d'une voix, la crédibilité d'un visage, la force d'un
hook — reste celui d'Adrien, et c'est pour ça que la
[boucle de validation](../les-regles/boucle-de-validation.html) existe.
