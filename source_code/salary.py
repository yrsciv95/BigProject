import time

def rSalary():
    time.sleep(.4)
    print("TYPES DE PAYES")
    time.sleep(.2)
    print("1. Non - Cadre")
    print("2. Cadre")
    print("3. Profession Libérale")
    print("4. Fonction Publique")
    time.sleep(.6)
    answer = int(input("Entrez son numéro  ==>  "))
    if answer == 1:
        print("Initialisation ...")
        time.sleep(.9)
        rSalaryNC()
    elif answer == 2:
        print("Initialisation ...")
        time.sleep(.9)
        rSalaryC()
    elif answer == 3:
        print("Initialisation ...")
        time.sleep(.9)
        rSalaryL()
    elif answer == 4:
        print("Initialisation ...")
        time.sleep(.9)
        rSalaryFP()
    elif answer != 1 or 2 or 3 or 4:
        print("Entrez 1, 2, 3 ou 4 pour faire un choix !")
        time.sleep(.7)
        rSalary()
    replay()

def rSalaryC():
    print("Calculer son salaire après taxes (Cadre)")
    salary = float(input("Entrez un salaire brut mensuel  ==>  "))
    currency = ['$', '£', '€']
    user_currency = input("Entrez la devise de votre salaire  ==>  ")
    if user_currency  not in currency:
        print("Entrez une devise valide ($, £, €)")
        time.sleep(1)
        rSalaryC()
    net = (salary * 25)/100
    net_salary_month = salary - net
    net_salary_year = net_salary_month*12
    print("Calcul ...")
    time.sleep(1.5)
    print("Voici votre salaire net mensuel:", round(net_salary_month), user_currency)
    print("Ainsi que votre salaire net annuel:", round(net_salary_year), user_currency)

def rSalaryFP():
    print("Calculer son salaire après taxes (Fonction Publique)")
    salary = float(input("Entrez un salaire brut mensuel  ==>  "))
    currency = ['$', '£', '€']
    user_currency = input("Entrez la devise de votre salaire  ==>  ")
    if user_currency  not in currency:
        print("Entrez une devise valide ($, £, €)")
        time.sleep(1)
        rSalaryFP()
    net = (salary * 15)/100
    net_salary_month = salary - net
    net_salary_year = net_salary_month*12
    print("Calcul ...")
    time.sleep(1.5)
    print("Voici votre salaire net mensuel:", round(net_salary_month), user_currency)
    print("Ainsi que votre salaire net annuel:", round(net_salary_year), user_currency)

def rSalaryL():
    print("Calculer son salaire après taxes (Profession Libérale)")
    salary = float(input("Entrez un salaire brut mensuel  ==>  "))
    currency = ['$', '£', '€']
    user_currency = input("Entrez la devise de votre salaire  ==>  ")
    if user_currency  not in currency:
        print("Entrez une devise valide ($, £, €)")
        time.sleep(1)
        rSalaryNC()
    net = (salary * 45)/100
    net_salary_month = salary - net
    net_salary_year = net_salary_month*12
    print("Calcul ...")
    time.sleep(1.5)
    print("Voici votre salaire net mensuel:", round(net_salary_month), user_currency)
    print("Ainsi que votre salaire net annuel:", round(net_salary_year), user_currency)

def rSalaryNC():
    print("Calculer son salaire après taxes (Non - Cadre)")
    salary = float(input("Entrez un salaire brut mensuel  ==>  "))
    currency = ['$', '£', '€']
    user_currency = input("Entrez la devise de votre salaire  ==>  ")
    if user_currency  not in currency:
        print("Entrez une devise valide ($, £, €)")
        time.sleep(1)
        rSalaryNC()
    net = (salary * 22)/100
    net_salary_month = salary - net
    net_salary_year = net_salary_month*12
    print("Calcul ...")
    time.sleep(1.5)
    print("Voici votre salaire net mensuel:", round(net_salary_month), user_currency)
    print("Ainsi que votre salaire net annuel:", round(net_salary_year), user_currency)

def ask():
    print("CALCULATEUR DE SALAIRE")
    answer = input("Si vous souhaitez commencer tapez 1 sinon tapez 'q' pour Quitter  ==>  ")
    if answer == '1':
        print("GENIAL !!")
    elif answer == 'q':
        print("Dommage, Au revoir !!")
        time.sleep(1)
        exit()
    elif answer != '1' or 'q':
        print("Si vous souhaitez commencer tapez 1 sinon tapez 'q' pour Quitter. Attention !")
        ask()

def replay():
    answer_replay = input("Voulez vous recommencer ? Si oui, entrez 'o'  ==>  ")
    if answer_replay == 'o':
        print("Super!!")
        rSalary()
    else:
        print("Revenez quand vous voulez !!")
        time.sleep(1)
        exit()

def salary():
    ask()
    rSalary()
    replay()