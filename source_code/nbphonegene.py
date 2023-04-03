from time import sleep
from os import system
import random

def numgene():
    system('@echo off')
    system('cls')
    print("Générateur de numéro de Téléphone")
    sleep(1.5)
    print("Quelle action voulez-vous effectuer ?")
    print("1. Générer un numéro de Téléphone")
    print("0. Quitter")
    answer = int(input("==>  "))
    if answer == 1:
        gene()
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
        numgene()

def gene():
    sleep(1.2)
    system('@echo off')
    system('cls')
    print("Générateur de Numéro de Téléphone".upper())
    sleep(1)
    print("Avec '06' ou '07' ?")
    answer = input("==>  ")
    if answer == '06':
        num_list = random.sample(range(10, 99), 4)
        num_choice = str(num_list)[1:-1]
        num = num_choice.replace(',','')
        print("Création de numéro...")
        sleep(2)
        print(f"Numéro généré : 06 {num}")
    elif answer == '07':
        num_list = random.sample(range(10, 99), 4)
        num_choice = str(num_list)[1:-1]
        num = num_choice.replace(',','')
        print("Création de numéro...")
        sleep(2)
        print(f"Numéro généré : 07 {num}")
    elif answer != '06' or '07':
        print("Entrez '06' ou '07' pour faire un choix !")
        sleep(2)
        gene()
    sleep(2.5)
    system('pause')
    print('Accueil...')
    sleep(1.2)
    numgene()