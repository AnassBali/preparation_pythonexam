from prettytable import PrettyTable
from colorama import *

admin = {"id 0": {"username": "admin", "password": "admin"}}

employers = {"id 1": {"name": "john", "gender": "man", "department": "marketing", "year_of_service": 2010,
                      "salary": 2500},
             "id 2": {"name": "mark", "gender": "man", "department": "marketing", "year_of_service": 2010,
                      "salary": 3000},
             "id 3": {"name": "lisa", "gender": "woman", "department": "sales", "year_of_service": 2012,
                      "salary": 2800},
             "id 4": {"name": "lien", "gender": "woman", "department": "sales", "year_of_service": 2013,
                      "salary": 2200},
             "id 5": {"name": "jordy", "gender": "man", "department": "developer", "year_of_service": 2013,
                      "salary": 4600},
             "id 6": {"name": "bjorn", "gender": "man", "department": "developer", "year_of_service": 2014,
                      "salary": 3200},
             "id 7": {"name": "david", "gender": "man", "department": "developer", "year_of_service": 2014,
                      "salary": 3400},
             "id 8": {"name": "maja", "gender": "woman", "department": "sales", "year_of_service": 2016,
                      "salary": 3000},
             "id 9": {"name": "stephen", "gender": "man", "department": "marketing", "year_of_service": 2017,
                      "salary": 4400},
             "id 10": {"name": "bertha", "gender": "woman", "department": "sales", "year_of_service": 2019,
                       "salary": 2100}}


def show_employers():
    employers_information = PrettyTable(["ID", "name", "gender", "department", "years_of_service", "salary"])
    for id, employer in employers.items():
        employers_information.add_row(
            [id, employer["name"], employer["gender"], employer["department"], employer["year_of_service"],
             employer["salary"]])
    print(employers_information)


def admin_login():
    username = input("Enter your username as admin:")
    password = input("Enter your password:")
    for id, employer in admin.items():
        while not password == employer["password"] or not username == employer['username']:
            print(Fore.RED,"\nIncorrect input!", Fore.RESET)
            username = input("\n\nEnter your username again as admin:")
            password = input("Enter your password:")
    print(Fore.BLACK)
    print("-----------------------------------------------------------------------------------------------------------"
          "-")
    print(Fore.LIGHTGREEN_EX)
    print("\t\t\t\t\t\t\t\t\t\t\t\tADMIN LOGIN SUCCESSFUL\n")
    for id, employer in admin.items():
        username = employer['username']
        text = employer['password']
        s = 4
    print(Fore.LIGHTGREEN_EX, "\n\t\t\t\t\t\t\t\t\t\t\t\tUsername: " + username)
    print("\t\t\t\t\t\t\t\t\t\t\t\tPassword (encrypted): " + encrypt(text, s))
    encrypt("admin", 4)
    print(Fore.BLACK, "------------------------------------------------------------------------------------------------"
                      "-----------", Fore.GREEN)


def admin_functions_or_filter():
    Fore.RESET
    option = input("Choose a number:\n1: Admin Functions\n2: Filter system\n")
    if option == "1":
        admin_functions()
    elif option == "2":
        filter_admin()
    else:
        print(Fore.RED, "Incorrect input!")
        admin_functions_or_filter()


def admin_functions():
    print(Fore.GREEN,
          "\n-------------------------------------------------------------------------------------------------------"
          "----")
    print("-----------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t\t\t\t\tWelcome to the Admin Functions!")
    print("-----------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------",
          Fore.BLACK)
    functions = input(
        "0: Show filter\n1: Add employer \n2: Add multiple employers\n3: Delete employer\n4: "
        "Raise salary employer\n5: Raise salary all employers\n\n ")
    print(Fore.RESET)
    if functions == "1":
        add_employer()
    elif functions == "2":
        add_multiple_employers()
    elif functions == "3":
        remove_employee()
    elif functions == "4":
        increase_employee_salary()
    elif functions == "5":
        increase_salary_for_all_employees()
    elif functions == "0":
        filter_admin()
    else:
        print(Fore.RED, "Incorrect input", Fore.RESET), admin_functions()


def add_employer_help():
    id = "id " + str(len(employers) + 1)
    name = input("What is the name of the employee?")
    gender = input("What is his / her gender?")
    department = input(f"In which department does {name.title()} work?")
    year_of_service = input(f"In what year did {name.title()} start working?")
    monthly_salary = input(f"What is the monthly salary of {name.title()}?")
    employers.update({id: {"name": name, "gender": gender, "department": department,
                           "year_of_service": year_of_service, "salary": monthly_salary}})


def add_employer():
    add_employer_help()
    show_employers()
    print(Fore.GREEN, f"\nNew employer got successfully added, welcome on board! \n", Fore.RESET)
    admin_functions()


