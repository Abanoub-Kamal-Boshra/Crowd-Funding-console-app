from pkg_validations.validations import validateExtractEmail
from pkg_validations.validations import validatePassword
from pkg_code.fileHandler import checkUserExistence
from pkg_code.projects import projects
from pkg_code.fileHandler import getUserId

def login():
    email = input("plz enter your email :")
    email = validateExtractEmail(email)

    password = input("plz enter a password :")
    password = validatePassword(password)

    if checkUserExistence(email, password):
        print("Logged in successfully.")
        return projects(getUserId(email))

    print("plz enter correct credentials!")
    return login()