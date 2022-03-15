from pkg_validations.validations import validateProjectChoice
from pkg_code.createProject import createProject
from pkg_code.viewProjects import viewProjects
from pkg_code.editProjects import editProjects
from pkg_code.searchOnProject import searchOnProject
from pkg_code.deleteProject import deleteProject

def projectsInstructions():
    print("1) create a project.")
    print("2) view all projects.")
    print("3) edit your projects.")
    print("4) delete your project.")
    print("5) search for a project using date.")
    print("6) back.")

    choice = input("plz enter a choice number :")
    choice = validateProjectChoice(choice)
    return choice


def projects(user_id):
    print("")
    print("************************************")
    print("******** Project Operations ********")
    print("************************************")
    while True:
        choice = int(projectsInstructions())
        match choice:
            case 1:
                createProject(user_id)
                print("")
            case 2:
                viewProjects(user_id)
                print("")
            case 3:
                editProjects(user_id)
                print("")
            case 4:
                deleteProject(user_id)
                print("")
            case 5:
                searchOnProject(user_id)
                print("")
            case 6:
                print("************************************")
                return
