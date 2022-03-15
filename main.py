from pkg_validations.validations import validateChoice
from pkg_code.login import login
from pkg_code.register import register

def instructions():
    print("1) Login.")
    print("2) Register.")
    print("3) Exit.")

    choice = input("plz enter a choice number :")
    choice = validateChoice(choice)
    return choice

def myMain():
    print("*******************************************")
    print("******** Crowd-Funding console app ********")
    print("*******************************************")
    while True:
        choice = int(instructions())
        match choice:
            case 1:
                login()
                print("")
            case 2:
                register()
                print("")
            case 3:
                print("*******************************************")
                return

myMain()