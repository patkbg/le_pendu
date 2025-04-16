# Initialiser un dépôt Git local.
git init
# Ajouter tous les fichiers modifiés au staging.
git add .
# Créer un premier commit avec un message.
git commit -m "1er commit"
# Renommer la branche principale en main.
git branch -M main
# Configurer l'URL du dépôt distant GitHub.
git remote set-url origin https://...
# Pousser la branche main vers le dépôt distant et définir la relation par défaut.
git push --set-upstream origin main
# Pousser les changements vers GitHub sur la branche main.
git push -u origin main
# Vérifier les dépôts distants configurés.
git remote -v
