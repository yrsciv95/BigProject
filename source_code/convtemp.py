from time import sleep
from os import system

def tempeconv():
    system('@echo off')
    system('cls')
    print("LOGICIEL Convertisseur de Température")
    sleep(1.5)
    print("Ce logiciel peut convertir les températures en °C vers °F, °R, K")
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
        tempeconv()

def fconv():
    sleep(1.2)
    system('@echo off')
    system('cls')
    print("Celsius --> Fahrenheit".upper())
    sleep(1)
    print("Entrez une température (en °C)")
    input_tempe = float(input("==>  "))
    print("Calcul...")
    sleep(2)
    tempe_conv = (input_tempe * 9/5) + 32         
    print(f"{input_tempe}°C correspond à {tempe_conv}°F")
    sleep(2.5)
    system('pause')
    print('Accueil...')
    sleep(1.2)
    tempeconv()

def kconv():
    sleep(1.2)
    system('@echo off')
    system('cls')
    print("Celsius --> Kelvin".upper())
    sleep(1)
    print("Entrez une température (en °C)")
    input_tempe = float(input("==>  "))
    print("Calcul...")
    sleep(2)
    tempe_conv = input_tempe + 273.15    
    print(f"{input_tempe}°C correspond à {tempe_conv} K")
    sleep(2.5)
    system('pause')
    print('Accueil...')
    sleep(1.2)
    tempeconv()

def rconv():
    sleep(1.2)
    system('@echo off')
    system('cls')
    print("Celsius --> Rankine".upper())
    sleep(1)
    print("Entrez une température (en °C)")
    input_tempe = float(input("==>  "))
    print("Calcul...")
    sleep(2)
    tempé_conv = input_tempe * 9/5 + 491.67       
    print(f"{input_tempe}°C correspond à {tempé_conv}°R")
    sleep(2.5)
    system('pause')
    print('Accueil...')
    sleep(1.2)
    tempeconv()