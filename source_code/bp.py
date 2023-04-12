import os.path
import random
import string
from os import system
from time import sleep
from unidecode import unidecode


def bp():

    def intro():
        sleep(0.5)
        system("cls")
        sleep(0.5)
        system("echo.")
        system("echo BigProject")
        system("echo.")
        print("Salut !")
        id = input("Quel est ton identifiant ?  ==>  ")
        sleep(2)
        print("Super ! Bienvenue", id, "!!")
        sleep(1)
        print("Voulez vous passer au thème Light ? ('o' ou 'n')")
        answer = input("==>  ")
        if answer == "o":
            sleep(1)
            system("@echo off")
            system("color F0")
            system("@echo off")
            system("cls")
        elif answer == "n":
            system("@echo off")
            system("color 07")
            system("cls")
            pass
        elif answer != "n" or "o":
            print("Réponse non-incluse !!\n")
            system("@echo off")
            system("cls")
            pass
        sleep(1)
        system("@echo off")
        system("echo.")
        print("Bienvenue sur BigProject")
        print("L'application capable de tout (ou presque !)")

    def rBigProject():
        sleep(1)
        print("-- Outils --")
        print(" -- Jeux --")
        print("-- Quitter --")
        sleep(1)
        print(
            "Vous voulez utiliser un de nos nombreux outils ou jouer à un de nos mini-jeux ? 'o' ou 'j'\nPour quitter 'q'"
        )
        answer1 = input("==>  ")
        if answer1 == "o":
            print("Voici nos outils:")
            sleep(1)
            print("1. Générateur Ultime")
            print("2. Calculateur de salaire")
            sleep(1)
            print("3. Analyseur de Texte")
            print("4. Convertisseur de Température")
            # Ajt les autres outils
            sleep(1)
            print("Lequel voulez-vous utilisez ?")
            answer2 = input("Entrez son chiffre  ==>  ")
            if answer2 == "1":
                sleep(1)

                def pwdGeneratorLetters():
                    letters_uppercase = string.ascii_uppercase
                    letters_lowercase = string.ascii_lowercase
                    symbols = "!#$%&()*+-/<=>?@\_"
                    numbers = string.digits
                    pwd_sample = (letters_uppercase +
                                  letters_lowercase + numbers + symbols)
                    print("Bip... Bip... Nouveau Mot De Passe...")
                    answer2 = input(
                        "Avec combien de caractères ? Pour la sécu, 8 c'est bien!  ==>  ")
                    if answer2 not in '1234567890':
                        print("Entrez un chiffre !")
                        sleep(1.5)
                        pwdGeneratorLetters()
                    length = int(answer2)
                    pwd = "".join(random.sample(pwd_sample, length))
                    print("Nouveau Mot de Passe ultra-securisé  ==>  ", pwd)
                    sleep(2)
                    system('pause')
                    print("Accueil...")
                    sleep(1.5)
                    pwdGenerator()

                def pwdGeneratorNum():
                    numbers = string.digits
                    pwd_sample = numbers
                    print("Bip... Bip... Nouveau Mot De Passe...")
                    answer2 = input("Avec combien de caractères ?  ==>  ")
                    if answer2 not in '1234567890':
                        print("Entrez un chiffre !")
                        sleep(1.5)
                        pwdGeneratorNum()
                    length = int(answer2)
                    pwd = "".join(random.sample(pwd_sample, length))
                    print(
                        "Tiens, ton nouveau mot de passe de téléphone ultra-securisé  ==>  ", pwd)
                    sleep(2)
                    system('pause')
                    print("Accueil...")
                    sleep(1.5)
                    pwdGenerator()

                def pwdGenerator():
                    system('@echo off')
                    system('cls')
                    print("Générateur de Mots de Passe")
                    print(
                        "1. Génerer un Mot de Passe avec des Chiffres, des Lettres, et des Symboles")
                    print(
                        "2. Génerer un Mot de passe pour téléphone avec des Chiffres seulement")
                    print("0. Quitter")
                    answer = input(
                        "Tapez 1 ou 2 pour choisir une option  ==>  ")
                    if answer not in '120':
                        print("Entrez un chiffre !")
                        sleep(1.5)
                        pwdGenerator()
                    if answer == '1':
                        sleep(1.2)
                        pwdGeneratorLetters()
                    elif answer == '2':
                        sleep(1.2)
                        pwdGeneratorNum()
                    elif answer == '0':
                        sleep(1)
                        print("Accueil...")
                        sleep(1.5)
                        ultimateGenerator()

                def nbGenerator():
                    system('@echo off')
                    system('cls')
                    print("Générateur de Nombres")
                    print("Combien de nombres voulez-vous génerer ?")
                    nb = input("==>  ")
                    if nb not in '1234567890':
                        print("Entrez un chiffre !")
                        sleep(1.2)
                        nbGenerator()
                    print("Entre combien à combien ? (1 par ligne)")
                    range1 = input("==>  ")
                    if range1 not in '1234567890':
                        print("Entrez un chiffre !")
                        sleep(1.2)
                        nbGenerator()
                    range2 = input("==>  ")
                    if range2 not in '1234567890':
                        print("Entrez un chiffre !")
                        sleep(1.2)
                        nbGenerator()
                    generated_nb = random.choices(
                        range(int(range1), int(range2)), k=int(nb))
                    print(f"\nNombre(s) géneré(s)")
                    for nb in generated_nb:
                        print(nb, end="   ")
                    sleep(2)
                    print()
                    system('pause')
                    print("Accueil...")
                    sleep(1.5)
                    nbGenerator()

                def letterGenerator():
                    system('@echo off')
                    system('cls')
                    print("Générateur de Lettres")
                    print("Combien de lettres voulez-vous génerer ?")
                    letters = string.ascii_uppercase
                    ltr = input("==>  ")
                    if ltr not in '1234567890':
                        print("Entrez un chiffre !")
                        sleep(1.2)
                        letterGenerator()
                    generated_ltr = random.choices(letters, k=int(ltr))
                    print(f"\nLettre(s) génerée(s)")
                    for ltr in generated_ltr:
                        print(ltr, end="   ")
                    sleep(2)
                    print()
                    system('pause')
                    print("Accueil...")
                    sleep(1.5)
                    letterGenerator()

                def ultimateGenerator():
                    system('@echo off')
                    system('cls')
                    print("GENERATEUR ULTIME")
                    print("1. Génerateur de Mots de Passe")
                    print("2. Génerateur de Nombres aléatoire")
                    print("3. Génerateur de Lettres aléatoire")
                    print("0. Quitter")
                    print("Quelle action voulez-vous effectuer ?")
                    answer = input("==>  ")
                    if answer not in '0123':
                        print(
                            "Entrez 1, 2 ou 3 pour faire un choix. Pour Quitter, taper 0")
                        sleep(1.5)
                        ultimateGenerator()
                    if answer == "1":
                        sleep(1)
                        pwdGenerator()
                    elif answer == "2":
                        sleep(1)
                        nbGenerator()
                    elif answer == "3":
                        sleep(1)
                        letterGenerator()
                    elif answer == "0":
                        print("Vous allez quitter le logiciel dans 5 secondes...")
                        sleep(2.7)
                        print("BigProject...")
                        sleep(1.8)
                        rBigProject()

                ultimateGenerator()

            elif answer2 == "2":
                sleep(1)

                def cadre():
                    sleep(1)
                    system('cls')
                    print("Calculer son salaire après taxes (Cadre)")
                    salary = float(
                        input("Entrez un salaire brut mensuel  ==>  "))
                    currency = ["$", "£", "€"]
                    user_currency = input(
                        "Entrez la devise de votre salaire  ==>  ")
                    if user_currency not in currency:
                        print("Entrez une devise valide ($, £, €)")
                        sleep(1)
                        cadre()
                    net = (salary * 25) / 100
                    net_salary_month = salary - net
                    net_salary_year = net_salary_month * 12
                    print("Calcul ...")
                    sleep(1.5)
                    print(
                        "  ==>  ",
                        round(net_salary_month),
                        user_currency
                    )
                    print(
                        "Ainsi que votre salaire net annuel ==>  ",
                        round(net_salary_year),
                        user_currency
                    )
                    sleep(2)
                    system('pause')
                    print("Accueil...")
                    sleep(1.5)
                    salaire()

                def foncPub():
                    sleep(1)
                    system('cls')
                    print(
                        "Calculer son salaire après taxes (Fonction Publique)")
                    salary = float(
                        input("Entrez un salaire brut mensuel  ==>  "))
                    currency = ["$", "£", "€"]
                    user_currency = input(
                        "Entrez la devise de votre salaire  ==>  ")
                    if user_currency not in currency:
                        print("Entrez une devise valide ($, £, €)")
                        sleep(1)
                        foncPub()
                    net = (salary * 15) / 100
                    net_salary_month = salary - net
                    net_salary_year = net_salary_month * 12
                    print("Calcul ...")
                    sleep(1.5)
                    print(
                        "  ==>  ",
                        round(net_salary_month),
                        user_currency
                    )
                    print(
                        "Ainsi que votre salaire net annuel ==>  ",
                        round(net_salary_year),
                        user_currency
                    )
                    sleep(2)
                    system('pause')
                    print("Accueil...")
                    sleep(1.5)
                    salaire()

                def liberal():
                    sleep(1)
                    system('cls')
                    print(
                        "Calculer son salaire après taxes (Profession Libérale)"
                    )
                    salary = float(
                        input("Entrez un salaire brut mensuel  ==>  "))
                    currency = ["$", "£", "€"]
                    user_currency = input(
                        "Entrez la devise de votre salaire  ==>  ")
                    if user_currency not in currency:
                        print("Entrez une devise valide ($, £, €)")
                        sleep(1)
                        liberal()
                    net = (salary * 45) / 100
                    net_salary_month = salary - net
                    net_salary_year = net_salary_month * 12
                    print("Calcul ...")
                    sleep(1.5)
                    print(
                        "  ==>  ",
                        round(net_salary_month),
                        user_currency
                    )
                    print(
                        "Ainsi que votre salaire net annuel ==>  ",
                        round(net_salary_year),
                        user_currency
                    )
                    sleep(2)
                    system('pause')
                    print("Accueil...")
                    sleep(1.5)
                    salaire()

                def nonCadre():
                    sleep(1)
                    system('cls')
                    print("Calculer son salaire après taxes (Non - Cadre)")
                    salary = float(
                        input("Entrez un salaire brut mensuel  ==>  "))
                    currency = ["$", "£", "€"]
                    user_currency = input(
                        "Entrez la devise de votre salaire  ==>  ")
                    if user_currency not in currency:
                        print("Entrez une devise valide ($, £, €)")
                        sleep(1)
                        nonCadre()
                    net = (salary * 22) / 100
                    net_salary_month = salary - net
                    net_salary_year = net_salary_month * 12
                    print("Calcul ...")
                    sleep(1.5)
                    print(
                        "Voici votre salaire net mensuel  ==>  ",
                        round(net_salary_month),
                        user_currency,
                    )
                    print(
                        "Ainsi que votre salaire net annuel ==>  ",
                        round(net_salary_year),
                        user_currency
                    )
                    sleep(2)
                    system('pause')
                    print("Accueil...")
                    sleep(1.5)
                    salaire()

                def salaire():
                    print("CALCULATEUR DE SALAIRE")
                    print("1. Calculer mon salaire net")
                    print("0. Quitter")
                    print("Quelle action voulez-vous effectuer ?")
                    answer = input("==>  ")
                    if answer not in '01':
                        print("Entrez 1 pour commencer. Sinon, taper 0")
                        sleep(1.5)
                        salaire()
                    if answer == "1":
                        paye()
                    elif answer == "0":
                        print("Vous allez quitter le logiciel dans 5 secondes...")
                        sleep(2.7)
                        print("BigProject...")
                        sleep(1.8)
                        rBigProject()

                def paye():
                    sleep(1)
                    print("TYPES DE PAYES")
                    sleep(0.2)
                    print("1. Non - Cadre")
                    print("2. Cadre")
                    print("3. Profession Libérale")
                    print("4. Fonction Publique")
                    print("0. Quitter")
                    paye = input("==>  ")
                    if paye not in '01234':
                        sleep(1)
                        print(
                            "Entrez 1, 2, 3 ou 4 pour faire un choix ! Pour Quitter, taper 0.")
                        sleep(1.5)
                        salaire()
                    if paye == "0":
                        sleep(1)
                        print("Accueil...")
                        sleep(1.5)
                        salaire()
                    elif paye == "1":
                        nonCadre()
                    elif paye == "2":
                        cadre()
                    elif paye == "3":
                        liberal()
                    elif paye == "4":
                        foncPub()

                salaire()
            elif answer2 == "3":
                sleep(1)

                def choice():
                    system("@echo off")
                    system("cls")
                    print("LOGICIEL D'ANALYSE GRAMMATICALE")
                    sleep(1.5)
                    print("Quelle action voulez-vous effectuer ?")
                    print("1. Analyseur de Fichier Texte")
                    print("2. Compteur de Caractères")
                    print("0. Quitter")
                    answer = input("==>  ")
                    if answer not in '120':
                        print(
                            "Entrez 1 ou 2 pour faire un choix! Pour Quitter, taper 0.")
                        sleep(2)
                        choice()
                    if answer == "1":
                        analyse_text()
                    elif answer == "2":
                        counter()
                    elif answer == "0":
                        print("Vous allez quitter le logiciel dans 5 secondes...")
                        sleep(2.7)
                        print("BigProject...")
                        sleep(1.8)
                        rBigProject()
                    elif answer != 1 or 2 or 0:
                        print(
                            "Veuillez entrer 1 ou 2 pour faire un choix! Pour Quitter, taper 0.")
                        sleep(2)
                        choice()

                def counter():
                    system("@echo off")
                    system("cls")
                    print("LOGICIEL Compteur de Caractères")
                    sleep(1.5)
                    print("Quelle action voulez-vous effectuer ?")
                    print("1. Compter le nombre de mots dans une phrase")
                    print(
                        "2. Compter le nombre de lettres dans un élément grammaticale")
                    print(
                        "3. Compter le nombre de voyelles ou de consonnes dans mot ou une phrase")
                    print("0. Quitter")
                    answer = input("==>  ")
                    if answer not in '1230':
                        print(
                            "Entrez 1, 2 ou 3 pour faire un choix! Pour Quitter, taper 0.")
                        sleep(2)
                        counter()
                    if answer == '1':
                        wordNbCounter()
                    elif answer == '2':
                        lettersNbCounter()
                    elif answer == '3':
                        lettersTypeNbCounters()
                    elif answer == 0:
                        sleep(1)
                        print("Accueil...")
                        sleep(1.5)
                        choice()

                def wordNbCounter():
                    sleep(1.2)
                    system("@echo off")
                    system("cls")
                    print("Compter le nombre de mots dans une phrase".upper())
                    sleep(1)
                    print("Entrez une phrase")
                    answer = input("==>  ")
                    cut_word = answer.split()
                    words = len(cut_word)
                    print(f"Cette phrase compte {words} mots.")
                    sleep(2)
                    system('pause')
                    print("Accueil...")
                    sleep(1.5)
                    counter()

                def lettersNbCounter():
                    sleep(1.2)
                    system("@echo off")
                    system("cls")
                    print(
                        "Compter le nombre de lettres dans un élément grammaticale".upper())
                    sleep(1)
                    print("Entrez un mot ou une phrase")
                    answer = input("==>  ")
                    answer_min = answer.lower()
                    answer_clean = unidecode(answer_min)
                    letter_count = 0
                    for letter in answer_clean:
                        if letter in string.ascii_letters:
                            letter_count += 1
                    print(
                        f"Cet élément grammaticale compte {letter_count} lettres.")
                    sleep(2)
                    system('pause')
                    print("Accueil...")
                    sleep(1.5)
                    counter()

                def lettersTypeNbCounters():
                    sleep(1.2)
                    system("@echo off")
                    system("cls")
                    print(
                        "Compter le nombre de voyelles et de consonnes dans un élement grammaticale".upper())
                    sleep(1)
                    print("Entrez un mot ou une phrase")
                    answer = input("==>  ")
                    answer_min = answer.lower()
                    answer_clean = unidecode(answer_min)
                    vowels_count = 0
                    consonnes_count = 0
                    vowels = ["a", "e", "i", "o", "u", "y"]
                    for letter in answer_clean:
                        if letter in vowels:
                            vowels_count += 1
                        elif letter not in vowels:
                            if letter in string.ascii_letters:
                                consonnes_count += 1
                    print(
                        f"Cet élement grammaticale compte {vowels_count} voyelles et {consonnes_count} consonnes.")
                    sleep(2)
                    system('pause')
                    print("Accueil...")
                    sleep(1.5)
                    counter()

                def analyse_text():
                    system("@echo off")
                    system("cls")
                    print("LOGICIEL Analyseur de Fichier Texte")
                    sleep(1.5)
                    print("Quelle action voulez-vous effectuer ?")
                    print("1. Analyser un Fichier Texte")
                    print("0. Quitter")
                    answer = input(r"==>  ")
                    if answer not in '10':
                        print(
                            "Veuillez entrer 1 pour commencer ! Pour Quitter, taper 0.")
                        sleep(2)
                        analyse_text()
                    if answer == '1':
                        analyse()
                    elif answer == '0':
                        sleep(1)
                        print("Accueil...")
                        sleep(1.5)
                        choice()

                def analyse():
                    sleep(1.2)
                    system("@echo off")
                    system("cls")
                    print("-- ANALYSE --")
                    sleep(1)
                    print(
                        "Entrez le chemin d'accès vers le fichier texte (ou uploader le fichier)")
                    text_file_input = input("==>  ")
                    test_exist_file = os.path.exists(text_file_input)
                    test_file_text = os.path.splitext(text_file_input)
                    kind = [".txt"]
                    if test_exist_file == True:
                        if test_file_text[1] in kind:
                            print("Analyse en cours...")
                            sleep(2)
                            file = open(text_file_input, r"r")
                            read_file = unidecode(file.read())
                            text = read_file.lower()
                            words = 0
                            letter_count = 0
                            vowels_count = 0
                            consonnes_count = 0
                            alphabet = string.ascii_letters
                            vowels = ['a', 'e', 'i', 'o', 'u', 'y']
                            cut_word = text.split()
                            words = len(cut_word)
                            for letter in text:
                                if letter in vowels:
                                    vowels_count += 1
                                elif letter not in vowels:
                                    if letter in alphabet:
                                        consonnes_count += 1
                            for letter in text:
                                if letter in alphabet:
                                    letter_count += 1
                            print("Analyse terminée !")
                            print("Préparation du rapport...")
                            sleep(2)
                            print(
                                f"Votre Fichier Texte contient {words} mots et {letter_count} lettres.\nIl contient aussi {vowels_count} voyelles et {consonnes_count} consonnes")
                        else:
                            print("Ce n'est pas un fichier texte!")
                            sleep(2)
                            analyse_text()
                    else:
                        print(
                            "Le fichier n'existe pas ! Vérifier le chemin d'accès !")
                        sleep(2)
                        analyse_text()
                    sleep(2)
                    system("pause")
                    print("Accueil...")
                    sleep(1.2)
                    analyse_text()

                choice()

            elif answer2 == "4":
                sleep(1)

                def tempeconv():
                    system("@echo off")
                    system("cls")
                    print("LOGICIEL Convertisseur de Température")
                    sleep(1.5)
                    print(
                        "Ce logiciel peut convertir les températures en °C vers °F, °R, K")
                    print("Quelle action voulez-vous effectuer ?")
                    print("1. Celsius --> Fahrenheit")
                    print("2. Celsius --> Kelvin")
                    print("3. Celsius --> Rankine")
                    print("0. Quitter")
                    answer = input("==>  ")
                    if answer not in '0123':
                        print(
                            "Entrez 1, 2 ou 3 pour faire un choix. Pour Quitter, taper 0.")
                        sleep(2)
                        tempeconv()
                    if answer == 1:
                        fconv()
                    elif answer == 2:
                        kconv()
                    elif answer == 3:
                        rconv()
                    elif answer == 0:
                        print("Vous allez quitter le logiciel dans 5 secondes...")
                        sleep(2.7)
                        print("BigProject...")
                        sleep(1.8)
                        rBigProject()

                def fconv():
                    sleep(1.2)
                    system("@echo off")
                    system("cls")
                    print("Celsius --> Fahrenheit".upper())
                    sleep(1)
                    print("Entrez une température (en °C)")
                    input_tempe = float(input("==>  "))
                    print("Calcul...")
                    sleep(2)
                    tempe_conv = (input_tempe * 9 / 5) + 32
                    print(f"{input_tempe}°C correspond à {tempe_conv}°F")
                    sleep(2.5)
                    system("pause")
                    print("Accueil...")
                    sleep(1.2)
                    tempeconv()

                def kconv():
                    sleep(1.2)
                    system("@echo off")
                    system("cls")
                    print("Celsius --> Kelvin".upper())
                    sleep(1)
                    print("Entrez une température (en °C)")
                    input_tempe = float(input("==>  "))
                    print("Calcul...")
                    sleep(2)
                    tempe_conv = input_tempe + 273.15
                    print(f"{input_tempe}°C correspond à {tempe_conv} K")
                    sleep(2.5)
                    system("pause")
                    print("Accueil...")
                    sleep(1.2)
                    tempeconv()

                def rconv():
                    sleep(1.2)
                    system("@echo off")
                    system("cls")
                    print("Celsius --> Rankine".upper())
                    sleep(1)
                    print("Entrez une température (en °C)")
                    input_tempe = float(input("==>  "))
                    print("Calcul...")
                    sleep(2)
                    tempé_conv = input_tempe * 9 / 5 + 491.67
                    print(f"{input_tempe}°C correspond à {tempé_conv}°R")
                    sleep(2.5)
                    system("pause")
                    print("Accueil...")
                    sleep(1.2)
                    tempeconv()

                tempeconv()
            elif answer2 != "1" or "2" or "3" or "4":
                print("Entrez 1, 2, 3 ou 4 pour faire un choix !")
                sleep(2)
                rBigProject()
            # Ajt les autres elif pr les autres outils
        elif answer1 == "j":
            print("Voici nos mini-jeux:")
            sleep(1)
            print("1. Pierre, Feuille, Ciseaux")
            print("2. Juste Prix")
            print("3. Roulette Russe")
            print("4. Dés")
            print("5. Devine le Mot")
            # ajt les autres jeux
            sleep(1)
            print("Vous voulez jouer au quel ?")
            answer3 = input("Entrez son chiffre  ==>  ")
            if answer3 == "1":
                sleep(1)

                def chifoumi():
                    system('@echo off')
                    system('cls')
                    print("JEU DU CHIFOUMI")
                    print("1. Jouer au Chifoumi")
                    print("0. Quitter")
                    print("Quelle action voulez-vous effectuer ?")
                    answer = input("==>  ")
                    if answer not in '01':
                        print("Entrez 1 pour jouer. Pour Quitter, taper 0")
                        sleep(1.5)
                        chifoumi()
                    if answer == '1':
                        game()
                    elif answer == "0":
                        print("Vous allez quitter le logiciel dans 5 secondes...")
                        sleep(2.7)
                        print("BigProject...")
                        sleep(1.8)
                        rBigProject()

                def game():
                    sleep(1.5)
                    system('cls')
                    choice_list = ["Pierre", "Feuille", "Ciseaux"]
                    statut = False
                    p_score = 0
                    c_score = 0
                    turn = 0
                    print("Partie en combien de manches ?")
                    manches = input("==>  ")
                    if manches not in '1234567890':
                        print("Entrez un chiffre !")
                        sleep(1.5)
                        game()
                    while statut == False:
                        computer = choice_list[random.randint(0, 2)]
                        player = input(
                            "Pierre, Feuille ou Ciseaux (ou 'Quit' pour quitter)  ==>  ")
                        if player == "Quit":
                            sleep(1)
                            print("Accueil...")
                            sleep(1.5)
                            chifoumi()
                        elif player == computer:
                            print(
                                f"Votre adversaire choisit aussi {computer} !")
                            print(
                                "Il y a donc égalité ! Personne ne gagne de points")
                            turn += 1
                        elif player == "Pierre":
                            if computer == "Feuille":
                                print(f"Perdu! {computer} recouvre {player}")
                                turn += 1
                                c_score += 1
                            else:
                                print(f"Gagné! {player} écrase {computer}")
                                turn += 1
                                p_score += 1
                        elif player == "Feuille":
                            if computer == "Ciseaux":
                                print(f"Perdu! {computer} coupe {player}")
                                turn += 1
                                c_score += 1
                            else:
                                print(f"Gagné! {player} recouvre {computer}")
                                turn += 1
                                p_score += 1
                        elif player == "Ciseaux":
                            if computer == "Pierre":
                                print(f"Perdu! {computer} écrase {player}")
                                turn += 1
                                c_score += 1
                            else:
                                print("Gagné !", player, "coupe", computer)
                                turn += 1
                                p_score += 1
                        else:
                            print(
                                "Entrez 'Pierre', 'Feuille', ou 'Ciseaux' pour jouer!\nSinon entrez 'Quit' pour Quitter")
                        if turn == int(manches):
                            statut = True
                            print("Fin de la partie !!")
                            if p_score > c_score:
                                print("Vous avez gagné !")
                                print(
                                    f"{p_score} à {c_score} sur {manches} points possible")
                                sleep(2)
                                system('pause')
                                print("Accueil...")
                                sleep(1.5)
                                chifoumi()
                            elif c_score > p_score:
                                print("Vous avez Perdu! Dommage!")
                                print(
                                    f"{c_score} à {p_score} sur {manches} points possible")
                                sleep(2)
                                system('pause')
                                print("Accueil...")
                                sleep(1.5)
                                chifoumi()
                            elif c_score == p_score:
                                print("Egalité Parfaite !")
                                print(
                                    f"{c_score} à {p_score} sur {manches} points possible")
                                sleep(2)
                                system('pause')
                                print("Accueil...")
                                sleep(1.5)
                                chifoumi()

                chifoumi()
            elif answer3 == "2":
                sleep(1)

                def game():
                    sleep(1.5)
                    system('cls')
                    just_price = random.randint(1, 100)
                    statut = True
                    print("Partie en combien de manches ?")
                    nb_essais = input("==>  ")
                    if nb_essais not in '0123456789':
                        print("Entrez un chiffre !")
                        sleep(1.5)
                        game()
                    essais = 0
                    while statut == True:
                        remaining_trials = int(nb_essais) - essais - 1
                        user_price = input(
                            "Deviner le prix (entre 1 et 100) ==>  ")
                        user_price = int(user_price)
                        if type(user_price) is not int:
                            print("Entrez un chiffre !")
                            sleep(1.5)
                            continue
                        if int(user_price) == just_price:
                            print(
                                f"Bien joué, vous avez le juste prix en {essais} essais")
                            statut = False
                        elif int(user_price) > just_price:
                            print("Le chiffre à trouver est plus bas !!")
                            essais += 1
                            print(f"Il vous reste {remaining_trials} essais !")
                        elif int(user_price) < just_price:
                            print("Le chiffre à trouver est plus haut !!")
                            essais += 1
                            print(f"Il vous reste {remaining_trials} essais !")
                        if essais == int(nb_essais):
                            statut = False
                            print("Perdu! Dommage!")
                            print("Le chiffre était", just_price)
                    sleep(1.7)
                    system('pause')
                    print("Accueil...")
                    sleep(1.5)
                    justprice()

                def justprice():
                    sleep(1)
                    system('cls')
                    print("JUSTE PRIX")
                    print("1. Jouer au Juste Prix")
                    print("0. Quitter")
                    print("Quelle action voulez-vous effectuer ?")
                    answer = input("==>  ")
                    if answer not in '01':
                        print("Entrez 1 pour jouer. Pour Quitter, taper 0")
                        sleep(1.5)
                        justprice()
                    if answer == '1':
                        game()
                    elif answer not in "1":
                        print("Vous allez quitter le logiciel dans 5 secondes...")
                        sleep(2.7)
                        print("BigProject...")
                        sleep(1.8)
                        rBigProject()

                justprice()
            elif answer3 == "3":
                sleep(1)

                def game():
                    start = input("Tenter votre chance ? ('o' ou 'n') ==>  ")
                    if start == "o":
                        choice = ["1", "2", "3", "4", "5", "6"]
                        trigger = random.choice(choice)
                        if trigger == "1":
                            print("Ahaha! Perdu!")
                            roulette()
                        elif trigger != "1":
                            print("Vous avez gagné. Bien joué !")
                            game()
                    elif start == "n":
                        print("Tu n'as pas le goût du risque !")
                        sleep(1)
                        print("Accueil...")
                        sleep(1.5)
                        roulette()
                    elif start not in "o" or "n":
                        print("Entrez 'o' ou 'n' pour jouer !")
                        game()

                def roulette():
                    sleep(1)
                    system('cls')
                    print("ROULETTE RUSSE")
                    print("1. Jouer à la Roulette Russe")
                    print("0. Quitter")
                    print("Quelle action voulez-vous effectuer ?")
                    answer = input("==>  ")
                    if answer not in '01':
                        print("Entrez 1 pour jouer. Pour Quitter, taper 0")
                        sleep(1.5)
                        roulette()
                    if answer == '1':
                        game()
                    elif answer not in "1":
                        print("Vous allez quitter le logiciel dans 5 secondes...")
                        sleep(2.7)
                        print("BigProject...")
                        sleep(1.8)
                        rBigProject()

                roulette()
            elif answer3 == "4":
                def game():
                    start = input("Lancer les dés ? ('o' ou 'n') ==>  ")
                    statut = False
                    p_score = 0
                    c_score = 0
                    turn = 0
                    while statut == False:
                        if start == "o":
                            choice = [1, 2, 3, 4, 5, 6]
                            computer_choice = random.choices(choice, k=2)
                            user_choice = random.choices(choice, k=2)
                            user = sum(user_choice)
                            computer = sum(computer_choice)
                            if computer > user:
                                print("Lancement des dés ...")
                                sleep(2)
                                print("Votre adversaire gagne !")
                                print(
                                    f"Vous avez obtenu {user_choice[0]} et {user_choice[1]}"
                                )
                                print(
                                    f"Votre adversaire a obtenu {computer_choice[0]} et {computer_choice[1]}"
                                )
                                print(user, "<", computer)
                                turn += 1
                                c_score += 1
                                sleep(1)
                            elif computer == user:
                                print("Lancement des dés ...")
                                sleep(2)
                                print(
                                    f"Vous avez obtenu {user_choice[0]} et {user_choice[1]} comme votre adversaire !"
                                )
                                print("Egalité ! Plus 1 partout !")
                                c_score += 1
                                p_score += 1
                                turn += 1
                                sleep(1)
                            else:
                                print("Lancement des dés ...")
                                sleep(2)
                                print("Votre avez gagné !")
                                print(
                                    f"Vous avez obtenu {user_choice[0]} et {user_choice[1]}"
                                )
                                print(
                                    f"Votre adversaire a obtenu {computer_choice[0]} et {computer_choice[1]}"
                                )
                                print(user, ">", computer)
                                turn += 1
                                p_score += 1
                                sleep(1)
                        elif start == "n":
                            sleep(1)
                            print("Accueil...")
                            sleep(1.5)
                            dice()
                        elif start not in "o" or "n":
                            print("Entrez 'o' ou 'n' pour commencez !")
                            game()
                        if turn == 5:
                            statut = True
                            print("\nFin de la partie !!")
                            if p_score > c_score:
                                print("Vous avez gagné !")
                                print("Il y a", p_score, "à", c_score,
                                      "pour vous !")
                            elif c_score > p_score:
                                print("C'est perdu !! Dommage !")
                                print("Il y a", c_score, "à", p_score,
                                      "pour lui !")

                def dice():
                    sleep(1)
                    system('cls')
                    print("JEU DE DÉS")
                    print("1. Jouer au Dés")
                    print("0. Quitter")
                    print("Quelle action voulez-vous effectuer ?")
                    answer = input("==>  ")
                    if answer not in '01':
                        print("Entrez 1 pour jouer. Pour Quitter, taper 0")
                        sleep(1.5)
                        dice()
                    if answer == '1':
                        game()
                    elif answer not in "1":
                        print("Vous allez quitter le logiciel dans 5 secondes...")
                        sleep(2.7)
                        print("BigProject...")
                        sleep(1.8)
                        rBigProject()

                dice()
            elif answer3 == "5":
                sleep(1)

                def wrdguess():
                    system("@echo off")
                    system("cls")
                    print("DEVINE LE MOT")
                    sleep(1.5)
                    print("Quelle action voulez-vous effectuer ?")
                    print("1. JOUER")
                    print("0. Quitter")
                    answer = input("==>  ")
                    if answer not in '01':
                        print(
                            "Veuillez entrer 1 pour commencer! Pour Quitter, taper 0."
                        )
                        sleep(2)
                        wrdguess()
                    if answer == '1':
                        game()
                    elif answer == '0':
                        print("Vous allez quitter le logiciel dans 5 secondes...")
                        sleep(2.7)
                        print("BigProject...")
                        sleep(1.8)
                        rBigProject()

                def game():
                    sleep(1.2)
                    system("@echo off")
                    system("cls")
                    print("Devine le Mot")
                    sleep(1)
                    file = open(
                        r"C:\Users\yorisamani\Documents\perso\nsi perso\python\BigProject\source_code\sources\word_wordguess.txt",
                        r"r",
                        encoding="utf-8",
                    )
                    file_read = file.readlines()
                    sleep(1)
                    print("Je cherche un mot...")
                    sleep(1.5)
                    print("Essayez de deviner le mot !")
                    print("Combien d'essais ? (Max 10)")
                    attempts = input("==>  ")
                    if attempts not in '012345678910':
                        print("Entrez un chiffre !")
                        sleep(1.5)
                        game()
                    attempts = int(attempts)
                    word = unidecode(random.choice(file_read)
                                     ).lower().replace("\n", "")
                    false_word = []
                    false_letter = []
                    sleep(2)
                    print(
                        f"Le mot contient {len(word)} lettres.\nPremière lettre : {word[0].upper()}\nDernière lettre : {word[len(word)-1].upper()}")
                    tries = 0
                    print("Devinez le mot !")
                    while tries < attempts:
                        sleep(1)
                        word_try = input("==>  ").lower()
                        if word_try == word:
                            tries += 1
                            print("Trouvé! Bien joué!")
                            print(
                                "Vous avez trouvé le mot en {tries} essais !")
                            sleep(1)
                            break
                        elif word_try != word:
                            tries += 1
                            print("Faux !")
                            false_word.append(word_try)
                            print(
                                f"Liste des mauvais mots : {false_word.__repr__()[1:-1].replace(',',' -')}")
                            for letter in word_try:
                                if letter not in word[0:]:
                                    false_letter.append(letter)
                            print(
                                f"Liste des mauvaises lettres : {false_letter.__repr__()[1:-1].replace(',',' -')}")
                    print(f"Le bon mot était donc '{word}'")
                    sleep(2)
                    system("pause")
                    print("Accueil...")
                    sleep(1.2)
                wrdguess()

            elif answer3 != "1" or "2" or "3" or "4" or "5":
                print("Entrez 1, 2, 3, 4 ou 5 pour faire un choix !")
                sleep(1)
                rBigProject()
            # ajt des elif pour les autres jeux
        elif answer1 == "q":
            exit(
                "Au revoir. Reviens quand tu veux utiliser notre application !"
            )
        elif answer1 != "o" or "j" or "q":
            print(
                "Entrez un 'o' ou 'j' pour faire un choix. Sinon entrez 'q' pour Quitter. Attention!"
            )
            sleep(1)
        rBigProject()

    def bigProject():
        intro()
        rBigProject()

    bigProject()

bp()