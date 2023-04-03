import time

def rCalcDiv():
    print("Entrez le nombre dont vous voulez trouver les diviseurs")
    n = int(input("==>  "))
    print(f'Voici les diviseurs de {n}:', end='  ')
    for i in range(1, n+1):
        if n%i == 0:
            print(i, end= '  ')
    replay()
    
def replay():
    answer_replay = input("\n\nVoulez vous recommencer ? Si oui, entrez 'o'  ==>  ")
    if answer_replay == 'o':
        print("Super!!")
        rCalcDiv()
    else:
        print("Revenez quand vous voulez !!")
        time.sleep(1)
        exit()

def ask():
    print("CALCULATEUR DE DIVISEURS")
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

def calcDiv():
    ask()
    rCalcDiv()
    replay()