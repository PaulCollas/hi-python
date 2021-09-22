import random

## INPUT FOR USER SELECTION
user_action = input("Selectionner votre choix ('pierre', 'papier', 'ciseaux'): ")

## INPUT FOR PC CHOICE
possible_actions = ["pierre", "papier", "ciseaux"]
computer_action = random.choice(possible_actions)

## EXPLAIN BOTH CHOICE
print(f"\nVous avez choisi {user_action}, le PC a choisi {computer_action}.\n")

## CONDITION FOR WINNER

if user_action == computer_action:
    print(f"Vous avez séléctionné la même action: {user_action}. Égalité ! Recommencez")
elif user_action == "pierre":
    if computer_action == "ciseaux":
        print("Pierre casse les ciseaux : Vous avez gagnez")
    else:
        print("Papier recouvre la pierre ! Vous avez perdu.")
elif user_action == "papier":
    if computer_action == "pierre":
        print("Papier recouvre la pierre! Vous avez gagnez!")
    else:
        print("Ciseaux coupe le papier! Vous avez perdu.")
elif user_action == "ciseaux":
    if computer_action == "papier":
        print("Ciseaux coupe le papier! Vous avez gagnez!")
    else:
        print("Pierre casse les ciseaux ! Vous avez perdu")