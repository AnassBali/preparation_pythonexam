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
    print("--------------------------------------------------")
    print("ID", "\t\t", "Naam", "\t", "geslacht", "\t", "afdeling", "\t", "jaar in dienst", "maandloon")

    print("--------------------------------------------------\n")

    for id, gegevens in personeelsleden.items():
        print(id, end="\t")
        for info in gegevens.values():
            print(info, end="\t\t")
        print("")
    print("--------------------------------------------------")


def admin_login():
    gebruikersnaam = input("Geef je gebruikersnaam in als admin:")
    wachtwoord = input("Geef je wachtwoord in")
    for id, lid in admin.items():
        while not wachtwoord == lid["wachtwoord"] or not gebruikersnaam == lid['gebruikersnaam']:
            gebruikersnaam = input("Foutieve invoer! \n\n Geef je gebruikersnaam opnieuw in als admin:")
            wachtwoord = input("Geef je wachtwoord in")
    print("\n\n\t\t\t\tLOGIN SUCCEEDED\n")
    admin_functies()


def admin_functies():
    print(
        "U kunt kiezen tussen deze functies voor de personeelsleden:\n1 Personeel toevoegen \t - \t Meerdere "
        "personeel toevoegen \t - \tpersoneel verwijderen \t - \t loonsverhoging personeel \t - \t verhoog alle lonen "
        "")
    functies = input(
        "\n\ntyp:\n\n1 personeel toevoegen\nmeerdere personeel toevoegen\npersoneel verwijderen\nloonsverhoging 1 "
        "personeel\nloonsverhoging alle personeelsleden\n")
    if functies == '1 personeel toevoegen':
        voeg_personeelslid_toe()
    elif functies == 'meerdere personeel toevoegen':
        voeg_meerdere_leden_toe()
    elif functies == 'personeel verwijderen':
        verwijder_personeelslid()
    elif functies == 'loonsverhoging 1 personeel':
        verhoog_loon_personeelslid()
    elif functies == 'loonsverhoging alle personeelsleden':
        verhoog_loon_iedereen()
    else:
        print("Foutieve invoer"), admin_functies()


def voeg_lid_toe_hulp():
    id = "id  " + str(len(personeelsleden) + 1)
    naam = input("Geef de naam van het personeelslid?")
    geslacht = input("Wat is zijn / haar geslacht?")
    afdeling = input("Wat is zijn afdeling?")
    jaar_in_dienst = input("in welk jaar is hij in dienst gekomen?")
    maandloon = input("Wat is zijn maandloon")
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
    id = input("Geef het id van de personeelslid waar je zijn loon wil toevoegen:")
    maandloon = input("Welke maandloon wil je deze medewerker geven?")
    id_personeel = "id " + str(id)
    personeelsleden[id_personeel]["maandloon"] = maandloon
    toon_leden()
    admin_login()


def verhoog_loon_iedereen():
    verhogen = int(input("Met hoeveel wil iedereen hun maandloon verhogen?"))
    for personeel in personeelsleden.values():
        personeel["maandloon"] = personeel["maandloon"] + verhogen
    toon_leden()
    admin_login()


def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


for id, lid in admin.items():
    Gebruikersnaam = lid['gebruikersnaam']
    text = lid['wachtwoord']
    s = 4
    print("Gebruikersnaam: " + Gebruikersnaam)
    print("Shift : " + str(s))
    print("Wachtwoord encrypted: " + encrypt(text, s))
    print("Wachtwoord decrypted  : " + text)


def filter_admin():
    mannen_en_vrouwen()
    afdeling()
    maandloon_vergelijking()
    langer_in_dienst()


def mannen_en_vrouwen():
    geslacht = input("Wilt u alle mannen of vrouwen zien? (man / vrouw)")
    for id, lid in personeelsleden.items():
        if lid["geslacht"] == geslacht:
            lid.update({"id": {"naam": lid, "geslacht": lid, "afdeling": lid, "jaar_in_dienst": lid, "maandloon": lid}})
            print(id, end="\t")
            for info in lid.values():
                print(info, end="\t\t")
            print("")


def afdeling():
    afdeling = input("Welke afdeling wilt u bekijken?")
    for id, lid in personeelsleden.items():
        if lid["afdeling"] == afdeling:
            lid.update({"id": {"naam": lid, "geslacht": lid, "afdeling": lid, "jaar_in_dienst": lid, "maandloon": lid}})
            print(id, end="\t")
            for info in lid.values():
                print(info, end="\t\t")
            print("")


def maandloon_vergelijking():
    maandloon_vergelijken = int(input(
        "Geef een maandloon in en er wordt een overzicht gegeven van iedereen die meer verdient"))
    for id, lid in personeelsleden.items():
        if maandloon_vergelijken < lid['maandloon']:
            lid.update({"id": {"naam": lid, "geslacht": lid, "afdeling": lid, "jaar_in_dienst": lid, "maandloon": lid}})
            print(id, end="\t")
            for info in lid.values():
                print(info, end="\t\t")
            print("")


def langer_in_dienst():
    jaar_in_dienst = int(input("Geef een jaar in waarvan je wil weten welke personeelslid er langer werkt"))
    for id, lid in personeelsleden.items():
        if jaar_in_dienst > lid['jaar_in_dienst']:
            lid.update({"id": {"naam": lid, "geslacht": lid, "afdeling": lid, "jaar_in_dienst": lid, "maandloon": lid}})
            print(id, end="\t")
            for info in lid.values():
                print(info, end="\t\t")
            print("")


encrypt("admin", 4)
toon_leden()
admin_login()
filter_admin()
