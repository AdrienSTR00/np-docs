# Process NarratiFluent

La documentation interne de production, écrite en markdown et publiée en site statique.

**La source est `contenu/`. Le site n'en est que l'affichage.** Si le générateur disparaît, il
reste des fichiers texte lisibles et versionnés — c'est la raison d'être de ce choix.

## Modifier une page

Corriger le `.md` dans `contenu/`, commiter, pousser. Le site se reconstruit tout seul.

## Ajouter une page

Un nouveau `.md` dans le dossier de la section voulue. Le préfixe numérique du nom de fichier
décide de l'ordre dans le sommaire et ne s'affiche jamais. Le premier titre `#` donne son nom à la
page, et la première ligne commençant par `>` devient son chapô.

## Construire en local

```bash
pip install markdown
python3 construire.py
python3 -m http.server -d site 8000
```

Le site sort en `noindex` : accessible à qui a le lien, invisible des moteurs de recherche.
