import pkg_validations.validations

#project_info = [user_id, project_id, title, details, target, sdate, edate]
#user_info = [id, fname, lname, email, password, phone]
def insert(info):
    try:
        dataFile = open("pkg_data/users_data.txt", "a")
    except Exception as e:
        print(f"{e}")
    else:
        data = info.strip("\n")
        data = f"{data}\n"
        dataFile.write(data)
        dataFile.close()

def checkUserExistence(email , passwd):
    try:
        dataFile = open("pkg_data/users_data.txt", "r")
    except Exception as e:
        print(f"{e}")
    else:
        users = dataFile.readlines()
        for user in users:
            user_info = user.split(":")
            if user_info[3] == email and user_info[4] == passwd:
                dataFile.close()
                return True

        dataFile.close()
        return False


def checkEmailExistence(email):
    try:
        dataFile = open("pkg_data/users_data.txt", "r")
    except Exception as e:
        print(f"{e}")
    else:
        users = dataFile.readlines()
        for user in users:
            user_info = user.split(":")
            if user_info[3] == email:
                dataFile.close()
                return True

        dataFile.close()
        return False

def getNextId():
    id = ""
    try:
        dataFile = open("pkg_data/users_data.txt", "r")
    except Exception as e:
        print(f"{e}")
    else:
        users = dataFile.readlines()
        for user in users:
            user_info = user.split(":")
            id = user_info[0]
            dataFile.close()
        if id == "":  #this to handle the first user in the projects
            id = "0"
        else:
            id = str(int(id)+1)
        return id

def getUserId(email):
    try:
        dataFile = open("pkg_data/users_data.txt", "r")
    except Exception as e:
        print(f"{e}")
    else:
        users = dataFile.readlines()
        for user in users:
            user_info = user.split(":")
            if email == user_info[3]:
                id = user_info[0]
                dataFile.close()
                return id

def insertProjectInfo(project_info):
    try:
        dataFile = open("pkg_data/projects_data.txt", "a")
    except Exception as e:
        print(f"{e}")
    else:
        data = project_info.strip("\n")
        data = f"{data}\n"
        dataFile.write(data)
        dataFile.close()

def showAllProjectsFor(user_id):
    try:
        dataFile = open("pkg_data/projects_data.txt", "r")
        counter = 1
    except Exception as e:
        print(f"{e}")
    else:
        projects = dataFile.readlines()
        print("")
        for project in projects:
            project = project.split(":")
            if project[0] == user_id:
                print(f"\tthe poroject :{counter}")
                print(f"the title :{project[2]}.")
                print(f"details :{project[3]}.")
                print(f"the total target :{project[4]} EGP.")
                print(f"the start date :{project[5]}")
                print(f"the end date :{project[6]}")
                counter += 1

        dataFile.close()

def checkTitleExistence(title):
    try:
        dataFile = open("pkg_data/projects_data.txt", "r")
    except Exception as e:
        print(f"{e}")
    else:
        projects = dataFile.readlines()
        for project in projects:
            project = project.split(":")
            if project[2] == title:
                return True
        dataFile.close()
        return False

def checkExistenceProjectId(project_id):
    try:
        dataFile = open("pkg_data/projects_data.txt", "r")
    except Exception as e:
        print(f"{e}")
    else:
        projects = dataFile.readlines()
        for project in projects:
            project = project.split(":")
            if project[1] == project_id:
                return True
        dataFile.close()
        return False

def editProjectOf(copy_projact_id):
    try:
        dataFile = open("pkg_data/projects_data.txt", "r+")
    except Exception as e:
        print(f"{e}")
    else:
        projects = dataFile.readlines()
        index = 0
        for project in projects:
            project = project.split(":")
            # [user_id, title, details, target, sdate, edate]
            if project[1] == copy_projact_id:
                title = input("plz enter the new title :")
                title = pkg_validations.validations.validateName(title)
                project[2] = title

                details = input("plz enter the new details :")
                details = pkg_validations.validations.validateSentence(details)
                project[3] = details

                target = input("plz enter the new total target :")
                target = pkg_validations.validations.validateNumber(target)
                project[4] = target

                sdate = input("plz enter the new start date in format YYYY-MM-DD :")
                sdate = pkg_validations.validations.validateDate(sdate)
                project[5] = sdate
                edate = input("plz enter the new end date in format YYYY-MM-DD :")
                edate = pkg_validations.validations.validateDate(edate)
                project[6] = edate

                project = ":".join(project)
                projects[index] = project
            index += 1

        dataFile.truncate(0)  # need '0' when using r+
        for project in projects:
            data = project.strip("\n")
            dataFile.write(f"{data}\n")
        dataFile.close()
    return