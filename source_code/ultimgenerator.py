import random
import string
import time

#Générateur de Mot de Passe
def pwdGeneratorLetters():
    letters_uppercase = string.ascii_uppercase
    letters_lowercase = string.ascii_lowercase
    symbols = string.punctuation
    numbers = string.digits
    pwd_sample = letters_uppercase + letters_lowercase + numbers + symbols
    print("Bip... Bip... Nouveau Mot De Passe...")
    answer2 = int(input("Avec combien de caractères ? Pour la sécu, 8 c'est bien!  ==>  "))
    length = answer2
    pwd = "".join(random.sample(pwd_sample, length))

    print("Tiens, ton nouveau mot de passe ultra-securisé  ==>  ", pwd)
    quit = input("Tu t'en vas ?  ==>  ")
    if quit == 'Oui':
        print('Salut. A Bientôt !')
        time.sleep(1)
        exit()
    elif quit == 'Non':
        print("Cool !")
        pwdGeneratorLetters()
    else:
        quit2 = input("Répondez avec 'Oui' ou 'Non'  ==>  ")
        if quit2 == 'Oui':
            print('Salut. A Bientôt !')
            time.sleep(1)
            exit()
        elif quit == 'Non':
            print("Cool !")
            pwdGeneratorLetters()

def pwdGeneratorNum():
    numbers = string.digits
    pwd_sample = numbers
    print("Bip... Bip... Nouveau Mot De Passe...")
    answer2 = int(input("Avec combien de caractères ? 4 ou 6  ==>  "))
    if answer2 == 4:
        length = 4
    elif answer2 == 6:
        length = 6
    elif answer2 != '4' or '6':
        print("Entrez 4 ou 6!!")
        pwdGeneratorNum()
    pwd = "".join(random.sample(pwd_sample, length))
    print("Tiens, ton nouveau mot de passe de téléphone ultra-securisé  ==>  ", pwd)
    quit = input("Tu t'en vas ?  ==>  ")
    if quit == 'Oui':
        print('Salut. A Bientôt !')
        time.sleep(1)
        exit()
    elif quit == 'Non':
        print("Cool !")
        pwdGeneratorNum()
    else:
        quit2 = input("Répondez avec 'Oui' ou 'Non'  ==>  ")
        if quit2 == 'Oui':
            print('Salut. A Bientôt !')
            time.sleep(1)
            exit()
        elif quit == 'Non':
            print("Cool !")
            pwdGeneratorNum()

def pwdGenerator():
    print("Générateur de Mots de Passe")
    print("1. Génerer un Mot de Passe avec des Chiffres, des Lettres, et des Symboles")
    print("2. Génerer un Mot de passe pour téléphone avec des Chiffres seulement")
    print("3. Quitter")
    answer = int(input("Tapez 1 ou 2 pour choisir une option  ==>  "))
    if answer == 1:
        print("Ok, un Mot De Passe ultra-securisé ! Super !")
        pwdGeneratorLetters()
    elif answer == 2:
        print("Ca part pour un Mot De Passe de téléphone! Super !")
        pwdGeneratorNum()
    elif answer == 3:
        print("Dommage, Reviens quand tu voudras securiser tes Mots De Passe!")
        time.sleep(1)
        exit()

#Generateur de Nombre aléatoire
def nbGenerator():
    print("Générateur de Nombres")
    print("Combien de nombres voulez-vous génerer ?")
    nb = int(input("==>  "))
    print("Entre combien à combien ? (1 par ligne)")
    range1 = int(input('==>  '))
    range2 = int(input('==>  '))
    generated_nb = random.choices(range(range1, range2), k=nb)
    print(f"\nNombres génerés")
    for nb in generated_nb:
        print(nb, end="   ")
    answer_replay = input("\n\nVoulez vous recommencer ? Si oui, entrez 'o'  ==>  ")
    if answer_replay == 'o':
        print("Super!!")
        nbGenerator()
    else:
        print("Revenez quand vous voulez !!")
        time.sleep(1)
        exit()

#Generateur de Lettre aléatoire
def letterGenerator():
    print("Générateur de Lettres")
    print("Combien de lettres voulez-vous génerer ?")
    letters = string.ascii_uppercase
    ltr = int(input("==>  "))
    generated_ltr = random.choices(letters, k=ltr)
    print(f"\nLettres génerées")
    for ltr in generated_ltr:
        print(ltr, end="   ")
    answer_replay = input("\n\nVoulez vous recommencer ? Si oui, entrez 'o'  ==>  ")
    if answer_replay == 'o':
        print("Super!!")
        letterGenerator()
    else:
        print("Revenez quand vous voulez !!")
        time.sleep(1)
        exit()

#Ultime génerateur
def ultimateGenerator():
    print('GENERATEUR ULTIME')
    print('1. Génerateur de Mots de Passe')
    print('2. Génerateur de Nombres aléatoire')
    print('3. Génerateur de Lettres aléatoire')
    answer = input("Entrez un nombre pour faire un choix (Pour quitter 'q')  ==>  ")
    if answer == "1":
        time.sleep(1)
        pwdGenerator()
    elif answer == "2":
        time.sleep(1)
        nbGenerator()
    elif answer == "3":
        time.sleep(1)
        letterGenerator()
    elif answer == 'q':
        print("Dommage, Reviens quand tu voudras securiser tes Mots De Passe!")
        time.sleep(2)
        exit()
    elif answer != 'q' or '1' or '2' or '3':
        print("Entrez 1, 2 ou 3 pour faire un choix (Pour quitter 'q')")
        time.sleep(1.5)
        ultimateGenerator()