from pkg_validations.validations import validateName
from pkg_validations.validations import validateSentence
from pkg_validations.validations import validateNumber
from pkg_validations.validations import validateDate
from pkg_code.fileHandler import insertProjectInfo
from pkg_validations.validations import validateProjectId

def createProject(user_id):
    project_id = input("plz enter the project id :")
    project_id = validateProjectId(project_id)

    title = input("plz enter the project title :")
    title = validateName(title)

    details = input("plz enter the project details :")
    details = validateSentence(details)

    target = input("plz enter the project total target :")
    target = validateNumber(target)

    sdate = input("plz enter a start date in format YYYY-MM-DD :")
    sdate = validateDate(sdate)
    edate = input("plz enter an end date in format YYYY-MM-DD :")
    edate = validateDate(edate)

    user_id = str(user_id)
    info = [user_id, project_id, title, details, target, sdate, edate]
    project_info = ":".join(info)
    insertProjectInfo(project_info)
    return