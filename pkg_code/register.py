from pkg_validations.validations import validateName
from pkg_validations.validations import validateEmail
from pkg_validations.validations import validatePassword
from pkg_validations.validations import confirmPassword
from pkg_validations.validations import validatePhoneNumber
from pkg_code.fileHandler import insert
from pkg_code.fileHandler import getNextId

def register():
    fname = input("plz enter your first name :")
    fname = validateName(fname)

    lname = input("plz enter your last name :")
    lname = validateName(lname)

    email = input("plz enter your email :")
    email = validateEmail(email)

    password = input("plz enter a password :")
    password = validatePassword(password)
    confirmPass = input("plz confirm a password :")
    confirmPassword(password, confirmPass)

    phone = input("plz enter your phone number :")
    phone = validatePhoneNumber(phone)

    id = getNextId()
    info = [id, fname, lname, email, password, phone]
    user_info = ":".join(info)
    insert(user_info)
