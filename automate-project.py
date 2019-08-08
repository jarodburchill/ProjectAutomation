import os
import subprocess
import getpass
import configparser
from github import Github


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


# proccess for blank projects
def Blank():
    os.mkdir(projectName)
    os.chdir(projectName)
    subprocess.run(f"echo {repoName} >> README.md", shell=True)


# process for react projects
def React():
    subprocess.run(f"npx create-react-app {projectName}", shell=True)
    os.chdir(projectName)


# process for react typescript projects
def ReactTS():
    subprocess.run(
        f"npx create-react-app {projectName} --typescript", shell=True)
    os.chdir(projectName)


# project types dict with values for correct process function
types = {
    'blank': Blank,
    'react': React,
    'react-ts': ReactTS
}


# runs the proccess to run based on the type of project
def RunProjectProcess(projectType):
    types[projectType]()


# gets user input to update GitHub credentials
def GetCredentials():
    global repoName
    global username
    global password
    repoName = input("Enter a name for the new GitHub repository: ")
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


# loops until project type is valid
while projectType not in types:
    print(bcolors.WARNING + "Invalid project type; please try again." + bcolors.ENDC)
    print("Valid project types: ")
    for key, value in types.items():
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
editor = config.get("DEFAULT", "editor")

if editor is not "none":
    try:
        subprocess.run(f"{editor} .", shell=True)
    except Exception as e:
        print(bcolors.FAIL + "No editor found. ERROR: " + bcolors.ENDC + e)
else:
    print(bcolors.WARNING + "No editor selected." + bcolors.ENDC)
print(bcolors.OKGREEN + "Project created succesfully!" + bcolors.ENDC)

# starts dev server for react projects
if projectType == 'react' or projectType == 'react-ts':
    subprocess.run("npm start", shell=True)
