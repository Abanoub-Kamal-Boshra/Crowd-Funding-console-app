from pkg_validations.validations import validateExtractTitle
from pkg_code.fileHandler import editProjectOf
from pkg_code.fileHandler import checkExistenceProjectId

def editProjects(user_id):
    # title = input("plz enter the title of the project wanted :")
    # title = validateExtractTitle(title)
    # editProjectOf(title)
    project_id = input("plz enter the project id :")
    if checkExistenceProjectId(project_id):
        editProjectOf(project_id)
    return