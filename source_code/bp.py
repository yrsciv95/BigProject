from functions import *
import time, os

def intro():
    from plyer import notification
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
    notification_title = "BigProject"  
    notification_message = f"Salut {id},\nJ'espère que tu vas passer un bon moment sur BigProject !"
    notification_app_name = "BigProject"
    notification_ticker = "BigProject"
    notification.notify(title = notification_title, message = notification_message, app_icon = None, app_name = notification_app_name, ticker = notification_ticker, toast = False)
    time.sleep(1)
    print("Voulez vous changer la couleur du texte ? ('o' ou 'n')")
    answer = input("==>  ")
    if answer == 'o':
        time.sleep(1)
        print("\nGuide Couleur\n")
        time.sleep(1)
        os.system('@echo off')
        os.system('color guide')
        print("\nLes meilleurs associations de couleurs sont :\n'color 0A', 'color 02', 'color 07', 'color 0F', 'color 04'")
        print("\nEn quelle couleur voulez-vous changer le texte ?")
        time.sleep(1.2)
        os.system(input("==>  "))
        os.system('@echo off')
        os.system('cls')
    elif answer == 'n':
        os.system('@echo off')
        os.system('color')
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
        print("4. Calculateur de salaire")
        print("5. Calculateur de diviseurs")
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

        elif answer2 != '1' or '2' or '3' or '4' or '5':
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

        elif answer3 != '1' or '2' or '3' or '4' or '5':
            print("Entrez 1, 2, 3, 4 ou 5 pour faire un choix !")
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