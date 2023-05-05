import os.path
import random
import string
from os import system
from time import sleep
from unidecode import unidecode
from better_profanity import profanity


def bp():

    def intro():
        sleep(0.5)
        system("cls")
        sleep(0.5)
        system("echo.")
        system("echo BigProject")
        system("echo.")
        print("Salut !")
        print("Quel est ton identifiant ?")
        id = input("==>  ")
        if id == '':
            sleep(2)
            print(f"Bienvenue !")
        else:
            censor = profanity.censor(id)
            sleep(2)
            print(f"Bienvenue {censor} !")
        sleep(1)
        print("Choix du Thème")
        print("1. Sombre")
        print("2. Claire")
        answer = input("==>  ")
        if answer not in '12':
            sleep(1)
            print("Suite...")
            sleep(1.5)
        if answer == "2":
            sleep(1)
            system("@echo off")
            system("color F0")
            system("cls")
        elif answer == "1":
            system("@echo off")
            system("color 07")
            system("cls")
        elif answer == '':
            system('@echo off')
            system('cls')
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
            "Vous voulez utiliser un de nos nombreux outils ou jouer à un de nos mini-jeux ? 'o' ou 'j'\nPour quitter, taper 0"
        )
        answer1 = input("==>  ")
        if answer1 == "o":
            print("Voici nos outils:")
            sleep(1)
            print("1. Générateur Ultime")
            print("2. Analyseur de Texte")
            # Ajt les autres outils
            print("0. Quitter")
            sleep(1)
            print("Lequel voulez-vous utilisez ?")
            answer2 = input("Entrez son chiffre  ==>  ")
            if answer2 not in '012':
                print("Entrez 1 ou 2 pour faire un choix! Pour Quitter, taper 0.")
                sleep(2)
                rBigProject()
            if answer2 == '0':
                sleep(1)
                print("Accueil...")
                sleep(1.5)
                rBigProject()
            elif answer2 == "1":
                sleep(1)

                def ultimateGenerator():
                    system('@echo off')
                    system('cls')
                    print("GENERATEUR ULTIME")
                    sleep(1)
                    print("Quelle action voulez-vous effectuer ?")
                    print("1. Générateur de Mots de Passe")
                    print("2. Générateur Aléatoire")
                    print("0. Quitter")
                    answer = input("==>  ")
                    if answer not in '012':
                        print(
                            "Entrez 1 ou 2 pour faire un choix. Pour Quitter, taper 0")
                        sleep(1.5)
                        ultimateGenerator()
                    if answer == "1":
                        pwdGenerator()
                    elif answer == "2":
                        randomGenerator()
                    elif answer == "0":
                        print("Vous allez quitter le logiciel dans 5 secondes...")
                        sleep(2.7)
                        print("BigProject...")
                        sleep(1.8)
                        rBigProject()

                def pwdGenerator():
                    system('@echo off')
                    system('cls')
                    print("Générateur de Mots de Passe")
                    sleep(1)
                    print("Quelle action voulez-vous effectuer ?")
                    print(
                        "1. Génerer un Mot de Passe avec des Chiffres, des Lettres, et des Symboles")
                    print(
                        "2. Génerer un Mot de passe pour téléphone avec des Chiffres seulement")
                    print("0. Quitter")
                    sleep(1)
                    print("Tapez 1 ou 2 pour choisir une option")
                    answer = input("==>  ")
                    if answer not in '120':
                        print(
                            "Entrez 1 ou 2 pour faire un choix. Pour Quitter, taper 0")
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

                def pwdGeneratorLetters():
                    sleep(1)
                    letters_uppercase = string.ascii_uppercase
                    letters_lowercase = string.ascii_lowercase
                    symbols = "!#$%&()*+-/<=>?@\_"
                    numbers = string.digits
                    pwd_sample = (letters_uppercase +
                                  letters_lowercase + numbers + symbols)
                    print("Bip... Bip... Nouveau Mot De Passe...")
                    sleep(1.5)
                    print("Avec combien de caractères ? Pour la sécu, 8 c'est bien!")
                    answer2 = input('==>  ')
                    answer2_ = answer2.isdigit()
                    if answer2_ == False:
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
                    sleep(1.5)
                    answer2 = input("Avec combien de caractères ?  ==>  ")
                    answer2_ = answer2.isdigit()
                    if answer2_ == False:
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

                def randomGenerator():
                    system('@echo off')
                    system('cls')
                    print("Générateur Aléatoire")
                    sleep(1)
                    print("Quel élement aléatoire voulez-vous générer ?")
                    print("1. Nombre")
                    print("2. Lettre")
                    print("3. Couleur")
                    print("0. Quitter")
                    answer = input("==>  ")
                    if answer not in '0123':
                        print(
                            "Entrez 1, 2 ou 3 pour faire un choix. Pour Quitter, taper 0")
                        sleep(1.5)
                        pwdGenerator()
                    if answer == '1':
                        nbGenerator()
                    elif answer == '2':
                        letterGenerator()
                    elif answer == '3':
                        colorGenerator()
                    elif answer == '0':
                        sleep(1)
                        print("Accueil...")
                        sleep(1.5)
                        ultimateGenerator()

                def nbGenerator():
                    sleep(1)
                    system('@echo off')
                    system('cls')
                    print("Générateur de Nombres")
                    sleep(1)
                    print(
                        "Combien de nombres voulez-vous générer aléatoirement ? (Pour Quitter, taper 0)")
                    nb_nb = input("==>  ")
                    nb_nb_ = nb_nb.isdigit()
                    if nb_nb_ == False:
                        print(
                            "Entrez un nombre pour faire un choix. Pour quitter, taper 0")
                        sleep(1.5)
                        nbGenerator()
                    if nb_nb == '0':
                        sleep(1)
                        print("Accueil...")
                        sleep(1.5)
                        randomGenerator()
                    sleep(1)
                    nb_nb = int(nb_nb)
                    print("Dans quelle tranche de nombres ?")
                    nb_range_input1 = input("==>  ")
                    nb_range_input1_ = nb_range_input1.isdigit()
                    if nb_range_input1_ == False:
                        print("Entrez un nombre pour faire un choix.")
                        sleep(1.5)
                        nbGenerator()
                    nb_range_input2 = input("==>  ")
                    nb_range_input2_ = nb_range_input2.isdigit()
                    if nb_range_input2_ == False:
                        print("Entrez un nombre pour faire un choix. ")
                        sleep(1.5)
                        nbGenerator()
                    nb_range_input1 = int(nb_range_input1)
                    nb_range_input2 = int(nb_range_input2)
                    nb = random.choices(
                        range(nb_range_input1, nb_range_input2), k=nb_nb)
                    print_nb = []
                    sleep(1)
                    if nb_nb <= 1:
                        print()
                        print("Voici le nombre généré ==> ",
                              nb.__repr__()[1:-1])
                    elif nb_nb > 1:
                        print()
                        print(f"Voici les nombres générés:")
                        for n in nb:
                            if n not in print_nb:
                                print_nb.append(n)
                            if n in print_nb:
                                n_ = random.choice(
                                    range(nb_range_input1, nb_range_input2))
                                print_nb.append(n_)
                        print(print_nb.__repr__()[
                              1:-1].replace(',', ' -').replace("'", "").upper())
                    sleep(2)
                    print()
                    system('pause')
                    print("Accueil...")
                    sleep(1.5)
                    nbGenerator()

                def letterGenerator():
                    sleep(1)
                    system('@echo off')
                    system('cls')
                    print("Générateur de Lettres")
                    sleep(1)
                    print(
                        "Combien de lettres voulez-vous générer aléatoirement ? (Pour Quitter, taper 0)")
                    alphabet = string.ascii_lowercase
                    nb_let = input("==>  ")
                    nb_let_ = nb_let.isdigit()
                    if nb_let_ == False:
                        print(
                            "Entrez un nombre pour faire un choix. Pour quitter, taper 0")
                        sleep(1.5)
                        letterGenerator()
                    if nb_let == '0':
                        sleep(1)
                        print("Accueil...")
                        sleep(1.5)
                        randomGenerator()
                    sleep(1)
                    nb_let = int(nb_let)
                    if nb_let > len(alphabet):
                        print(
                            f"Il n'existe que {len(alphabet)} lettres! Je ne peux pas en générer plus!")
                        sleep(2)
                        letterGenerator()
                    let = random.choices(alphabet, k=nb_let)
                    print_let = []
                    print_alphabet = []
                    sleep(1)
                    if nb_let == 1:
                        print()
                        print("Voici la lettre générée ==> ",
                              let.__repr__()[1:-1].upper().replace("'", ""))
                    elif nb_let > 1:
                        if nb_let == 26:
                            print()
                            for letter in alphabet:
                                print_alphabet.append(letter)
                            print(f"Voici les lettres générés:")
                            random.shuffle(print_alphabet)
                            print(print_alphabet.__repr__()[
                                  1:-1].replace(',', ' -').replace("'", "").upper())
                        else:
                            print()
                            print(f"Voici les lettres générés:")
                            for l in let:
                                if l not in print_let:
                                    print_let.append(l)
                                else:
                                    l_ = random.choice(alphabet)
                                    print_let.append(l_)
                            print(print_let.__repr__()[
                                  1:-1].replace(',', ' -').replace("'", "").upper())
                    sleep(2)
                    print()
                    system('pause')
                    print("Accueil...")
                    sleep(1.5)
                    letterGenerator()

                def colorGenerator():
                    sleep(1)
                    system('@echo off')
                    system('cls')
                    print("Générateur de Couleurs")
                    sleep(1)
                    print(
                        "Combien de couleurs voulez-vous générer aléatoirement ? (Pour Quitter, taper 0)")
                    color = ['Bleu', 'Vert', 'Jaune',
                             'Rouge', 'Rose', 'Violet', 'Orange']
                    nb_clr = input("==>  ")
                    nb_clr_ = nb_clr.isdigit()
                    if nb_clr_ == False:
                        print(
                            "Entrez un nombre pour faire un choix. Pour quitter, taper 0")
                        sleep(1.5)
                        colorGenerator()
                    if nb_clr == '0':
                        sleep(1)
                        print("Accueil...")
                        sleep(1.5)
                        randomGenerator()
                    sleep(1)
                    nb_clr = int(nb_clr)
                    if nb_clr > len(color):
                        print(
                            f"Il n'existe que {len(color)} couleurs! Je ne peux pas en générer plus!")
                        sleep(2)
                        colorGenerator()
                    clr = random.choices(color, k=nb_clr)
                    print_clr = []
                    print_color = []
                    sleep(1)
                    if nb_clr <= 1:
                        print()
                        print("Voici la couleur généré ==> ",
                              clr.__repr__()[1:-1].replace("'", ""))
                    elif nb_clr > 1:
                        if nb_clr == 26:
                            print()
                            for color in color:
                                print_color.append(color)
                            print(f"Voici les couleurs générés:")
                            random.shuffle(print_color)
                            print(print_color.__repr__()[
                                  1:-1].replace(',', ' -').replace("'", "").upper())
                        else:
                            print()
                            print(f"Voici les couleurs générés:")
                            for c in clr:
                                if c not in print_clr:
                                    print_clr.append(c)
                                else:
                                    l_ = random.choice(color)
                                    print_clr.append(l_)
                            print(print_clr.__repr__()[
                                  1:-1].replace(',', ' -').replace("'", "").upper())
                    sleep(2)
                    print()
                    system('pause')
                    print("Accueil...")
                    sleep(1.5)
                    colorGenerator()

                ultimateGenerator()

            elif answer2 == "2":
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
                    print("Compteur de Caractères")
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
                    answer = input(u"==>  ")
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
                    answer = input(u"==>  ")
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
                            text = read_file.lower().replace('(r)', '').replace(
                                '(R)', '').replace('(c)', '').replace('(C)', '')
                            words = 0
                            letter_count = 0
                            vowels_count = 0
                            consonnes_count = 0
                            spechars_count = 0
                            chars_count = 0
                            space_count = 0
                            tab_count = 0
                            line_count = 0
                            nb_count = 0
                            alphabet = string.ascii_letters
                            vowels = ['a', 'e', 'i', 'o', 'u', 'y']
                            consonnes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                                         'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
                            spe_chars = string.punctuation
                            cut_word = text.split()
                            words = len(cut_word)
                            for word in cut_word:
                                isdigit_wrd = word.isdigit()
                                if isdigit_wrd == True:
                                    words -= 1
                            for letter in text:
                                isdigit_ltr = letter.isdigit()
                                if isdigit_ltr == False:
                                    if letter in vowels:
                                        vowels_count += 1
                                    elif letter in consonnes:
                                        consonnes_count += 1
                            for letter in text:
                                if letter in alphabet:
                                    letter_count += 1
                            for char in text:
                                if char in spe_chars:
                                    spechars_count += 1
                            chars_count = letter_count + spechars_count
                            for space in text:
                                if space == ' ':
                                    if space != '\t':
                                        space_count += 1
                            for tab in text:
                                if tab == '\t':
                                    tab_count += 1
                            for line in text:
                                if line == '\n':
                                    line_count += 1
                            for number in text:
                                isdigit_nb = number.isdigit()
                                if isdigit_nb == True:
                                    nb_count += 1

                            print("Analyse terminée !")
                            print("Préparation du rapport...")
                            sleep(2)
                            print()
                            print('*'*70)
                            print()
                            print("Rapport d'analyse du Fichier texte".upper())
                            print()
                            print(f"Nombres de Mots: {words}")
                            print(f"Nombres de Lettres: {letter_count}")
                            print(f"    Nombres de Voyelles: {vowels_count}")
                            print(f"    Nombres de Consonnes: {consonnes_count}")
                            print(f"Nombres de Caractères: {chars_count}")
                            print(f"    Spéciaux: {spechars_count}")
                            print(f"Nombres d'Espaces: {space_count}")
                            print(f"    Nombres de Tabulations: {tab_count}")
                            print(f"Nombres de Lignes: {line_count}")
                            print(f"Nombres de Chiffres: {nb_count}")
                            print()
                            print('*'*70)
                            print()
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
            # Ajt les autres elif pr les autres outils
        elif answer1 == "j":
            print("Voici nos mini-jeux:")
            sleep(1)
            print("1. Pierre, Feuille, Ciseaux")
            print("2. Juste Prix")
            print("3. Dés")
            print("4. Devine le Mot")
            # ajt les autres jeux
            print("0. Quitter")
            sleep(1)
            print("Vous voulez jouer au quel ?")
            answer3 = input("Entrez son chiffre  ==>  ")
            if answer3 not in '01234':
                print("Entrez 1, 2, 3 ou 4 pour faire un choix! Pour Quitter, taper 0.")
                sleep(1)
                rBigProject()
            if answer3 == '0':
                sleep(1)
                print("Accueil...")
                sleep(1.5)
                rBigProject()
            elif answer3 == "1":
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
                    manches_ = manches.isdigit()
                    if manches_ == False:
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
                    nb_essais_ = nb_essais.isdigit()
                    if nb_essais_ == False:
                        print("Entrez un chiffre !")
                        sleep(1.5)
                        game()
                    else:
                        nb_essais = int(nb_essais)
                    essais = 0
                    while statut == True:
                        remaining_trials = int(nb_essais) - essais - 1
                        user_price = input(
                            "Deviner le prix (entre 1 et 100) ==>  ")
                        user_price_ = user_price.isdigit()
                        if user_price_ == False:
                            print("Entrez un chiffre !")
                            sleep(1.5)
                            continue
                        else:
                            user_price = int(user_price)
                        if user_price == just_price:
                            print(
                                f"Bien joué, vous avez le juste prix en {essais} essais")
                            statut = False
                        elif user_price > just_price:
                            print("Le chiffre à trouver est plus bas !!")
                            essais += 1
                            print(f"Il vous reste {remaining_trials} essais !")
                        elif user_price < just_price:
                            print("Le chiffre à trouver est plus haut !!")
                            essais += 1
                            print(f"Il vous reste {remaining_trials} essais !")
                        if essais == nb_essais:
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
                    elif answer == "0":
                        print("Vous allez quitter le logiciel dans 5 secondes...")
                        sleep(2.7)
                        print("BigProject...")
                        sleep(1.8)
                        rBigProject()

                justprice()
            elif answer3 == "3":
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
                    elif answer == "0":
                        print("Vous allez quitter le logiciel dans 5 secondes...")
                        sleep(2.7)
                        print("BigProject...")
                        sleep(1.8)
                        rBigProject()

                dice()
            elif answer3 == "4":
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
                    print("Combien d'essais ? ")
                    attempts = input("==>  ")
                    attempts_ = attempts.isdigit()
                    if attempts_ == False:
                        print("Entrez un chiffre !")
                        sleep(1.5)
                        game()
                    else:
                        attempts = int(attempts)
                    word = unidecode(random.choice(file_read)).lower().replace("\n", "")
                    false_word = []
                    false_letter = []
                    sleep(2)
                    print(
                        f"Le mot contient {len(word)} lettres.\nPremière lettre : {word[0].upper()}\nDernière lettre : {word[len(word)-1].upper()}")
                    tries = 0
                    print("Devinez le mot !")
                    while tries < attempts:
                        sleep(1)
                        word_try_ = input("==>  ").lower()
                        word_try = profanity.censor(word_try_)
                        if word_try == word:
                            tries += 1
                            print("Trouvé! Bien joué!")
                            print(
                                f"Vous avez trouvé le mot en {tries} essais !")
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
                                    if letter not in false_letter:
                                        false_letter.append(letter)
                            print(
                                f"Liste des mauvaises lettres : {false_letter.__repr__()[1:-1].replace(',',' -')}")
                    print(f"Le bon mot était donc '{word}'")
                    sleep(2)
                    system("pause")
                    print("Accueil...")
                    sleep(1.2)
                    wrdguess()
                wrdguess()
            # ajt des elif pour les autres jeux
        elif answer1 == "0":
            print("Vous allez quitter le logiciel dans 5 secondes...")
            sleep(2.7)
            print("Sortie...")
            sleep(1.8)
            exit()
        elif answer1 not in "oj0":
            print(
                "Entrez un 'o' ou 'j' pour faire un choix. Sinon, tapez 0 pour Quitter."
            )
            sleep(1)
        rBigProject()

    def bigProject():
        intro()
        rBigProject()

    bigProject()


bp()
