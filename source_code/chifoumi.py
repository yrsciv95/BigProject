from random import *
import time

def replay():
    answer_replay = input("Voulez vous rejouer ? Si oui, entrez 'o'  ==>  ")
    if answer_replay == 'o':
        print("Super!!")
        rChifoumi()
    else:
        print("Revenez quand vous voulez !!")
        time.sleep(1)
        exit()

def ask():
    print("LE JEU DU CHIFOUMI")
    answer = input("Si vous souhaitez jouer tapez 1 sinon tapez 'q' pour Quitter  ==>  ")
    if answer == 1:
        print("SUPER !!")
    elif answer == 'q':
        print("Dommage, Au revoir !!")
        time.sleep(1)
        exit()

def rChifoumi():
    choice_list = ["Pierre", "Feuille", "Ciseaux"]
    computer = choice_list[randint(0,2)]
    player = False
    p_score = 0
    c_score = 0
    turn = 0
    while player == False:
        player = input("Pierre, Feuille ou Ciseaux (ou 'q' pour quitter)  ==>  ")
        if player == 'q':
            print("Salut! A bientôt !")
            time.sleep(1)
            exit()
        elif player == computer:
            print("Votre adversaire choisit aussi", computer,"!")
            print("Il y a donc égalité ! Personne ne gagne de points")
            turn += 1
        elif player == "Pierre":
            if computer == "Feuille":
                print("Perdu !", computer, "recouvre", player)
                turn += 1
                c_score += 1
            else:
                print("Gagné !", player, "écrase", computer)
                turn += 1
                p_score += 1
        elif player == "Feuille":
            if computer == "Ciseaux":
                print("Perdu !", computer, "coupe", player)
                turn += 1
                c_score += 1
            else:
                print("Gagné !", player, "recouvre", computer)
                turn += 1
                p_score += 1
        elif player == "Ciseaux":
            if computer == "Pierre":
                print("Perdu !", computer, "écrase", player)
                turn += 1
                c_score += 1
            else:
                print("Gagné !", player, "coupe", computer)
                turn += 1
        else:
            print("Entrez 'Pierre', 'Feuille', ou 'Ciseaux' pour faire un choix svp")
        player = False
        computer = choice_list[randint(0,2)]
        if turn == 5:
            player = True
            print("Fin de la partie !!")
            if p_score > c_score:
                print("Vous avez gagné !")
                time.sleep(1)
                exit()
            elif c_score > p_score:
                print("C'est perdu !! Dommage !")
                time.sleep(1)
                exit()

def chifoumi():
    ask()
    rChifoumi()
    replay()