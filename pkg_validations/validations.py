import re
import datetime
from pkg_code.fileHandler import checkEmailExistence
from pkg_code.fileHandler import checkTitleExistence
from pkg_code.fileHandler import checkExistenceProjectId

def validateChoice(num):
    while True:
        if not num.isdigit():
            num = input("plz enter a valid choice :")
        else:
            num = int(num)
            if 1 <= num <= 3:
                return num
            else:
                num = input("plz enter a valid choice :")

def validateProjectChoice(num):
    while True:
        if not num.isdigit():
            num = input("plz enter a valid choice :")
        else:
            num = int(num)
            if 1 <= num <= 6:
                return num
            else:
                num = input("plz enter a valid choice :")

def validateName(name):
    while True:
        if not name.isalpha():
            name = input("plz enter a valid input :")
        else:
            return name

def validateExtractTitle(title):
    while True:
        if not title.isalpha():
            title = input("plz enter a valid input :")
        else:
            if checkTitleExistence(title):
                return title
            else:
                title = input("plz enter an exist title :")

def validateNumber(num):
    while True:
        if not num.isdigit():
            num = input("plz enter a valid number :")
        else:
            return num


def validateSentence(string):
    while True:
        if string == "":
            string = input("plz enter a details :")
        else:
            return string

mailregex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def validateEmail(mail):
    while True:
        if not re.fullmatch(mailregex, mail):
            mail = input("plz enter a valid mail :")
        else:
            if checkEmailExistence(mail):
                print("this email is already exist!")
                mail = input("plz enter another mail :")
            else:
                return mail

def validateExtractEmail(mail):
    while True:
        if not re.fullmatch(mailregex, mail):
            mail = input("plz enter a valid mail :")
        else:
            if not checkEmailExistence(mail):
                print("this email isn't exist!")
                mail = input("plz enter another email :")
            else:
                return mail

passregex = r'[A-Za-z0-9@#$%^&+=]{8,}'
def validatePassword(passwd):
    while True:
        if not re.fullmatch(passregex, passwd):
            passwd = input("plz enter a valid password :")
        else:
            return passwd


def confirmPassword(passwd, confirmPass):
    while True:
        if passwd != confirmPass:
            confirmPass = input("plz enter the same password:")
        else:
            return True

phoneregex = r'^01[0125]\d{1,8}$'
def validatePhoneNumber(phone):
    while True:
        if not re.fullmatch(phoneregex, phone):
            phone = input("plz enter a valid phone number :")
        else:
            return phone

def validateDate(date):
    while True:
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except Exception as e:
            date = input("plz enter the date in format YYYY-MM-DD :")
        else:
            return date

def validateProjectId(project_id):
    while True:
        project_id = validateNumber(project_id)
        if checkExistenceProjectId(project_id):
            project_id = input("plz enter anothor project id :")
        else:
            return project_id

