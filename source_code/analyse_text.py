from time import sleep
from os import system
import os.path
from unidecode import unidecode
#Marche bien mais problèmes caractères spéciaux et d'autres bugs

def analyse_text():
    system('@echo off')
    system('cls')
    print("LOGICIEL Analyseur de Fichier Texte")
    sleep(1.5)
    print("Ce logiciel analysant un fichier texte peut compter les lettres et les voyelles ou consonnes dans le texte.\nIl peut aussi compter le nombre de mots et de phrases.")
    print("Attention! Pour l'instant, il ne reconnait pas les caractères spéciaux!!")
    print("\nIl est recommandé de placer ce logiciel dans le dossier du texte à analyser\n")
    sleep(1)
    print("Quelle action voulez-vous effectuer ?")
    print("1. Analyser un fichier texte")
    print("0. Quitter")
    answer = int(input(r"==>  "))
    if answer == 1:
        analyse()
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
        analyse_text()
    
def analyse():
    sleep(1.2)
    system('@echo off')
    system('cls')
    print("-- ANALYSE --")
    sleep(1)
    print("Entrez le chemin d'accès vers le texte (ou uploader le fichier)")
    text_file_input = input("==>  ")
    test_exist_file = os.path.exists(text_file_input)
    test_file_text = os.path.splitext(text_file_input)
    kind = ['.txt']
    if test_exist_file == True:
        if test_file_text[1] in kind:
            print("Analyse en cours...")
            sleep(4)
            file = open(text_file_input, r'r')
            read_file = unidecode(file.read())
            text_min = read_file.lower()
            words = 0
            word_cut = text_min.split()
            for word in word_cut:
                words += 1
            letter_count = 0
            vowels_count = 0
            consonnes_count = 0
            alphabet = ['a','à','â','b','c','ç','d','e','é','ê','è','f','g','h','i','ï','î','j','k','l','m','n','o','ô','p','q','r','s','t','u','û','ü','v','w','x','y','ÿ','z']
            vowels = ['a','à','â','e','é','ê','è','i','ï','î','o','ô','u','û','ü', 'ÿ','y']
            consonnes = ['b','c','ç','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
            for letter in text_min:
                if letter in alphabet:
                    letter_count += 1
                if letter in vowels:
                    vowels_count += 1
                elif letter in consonnes:
                    consonnes_count += 1
            print("Analyse terminée !")
            print('Préparation du rapport...')
            sleep(2)
            sleep(1)
            print(f"Votre fichier texte contient : {words} mots, {letter_count} lettres.\nIl contient aussi {vowels_count} voyelles et {consonnes_count} consonnes")
        else:
            print("Ce n'est pas un fichier texte!")
            sleep(2)
            analyse_text()
    else:
        print("Le fichier n'existe pas ! Vérifier le chemin d'accès !")
        sleep(2)
        analyse_text()
    system('pause')
    print('Accueil...')
    sleep(1.2)
    analyse_text()