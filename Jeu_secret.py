import random

def jeu_secret():
    # Choisir un nombre aléatoire entre 1 et 100
    nombre_secret = random.randint(1, 100)
    print("J'ai choisi un nombre entre 1 et 100. Essaie de le deviner !")

    while True:
        try:
            # Demander à l'utilisateur de saisir un nombre
            saisie = int(input("Entre ton nombre : "))
            
            if saisie < nombre_secret:
                print("Trop petit ! Essaie encore.")
            elif saisie > nombre_secret:
                print("Trop grand ! Essaie encore.")
            else:
                print("Bravo ! Tu as trouvé le nombre.")
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

# Lancer le jeu
jeu_secret()
