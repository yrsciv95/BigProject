import datetime
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
            system("color 70")
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
        # ajt d'autres catégories
        sleep(1)
        print(
            "Vous voulez utiliser un de nos nombreux outils ou jouer à un de nos mini-jeux ? 'o' ou 'j'\nPour quitter 'q'"
        )  
        # ajt les lettres pr les catégories
        answer1 = input("==>  ")
        if answer1 == "o":
            print("Voici nos outils:")
            sleep(1)
            print("1. Générateur Ultime")
            print("2. Calculateur d'IMC")
            print("3. Calculateur d'âge grâce à la date de naissance")
            sleep(1)
            print("4. Calculateur de salaire")
            print("5. Analyseur de Texte")
            print("6. Convertisseur de Température")
            # Ajt les autres outils
            sleep(1)
            print("Lequel voulez-vous utilisez ?")
            answer2 = input("Entrez son chiffre  ==>  ")
            if answer2 == "1":
                sleep(1)

                def pwdGeneratorLetters():
                    letters_uppercase = string.ascii_uppercase
                    letters_lowercase = string.ascii_lowercase
                    symbols = string.punctuation
                    numbers = string.digits
                    pwd_sample = (letters_uppercase + letters_lowercase +
                                  numbers + symbols)
                    print("Bip... Bip... Nouveau Mot De Passe...")
                    answer2 = int(
                        input(
                            "Avec combien de caractères ? Pour la sécu, 8 c'est bien!  ==>  "
                        ))
                    length = answer2
                    pwd = "".join(random.sample(pwd_sample, length))

                    print(
                        "Tiens, ton nouveau mot de passe ultra-securisé  ==>  ",
                        pwd)
                    quit = input("Tu t'en vas ?  ==>  ")
                    if quit == "Oui":
                        print("Salut. A Bientôt !")
                        sleep(1)
                        exit()
                    elif quit == "Non":
                        print("Cool !")
                        pwdGeneratorLetters()
                    else:
                        quit2 = input("Répondez avec 'Oui' ou 'Non'  ==>  ")
                        if quit2 == "Oui":
                            print("Salut. A Bientôt !")
                            sleep(1)
                            exit()
                        elif quit == "Non":
                            print("Cool !")
                            pwdGeneratorLetters()

                def pwdGeneratorNum():
                    numbers = string.digits
                    pwd_sample = numbers
                    print("Bip... Bip... Nouveau Mot De Passe...")
                    answer2 = int(
                        input("Avec combien de caractères ? 4 ou 6  ==>  "))
                    if answer2 == 4:
                        length = 4
                    elif answer2 == 6:
                        length = 6
                    elif answer2 != "4" or "6":
                        print("Entrez 4 ou 6!!")
                        pwdGeneratorNum()
                    pwd = "".join(random.sample(pwd_sample, length))
                    print(
                        "Tiens, ton nouveau mot de passe de téléphone ultra-securisé  ==>  ",
                        pwd,
                    )
                    quit = input("Tu t'en vas ?  ==>  ")
                    if quit == "Oui":
                        print("Salut. A Bientôt !")
                        sleep(1)
                        exit()
                    elif quit == "Non":
                        print("Cool !")
                        pwdGeneratorNum()
                    else:
                        quit2 = input("Répondez avec 'Oui' ou 'Non'  ==>  ")
                        if quit2 == "Oui":
                            print("Salut. A Bientôt !")
                            sleep(1)
                            exit()
                        elif quit == "Non":
                            print("Cool !")
                            pwdGeneratorNum()

                def pwdGenerator():
                    print("Générateur de Mots de Passe")
                    print(
                        "1. Génerer un Mot de Passe avec des Chiffres, des Lettres, et des Symboles"
                    )
                    print(
                        "2. Génerer un Mot de passe pour téléphone avec des Chiffres seulement"
                    )
                    print("3. Quitter")
                    answer = int(
                        input("Tapez 1 ou 2 pour choisir une option  ==>  "))
                    if answer == 1:
                        print("Ok, un Mot De Passe ultra-securisé ! Super !")
                        pwdGeneratorLetters()
                    elif answer == 2:
                        print(
                            "Ca part pour un Mot De Passe de téléphone! Super !"
                        )
                        pwdGeneratorNum()
                    elif answer == 3:
                        print(
                            "Dommage, Reviens quand tu voudras securiser tes Mots De Passe!"
                        )
                        sleep(1)
                        exit()

                def nbGenerator():
                    print("Générateur de Nombres")
                    print("Combien de nombres voulez-vous génerer ?")
                    nb = int(input("==>  "))
                    print("Entre combien à combien ? (1 par ligne)")
                    range1 = int(input("==>  "))
                    range2 = int(input("==>  "))
                    generated_nb = random.choices(range(range1, range2), k=nb)
                    print(f"\nNombres génerés")
                    for nb in generated_nb:
                        print(nb, end="   ")
                    answer_replay = input(
                        "\n\nVoulez vous recommencer ? Si oui, entrez 'o'  ==>  "
                    )
                    if answer_replay == "o":
                        print("Super!!")
                        nbGenerator()
                    else:
                        print("Revenez quand vous voulez !!")
                        sleep(1)
                        exit()

                def letterGenerator():
                    print("Générateur de Lettres")
                    print("Combien de lettres voulez-vous génerer ?")
                    letters = string.ascii_uppercase
                    ltr = int(input("==>  "))
                    generated_ltr = random.choices(letters, k=ltr)
                    print(f"\nLettres génerées")
                    for ltr in generated_ltr:
                        print(ltr, end="   ")
                    answer_replay = input(
                        "\n\nVoulez vous recommencer ? Si oui, entrez 'o'  ==>  "
                    )
                    if answer_replay == "o":
                        print("Super!!")
                        letterGenerator()
                    else:
                        print("Revenez quand vous voulez !!")
                        sleep(1)
                        exit()

                def ultimateGenerator():
                    print("GENERATEUR ULTIME")
                    print("1. Génerateur de Mots de Passe")
                    print("2. Génerateur de Nombres aléatoire")
                    print("3. Génerateur de Lettres aléatoire")
                    answer = input(
                        "Entrez un nombre pour faire un choix (Pour quitter 'q')  ==>  "
                    )
                    if answer == "1":
                        sleep(1)
                        pwdGenerator()
                    elif answer == "2":
                        sleep(1)
                        nbGenerator()
                    elif answer == "3":
                        sleep(1)
                        letterGenerator()
                    elif answer == "q":
                        print(
                            "Dommage, Reviens quand tu voudras securiser tes Mots De Passe!"
                        )
                        sleep(2)
                        exit()
                    elif answer != "q" or "1" or "2" or "3":
                        print(
                            "Entrez 1, 2 ou 3 pour faire un choix (Pour quitter 'q')"
                        )
                        sleep(1.5)
                        ultimateGenerator()

                ultimateGenerator()
            elif answer2 == "2":
                sleep(1)

                def rCalcImc():
                    height = float(
                        input(
                            "Entrez votre poids (en kg avec un '.' si décimal)  ==>  "
                        ))
                    weight = float(
                        input(
                            "Entrez votre taille (en m avec un '.' si décimal)  ==>  "
                        ))
                    print("Votre taille : ", weight, " m")
                    print("Votre poids : ", height, " kg")
                    imc = height / (weight * weight)
                    print(f"Vous avez une IMC de {round(imc)} kg/m²")
                    if imc < 18.5:
                        print("Vous êtes en Insuffisance pondérale (maigreur)")
                    elif 18.5 <= imc < 25:
                        print("Vous avez une corpulence normale !")
                    elif 25 <= imc < 30:
                        print("Vous êtes en surpoids")
                    elif 30 <= imc < 35:
                        print("Vous êtes en obésité modérée")
                    elif 35 <= imc < 40:
                        print("Vous êtes en obésité sévère")
                    elif imc > 40:
                        print("Vous êtes en obésité massive")

                def replay():
                    answer_replay = input(
                        "Voulez vous recommencer ? Si oui, entrez 'o'  ==>  ")
                    if answer_replay == "o":
                        print("Super!!")
                        rCalcImc()
                    else:
                        print("Revenez quand vous voulez !!")
                        sleep(1)
                        exit()

                def ask():
                    print("CALCULATEUR D'IMC")
                    answer = input(
                        "Si vous souhaitez commencer tapez 1 sinon tapez 'q' pour Quitter  ==>  "
                    )
                    if answer == "1":
                        print("GENIAL !!")
                    elif answer == "q":
                        print("Dommage, Au revoir !!")
                        sleep(1)
                        exit()
                    elif answer != "1":
                        print(
                            "Si vous souhaitez commencer tapez 1 sinon tapez 'q' pour Quitter. Attention !"
                        )
                        ask()

                def calcImc():
                    ask()
                    rCalcImc()
                    replay()

                calcImc()
            elif answer2 == "3":
                sleep(1)

                def rCalcAge(y, m, d):
                    current_date = datetime.datetime.now().date()
                    date_of_birth = datetime.date(y, m, d)
                    age = int((current_date - date_of_birth).days / 365.25)
                    print(f"Vous avez {age} ans")
                    replay()

                def ask():
                    print("CALCULATEUR D'AGE")
                    answer = input(
                        "Si vous souhaitez commencer tapez 1 sinon tapez 'q' pour Quitter  ==>  "
                    )
                    if answer == "1":
                        print("GENIAL !!")
                    elif answer == "q":
                        print("Dommage, Au revoir !!")
                        sleep(1)
                        exit()
                    elif answer != "1":
                        print(
                            "Si vous souhaitez commencer tapez 1 sinon tapez 'q' pour Quitter. Attention !"
                        )
                        ask()

                def replay():
                    answer_replay = input(
                        "Voulez vous recommencer ? Si oui, entrez 'o'  ==>  ")
                    if answer_replay == "o":
                        print("Super!!")
                        rCalcAge(
                            int(input("Année de naissance  ==>  ")),
                            int(input("Mois de naissance  ==>  ")),
                            int(input("Jour de naissance  ==>  ")),
                        )
                    else:
                        print("Revenez quand vous voulez !!")
                        sleep(1)
                        exit()

                def calcAge():
                    ask()
                    rCalcAge(
                        int(input("Année de naissance  ==>  ")),
                        int(input("Mois de naissance  ==>  ")),
                        int(input("Jour de naissance  ==>  ")),
                    )
                    replay()

                calcAge()
            elif answer2 == "4":
                sleep(1)

                def rSalary():
                    sleep(0.4)
                    print("TYPES DE PAYES")
                    sleep(0.2)
                    print("1. Non - Cadre")
                    print("2. Cadre")
                    print("3. Profession Libérale")
                    print("4. Fonction Publique")
                    sleep(0.6)
                    answer = int(input("Entrez son numéro  ==>  "))
                    if answer == 1:
                        print("Initialisation ...")
                        sleep(0.9)
                        rSalaryNC()
                    elif answer == 2:
                        print("Initialisation ...")
                        sleep(0.9)
                        rSalaryC()
                    elif answer == 3:
                        print("Initialisation ...")
                        sleep(0.9)
                        rSalaryL()
                    elif answer == 4:
                        print("Initialisation ...")
                        sleep(0.9)
                        rSalaryFP()
                    elif answer != 1 or 2 or 3 or 4:
                        print("Entrez 1, 2, 3 ou 4 pour faire un choix !")
                        sleep(0.7)
                        rSalary()
                    replay()

                def rSalaryC():
                    print("Calculer son salaire après taxes (Cadre)")
                    salary = float(
                        input("Entrez un salaire brut mensuel  ==>  "))
                    currency = ["$", "£", "€"]
                    user_currency = input(
                        "Entrez la devise de votre salaire  ==>  ")
                    if user_currency not in currency:
                        print("Entrez une devise valide ($, £, €)")
                        sleep(1)
                        rSalaryC()
                    net = (salary * 25) / 100
                    net_salary_month = salary - net
                    net_salary_year = net_salary_month * 12
                    print("Calcul ...")
                    sleep(1.5)
                    print(
                        "Voici votre salaire net mensuel:",
                        round(net_salary_month),
                        user_currency,
                    )
                    print(
                        "Ainsi que votre salaire net annuel:",
                        round(net_salary_year),
                        user_currency,
                    )

                def rSalaryFP():
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
                        rSalaryFP()
                    net = (salary * 15) / 100
                    net_salary_month = salary - net
                    net_salary_year = net_salary_month * 12
                    print("Calcul ...")
                    sleep(1.5)
                    print(
                        "Voici votre salaire net mensuel:",
                        round(net_salary_month),
                        user_currency,
                    )
                    print(
                        "Ainsi que votre salaire net annuel:",
                        round(net_salary_year),
                        user_currency,
                    )

                def rSalaryL():
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
                        rSalaryNC()
                    net = (salary * 45) / 100
                    net_salary_month = salary - net
                    net_salary_year = net_salary_month * 12
                    print("Calcul ...")
                    sleep(1.5)
                    print(
                        "Voici votre salaire net mensuel:",
                        round(net_salary_month),
                        user_currency,
                    )
                    print(
                        "Ainsi que votre salaire net annuel:",
                        round(net_salary_year),
                        user_currency,
                    )

                def rSalaryNC():
                    print("Calculer son salaire après taxes (Non - Cadre)")
                    salary = float(
                        input("Entrez un salaire brut mensuel  ==>  "))
                    currency = ["$", "£", "€"]
                    user_currency = input(
                        "Entrez la devise de votre salaire  ==>  ")
                    if user_currency not in currency:
                        print("Entrez une devise valide ($, £, €)")
                        sleep(1)
                        rSalaryNC()
                    net = (salary * 22) / 100
                    net_salary_month = salary - net
                    net_salary_year = net_salary_month * 12
                    print("Calcul ...")
                    sleep(1.5)
                    print(
                        "Voici votre salaire net mensuel:",
                        round(net_salary_month),
                        user_currency,
                    )
                    print(
                        "Ainsi que votre salaire net annuel:",
                        round(net_salary_year),
                        user_currency,
                    )

                def ask():
                    print("CALCULATEUR DE SALAIRE")
                    answer = input(
                        "Si vous souhaitez commencer tapez 1 sinon tapez 'q' pour Quitter  ==>  "
                    )
                    if answer == "1":
                        print("GENIAL !!")
                    elif answer == "q":
                        print("Dommage, Au revoir !!")
                        sleep(1)
                        exit()
                    elif answer != "1" or "q":
                        print(
                            "Si vous souhaitez commencer tapez 1 sinon tapez 'q' pour Quitter. Attention !"
                        )
                        ask()

                def replay():
                    answer_replay = input(
                        "Voulez vous recommencer ? Si oui, entrez 'o'  ==>  ")
                    if answer_replay == "o":
                        print("Super!!")
                        rSalary()
                    else:
                        print("Revenez quand vous voulez !!")
                        sleep(1)
                        exit()

                def salary():
                    ask()
                    rSalary()
                    replay()

                salary()
            elif answer2 == "5":

                def choice():
                    system("@echo off")
                    system("cls")
                    print("LOGICIEL D'AIDE AU FRANCAIS")
                    sleep(1.5)
                    print("Quelle action voulez-vous effectuer ?")
                    print("1. Analyseur de Texte")
                    print("2. Compteur de Mots ou Lettres")
                    print("0. Quitter")
                    answer = int(input("==>  "))
                    if answer == 1:
                        analyse_text()
                    elif answer == 2:
                        counter()
                    elif answer == 0:
                        print(
                            "Vous allez quitter le logiciel dans 5 secondes..."
                        )
                        sleep(2.7)
                        print("Vous quittez le logiciel...")
                        sleep(1.8)
                        system("cls")
                        sleep(1)
                        exit("Exit...")
                    elif answer != 1 or 2 or 0:
                        print(
                            "Veuillez entrer 1 ou 2 pour faire un choix! Pour Quitter, taper 0."
                        )
                        sleep(2)
                        choice()

                def counter():
                    system("@echo off")
                    system("cls")
                    print("LOGICIEL COMPTEUR De Mots et De Lettres")
                    sleep(1.5)
                    print(
                        "Ce logiciel peut compter les lettres et les voyelles ou consonnes dans un mot.\nIl peut aussi compter le nombre de mots dans une phrase."
                    )
                    print("Quelle action voulez-vous effectuer ?")
                    print("1. Compter le nombre de mots dans une phrase")
                    print(
                        "2. Compter le nombre de lettres dans un mot ou dans une phrase"
                    )
                    print(
                        "3. Compter le nombre de voyelles ou de consonnes dans mot ou une phrase"
                    )
                    print("0. Quitter")
                    answer = int(input("==>  "))
                    if answer == 1:
                        wordNbCounter()
                    elif answer == 2:
                        lettersNbCounter()
                    elif answer == 3:
                        lettersTypeNbCounters()
                    elif answer == 0:
                        print(
                            "Vous allez quitter le logiciel dans 5 secondes..."
                        )
                        sleep(2.7)
                        print("Vous quittez le logiciel...")
                        sleep(1.8)
                        system("cls")
                        sleep(1)
                        exit("Exit...")
                    elif answer != 1 or 2 or 3 or 0:
                        print(
                            "Veuillez entrer 1, 2 ou 3 pour faire un choix! Pour Quitter, taper 0."
                        )
                        sleep(2)
                        counter()

                def wordNbCounter():
                    sleep(1.2)
                    system("@echo off")
                    system("cls")
                    print("Compteur de nombre de mots dans une phrase".upper())
                    sleep(1)
                    print("Entrez une phrase")
                    answer = input("==>  ")
                    word = 0
                    for space in answer:
                        if space == " ":
                            word += 1
                    word = word + 1
                    print("Il y a", word, "mots dans cette phrase.")
                    sleep(4)
                    print("Accueil...")
                    sleep(1.2)
                    counter()

                def lettersNbCounter():
                    sleep(1.2)
                    system("@echo off")
                    system("cls")
                    print(
                        "Compteur de nombre de lettres dans un mot ou dans une phrase"
                        .upper())
                    sleep(1)
                    print("Entrez un mot ou une phrase")
                    answer = input("==>  ")
                    answer_min = answer.lower()
                    letter_count = 0
                    alphabet = [
                        "a",
                        "b",
                        "c",
                        "d",
                        "e",
                        "f",
                        "g",
                        "h",
                        "i",
                        "j",
                        "k",
                        "l",
                        "m",
                        "n",
                        "o",
                        "p",
                        "q",
                        "r",
                        "s",
                        "t",
                        "u",
                        "v",
                        "w",
                        "x",
                        "y",
                        "z",
                    ]
                    for letter in answer_min:
                        if letter in alphabet:
                            letter_count += 1
                    print(f"Votre phrase/mot compte {letter_count} lettre(s)")
                    sleep(4)
                    print("Accueil...")
                    sleep(1.2)
                    counter()

                def lettersTypeNbCounters():
                    sleep(1.2)
                    system("@echo off")
                    system("cls")
                    print(
                        "Compteur de nombre de voyelles ou de consonnes dans mot ou une phrase"
                        .upper())
                    sleep(1)
                    print("Entrez un mot ou une phrase")
                    vowels = ["a", "e", "i", "o", "u", "y"]
                    consonnes = [
                        "b",
                        "c",
                        "d",
                        "f",
                        "g",
                        "h",
                        "j",
                        "k",
                        "l",
                        "m",
                        "n",
                        "p",
                        "q",
                        "r",
                        "s",
                        "t",
                        "v",
                        "w",
                        "x",
                        "z",
                    ]
                    answer = input("==>  ")
                    answer_min = answer.lower()
                    vowels_count = 0
                    consonnes_count = 0
                    for letter in answer_min:
                        if letter in vowels:
                            vowels_count += 1
                        elif letter in consonnes:
                            consonnes_count += 1
                    print(
                        f"Votre phrase/mot compte {vowels_count} voyelle(s) et {consonnes_count} consonne(s)."
                    )
                    sleep(4)
                    print("Accueil...")
                    sleep(1.2)
                    counter()

                def analyse_text():
                    system("@echo off")
                    system("cls")
                    print("LOGICIEL Analyseur de Fichier Texte")
                    sleep(1.5)
                    print(
                        "Ce logiciel analysant un fichier texte peut compter les lettres et les voyelles ou consonnes dans le texte.\nIl peut aussi compter le nombre de mots et de phrases."
                    )
                    print(
                        "Attention! Pour l'instant, il ne reconnait pas les caractères spéciaux!!"
                    )
                    print(
                        "\nIl est recommandé de placer ce logiciel dans le dossier du texte à analyser\n"
                    )
                    sleep(1)
                    print("Quelle action voulez-vous effectuer ?")
                    print("1. Analyser un fichier texte")
                    print("0. Quitter")
                    answer = int(input(r"==>  "))
                    if answer == 1:
                        analyse()
                    elif answer == 0:
                        print(
                            "Vous allez quitter le logiciel dans 5 secondes..."
                        )
                        sleep(2.7)
                        print("Vous quittez le logiciel...")
                        sleep(1.8)
                        system("cls")
                        sleep(1)
                        exit("Exit...")
                    elif answer != 1 or 0:
                        print(
                            "Veuillez entrer 1 pour commencer ! Pour Quitter, taper 0."
                        )
                        sleep(2)
                        analyse_text()

                def analyse():
                    sleep(1.2)
                    system("@echo off")
                    system("cls")
                    print("-- ANALYSE --")
                    sleep(1)
                    print(
                        "Entrez le chemin d'accès vers le texte (ou uploader le fichier)"
                    )
                    text_file_input = input("==>  ")
                    test_exist_file = os.path.exists(text_file_input)
                    test_file_text = os.path.splitext(text_file_input)
                    kind = [".txt"]
                    if test_exist_file == True:
                        if test_file_text[1] in kind:
                            print("Analyse en cours...")
                            sleep(4)
                            file = open(text_file_input, r"r")
                            read_file = unidecode(file.read())
                            text_min = read_file.lower()
                            words = 0
                            word_cut = text_min.split()
                            for word in word_cut:
                                words += 1
                            letter_count = 0
                            vowels_count = 0
                            consonnes_count = 0
                            alphabet = [
                                "a",
                                "à",
                                "â",
                                "b",
                                "c",
                                "ç",
                                "d",
                                "e",
                                "é",
                                "ê",
                                "è",
                                "f",
                                "g",
                                "h",
                                "i",
                                "ï",
                                "î",
                                "j",
                                "k",
                                "l",
                                "m",
                                "n",
                                "o",
                                "ô",
                                "p",
                                "q",
                                "r",
                                "s",
                                "t",
                                "u",
                                "û",
                                "ü",
                                "v",
                                "w",
                                "x",
                                "y",
                                "ÿ",
                                "z",
                            ]
                            vowels = [
                                "a",
                                "à",
                                "â",
                                "e",
                                "é",
                                "ê",
                                "è",
                                "i",
                                "ï",
                                "î",
                                "o",
                                "ô",
                                "u",
                                "û",
                                "ü",
                                "ÿ",
                                "y",
                            ]
                            consonnes = [
                                "b",
                                "c",
                                "ç",
                                "d",
                                "f",
                                "g",
                                "h",
                                "j",
                                "k",
                                "l",
                                "m",
                                "n",
                                "p",
                                "q",
                                "r",
                                "s",
                                "t",
                                "v",
                                "w",
                                "x",
                                "z",
                            ]
                            for letter in text_min:
                                if letter in alphabet:
                                    letter_count += 1
                                if letter in vowels:
                                    vowels_count += 1
                                elif letter in consonnes:
                                    consonnes_count += 1
                            print("Analyse terminée !")
                            print("Préparation du rapport...")
                            sleep(2)
                            sleep(1)
                            print(
                                f"Votre fichier texte contient : {words} mots, {letter_count} lettres.\nIl contient aussi {vowels_count} voyelles et {consonnes_count} consonnes"
                            )
                        else:
                            print("Ce n'est pas un fichier texte!")
                            sleep(2)
                            analyse_text()
                    else:
                        print(
                            "Le fichier n'existe pas ! Vérifier le chemin d'accès !"
                        )
                        sleep(2)
                        analyse_text()
                    system("pause")
                    print("Accueil...")
                    sleep(1.2)
                    analyse_text()

                analyse_text()
            elif answer2 == "6":
                sleep(1)

                def tempeconv():
                    system("@echo off")
                    system("cls")
                    print("LOGICIEL Convertisseur de Température")
                    sleep(1.5)
                    print(
                        "Ce logiciel peut convertir les températures en °C vers °F, °R, K"
                    )
                    print("Quelle action voulez-vous effectuer ?")
                    print("1. Celsius --> Fahrenheit")
                    print("2. Celsius --> Kelvin")
                    print("3. Celsius --> Rankine")
                    print("0. Quitter")
                    answer = int(input("==>  "))
                    if answer == 1:
                        fconv()
                    elif answer == 2:
                        kconv()
                    elif answer == 3:
                        rconv()
                    elif answer == 0:
                        print(
                            "Vous allez quitter le logiciel dans 5 secondes..."
                        )
                        sleep(2.7)
                        print("Vous quittez le logiciel...")
                        sleep(1.8)
                        system("cls")
                        sleep(1)
                        exit("Exit...")
                    elif answer != 1 or 2 or 3 or 0:
                        print(
                            "Veuillez entrer 1, 2 ou 3 pour faire un choix! Pour Quitter, taper 0."
                        )
                        sleep(2)
                        tempeconv()

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
            elif answer2 != "1" or "2" or "3" or "4" or "5" or "6":
                print("Entrez 1, 2, 3, 4, 5 ou 6 pour faire un choix !")
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

                def replay():
                    answer_replay = input(
                        "Voulez vous rejouer ? Si oui, entrez 'o'  ==>  ")
                    if answer_replay == "o":
                        print("Super!!")
                        rChifoumi()
                    else:
                        print("Revenez quand vous voulez !!")
                        sleep(1)
                        exit()

                def ask():
                    print("LE JEU DU CHIFOUMI")
                    answer = input(
                        "Si vous souhaitez jouer tapez 1 sinon tapez 'q' pour Quitter  ==>  "
                    )
                    if answer == 1:
                        print("SUPER !!")
                    elif answer == "q":
                        print("Dommage, Au revoir !!")
                        sleep(1)
                        exit()

                def rChifoumi():
                    choice_list = ["Pierre", "Feuille", "Ciseaux"]
                    computer = choice_list[random.randint(0, 2)]
                    player = False
                    p_score = 0
                    c_score = 0
                    turn = 0
                    while player == False:
                        player = input(
                            "Pierre, Feuille ou Ciseaux (ou 'q' pour quitter)  ==>  "
                        )
                        if player == "q":
                            print("Salut! A bientôt !")
                            sleep(1)
                            exit()
                        elif player == computer:
                            print("Votre adversaire choisit aussi", computer,
                                  "!")
                            print(
                                "Il y a donc égalité ! Personne ne gagne de points"
                            )
                            turn += 1
                        elif player == "Pierre":
                            if computer == "Feuille":
                                print("Perdu !", computer, "recouvre", player)
                                turn += 1
                                c_score += 1
                            else:
                                print("Gagné !", player, "écrase", computer)
                                turn += 1
                                p_score += 1
                        elif player == "Feuille":
                            if computer == "Ciseaux":
                                print("Perdu !", computer, "coupe", player)
                                turn += 1
                                c_score += 1
                            else:
                                print("Gagné !", player, "recouvre", computer)
                                turn += 1
                                p_score += 1
                        elif player == "Ciseaux":
                            if computer == "Pierre":
                                print("Perdu !", computer, "écrase", player)
                                turn += 1
                                c_score += 1
                            else:
                                print("Gagné !", player, "coupe", computer)
                                turn += 1
                        else:
                            print(
                                "Entrez 'Pierre', 'Feuille', ou 'Ciseaux' pour faire un choix svp"
                            )
                        player = False
                        computer = choice_list[random.randint(0, 2)]
                        if turn == 5:
                            player = True
                            print("Fin de la partie !!")
                            if p_score > c_score:
                                print("Vous avez gagné !")
                                sleep(1)
                                exit()
                            elif c_score > p_score:
                                print("C'est perdu !! Dommage !")
                                sleep(1)
                                exit()

                def chifoumi():
                    ask()
                    rChifoumi()
                    replay()

                chifoumi()
            elif answer3 == "2":
                sleep(1)

                def nbGuessUser():
                    just_price = random.randint(1, 100)
                    running = True
                    nb_essais = int(input("Combien d'essais desirez-vous ?"))
                    essais = 0
                    while running:
                        remaining_trials = nb_essais - essais - 1
                        user_price = int(
                            input("Deviner le prix (entre 1 et 100) ==>  "))
                        if user_price == just_price:
                            print(
                                "Bien joué, vous avez le juste prix en ",
                                essais,
                                "essais",
                            )
                            running = False
                        elif user_price > just_price:
                            print("C'est moins !!")
                            essais += 1
                            print("Il vous reste ", remaining_trials,
                                  " essais !")
                        elif user_price < just_price:
                            print("Plus haut !!")
                            essais += 1
                            print("Il vous reste ", remaining_trials,
                                  " essais !")
                        if essais == nb_essais:
                            print("Dommage !!")
                            print("Le chiffre c'était", just_price)
                            replay()
                            essais = 0
                    print("Fin du jeu !")
                    replay()

                def ask():
                    print("LE JUSTE PRIX")
                    answer = int(
                        input("Si vous souhaitez jouer tapez 1  ==>  "))
                    if answer == 1:
                        print("SUPER !!")
                        nbGuessUser()
                    elif answer not in "1":
                        print("Dommage, Au revoir !!")
                        sleep(1)
                        exit()

                def replay():
                    answer_replay = input(
                        "Voulez vous rejouer ? Si oui, entrez 'o'  ==>  ")
                    if answer_replay == "o":
                        print("Super!!")
                    else:
                        print("Revenez quand vous voulez !!")
                        sleep(1)
                        exit()

                def nbGuess():
                    ask()
                    nbGuessUser()

                nbGuess()
            elif answer3 == "3":
                sleep(1)

                def rRouletteRu():
                    start = input("Tenter votre chance ? ('o' ou 'n') ==>  ")
                    if start == "o":
                        choice = ["1", "2", "3", "4", "5", "6"]
                        trigger = random.choice(choice)
                        if trigger == "1":
                            print("Ahaha! Perdu!")
                            replay()
                        elif trigger == "2" or "3" or "4" or "5" or "6":
                            print("Vous avez gagné. Bien joué !")
                            rRouletteRu()
                    elif start == "n":
                        print("Tu n'as pas le goût du risque. Va-t'en !")
                        sleep(1)
                        exit()
                    elif start != "o" or "n":
                        print("Entrez 'o' ou 'n' pour commencez !")
                        rRouletteRu()

                def ask():
                    print("ROULETTE RUSSE")
                    answer = input(
                        "Si vous souhaitez commencer tapez 1 sinon tapez 'q' pour Quitter  ==>  "
                    )
                    if answer == "1":
                        print("GENIAL !!")
                    elif answer == "q":
                        print("Dommage, Au revoir !!")
                        sleep(1)
                        exit()
                    elif answer != "1":
                        print(
                            "Si vous souhaitez commencer tapez 1 sinon tapez 'q' pour Quitter. Attention !"
                        )
                        ask()

                def replay():
                    answer_replay = input(
                        "Voulez vous recommencer ? Si oui, entrez 'o'  ==>  ")
                    if answer_replay == "o":
                        print("Super!!")
                        rouletteRu()
                    else:
                        print("Revenez quand vous voulez !!")
                        sleep(1)
                        exit()

                def rouletteRu():
                    ask()
                    rRouletteRu()
                    replay()

                rouletteRu()
            elif answer3 == "4":
                sleep(1)

                def rDice():
                    start = input("Lancer les dés ? ('o' ou 'n') ==>  ")
                    player = False
                    p_score = 0
                    c_score = 0
                    turn = 0
                    while player == False:
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
                            print("Dommage tu m'avais l'air assez fort !")
                            sleep(1)
                            exit()
                        elif start != "o" or "n":
                            print("Entrez 'o' ou 'n' pour commencez !")
                            rDice()
                        if turn == 5:
                            player = True
                            print("\nFin de la partie !!")
                            if p_score > c_score:
                                print("Vous avez gagné !")
                                print("Il y a", p_score, "à", c_score,
                                      "pour vous !")
                            elif c_score > p_score:
                                print("C'est perdu !! Dommage !")
                                print("Il y a", c_score, "à", p_score,
                                      "pour lui !")

                def ask():
                    print("JEU DE DÉS")
                    answer = input(
                        "Si vous souhaitez commencer tapez 1 sinon tapez 'q' pour Quitter  ==>  "
                    )
                    if answer == "1":
                        print("GENIAL !!")
                    elif answer == "q":
                        print("Dommage, Au revoir !!")
                        sleep(1)
                        exit()
                    elif answer != "1":
                        print(
                            "Si vous souhaitez commencer tapez 1 sinon tapez 'q' pour Quitter. Attention !"
                        )
                        ask()

                def replay():
                    answer_replay = input(
                        "Voulez vous recommencer ? Si oui, entrez 'o'  ==>  ")
                    if answer_replay == "o":
                        print("Super!!")
                        rDice()
                    else:
                        print("Revenez quand vous voulez !!")
                        sleep(1)
                        exit()

                def dice():
                    ask()
                    rDice()
                    replay()

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
                    answer = int(input("==>  "))
                    if answer == 1:
                        game()
                    elif answer == 0:
                        print(
                            "Vous allez quitter le logiciel dans 5 secondes..."
                        )
                        sleep(2.7)
                        print("Vous quittez le logiciel...")
                        sleep(1.8)
                        system("cls")
                        sleep(1)
                        exit("Exit...")
                    elif answer != 1 or 0:
                        print(
                            "Veuillez entrer 1 pour commencer! Pour Quitter, taper 0."
                        )
                        sleep(2)
                        wrdguess()

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
                    word = unidecode(choice(file_read)).lower().replace(
                        "\n", "")
                    false_word = []
                    sleep(2)
                    print(
                        f"Le mot contient {len(word)} lettres.\nPremière lettre : {word[0].upper()}\nDernière lettre : {word[len(word)-1].upper()}"
                    )
                    print("Combien d'essais ?")
                    tries = 0
                    attempts = int(input("==>  "))
                    print("Devinez le mot !")
                    while tries <= attempts:
                        sleep(1)
                        word_try = input("==>  ").lower()
                        if len(word_try) > len(word):
                            print("Incorrect! Le mot est plus petit!")
                            tries += 1
                        elif len(word_try) < len(word):
                            print("Incorrect! Le mot est plus grand!")
                            tries += 1
                        if word_try == word:
                            tries += 1
                            print("Trouvé! Bien joué!")
                            sleep(1)
                            break
                        elif word_try != word:
                            tries += 1
                            print("Faux !")
                            false_word.append(word_try)
                            print(
                                f"Liste des mauvais mots : {false_word.__repr__()[1:-1].replace(',',' -')}"
                            )
                            for letter in word_try:
                                if letter not in word[0:]:
                                    print(
                                        f"La lettre '{letter.upper()}' n'est pas dans le mot à trouver!"
                                    )
                    sleep(3)
                    system("pause")
                    print("Accueil...")
                    sleep(1.2)
                    wrdguess()

            elif answer3 != "1" or "2" or "3" or "4" or "5":
                print("Entrez 1, 2, 3, 4 ou 5 pour faire un choix !")
                sleep(1)
                rBigProject()
            # ajt des elif pour les autres jeux
        # ajt des elif pour les autres catégories
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