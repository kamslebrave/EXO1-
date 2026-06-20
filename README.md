<<<<<<< HEAD
# Comment merger les différentes branches

1. On met d'abord à jour le dépôt local

``bash
git fetch origin

2. On se place sur main
   git switch main (commande moderne) ou git checkout main (commande ancienne)

3. On merge la 1ere branche
   git merge branche1,

puis on valide avec
git add .
git commit

4. On merge la 2e branche2

git merge branche2

Même principe : résoudre les conflits si nécessaire, puis valider.
=======
# Etape 3: Partage dans Github

# Pour cloner un dossier distant

``bash
git clone https://github.com/kamslebrave/EXO1-.git

# Etape 4: Pour ajouter la dernière opération apportée au code

`` bash
git add nom du fichier (pour un fichier précis)

ou encore

git add . (pour tous les fichiers qui ont subi une quelque opération)
>>>>>>> branche1
