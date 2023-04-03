from time import sleep
from os import system

def calctva():
    system('@echo off')
    system('cls')
    print("Calculatrice de TVA")
    sleep(1.5)
    print("Quelle action voulez-vous effectuer ?")
    print("1. Calculer la TVA")
    print("0. Quitter")
    answer = int(input("==>  "))
    if answer == 1:
        calc()
    elif answer == 0:
        print("Vous allez quitter le logiciel dans 5 secondes...")
        sleep(2.7)
        print("Vous quittez le logiciel...")
        sleep(1.8)
        system('cls')
        sleep(1)
        exit("Exit...")
    elif answer != 1 or 0:
        print("Veuillez entrer 1 pour commencer ! Pour Quitter, taper 0.")
        sleep(2)
        calctva()

def calc():
    sleep(1.2)
    system('@echo off')
    system('cls')
    print("Calculatrice de TVA".upper())
    sleep(1)
    print('Informations')
    taux = float(input("Entrez votre taux (sans le %)  ==>  "))
    prix = float(input("Entrez le prix (Hors Taxes)  ==>  "))
    tva = (prix / (100 + taux)) * taux
    result = prix + tva
    sleep(1)
    print('Calcul...')
    sleep(2)
    print(f"Prix après TVA  ~~>  {round(number= result, ndigits= 2)}€")
    print('\x1B[3m','Peut varier de quelques ct. ou €','\x1B[0m')
    sleep(2.5)
    system('pause')
    print('Accueil...')
    sleep(1.2)
    calctva()