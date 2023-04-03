from time import sleep
from os import system

def converter():
    system('@echo off')
    system('cls')
    print("TRANSFORMATEUR Majuscule - Minuscule")
    sleep(1)
    print("Quelle action voulez-vous effectuer ?")
    print("1. Transformer un mot ou une phrase en MAJUSCULE")
    print("2. Transformer un mot ou une phrase en minuscule")
    answer = int(input("==>  "))
    if answer == 1:
        upperconv()
    elif answer == 2:
        lowerconv()
    elif answer == 0:
        print("Vous allez quitter le logiciel dans 5 secondes...")
        sleep(2.7)
        print("Vous quittez le logiciel...")
        sleep(1.8)
        system('cls')
        sleep(1)
        exit("Exit...")
    elif answer != 1 or 2 or 0:
        print("Veuillez entrer 1, 2 ou 3 pour faire un choix! Pour Quitter, taper 0.")
        sleep(2)
        converter()


def lowerconv():
    sleep(1.2)
    system('@echo off')
    system('cls')
    print("Entrez une phrase en MAJUSCULE")
    sentence = input("==>  ")
    conv = sentence.lower()
    print(f"Voici votre phrase en minuscule ==>  {conv}")
    sleep(4)
    print('Accueil...')
    sleep(1.2)
    converter()

def upperconv():
    sleep(1.2)
    system('@echo off')
    system('cls')
    print("Entrez une phrase en minuscule")
    sentence = input("==>  ")
    conv = sentence.upper()
    print(f"Voici votre phrase en MAJUSCULE  ==>  {conv}")
    sleep(4)
    print('Accueil...')
    sleep(1.2)
    converter()