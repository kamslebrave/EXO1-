# Etape 1: Création du fichier 'Jeu_secret.py'

Sur VS Code, on va sur le dossier (GENAI) puis (EXO1-).
Sachant que le sous-dossier (EXO1-) a été cloné partant du lien github https://github.com/kamslebrave/EXO1-.git

# Etape 2: Explication opérationnelle du programme

1. On met d'abord à jour le dépôt local
   ``bash

   git fetch origin

Il y a toute une logique selon laquelle l'utilisateur devra déviner un nombre au hazard jusqu'à ce que ce dernier corresponde à celui que le système a pu générer aléatoirement.

2. On se place sur la branche pricipale "main"
   ``bash

   git switch main (commande moderne) ou git checkout main (commande ancienne)

3. On merge la 1ere branche
   ``bash

   git merge branche1,

puis on valide avec:

git add .
git commit

4. On merge la 2e branche2
   ``bash

git merge branche2

Le principe est le même, celui de résoudre les conflits si nécessaire, puis valider.
