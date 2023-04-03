from time import sleep
from os import system

def counter():
    system('@echo off')
    system('cls')
    print("LOGICIEL COMPTEUR De Mots et De Lettres")
    sleep(1.5)
    print("Ce logiciel peut compter les lettres et les voyelles ou consonnes dans un mot.\nIl peut aussi compter le nombre de mots dans une phrase.")
    print("Quelle action voulez-vous effectuer ?")
    print("1. Compter le nombre de mots dans une phrase")
    print("2. Compter le nombre de lettres dans un mot ou dans une phrase")
    print("3. Compter le nombre de voyelles ou de consonnes dans mot ou une phrase")
    print("0. Quitter")
    answer = int(input("==>  "))
    if answer == 1:
        wordNbCounter()
    elif answer == 2:
        lettersNbCounter()
    elif answer == 3:
        lettersTypeNbCounters()
    elif answer == 0:
        print("Vous allez quitter le logiciel dans 5 secondes...")
        sleep(2.7)
        print("Vous quittez le logiciel...")
        sleep(1.8)
        system('cls')
        sleep(1)
        exit("Exit...")
    elif answer != 1 or 2 or 3 or 0:
        print("Veuillez entrer 1, 2 ou 3 pour faire un choix! Pour Quitter, taper 0.")
        sleep(2)
        counter()

def wordNbCounter():
    sleep(1.2)
    system('@echo off')
    system('cls')
    print("Compteur de nombre de mots dans une phrase".upper())
    sleep(1)
    print("Entrez une phrase")
    answer = input("==>  ")
    word = 0
    for space in answer:
        if space == ' ':
            word += 1
    word = word+1
    print("Il y a", word,"mots dans cette phrase.")
    sleep(4)
    print('Accueil...')
    sleep(1.2)
    counter()

def lettersNbCounter():
    sleep(1.2)
    system('@echo off')
    system('cls')
    print("Compteur de nombre de lettres dans un mot ou dans une phrase".upper())
    sleep(1)
    print("Entrez un mot ou une phrase")
    answer = input("==>  ")
    answer_min = answer.lower()
    letter_count = 0
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in answer_min:
        if letter in alphabet:
            letter_count += 1
    print(f"Votre phrase/mot compte {letter_count} lettre(s)")
    sleep(4)
    print('Accueil...')
    sleep(1.2)
    counter()

def lettersTypeNbCounters():
    sleep(1.2)
    system('@echo off')
    system('cls')
    print("Compteur de nombre de voyelles ou de consonnes dans mot ou une phrase".upper())
    sleep(1) 
    print("Entrez un mot ou une phrase")
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    consonnes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
    answer = input("==>  ")
    answer_min = answer.lower()
    vowels_count = 0
    consonnes_count = 0
    for letter in answer_min:
        if letter in vowels:
            vowels_count += 1
        elif letter in consonnes:
            consonnes_count += 1
    print(f"Votre phrase/mot compte {vowels_count} voyelle(s) et {consonnes_count} consonne(s).")
    sleep(4)
    print('Accueil...')
    sleep(1.2)
    counter()