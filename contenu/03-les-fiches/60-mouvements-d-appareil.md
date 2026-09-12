# Les mouvements d'appareil sur les plans parlés

Un plan d'avatar ne reste jamais parfaitement fixe. C'est une exigence d'Adrien, et sa raison tient
en une phrase : une suite de plans immobiles donne une vidéo inerte, quelle que soit la qualité du
rendu. Le mouvement d'appareil est ce qui sépare un enchaînement de rushes d'un montage.

Sa formulation : « des zooms pendant que le mec parle, pas un cut, un zoom-dézoom », ou bien « pas
de zoom, juste un plan qui coupe et un nouveau plan au même endroit, mais un peu plus serré sur le
visage — avec un cut ».

---

## Les trois gestes

| Nom | Échelle | Ce qu'on voit |
|---|---|---|
| `avant` | 1,00 → 1,07 | le cadre se resserre lentement pendant la réplique |
| `serre` | 1,13 → 1,19 | on repart nettement plus près : la coupe se lit |
| `arriere` | 1,11 → 1,02 | le cadre s'ouvre lentement |

Ils **alternent automatiquement** d'un plan parlé au suivant, dans cet ordre. Deux plans voisins
qui bougent de la même façon annulent l'effet et se remarquent comme un tic ; le cycle l'empêche
sans qu'on ait à y penser.

Un plan peut imposer son geste en portant une clé `mouvement` dans le plan visuel — `'avant'`,
`'serre'`, `'arriere'` ou `'fixe'`. C'est l'exception, pas la règle : par défaut on laisse le cycle
travailler.

---

## L'amplitude reste faible, et ce n'est pas de la timidité

Quelques pour cent sur la durée d'une réplique suffisent. Un mouvement qu'on remarque consciemment
fatigue le spectateur et trahit l'artifice. L'effet recherché est celui d'une caméra tenue par un
humain, qui respire — pas celui d'un zoom motorisé.

---

## Qui bouge, qui ne bouge pas

C'est la distinction la plus importante du document, et elle ne se devine pas.

| Format | Mouvement |
|---|---|
| UGC IA, micro-trottoir, podcast de synthèse — **avatars générés** | oui, cycle par défaut |
| **Tournage réel** — Adrien se filme en selfie, en voiture, en salle | **non, aucun** |
| Plans de banque | non, ils bougent déjà |
| Cartes de fin, encarts de question | non, ils ont leur propre animation |

La raison de la deuxième ligne : une publicité tournée pour de vrai tire sa force de son air de
**vidéo prise sur le vif**. Un zoom-dézoom propre la trahit immédiatement en montage travaillé, et
détruit exactement ce qu'on cherchait. À l'inverse, sur un avatar généré, c'est l'immobilité
parfaite de la caméra qui sonne faux — d'où le mouvement.

**Le choix se commande par publicité**, par le paramètre `mouvements` de `monter()`, et Adrien
annonce le cas au moment de lancer le montage : « je te le dirai à chaque fois ». Sa consigne prime
sur le réglage par défaut.

**Les plans de banque portent déjà leur propre mouvement**, filmé. Leur ajouter un geste d'appareil
par-dessus donne un flottement désagréable, où deux mouvements se contrarient.

Les cartes de fin et les encarts de question ont leur propre animation, décrite dans
`cartes-de-fin.md`. Ils ne passent pas par ce mécanisme.

---

## Pourquoi le code n'emploie pas `zoompan`

`zoompan` est fait pour les images fixes : son facteur de zoom est quantifié, et sur de la vidéo le
mouvement saccade visiblement. Le montage anime donc l'échelle elle-même, avec `eval=frame` pour
qu'elle soit réévaluée à chaque image, puis recadre au format voulu. Le mouvement reste continu et
le coût de calcul est négligeable.

Le geste s'applique **après** `tpad`, de sorte qu'il court sur toute la durée du plan, silence de
fin compris. Appliqué avant, l'image se figerait pendant la respiration qui suit la réplique —
exactement ce qu'on cherche à éviter.
