import time

def rCalcImc():
    height = float(input("Entrez votre poids (en kg avec un '.' si décimal)  ==>  "))
    weight = float(input("Entrez votre taille (en m avec un '.' si décimal)  ==>  "))
    print("Votre taille : ", weight, " m")
    print("Votre poids : ", height, " kg")
    imc = height / (weight * weight)
    print(f"Vous avez une IMC de {round(imc)} kg/m²")
    if imc < 18.5:
        print("Vous êtes en Insuffisance pondérale (maigreur)")
    elif 18.5 <= imc < 25:
        print("Vous avez une corpulence normale !")
    elif 25 <= imc < 30:
        print("Vous êtes en surpoids")
    elif 30 <= imc < 35:
        print("Vous êtes en obésité modérée")
    elif 35 <= imc < 40:
        print("Vous êtes en obésité sévère")
    elif imc > 40:
        print("Vous êtes en obésité massive")    

def replay():
    answer_replay = input("Voulez vous recommencer ? Si oui, entrez 'o'  ==>  ")
    if answer_replay == 'o':
        print("Super!!")
        rCalcImc()
    else:
        print("Revenez quand vous voulez !!")
        time.sleep(1)
        exit()

def ask():
    print("CALCULATEUR D'IMC")
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
        
def calcImc():
    ask()
    rCalcImc()
    replay()