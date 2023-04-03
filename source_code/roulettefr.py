import random
import time

def rRouletteFr():
    print("Vous avez une chance sur deux d'augmenter votre mise")
    start = input("Tenter votre chance ? ('o' ou 'n')  ==>  ")
    if start == 'o':
        mise = int(input('Entrez le montant de votre mise  ==>  '))
        mise_list = [mise, ]
        print(f"Votre mise : {mise}$")
        case = input("Pariez sur une case paire ou impaire ('p' ou 'i')  ==>  ")
        case1 = 'p'
        case2 = 'i'
        launch = random.choice(range(1, 3))
        if case == case1:
            if launch == 1:
                print(f'Vous tombez sur un impaire')
                print("Ahaha! Perdu!")
                mise_list.append(-200)
                total = sum(mise_list)
                print(f'Vous avez {total} $')
                time.sleep(1)
                if total > 0:
                    rRouletteFr()
                elif total == 0:
                    print("Vous avez tout perdu !")
                    time.sleep(1)
                    replay()
                elif total <= 0:
                    print(f"Vous êtes en perte : {total}$ !")
                    replay()
            elif launch == 2:
                print(f'Vous tombez sur un paire!')
                print("Vous avez gagné. Bien joué !")
                mise_list.append(100)
                total = sum(mise_list)
                print(f'Vous avez {total} $')
                time.sleep(1)
                if total > 0:
                    rRouletteFr()
                elif total == 0:
                    print("Vous avez tout perdu !")
                    time.sleep(1)
                    replay()
                elif total <= 0:
                    print(f"Vous êtes en perte : {total}$ !")
                    replay()
                    return total
        elif case == case2:
            if launch == 2:
                print(f'Vous tombez sur un paire!')
                print("Ahaha! Perdu!")
                mise_list.append(-200)
                total = sum(mise_list)
                print(f'Vous avez {total} $')
                time.sleep(1)
                if total > 0:
                    rRouletteFr()
                elif total == 0:
                    print("Vous avez tout perdu !")
                    time.sleep(1)
                    replay()
                elif total <= 0:
                    print(f"Vous êtes en perte : {total}$ !")
                    replay()
            elif launch == 1:
                print(f'Vous tombez sur un impaire!')
                print("Vous avez gagné. Bien joué !")
                mise_list.append(100)
                total = sum(mise_list)
                print(f'Vous avez {total} $')
                time.sleep(1)
                if total > 0:
                    rRouletteFr()
                elif total == 0:
                    print("Vous avez tout perdu !")
                    time.sleep(1)
                    replay()
                elif total <= 0:
                    print(f"Vous êtes en perte : {total}$ !")
                    replay()
        elif case == 'q':
            print("Tu n'as pas le goût du risque. Va-t'en !")
            time.sleep(1)
            exit()
        elif case != 'p' or 'i':
            print("Entrez 'p' ou 'i' pour faire un choix. Pour quitter entrez 'q'")
            time.sleep(1.5)
            rRouletteFr()
    elif start == 'n':
        print("Tu n'as pas le goût du risque. Va-t'en !")
        time.sleep(1)
        exit()
    elif start != 'o' or 'n':
        print("Entrez 'o' ou 'n' pour commencez !")
        rRouletteFr()

def ask():
    print("ROULETTE FRANCAISE")
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
        rouletteFr()
    else:
        print("Revenez quand vous voulez !!")
        time.sleep(1)
        exit()

def rouletteFr():
    ask()
    rRouletteFr()
    replay()