from prettytable import PrettyTable

admin = {"id 0": {"gebruikersnaam": "admin", "wachtwoord": "admin"}}

personeelsleden = {"id 1": {"naam": "john", "geslacht": "man", "afdeling": "marketing", "jaar_in_dienst": 2010,
                            "maandloon": 2500},
                   "id 2 ": {"naam": "mark", "geslacht": "man", "afdeling": "marketing", "jaar_in_dienst": 2010,
                             "maandloon": 3000},
                   "id 3": {"naam": "lisa", "geslacht": "vrouw", "afdeling": "sales", "jaar_in_dienst": 2012,
                            "maandloon": 2800},
                   "id 4": {"naam": "lien", "geslacht": "vrouw", "afdeling": "sales", "jaar_in_dienst": 2013,
                            "maandloon": 2200},
                   "id 5": {"naam": "anass", "geslacht": "man", "afdeling": "developer", "jaar_in_dienst": 2013,
                            "maandloon": 2700},
                   "id 6": {"naam": "bjorn", "geslacht": "man", "afdeling": "developer", "jaar_in_dienst": 2014,
                            "maandloon": 3200},
                   "id 7": {"naam": "david", "geslacht": "man", "afdeling": "developer", "jaar_in_dienst": 2014,
                            "maandloon": 3400},
                   "id 8": {"naam": "maja", "geslacht": "vrouw", "afdeling": "sales", "jaar_in_dienst": 2016,
                            "maandloon": 3000},
                   "id 9": {"naam": "stephen", "geslacht": "man", "afdeling": "marketing", "jaar_in_dienst": 2017,
                            "maandloon": 4000},
                   "id 10": {"naam": "bertha", "geslacht": "vrouw", "afdeling": "sales", "jaar_in_dienst": 2019,
                             "maandloon": 2100}}


def toon_leden():
    leden = PrettyTable(["ID", "Naam", "Geslacht", "Afdeling", "jaar in dienst", "loon"])
    for id, lid in personeelsleden.items():
        leden.add_row(
            [id, lid["naam"], lid["geslacht"], lid["afdeling"], lid["jaar_in_dienst"], lid["maandloon"]])
    print(leden)


def admin_login():
    gebruikersnaam = input("Geef je gebruikersnaam in als admin:")
    wachtwoord = input("Geef je wachtwoord in")
    for id, lid in admin.items():
        while not wachtwoord == lid["wachtwoord"] or not gebruikersnaam == lid['gebruikersnaam']:
            gebruikersnaam = input("Foutieve invoer! \n\n Geef je gebruikersnaam opnieuw in als admin:")
            wachtwoord = input("Geef je wachtwoord in")
    print("-----------------------------------------------------------------------------------------------------------")
    print("ADMIN LOGIN SUCCEEDED\n")
    for id, lid in admin.items():
        Gebruikersnaam = lid['gebruikersnaam']
        text = lid['wachtwoord']
        s = 4
    print("Gebruikersnaam: " + Gebruikersnaam)
    print("Wachtwoord (encrypted): " + encrypt(text, s))
    encrypt("admin", 4)
    print("-----------------------------------------------------------------------------------------------------------")


def filter_of_adminfuncties():
    optie = input("Typ 1 voor admin functies of typ 2 voor te filteren")
    if optie == "1":
        admin_functies()
    elif optie == "2":
        filter_admin()
    else:
        print("Foutieve invoer!")
        filter_of_adminfuncties()


def admin_functies():
    print("-----------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------")
    functies = input(
        "0: Toon filter\n1: Personeel Toevoegen\n2: Meerdere personeel toevoegen\n3: Personeel verwijderen\n4: "
        "Loonsverhoging 1 personeel\n5: Loonsverhoging alle personeelsleden ")
    if functies == "1":
        voeg_personeelslid_toe()
    elif functies == "2":
        voeg_meerdere_leden_toe()
    elif functies == "3":
        verwijder_personeelslid()
    elif functies == "4":
        verhoog_loon_personeelslid()
    elif functies == "5":
        verhoog_loon_iedereen()
    elif functies == "0":
        filter_admin()
    else:
        print("Foutieve invoer"), admin_functies()


def voeg_lid_toe_hulp():
    id = "id " + str(len(personeelsleden) + 1)
    naam = input("Geef de naam van het personeelslid?")
    geslacht = input("Wat is zijn / haar geslacht?")
    afdeling = input(f"In welke afdeling werkt {naam.title()}?")
    jaar_in_dienst = input(f"in welk jaar is {naam.title()} in dienst gekomen?")
    maandloon = input(f"Wat is het maandloon van {naam.title()}?")
    personeelsleden.update({id: {"naam": naam, "geslacht": geslacht, "afdeling": afdeling,
                                 "jaar_in_dienst": jaar_in_dienst, "maandloon": maandloon}})


