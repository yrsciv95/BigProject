import random
import time

def rDice():
    start = input("Lancer les dés ? ('o' ou 'n') ==>  ")
    player = False
    p_score = 0
    c_score = 0
    turn = 0
    while player == False:
        if start == 'o':
            choice = [1, 2, 3, 4, 5, 6]
            computer_choice = random.choices(choice, k= 2)
            user_choice = random.choices(choice, k= 2)
            user = sum(user_choice)
            computer = sum(computer_choice)
            if computer > user:
                print("Lancement des dés ...")
                time.sleep(2)
                print("Votre adversaire gagne !")
                print(f"Vous avez obtenu {user_choice[0]} et {user_choice[1]}")
                print(f"Votre adversaire a obtenu {computer_choice[0]} et {computer_choice[1]}")
                print(user, "<",computer)
                turn += 1
                c_score += 1
                time.sleep(1)
            elif computer == user:
                print("Lancement des dés ...")
                time.sleep(2)
                print(f"Vous avez obtenu {user_choice[0]} et {user_choice[1]} comme votre adversaire !")
                print("Egalité ! Plus 1 partout !")
                c_score += 1
                p_score += 1
                turn += 1
                time.sleep(1)
            else:
                print("Lancement des dés ...")
                time.sleep(2)
                print("Votre avez gagné !")
                print(f"Vous avez obtenu {user_choice[0]} et {user_choice[1]}")
                print(f"Votre adversaire a obtenu {computer_choice[0]} et {computer_choice[1]}")
                print(user,">" ,computer)
                turn += 1
                p_score += 1
                time.sleep(1)

        elif start == 'n':
            print("Dommage tu m'avais l'air assez fort !")
            time.sleep(1)
            exit()
        elif start != 'o' or 'n':
            print("Entrez 'o' ou 'n' pour commencez !")
            rDice()

        if turn == 5:
            player = True
            print("\nFin de la partie !!")
            if p_score > c_score:
                print("Vous avez gagné !")
                print("Il y a", p_score, "à", c_score, "pour vous !")
            elif c_score > p_score:
                print("C'est perdu !! Dommage !")
                print("Il y a", c_score, "à", p_score, "pour lui !")

def ask():
    print("JEU DE DÉS")
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
        rDice()
    else:
        print("Revenez quand vous voulez !!")
        time.sleep(1)
        exit()

def dice():
    ask()
    rDice()
    replay()