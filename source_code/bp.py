from functions import *
import time, os

def intro():
    time.sleep(0.5)
    os.system('cls')
    time.sleep(0.5)
    os.system("echo.")
    os.system("echo BigProject")
    os.system("echo.")
    print("Salut !")
    id = input("Quel est ton identifiant ?  ==>  ")
    time.sleep(2)
    print("Super ! Bienvenue", id, "!!")
    time.sleep(1)
    print("Voulez vous passer au thème Light ? ('o' ou 'n')")
    answer = input("==>  ")
    if answer == 'o':
        time.sleep(1)
        os.system('@echo off')
        os.system('color 70')
        os.system('@echo off')
        os.system('cls')
    elif answer == 'n':
        os.system('@echo off')
        os.system('color 07')
        os.system('cls')
        pass
    elif answer != 'n' or 'o':
        print('Réponse non-incluse !!\n')
        os.system('@echo off')
        os.system('cls')
        pass
    time.sleep(1)
    os.system('@echo off')
    os.system('echo.')
    print("Bienvenue sur BigProject")
    print("L'application capable de tout (ou presque !)")

def rBigProject():
    time.sleep(1)
    print("-- Outils --")
    print(" -- Jeux --")
    print("-- Quitter --")
    # ajt d'autres catégories
    time.sleep(1)
    print("Vous voulez utiliser un de nos nombreux outils ou jouer à un de nos mini-jeux ? 'o' ou 'j'\nPour quitter 'q'") # ajt les lettres pr les catégories
    answer1 = input("==>  ")
    if answer1 == 'o':
        print("Voici nos outils:")
        time.sleep(1)
        print("1. Générateur Ultime")
        print("2. Calculateur d'IMC")
        print("3. Calculateur d'âge grâce à la date de naissance")
        sleep(1)
        print("4. Calculateur de salaire")
        print("5. Calculateur de diviseurs")
        print("6. Analyseur de Texte")
        sleep(1)
        print("7. Calculateur de Pourcentage")
        print("8. Calculateur de TVA")
        print("9. Convertisseur de Température")
        sleep(1)
        print("10. Générateur de Numéro de Téléphone")
        print("11. Convertisseur Majuscule-Minuscule")
        print("12. Compteur de Mots")
        #Ajt les autres outils
        time.sleep(1)
        print("Lequel voulez-vous utilisez ?")
        answer2 = input("Entrez son chiffre  ==>  ")
        if answer2 == '1':
            print("Ouais !")
            time.sleep(1)
            ultimateGenerator()
        elif answer2 == '2':
            print("Ok !")
            time.sleep(1)
            calcImc()
        elif answer2 == '3':
            print("Yes !")
            time.sleep(1)
            calcAge()
        elif answer2 == '4':
            print("Ok !")
            time.sleep(1)
            salary()
        elif answer2 == '5':
            print('Super !')
            time.sleep(1)
            calcDiv()
        elif answer2 == '6':
            print('OK !')
            analyse_text()
        elif answer2 == '7':
            print("Ouais !")
            time.sleep(1)
            calcperc()
        elif answer2 == '8':
            print("Ok !")
            time.sleep(1)
            calctva()
        elif answer2 == '9':
            print("Yes !")
            time.sleep(1)
            tempeconv()
        elif answer2 == '10':
            print("Ok !")
            time.sleep(1)
            numgene()
        elif answer2 == '11':
            print('Super !')
            time.sleep(1)
            converter()
        elif answer2 == '12':
            print('OK !')
            counter()

        elif answer2 != '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '10' or '11' or '12':
            print("Entrez 1, 2, 3, 4 ou 5 pour faire un choix !")
            time.sleep(2)
            rBigProject()
        #Ajt les autres elif pr les autres outils
    elif answer1 == 'j':
        print("Voici nos mini-jeux:")
        time.sleep(1)
        print("1. Pierre, Feuille, Ciseaux")
        print("2. Juste Prix")
        print("3. Roulette Russe")
        print("4. Dés")
        print("5. Roulette")
        print("6. Pièce")
        print("7. Devine le Mot")
        #ajt les autres jeux
        time.sleep(1)
        print("Vous voulez jouer au quel ?")
        answer3 = input("Entrez son chiffre  ==>  ")
        if answer3 == '1':
            print("Ouais !")
            time.sleep(1)
            chifoumi()
        elif answer3 == '2':
            print("Super !")
            time.sleep(1)
            nbGuess()
        elif answer3 == '3':
            print("Yes !")
            time.sleep(1)
            rouletteRu()
        elif answer3 == '4':
            print("Super !")
            time.sleep(1)
            dice()
        elif answer3 == '5':
            print("Ok !")
            time.sleep(1)
            rouletteFr()
        elif answer3 == '6':
            print("Super !")
            time.sleep(1)
            piece()
        elif answer3 == '7':
            print("Yes !")
            time.sleep(1)
            wrdguess()
        elif answer3 != '1' or '2' or '3' or '4' or '5' or '6' or '7':
            print("Entrez 1, 2, 3, 4, 5, 6 ou 7 pour faire un choix !")
            time.sleep(1)
            rBigProject()
        #ajt des elif pour les autres jeux
    #ajt des elif pour les autres catégories
    elif answer1 == 'q':
        exit("Au revoir. Reviens quand tu veux utiliser notre application !")
    elif answer1 != 'o' or 'j' or 'q':
        print("Entrez un 'o' ou 'j' pour faire un choix. Sinon entrez 'q' pour Quitter. Attention!")
        time.sleep(1)
    rBigProject()
    
def bigProject():
    intro()
    rBigProject()

bigProject()