def voeg_personeelslid_toe():
    voeg_lid_toe_hulp()
    toon_leden()
    admin_functies()


def voeg_meerdere_leden_toe():
    voeg_lid_toe_hulp()
    doorgaan = input("Wil je nog een lid toevoegen? (ja of nee)")
    while not doorgaan == "nee":
        voeg_lid_toe_hulp()
        doorgaan = input("Wil je nog een lid toevoegen? (ja of nee)")
    toon_leden()
    admin_functies()


def verwijder_personeelslid():
    toon_leden()
    id = input("Geef het id van de personeelslid die je wil verwijderen:")
    id_personeel = "id " + str(id)
    del personeelsleden[id_personeel]
    toon_leden()
    admin_functies()


def verhoog_loon_personeelslid():
    toon_leden()
    id = input("Geef het id van de personeelslid die je zijn / haar loon wil verhogen:")
    id_personeel = "id " + str(id)
    while id_personeel not in personeelsleden:
        print("Foutieve ID, probeer opnieuw")
        id = input("Geef het id van de personeelslid waar je zijn / haar loon wil toevoegen:")
    maandloon = input("Welke maandloon wil je deze lid geven?")
    personeelsleden[id_personeel]["maandloon"] = maandloon
    toon_leden()
    admin_functies()


def verhoog_loon_iedereen():
    verhogen = int(input("Met hoeveel wil je iedereen hun maandloon verhogen?"))
    for id, lid in personeelsleden.items():
        lid["maandloon"] += verhogen
    toon_leden()
    admin_functies()


def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def filter_admin():
    print("-----------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------")
    functies = input(
        "0: Ga terug naar admin functies\n1: Filter man / vrouw\n2: Filter op afdeling\n3: Maandloon\n4: "
        "Vergelijking jaar in dienst")
    if functies == "1":
        mannen_en_vrouwen()
    elif functies == "2":
        afdeling()
    elif functies == "3":
        maandloon_vergelijking()
    elif functies == "4":
        langer_in_dienst()
    elif functies == "0":
        admin_functies()
    else:
        print("Foutieve invoer"), filter_admin()


def mannen_en_vrouwen():
    geslacht = input("Wilt u alle mannen of vrouwen zien? (man / vrouw)")
    if geslacht.lower() == "man" or geslacht.lower() == "vrouw":
        for id, lid in personeelsleden.items():
            if lid["geslacht"] == geslacht:
                lid.update({"id": {"naam": lid, "geslacht": lid, "afdeling": lid, "jaar_in_dienst": lid, "maandloon": lid}})
                print(id, end="\t")
                for info in lid.values():
                    print(info, end="\t\t")
                print("")
    else:
        print("Foutieve invoer")
        mannen_en_vrouwen()

    filter_admin()


def afdeling():
    afdeling_keuze = input("Welke afdeling wilt u bekijken?")
    if afdeling_keuze.lower() == 'sales' or afdeling_keuze.lower() == 'marketing' or afdeling_keuze.lower() == 'developer':
        for id, lid in personeelsleden.items():
            if lid["afdeling"] == afdeling_keuze:
                lid.update({"id": {"naam": lid, "geslacht": lid, "afdeling": lid, "jaar_in_dienst": lid, "maandloon": lid}})
                print(id, end="\t")
                for info in lid.values():
                    print(info, end="\t\t")
                print("")
    else:
        print("Foutieve invoer")
        afdeling()
    filter_admin()


def maandloon_vergelijking():
    maandloon_vergelijken = int(input(
        "Geef een maandloon in (vb: 2500) en er wordt een overzicht gegeven van iedereen die meer verdient"))
    for id, lid in personeelsleden.items():
        if maandloon_vergelijken < lid['maandloon']:
            lid.update({"id": {"naam": lid, "geslacht": lid, "afdeling": lid, "jaar_in_dienst": lid, "maandloon": lid}})
            print(id, end="\t")
            for info in lid.values():
                print(info, end="\t\t")
            print("")
    filter_admin()


def langer_in_dienst():
    jaar_in_dienst = int(
        input("Geef een jaar in waarvan je wil weten welke personeelslid er langer dan dat jaar werkt"))
    for id, lid in personeelsleden.items():
        if jaar_in_dienst > lid['jaar_in_dienst']:
            lid.update({"id": {"naam": lid, "geslacht": lid, "afdeling": lid, "jaar_in_dienst": lid, "maandloon": lid}})
            print(id, end="\t")
            for info in lid.values():
                print(info, end="\t\t")
            print("")
    filter_admin()


toon_leden()
admin_login()
filter_of_adminfuncties()
