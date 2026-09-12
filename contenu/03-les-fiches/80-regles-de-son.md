> Écrit après deux heures passées sur une seule maquette. Aucun réglage ici ne
> se devine : chacun a été trouvé en mesurant, souvent après plusieurs erreurs.
> Le relire avant de produire coûte deux minutes ; ne pas le relire a coûté une
> matinée.

# Les règles de son, format par format

Trois choses valent pour **tous** les formats et ne se rediscutent pas.

**Un tour de parole part en une seule génération.** Jamais une requête de synthèse par phrase. Le
découpage par plan se fait après, sur la prise continue. C'est la règle qui supprime les
décrochages ; le détail est dans `faire-sonner-une-voix-vraie.md`.

**Chaque prise est ramenée à la même sonie** — −18 LUFS — par un gain linéaire, avant tout
assemblage. Sans ça l'écart entre deux phrases atteint douze LUFS.

**Un souffle de salle continu à −54 dB** passe sous toute la bande, pour qu'elle ne tombe jamais au
silence numérique absolu.

---

## Une seule personne qui parle — UGC, voix off, B-Rolls, ASMR

C'est le cas le plus simple : **toute la publicité est une seule prise**. Il n'y a aucune jointure,
donc rien à raccorder.

| | |
|---|---|
| Blanc entre répliques | 0,12 s |
| Recouvrement | sans objet — il n'y a pas de jointure |
| Musique de fond | oui sur l'UGC et la voix off, à −22 dB. Sur l'ASMR, non : le silence est le sujet |
| Ambiance de lieu | seulement si la personne est quelque part. Une voix off n'est nulle part |

Le blanc de 0,12 s peut surprendre par sa brièveté. Il est juste : les respirations que le modèle
pose lui-même à l'intérieur de la prise portent déjà le rythme, et tout blanc ajouté par-dessus
s'entend comme un trou.

---

## Deux personnes qui se parlent — interview, podcast, micro-trottoir

Ici les jointures existent et elles sont légitimes : c'est un dialogue. Elles se traitent par le
recouvrement.

| | |
|---|---|
| Blanc entre répliques d'un même personnage | 0,12 s |
| **Blanc entre personnages** | **0,50 s** |
| Recouvrement entre deux prises du même personnage | 0,08 s |
| **Recouvrement à un changement de personnage** | **aucun** |
| Musique de fond | oui, à −14 dB |
| Ambiance de lieu | selon le décor ; coupée sous une voix off, qui n'a pas de lieu |

**Une demi-seconde franche, et aucun recouvrement.** C'est la formulation d'Adrien : « une vraie
pause d'une demi-seconde, comme des gens normaux qui parlent, mais sur la même bande ». L'invité
finit sa phrase, un temps, l'intervieweuse relance.

Les deux extrêmes ont été essayés et refusés. **Recouvrir** — jusqu'à 0,70 s — faisait entrer
l'intervieweuse pendant que l'invité parlait encore : « ses phrases sont incrustées par-dessus,
c'est dégueulasse ». **Ne rien mettre** laissait un trou : le niveau tombait à −40 dB dans la
pause, contre −29 dB pour les creux naturels de la parole, et cela s'entendait comme un
décrochage.

**Ce qui remplit la pause, c'est la musique.** À −14 dB, le niveau dans la demi-seconde de silence
est de −32 dB, à peine plus creux que les respirations à l'intérieur de la parole. La pause existe,
elle s'entend comme une pause, et la bande ne décroche jamais. C'est pour cette raison que la
musique de fond est plus haute sur un dialogue que sur une voix seule.

**Et la queue de respiration se conserve** — 0,15 s en fin de prise. Couper la fin à zéro supprime
le souffle qui suit la dernière syllabe, et le personnage s'arrête net.

### Un personnage garde exactement la même voix du début à la fin

Deux appels de synthèse successifs sur la même voix clonée ne rendent pas le même timbre, et le
personnage semble remplacé au milieu de son propre discours. **Le regroupement des répliques en
prises ne tient donc compte que de la voix**, jamais des réglages.

Le piège concret, qui a coûté deux raccords audibles sur l'Ads 118 : une stabilité forcée sur
**une seule** réplique, pour corriger un mot mal articulé, avait suffi à couper le tour de parole
en trois générations, donc en trois timbres. Un réglage par réplique ne doit jamais découper un
tour de parole — et il devient le plus souvent inutile, puisqu'une réplique courte noyée dans une
longue prise est bien articulée par le contexte qui l'entoure.

**Le contrôle :** un personnage ne doit avoir qu'autant de prises que de tours réellement séparés
par quelqu'un d'autre. Deux prises du même personnage qui se suivent sans que personne ne parle
entre les deux sont une erreur.

### Le débit se règle par rôle, et au besoin par réplique

L'intervieweur va plus vite que l'invité : il relance, il n'expose pas. Le casting porte donc une
`vitesse_role`. Une `vitesse_replique` permet en plus d'accélérer une fin de publicité sans toucher
au reste. Ces réglages s'appliquent **après** la génération, sur des tranches de la même prise :
ils ne découpent rien.

Une réplique de moins d'une seconde et demie ne s'accélère jamais — la dernière syllabe s'y perd.

---

## Ce qui ne se corrige jamais dans le texte

Un raccord qui s'entend se règle au son. **Ajouter un mot pour arranger une transition est
interdit** : le script est validé, et un personnage qui dit ce qu'il n'a pas à dire sonne faux.
La seule liberté est la mise en bouche — élisions, appuis, hésitations — qui change la manière de
dire, jamais ce qui est dit.

---

## Les contrôles avant de livrer une bande son

1. `verifier_voix.py` au vert, et le texte intégral du mixage comparé au script.
2. Aucune prise tronquée : une prise qui finit normalement décroît, une prise coupée s'arrête à
   plein niveau.
3. Écart de sonie entre prises sous 1 LUFS.
4. Creux au changement de personnage pas plus profond que les creux naturels de la parole.
5. Aucun silence sous −70 dB.