def add_multiple_employers():
    add_employer_help()
    add_member = input("Do you want to add another employee? (type 'yes' to continue)")
    while add_member == "yes":
        add_employer_help()
        add_member = input("Do you want to add another employee? (yes or no)")
    show_employers()
    print(Fore.GREEN, f"\nNew employer got successfully added! \n", Fore.RESET)
    admin_functions()


def remove_employee():
    show_employers()
    id = input("Enter the id of the employee you want to remove:")
    id_employee = "id " + str(id)
    while id_employee not in employers.keys():
        print(Fore.RED, "\nIncorrect input!", Fore.RESET)
        id = input("Enter the id of the employee you want to remove:")
        id_employee = "id " + str(id)
    del employers[id_employee]
    show_employers()
    print(Fore.GREEN, f"\nID {id} got successfully deleted! \n", Fore.RESET)
    admin_functions()


def increase_employee_salary():
    show_employers()
    id = input("Enter the id of the employee whose salary you want to increase:")
    id_employee = "id " + id
    while id_employee not in employers:
        print(Fore.RED, "Incorrect ID, try again", Fore.RESET)
        id = input("Enter the id of the employee whose salary you want to add:")
        id_employee = "id " + id
    monthly_salary = int(input(f"How much would you like to increase for id {id}?"))
    employers[id_employee]["salary"] += monthly_salary
    show_employers()
    print(Fore.GREEN, f"\nID {id} his salary got successfully increased! \n", Fore.RESET)
    admin_functions()


def increase_salary_for_all_employees():
    increase = int(input("How much would you like to increase everyone's monthly salary?"))
    for id, employer in employers.items():
        employer["salary"] += increase

    show_employers()
    print(Fore.GREEN, f"\nEveryone's salary got successfully increased by €{increase}!\n ", Fore.RESET)
    admin_functions()


def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


def filter_admin():
    print(Fore.BLUE,
          "\n----------------------------------------------------------------------------------------------------------"
          "-")
    print("-----------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t\t\t\t\tWelcome to the filter system!")
    print("-----------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------",
          Fore.BLACK)
    functions = input(
        "0: Go back to admin functions\n1: Filter man / woman\n2: Filter by department\n3: Monthly salary\n4: "
        "Service year comparison")
    if functions == "1":
        men_and_women()
    elif functions == "2":
        department()
    elif functions == "3":
        salary_comparison()
    elif functions == "4":
        longer_in_service()
    elif functions == "0":
        admin_functions()
    else:
        print(Fore.RED, "Incorrect input", Fore.RESET), filter_admin()


def men_and_women():
    gender = input("Do you want to see all men or women? (man / woman)")
    print(Fore.RESET)
    if gender.lower() == "man" or gender.lower() == "woman":
        for id, employer in employers.items():
            if employer["gender"] == gender:
                employer.update(
                    {"id": {"name": employer, "gender": employer, "department": employer, "year_of_service": employer,
                            "salary": employer}})
                print(id, end="\t")
                for info in employer.values():
                    print(info, end="\t\t")
                print("")
    else:
        print(Fore.RED, "Incorrect input", Fore.RESET)
        men_and_women()
    filter_admin()


def department():
    department_choice = input("Which department would you like to view?")
    print(Fore.RESET)
    if department_choice.lower() == 'sales' or department_choice.lower() == 'marketing' \
            or department_choice.lower() == 'developer':
        for id, employer in employers.items():
            if employer["department"] == department_choice:
                employer.update(
                    {"id": {"name": employer, "gender": employer, "department": employer, "year_of_service": employer,
                            "salary": employer}})
                print(id, end="\t")
                for info in employer.values():
                    print(info, end="\t\t")
                print("")
    else:
        print(Fore.RED, "Incorrect input", Fore.RESET)
        department()
    filter_admin()


def salary_comparison():
    salary_to_compare = int(input("Enter a monthly salary (e.g.: 2500) and a list will be shown of everyone who earns "
                                  "more"))
    print(Fore.RESET)
    for id, employer in employers.items():
        if salary_to_compare < employer['salary']:
            employer.update({"id": {"name": employer, "gender": employer, "department": employer,
                                    "year_of_service": employer, "salary": employer}})
            print(id, end="\t")
            for info in employer.values():
                print(info, end="\t\t")
            print("")
    filter_admin()


def longer_in_service():
    year_of_service = int(
        input("Enter a year to see which employees have been working longer than that year"))
    print(Fore.RESET)
    for id, employer in employers.items():
        if year_of_service > employer['year_of_service']:
            employer.update({"id": {"name": employer, "gender": employer, "department": employer,
                                    "year_of_service": employer, "salary": employer}})
            print(id, end="\t")
            for info in employer.values():
                print(info, end="\t\t")
            print("")
    filter_admin()


show_employers()
admin_login()
admin_functions_or_filter()
