# Etape 5: Fusionner (merger) et résoudre les conflits éventuels

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

# En cas de conflits

Si Git détecte des conflits, il arrête le merge et te demande de les résoudre manuellement.

Tu modifies les fichiers concernés, puis tu valides la résolution :

``bash

git add fichier_conflit
git commit -m "message"
