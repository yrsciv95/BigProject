from time import sleep
from os import system
from random import choice
from unidecode import unidecode

def wrdguess():
    system('@echo off')
    system('cls')
    print("DEVINE LE MOT")
    sleep(1.5)
    print("Quelle action voulez-vous effectuer ?")
    print("1. JOUER")
    print("0. Quitter")
    answer = int(input("==>  "))
    if answer == 1:
        game()
    elif answer == 0:
        print("Vous allez quitter le logiciel dans 5 secondes...")
        sleep(2.7)
        print("Vous quittez le logiciel...")
        sleep(1.8)
        system('cls')
        sleep(1)
        exit("Exit...")
    elif answer != 1 or 0:
        print("Veuillez entrer 1 pour commencer! Pour Quitter, taper 0.")
        sleep(2)
        wrdguess()

def game():
    sleep(1.2)
    system('@echo off')
    system('cls')
    print("Devine le Mot")
    sleep(1)
    file = open(r'C:\Users\yorisamani\Documents\perso\nsi perso\python\BigProject\source_code\sources\word_wordguess.txt', r'r', encoding='utf-8')
    file_read = file.readlines()
    sleep(1)
    print('Je cherche un mot...')
    sleep(1.5)
    print('Essayez de deviner le mot !')
    word = unidecode(choice(file_read)).lower().replace('\n', '')
    false_word = []
    sleep(2)
    print(f"Le mot contient {len(word)} lettres.\nPremière lettre : {word[0].upper()}\nDernière lettre : {word[len(word)-1].upper()}")
    print("Combien d'essais ?")
    tries = 0
    attempts = int(input('==>  '))
    print("Devinez le mot !")
    while tries <= attempts: 
        sleep(1)
        word_try = input('==>  ').lower()
        if len(word_try) > len(word):
            print('Incorrect! Le mot est plus petit!')
            tries += 1
        elif len(word_try) < len(word):
            print('Incorrect! Le mot est plus grand!')
            tries += 1
        if word_try == word:
            tries += 1
            print('Trouvé! Bien joué!')
            sleep(1)
            break
        elif word_try != word:
            tries += 1
            print("Faux !")
            false_word.append(word_try)
            print(f"Liste des mauvais mots : {false_word.__repr__()[1:-1].replace(',',' -')}")
            for letter in word_try:
                if letter  not in word[0:]:
                    print(f"La lettre '{letter.upper()}' n'est pas dans le mot à trouver!")
    sleep(3)
    system('pause')
    print('Accueil...')
    sleep(1.2)
    wrdguess()