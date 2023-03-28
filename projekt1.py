"""
projekt1.py: první projekt do Engeto Online Python Akademie
author: Daniel Filip
email: danielfilip102@gmail.com
discord: Danko#3595 (Daniel F.)
"""


# předem zadaný text v listu
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]



# uživatelská jména
uzivatele = ("bob" , "ann" , "mike" , "liz")
# uživatelská hesla
hesla = ("123" , "pass123" , "password123" , "pass123")
# "grafický" oddělovač 
oddelovac = "=" *35

list2 = dict(zip(uzivatele , hesla))
print(list2)

#přihlašování
print(oddelovac)
jmeno = input("Zadej své uživatelské jmeno: ")
print(oddelovac)

if jmeno in list2:
    print("Jméno přijato")
    print(oddelovac)
else:
    print(oddelovac)
    print("Jméno "+str(jmeno) +" nebylo nalezeno v databázi!")
    print(oddelovac)
    quit()

heslo = input("zadej heslo:")
if list2[jmeno] == heslo:
    print("Vítej, " +str(jmeno) +"!")
    print(oddelovac)
else:
    print("Špatné heslo!")

#výpis možností a nadále volba uživatele po přihlášení
print(""" 
1 - TEXT #1
2 - TEXT #2
3 - TEXT #3
""")
#------------------------------------------------------------------------------------------------------------------

volba = input("Zadejte číslo řádku textu, který si přejete rozebrat:")

if volba is '1':
   #print(TEXTS[0])  # výpis textu 1 pouze pro ověření

    slova = []
    for slovo in TEXTS[0].split():
       cisteSlovo = slovo.strip(".,?!")
       slova.append(cisteSlovo.lower())

    #print(slova)
    # hodnoty všech slov kolik mají znaků
    res = list (map(len, slova))
    for slovo in res:   #
      res[slovo] = res.count(slovo) #

    res2 = []
    res2 = {i:res.count(i) for i in res}
    res2 = sorted(res2.items())

  
    #print(res)
    # list tuplu do slovníku
    dictionary = {}
    for key, val in res2:
      dictionary.setdefault(key, val)
      #print(dictionary)
   
    

    pocetSlov = TEXTS[0].split() #pass
    zacatekVelke = sum(1 for c in TEXTS[0].split() if c.istitle()) #pass
    celaVelka = sum(1 for c in TEXTS[0].split() if c.isupper() and c.isalpha()) #pass
    malaPismena = sum(1 for c in TEXTS[0].split() if c.islower() ) #pass
    sumaCisel = sum([int(i) for i in TEXTS[0].split() if type(i)== int or i.isnumeric()]) #pass
    pocetCisel = sum(1 for c in TEXTS[0].split() if c.isdigit()) #pass
   
    print(oddelovac)
    print("Počet slov: ", len(pocetSlov))
    print("Počet slov začínajících velkým písmenem: " +str(zacatekVelke))
    print("Počet slov psaných velkými písmeny: "+str(celaVelka))
    print("Počet slov psaných malými písmeny: " +str(malaPismena))
    print("Počet čísel: "+str(pocetCisel))
    print("Sumu všech čísel: "+str(sumaCisel))
    print(oddelovac)
    print("Graf")
    print(oddelovac)

    for key, value in dictionary.items():
        print(key, ' * '*value, value)
   # print(res2)
else:
    if volba is '2':
      #print(TEXTS[1])

     slova = []
     for slovo in TEXTS[1].split():
       cisteSlovo = slovo.strip(".,?!")
       slova.append(cisteSlovo.lower())

    #print(slova)
    # hodnoty všech slov kolik mají znaků
     res = list (map(len, slova))
     for slovo in res:   #
        res[slovo] = res.count(slovo) #

     res2 = []
     res2 = {i:res.count(i) for i in res}
     res2 = sorted(res2.items())

  
    #print(res)
    # list tuplu do slovníku
     dictionary = {}
     for key, val in res2:
        dictionary.setdefault(key, val)
      #print(dictionary)

      
      
     pocetSlov = TEXTS[1].split() #pass
     zacatekVelke = sum(1 for c in TEXTS[1].split() if c.istitle()) #pass
     celaVelka = sum(1 for c in TEXTS[1].split() if c.isupper() and c.isalpha()) #pass
     malaPismena = sum(1 for c in TEXTS[1].split() if c.islower() ) #pass
     sumaCisel = sum([int(i) for i in TEXTS[1].split() if type(i)== int or i.isnumeric()]) #pass
     pocetCisel = sum(1 for c in TEXTS[1].split() if c.isdigit()) #pass

     print(oddelovac)
     print("Počet slov: ", len(pocetSlov))
     print("Počet slov začínajících velkým písmenem: " +str(zacatekVelke))
     print("Počet slov psaných velkými písmeny: "+str(celaVelka))
     print("Počet slov psaných malými písmeny: " +str(malaPismena))
     print("Počet čísel: "+str(pocetCisel))
     print("Sumu všech čísel: "+str(sumaCisel))
     print(oddelovac)
     print("Graf")
     print(oddelovac)

     for key, value in dictionary.items():
        print(key, ' * '*value, value)

    else:
      if volba is '3':
       # print(TEXTS[2])
        slova = []
        for slovo in TEXTS[0].split():
            cisteSlovo = slovo.strip(".,?!")
            slova.append(cisteSlovo.lower())

    #print(slova)
    # hodnoty všech slov kolik mají znaků
        res = list (map(len, slova))
        for slovo in res:   #
            res[slovo] = res.count(slovo) #

        res2 = []
        res2 = {i:res.count(i) for i in res}
        res2 = sorted(res2.items())

  
    #print(res)
    # list tuplu do slovníku
        dictionary = {}
        for key, val in res2:
            dictionary.setdefault(key, val)
      #print(dictionary)

        
        
               
        pocetSlov = TEXTS[2].split() #pass
        zacatekVelke = sum(1 for c in TEXTS[2].split() if c.istitle()) #pass
        celaVelka = sum(1 for c in TEXTS[2].split() if c.isupper() and c.isalpha()) #pass
        malaPismena = sum(1 for c in TEXTS[2].split() if c.islower() ) #pass
        sumaCisel = sum([int(i) for i in TEXTS[2].split() if type(i)== int or i.isnumeric()]) #pass
        pocetCisel = sum(1 for c in TEXTS[2].split() if c.isdigit()) #pass

        print(oddelovac)
        print("Počet slov: ", len(pocetSlov))
        print("Počet slov začínajících velkým písmenem: " +str(zacatekVelke))
        print("Počet slov psaných velkými písmeny: "+str(celaVelka))
        print("Počet slov psaných malými písmeny: " +str(malaPismena))
        print("Počet čísel: "+str(pocetCisel))
        print("Sumu všech čísel: "+str(sumaCisel))
        print(oddelovac)
        print("Graf")
        print(oddelovac)

        for key, value in dictionary.items():
            print(key, ' * '*value, value)
      else:
        print("Špatná volba!")
        quit()



                 


