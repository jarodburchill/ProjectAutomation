import os
import subprocess
import getpass
import configparser
import project_types
from github import Github


# makes the ANSI colors work on Windows (known Python bug)
subprocess.run("", shell=True)


# common ANSI console colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


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
        user.create_repo(repoName)
        return True
    except Exception as e:
        username = ""
        password = ""
        print(bcolors.FAIL)
        print(e)
        print(bcolors.ENDC)
        return False


# loops until there is a valid file path
if not os.path.isdir(localPath):
    print(bcolors.FAIL + "Invalid string for the localPath option in script.config; please make sure " +
          "the localPath in script.config exists to stop seeing this message in the future." + bcolors.ENDC)
    localPath = input("Enter valid local path: ")
    while not os.path.isdir(localPath):
        print(bcolors.WARNING + "Invalid local path; please try again." + bcolors.ENDC)
        localPath = input("Enter valid local path: ")


# requests user for project name
projectName = input("Project name: ")


# loops until there is a valid project name
while os.path.isdir(localPath + "\\" + projectName):
    print(bcolors.WARNING +
          "Project name already exists; please try again." + bcolors.ENDC)
    projectName = input("Project name: ")


# requests user for project type
projectType = input("Project type: ")


# loops until project type is valid
while projectType not in project_types.types:
    print(bcolors.WARNING + "Invalid project type; please try again." + bcolors.ENDC)
    print("Valid project types: ")
    for key, value in project_types.types.items():
        print(bcolors.OKBLUE + key + bcolors.ENDC)
    projectType = input("Project type: ")


# loops until GitHub repo has been created successfully
while CreateGitHubRepo() == False:
    print(bcolors.WARNING +
          "Something went wrong when creating the GitHub repo. See above for more details." + bcolors.ENDC)


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
        print(bcolors.FAIL + "No editor found: " + bcolors.ENDC + e)
else:
    print(bcolors.WARNING + "No editor selected." + bcolors.ENDC)
print(bcolors.OKGREEN + "Project created succesfully!" + bcolors.ENDC)


# starts dev server for react projects
if projectType == 'react' or projectType == 'react-ts':
    subprocess.run("npm start", shell=True)
