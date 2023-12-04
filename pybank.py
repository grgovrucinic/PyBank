# SIMULACIJA BANKOVNOG RAČUNA - PyBank

import datetime
import os

# -------------------------------------
# Global variable
# -------------------------------------

# Company information
company_name = ""
company_street_and_number = ""
company_postal_code = ""
company_city = ""
company_tax_id = ""
company_manager = ""

# Currency information
currency = "eur"

# Account information
# Account number format: BA-YEAR-MONTH-ID (5 digit ID)
account_id = 1
account_number = ""
account_balance = 0.00

# Transaction information
transaction_id = 0
transactions = {}


# -------------------------------------
# Functions
# -------------------------------------

def main_menu() -> int:
    """Prints main menu and returns user's choice.

    Returns:
        int: User's choice - 1, 2, 3, 4, 5 or 0
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    choice = -1
    global account_number

    print("*" * 65)
    print("PyBank Algebra\n".center(65))
    print("GLAVNI IZBORNIK\n".center(65))

    if account_number == "":
        print("1. Kreiranje računa")
    else:
        print("1. Ažuriranje računa")

    print("2. Prikaz stanja računa")
    print("3. Prikaz prometa po računu")
    print("4. Polog novca na račun")
    print("5. Podizanje novca s računa")

    print("0. izlaz")

    print("_" * 65)
    if account_number == "":
        while choice != 1 and choice != 0:
            print("Još niste otvorili račun. Molimo prvo kreirajte račun. Hvala!")
            print("_" * 65)
            choice = int(input("Vaš izbor:\t"))
    else:
        print("Molimo Vas upišite samo broj ispred opcije koju želite odabrati")
        print("_" * 65)
        choice = int(input("Vaš izbor:\t"))

    return choice


def open_account():
    """Creates a new company bank account.

    Returns:
        Information of our new bank memeber, company name, adress, postal code, city, persoanl identifying number, name of the company manager and currency of choice.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('KREIRANJE RACUNA\n'.center(65))
    print('Podaci o vlasniku racuna\n'.center(65))

    global company_name
    global company_street_and_number 
    global company_postal_code
    global company_city
    global company_tax_id
    global company_manager
    global currency
    global transactions
    global account_balance

    company_name = input('Naziv Tvrtke:\t\t\t\t')
    company_street_and_number = input('Ulica i broj sjedista Tvrtke:\t\t')
    company_postal_code = input('Postanski broj sjedista Tvrtke:\t\t')
    company_city = input('Grad u kojem je sjediste Tvrtke:\t')
    while True:
        company_tax_id = input('OIB Tvrtke:\t\t\t\t')
        if len(company_tax_id) != 11 and company_tax_id.isdigit():
            print('OIB mora imati tocno 11 znamenki i moraju biti samo brojke.\nMolimo Vas ponovite unos\n')
        else:
            break
    company_manager = input('Ime i prezime odgovorne osobe Tvrtke:\t')
    currency = input('Upisite naziv valute racuna (EUR ili HRK):\t')
    if currency.upper() == 'HRK':
        currency = ' hr'
    else:
        currency = ' €'

    input('\nSPREMI? (Pritisnite bilo koju tipku) ')

    os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('KREIRANJE RACUNA\n'.center(65))
    print(f'Podaci o vlasniku racuna tvrtke {company_name}, su uspjesno spremljeni.')
    input('Za nastavak pritisnite bilo koju tipku\t')

    os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('KREIRANJE RACUNA\n'.center(65))
    print('Stanje racuna\n'.center(65), '\n')

    print(f'Broj racuna {generate_account_number()}')
    print(f'Trenutno stanje racuna:\t{account_balance:.2f}{currency}\n')

    print('Molimo Vas upisite iznos koji zelite poloziti na racun.\nNAPOMENA Molimo Vas koristite decimalnu tocku, a ne zarez.\n')

    amount = float(input('\t'))

    transaction = {}
    account_balance += amount

    # -----------------------------------
    # Transaction
    # {ID: {date, time, amount, amount balance, account number, description, manager}}
    # -----------------------------------
    transaction["date"] = datetime.date.today()
    transaction["time"] = datetime.datetime.now().time()
    transaction["amount"] = amount
    transaction["account balance"] = account_balance
    transaction["account number"] = account_number
    transaction["description"] = 'Polog kod otvaranja racuna'
    transaction["manager"] = company_manager
    transactions[transaction_id + 1] = transaction


