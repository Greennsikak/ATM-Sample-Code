import random
import datetime as dt



database = {}

#  Initializing the system
def init():

    print("Welcome to Save-Heaven Platform")

    have_account = int(input("Do you have an account with us? Yes = 1, No = 2 \n"))

    if have_account == 1:
        login()

    elif have_account == 2:
            print(register())

    else:
        print("You have selected an invalid option")
        init()

def login(): 
    print("***** Login into your account *****")

    userAccountNumber = int(input("Please enter your account number. \n"))
    password = input("Enter your password: \n")

    for accountNumber, userDetails in database.items():
        if accountNumber == userAccountNumber:
            if userDetails[3] == password:
                bankOperation(userDetails)


def register():
    print("***** Registration Form *****")

    first_name = input("Enter first name: \n")
    last_name = input("Enter last name: \n")
    email = input("Enter email address: \n")
    password = input("Create password: \n")

    accountNumber = generatingAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Account Created Successfully")
    print("===== * ======= * ===== *")
    print(f"Your account number is {accountNumber}")
    print("Make sure you keep it safe")
    print("===== * ======= * ===== *")


    login()


def generatingAccountNumber():
    return random.randrange(1111111111,9999999999)

def bankOperation(user):
    print(f"Welcome {user[0]} {user[1]}.")

    date = dt.date.today()
    time = dt.datetime.now().time()
    print(f"Date: {date}, Time: {time}")

    print("""
    There are the available options:
    1. Cash Withdrawal
    2. Cash deposit
    3. Complaint
    4. Logout
    5. Exit
    """)

    selected_option = int(input("Please select an option: "))

    if selected_option == 1:
        withdrawerOperation()
        
    elif selected_option == 2:
        depositOperation()

    elif selected_option == 3:
        issuesReport()

    elif selected_option == 4:
        login()

    elif selected_option == 5:
        exit()

    else:
        print("You selected a wrong option. Please try again")
        

def withdrawerOperation():
    cash_amount = int(input("How much would you like the withdraw? "))

    current_balance = 200000

    current_balance -= cash_amount
        
    if cash_amount <= current_balance:
        print("Take your cash")
        print(f"Your avaible balance = {current_balance}")
    else:
        print("Insuffient fund")

def depositOperation():
    cash_deposit = int(input("How much would you like to deposit? "))

    current_balance = 200000 

    current_balance += cash_deposit
    print(f"Your current balance = {current_balance}")
    

def issuesReport():
    issue = input("What issue will you like to report? ")

    print(f"Your issue: {issue} is noted, Thank you for contacting us.")


""" ACTUAl SAVE-HEAVEN PLATFORM """

init()


