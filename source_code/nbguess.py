from random import *
import time

def nbGuessUser():
    just_price = randint(1, 100)
    running = True
    nb_essais = int(input("Combien d'essais desirez-vous ?"))
    essais = 0
    
    while running:
        remaining_trials = nb_essais - essais - 1
        user_price = int(input("Deviner le prix (entre 1 et 100) ==>  "))
        if user_price == just_price:
            print("Bien joué, vous avez le juste prix en ", essais, "essais")
            running = False
        elif user_price > just_price:
            print("C'est moins !!")
            essais += 1
            print("Il vous reste ", remaining_trials," essais !")
        elif user_price < just_price:
            print("Plus haut !!")
            essais += 1
            print("Il vous reste ", remaining_trials," essais !")

        if essais == nb_essais:
            print("Dommage !!")
            print("Le chiffre c'était", just_price)
            replay()
            essais = 0
    print("Fin du jeu !")
    replay()

def ask():
    print("LE JUSTE PRIX")
    answer = int(input("Si vous souhaitez jouer tapez 1  ==>  "))
    if answer == 1:
        print("SUPER !!")
        nbGuessUser()
    elif answer not in '1':
        print("Dommage, Au revoir !!")
        time.sleep(1)
        exit()

def replay():
    answer_replay = input("Voulez vous rejouer ? Si oui, entrez 'o'  ==>  ")
    if answer_replay == 'o':
        print("Super!!")
        
    else:
        print("Revenez quand vous voulez !!")
        time.sleep(1)
        exit()

def nbGuess():
    ask()
    nbGuessUser()
