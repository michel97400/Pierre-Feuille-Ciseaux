# importation de la bibliotéque random
import random

# Liste contenant les choix de l'ordinateur
list_choices = ['pierre', 'feuille', 'ciseaux']

# Fonction pour récupérer le choix de l'ordinateur
def computer():
    computer_choice = random.choice(list_choices)
    return computer_choice

# Fonction pour récupérer l'entré de l'utilisateur
def user():
    user_choice = input("Entrez votre choix: ").lower()

    # Boucle pour vérifier l'entré utilisateur si il se trouve dans la liste (list_choices)
    while user_choice not in list_choices:
        print("Veuillez entrer un choix valide !")
        user_choice = input("Entrez votre choix: ").lower()
    
    return user_choice

def info():
    print(" ")
    print("======================Bienvenue dans le jeu du Pierre-Feuille-Ciseaux.===================")
    print(" ")
    print("Régle:")
    print("Choisissez parmis la liste: pierre, feuille ou ciseaux.")
    print("Et affronter l'ordinateur !")
    print(" ")


# Fonction pour lancer le jeu
def play_game():
    info()

    # Variable pour les tours et les points
    tour = 0
    count = 0

    # Boucle du jeu avec un compteur
    while tour < 3:
        print(f'==================================TOUR N°{tour + 1}==================================')
        choice_computer = computer()
        choice_user = user()

        if choice_user == choice_computer:
            print(" ")
            print("-- Match nul ! --")
            print(f"Vous et l'ordinateur avez choisi : {choice_user}")
            print(" ")
            # On ne compte pas le tour, on recommence
            continue
        # Règles du jeu
        elif (choice_user == 'pierre' and choice_computer == 'ciseaux') or \
             (choice_user == 'feuille' and choice_computer == 'pierre') or \
             (choice_user == 'ciseaux' and choice_computer == 'feuille'):
            print(" ")
            print("-- Vous avez gagnez ! --")
            print(f"L'ordinateur a choisi : {choice_computer}")
            print(" ")
            count += 1
        else:
            print(" ")
            print("-- Vous avez perdu --")
            print(f"L'ordinateur a choisi : {choice_computer}")
            print(" ")
        tour += 1

        if count == 3:
            print("======Bravo vous avez gagné la partie======")
            print(" ")
            print(f'-- Votre score: {count} point. --')
            print(" ")


# Fonction pour demander à l'utilisateur si il veut rejouer
def rejoue():
    rejouer = input("Voulez-vous rejouer ? oui/non: ")
    
    while rejouer not in ['oui', 'non']:
        print("Veuillez répondre par 'oui' ou 'non'.")
        rejouer = input("Voulez-vous rejouer ? oui/non: ")

    return rejouer == 'oui'


# Permet de lancer le jeu uniquement si le fichier est exécuté directement
if __name__ == "__main__":
    play_game()
    choix_rejouer = rejoue()
    while True:
        if choix_rejouer:
            play_game()
        else:
            print("A bientot !")
            break
