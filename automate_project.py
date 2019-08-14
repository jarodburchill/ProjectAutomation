import os
import subprocess
import getpass
import configparser
import project_types
from github import Github
from colorama import init, Fore


# makes colorama work on Windows
init()
print(Fore.WHITE)


# config parser set up
config = configparser.ConfigParser()
config.read("script.config")


# global project variables
localPath = config.get("DEFAULT", "localPath")
projectName = ""
projectType = ""
editor = config.get("DEFAULT", "editor")


# global GitHub credentials
repoName = ""
username = config.get("DEFAULT", "username")
password = config.get("DEFAULT", "password")


# runs the proccess to run based on the type of project
def RunProjectProcess(projectType):
    project_types.Init(projectName, repoName)
    project_types.types[projectType]()


# gets user input to update GitHub credentials
def GetCredentials():
    global repoName
    global username
    global password
    repoName = input("Enter a name for the GitHub repository: ")
    if (username == ""):
        username = input("Enter your GitHub username: ")
    if (username == "" or password == ""):
        password = getpass.getpass("Enter your GitHub password: ")


# creates GitHub repo if credentials are valid
def CreateGitHubRepo():
    global repoName
    global username
    global password
    GetCredentials()
    try:
        user = Github(username, password).get_user()
        repo = user.create_repo(repoName)
        return True
    except Exception as e:
        username = ""
        password = ""
        if repo != None:
            try:
                repo.delete()
            except:
                print(Fore.RED)
                print("Could not delete new repository")
                print(Fore.WHITE)
        print(Fore.RED)
        print(e)
        print(Fore.WHITE)
        return False


# loops until there is a valid file path
if not os.path.isdir(localPath):
    print(Fore.RED + "Invalid string for the localPath option in script.config; please make sure " +
          "the localPath in script.config exists to stop seeing this message in the future." + Fore.WHITE)
    localPath = input("Enter valid local path: ")
    while not os.path.isdir(localPath):
        print(Fore.YELLOW + "Invalid local path; please try again." + Fore.WHITE)
        localPath = input("Enter valid local path: ")


# requests user for project name
projectName = input("Project name: ")


# loops until there is a valid project name
while os.path.isdir(localPath + "\\" + projectName):
    print(Fore.YELLOW +
          "Project name already exists; please try again." + Fore.WHITE)
    projectName = input("Project name: ")


# requests user for project type
projectType = input("Project type: ")


# loops until project type is valid
while projectType not in project_types.types:
    print(Fore.YELLOW + "Invalid project type; please try again." + Fore.WHITE)
    print("Valid project types: ")
    for key, value in project_types.types.items():
        print(Fore.BLUE + key + Fore.WHITE)
    projectType = input("Project type: ")


# loops until GitHub repo has been created successfully
while CreateGitHubRepo() == False:
    print(Fore.YELLOW +
          "Something went wrong when creating the GitHub repo. See above for more details." + Fore.WHITE)


try:
    # changes into correct directory and runs the project proccess for the declared project type
    os.chdir(localPath)
    RunProjectProcess(projectType)

    # git proccesses
    subprocess.run("git init", shell=True)
    subprocess.run("git add .", shell=True)
    subprocess.run("git commit -m \"initial commit\"", shell=True)
    subprocess.run(
        f"git remote add origin https://github.com/{username}/{repoName}",
        shell=True)
    subprocess.run("git push -u origin master", shell=True)

    # opens project in editor
    if editor is not "none":
        try:
            subprocess.run(f"{editor} .", shell=True)
        except Exception as e:
            print(Fore.RED + "No editor found: " + Fore.WHITE + e)
    else:
        print(Fore.YELLOW + "No editor selected." + Fore.WHITE)
    print(Fore.GREEN + "Project created succesfully!" + Fore.WHITE)

    # starts dev server for react projects
    if projectType == 'react' or projectType == 'react-ts':
        subprocess.run("npm start", shell=True)
except Exception:
    print(Fore.RED + "There was an error when creating the project. " +
          "See above for more details." + Fore.WHITE)
    if username != "" and password != "":
        try:
            user = Github(username, password)
            repo = user.get_repo(repoName)
            repo.delete()
        except:
            print(f"{Fore.RED}Could not delete new repository \'{repoName}\'. Please try again or delete it online. {Fore.WHITE}")
