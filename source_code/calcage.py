import datetime
import time

def rCalcAge(y, m, d):
    current_date = datetime.datetime.now().date()
    date_of_birth = datetime.date(y, m, d)
    age = int((current_date-date_of_birth).days / 365.25)
    print(f"Vous avez {age} ans")
    replay()

def ask():
    print("CALCULATEUR D'AGE")
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
        rCalcAge(int(input("Année de naissance  ==>  ")), int(input("Mois de naissance  ==>  ")), int(input("Jour de naissance  ==>  ")))
    else:
        print("Revenez quand vous voulez !!")
        time.sleep(1)
        exit()

def calcAge():
    ask()
    rCalcAge(int(input("Année de naissance  ==>  ")), int(input("Mois de naissance  ==>  ")), int(input("Jour de naissance  ==>  ")))
    replay()