def update_account():
    """Updates an already made account bank account.

    Returns:
        Updated information on our bank account without changing its account number.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('AZURIRANJE RACUNA\n'.center(65))
    print('Podaci o vlasniku racuna\n'.center(65))

    global company_name
    global company_street_and_number 
    global company_postal_code
    global company_city
    global company_tax_id
    global company_manager
    global currency
    global transactions
    global account_balance

    company_name = input('Naziv Tvrtke:\t\t\t\t')
    company_street_and_number = input('Ulica i broj sjedista Tvrtke:\t\t')
    company_postal_code = input('Postanski broj sjedista Tvrtke:\t\t')
    company_city = input('Grad u kojem je sjediste Tvrtke:\t')
    while True:
        company_tax_id = input('OIB Tvrtke:\t\t\t\t')
        if len(company_tax_id) != 11 and company_tax_id.isdigit():
            print('OIB mora imati tocno 11 znamenki i moraju biti samo brojke.\nMolimo Vas ponovite unos\n')
        else:
            break
    company_manager = input('Ime i prezime odgovorne osobe Tvrtke:\t')
    currency = input('Upisite naziv valute racuna (EUR ili HRK):\t')
    if currency.upper() == 'HRK':
        currency = ' hr'
    else:
        currency = ' €'

    input('\nSPREMI? (Pritisnite bilo koju tipku) ')

    os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('AZURIRANJE RACUNA\n'.center(65))
    print(f'Podaci o vlasniku racuna tvrtke {company_name}, su uspjesno spremljeni.')
    input('Za nastavak pritisnite bilo koju tipku\t')
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('AZURIRANJE RACUNA\n'.center(65))
    print('Stanje racuna\n'.center(65), '\n')

    print(f'Broj racuna {account_number}')
    print(f'Trenutno stanje racuna:\t{account_balance:.2f}{currency}\n')

    print('Molimo Vas upisite iznos koji zelite poloziti na racun.\nNAPOMENA Molimo Vas koristite decimalnu tocku, a ne zarez.\n')

    amount = float(input('\t'))

    transaction = {}
    account_balance += amount

    # -----------------------------------
    # Transaction
    # {ID: {date, time, amount, amount balance, account number, description, manager}}
    # -----------------------------------
    transaction["date"] = datetime.date.today()
    transaction["time"] = datetime.datetime.now().time()
    transaction["amount"] = amount
    transaction["account balance"] = account_balance
    transaction["account number"] = account_number
    transaction["description"] = 'Polog kod azuriranja racuna'
    transaction["manager"] = company_manager
    transactions[int(list(transactions)[-1]) + 1] = transaction


def generate_account_number() -> str:
    """Returns account number.

    Returns:
        str: Account number in 'BA-YYYY-MM-00001' format
    """
    global account_id
    global account_number

    year = datetime.datetime.now().year
    month = datetime.datetime.now().month

    # Ensure two digits for month
    month = f"{month:0>2}"

    # Ensure five digit for ID
    id = f"{account_id:0>5}"
    account_id += 1

    account_number = f"BA-{year}-{month}-{id}"
    return account_number


def display_account_balance():
    """Displays current account balance of created bank account.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('PRIKAZ STANJA RACUNA\n'.center(65))

    global account_number
    global account_balance
    global currency

    date = datetime.datetime.now().today()

    print(f'Broj racuna:\t\t{account_number}')
    print(f'Datum i vrijeme:\t{date}\n')

    print(f'Trenutno stanje na racunu:\t{account_balance} {currency}\n')

    print("_" * 65)
    input('Za Povratak na Glavni izbornik pritisnite bilo koju tipku\t')






def display_transaction_history():
    """Displays all transactions of our current bank account.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('POVIJEST TRANSAKCIJA\n'.center(65))

    global transactions

    for id, transaction_details in transactions.items():
        print(f"ID: {id}")
        for key, value in transaction_details.items():
            print(f"\t{key.capitalize()}: {value}")

    input('\nNASTAVITI? (Pritisnite bilo koju tipku) ')






def add_to_account_balance():
    """Making a deposit on our current account.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    global transactions
    global account_balance

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('UPLATA NA RACUN\n'.center(65))

    print('Molimo Vas upisite iznos koji zelite uplatiti na racun.\nNAPOMENA Molimo Vas koristite decimalnu tocku, a ne zarez.\n')

    amount = float(input('\t'))

    transaction = {}
    account_balance += amount

    # -----------------------------------
    # Transaction
    # {ID: {date, time, amount, amount balance, account number, description, manager}}
    # -----------------------------------
    transaction["date"] = datetime.date.today()
    transaction["time"] = datetime.datetime.now().time()
    transaction["amount"] = amount
    transaction["account balance"] = account_balance
    transaction["account number"] = account_number
    transaction["description"] = 'Polog kod uplate na racun'
    transaction["manager"] = company_manager
    transactions[int(list(transactions)[-1]) + 1] = transaction






def remove_from_account_balance():
    """Making a withdraw from our current bank account.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    global transactions
    global account_balance

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('ISPLATA SA RACUNa\n'.center(65))

    print('Molimo Vas upisite iznos koji zelite skinuti sa racuna.\nNAPOMENA Molimo Vas koristite decimalnu tocku, a ne zarez.\n')

    amount = float(input('\t'))

    transaction = {}
    account_balance -= amount

    # -----------------------------------
    # Transaction
    # {ID: {date, time, amount, amount balance, account number, description, manager}}
    # -----------------------------------
    transaction["date"] = datetime.date.today()
    transaction["time"] = datetime.datetime.now().time()
    transaction["amount"] = amount
    transaction["account balance"] = account_balance
    transaction["account number"] = account_number
    transaction["description"] = 'Polog kod uplate na racun'
    transaction["manager"] = company_manager
    transactions[int(list(transactions)[-1]) + 1] = transaction


# -------------------------------------
# Main program
# -------------------------------------

choice = main_menu()

while choice != 0:
    if choice == 1 and account_number == "":
        open_account()
    elif choice == 1 and account_number != "":
        update_account()
    elif choice == 2:
        display_account_balance()
    elif choice == 3:
        display_transaction_history()
    elif choice == 4:
        add_to_account_balance()
    elif choice == 5:
        remove_from_account_balance()

    choice = main_menu()
