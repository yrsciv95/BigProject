from time import sleep
from os import system
import random

def piece():
    system('@echo off')
    system('cls')
    print("Pile ou Face")
    sleep(1.5)
    print("Quelle action voulez-vous effectuer ?")
    print("1. Lancer la Pièce")
    print("0. Quitter")
    answer = int(input("==>  "))
    if answer == 1:
        lancer()
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
        piece()

def lancer():
    sleep(1.2)
    system('@echo off')
    system('cls')
    print("Lancer de Pièce".upper())
    sleep(1)
    nb = [1, 2]
    nb_result = random.choice(nb)
    print('Pile ou Face ?')
    answer = input('==>  ')
    if answer == 'Pile':
        if nb_result == 1:
            result = 'Pile'
            print("Lancement...")
            sleep(1.8)
            print('Vous tombez sur', result)
            print('Gagné !')
        elif nb_result == 2:
            result = 'Face'
            print("Lancement...")
            sleep(1.8)
            print('Vous tombez sur', result)
            print('Perdu !')
    elif answer == 'Face':
        if nb_result == 2:
            result = 'Face'
            print("Lancement...")
            sleep(1.8)
            print('Vous tombez sur', result)
            print('Gagné !')
        elif nb_result == 1:
            result = 'Pile'
            print("Lancement...")
            sleep(1.8)
            print('Vous tombez sur', result)
            print('Perdu !')
    elif answer != 'Pile' or 'Face':
        print('Entrez "Pile" ou "Face" !')
        sleep(2)
        lancer()
    sleep(2.5)
    system('pause')
    print('Accueil...')
    sleep(1.2)
    piece()