import os
import subprocess
import getpass
import configparser
from github import Github
import json


# Makes the ANSI colors work on Windows (known Python bug)
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
projectName = input("Project name: ")
projectType = input("Project type: ")


# global GitHub credentials
repoName = ""
username = config.get("DEFAULT", "username")
password = config.get("DEFAULT", "password")

# project types dict with values for correct process function
types = []
for file in os.listdir('languages'):
    types.append(file.replace('.json', ''))

jsonVars = {
    '{projectName}': projectName,
    '{repoName}': repoName
}

# runs the proccess to run based on the type of project
def RunProjectProcess(projectType):
    print(type(projectType), projectType)
    try:
        with open(f'./languages/{projectType}.json') as file:
            raw = json.load(file)
            cmd = raw['cmd']
            for key, value in jsonVars.items():
                if cmd.find(key) != -1:
                    cmd = cmd.replace(key, value)
            # changes into correct directory and runs the project proccess for the declared project type
            os.chdir(localPath)
            subprocess.run(cmd, shell=True)
    except FileNotFoundError:
        # This should never happen
        print(bcolors.FAIL + "An internal error occurred" + bcolors.ENDC)

# gets user input to update GitHub credentials
def GetCredentials():
    global repoName
    global username
    global password
    repoName = input("Enter new GitHub repository name: ")
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
        # user.create_repo(repoName)
        return True
    except Exception as e:
        username = ""
        password = ""
        print(bcolors.FAIL)
        print(e)
        print(bcolors.ENDC)
        return False


# loops until project type is valid
while projectType not in types:
    print(bcolors.WARNING + "Invalid project type, please try again." + bcolors.ENDC)
    print("Valid project types: ")
    projectType = input("Project type: ")


# loops until GitHub repo has been created successfully
while CreateGitHubRepo() == False:
    print(bcolors.WARNING +
          "Something went wrong when creating the GitHub repo. See above for more details." + bcolors.ENDC)

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
if config.get("DEFAULT", "editor") == "vscode":
    subprocess.run("code .", shell=True)
elif config.get("DEFAULT", "editor" == "atom"):
    subprocess.run("atom .", shell=True)
elif config.get("DEFAULT", "editor" == "none"):
    print("No editor selected.")
else:
    print(bcolors.WARNING + "Editor unknown. Please consult config.script.")

print(bcolors.OKGREEN + "Project created successfully!" + bcolors.ENDC)


# Post project creation commands
os.chdir(localPath + f"\{projectName}")
try:
    with open(f'./languages/{projectType}.json') as file:
        cmd = json.load(file)['post-cmd']
        subprocess.run(cmd, shell=True)
except FileNotFoundError:
    print("An internal error occurred")
