import random
import time

def rRouletteRu():
    start = input("Tenter votre chance ? ('o' ou 'n') ==>  ")
    if start == 'o':
        choice = ['1', '2', '3','4', '5', '6']
        trigger = random.choice(choice)
        if trigger == '1':
            print("Ahaha! Perdu!")
            replay()
        elif trigger == '2' or '3' or '4' or '5' or '6':
            print("Vous avez gagné. Bien joué !")
            rRouletteRu()
    elif start == 'n':
        print("Tu n'as pas le goût du risque. Va-t'en !")
        time.sleep(1)
        exit()
    elif start != 'o' or 'n':
        print("Entrez 'o' ou 'n' pour commencez !")
        rRouletteRu()

def ask():
    print("ROULETTE RUSSE")
    answer = input("Si vous souhaitez commencer tapez 1 sinon tapez 'q' pour Quitter  ==>  ")
    if answer == '1':
        print("GENIAL !!")
    elif answer == 'q':
        print("Dommage, Au revoir !!")
        time.sleep(1)
        exit()
    elif answer != '1':
        print("Si vous souhaitez commencer tapez 1 sinon tapez 'q' pour Quitter. Attention !")
        ask()

def replay():
    answer_replay = input("Voulez vous recommencer ? Si oui, entrez 'o'  ==>  ")
    if answer_replay == 'o':
        print("Super!!")
        rouletteRu()
    else:
        print("Revenez quand vous voulez !!")
        time.sleep(1)
        exit()

def rouletteRu():
    ask()
    rRouletteRu()
    replay()