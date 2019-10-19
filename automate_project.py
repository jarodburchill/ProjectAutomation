import os
import subprocess
import getpass
import configparser
import webbrowser
import project_types
try:
    from github import Github
except ImportError:
    subprocess.call("pip install PyGithub", shell=True)
    from github import Github
try:
    from colorama import init, Fore
except ImportError:
    subprocess.call("pip install colorama", shell=True)
    from colorama import init, Fore


# makes colorama work on Windows
init()
print(Fore.WHITE)


# config parser set up
config = configparser.ConfigParser()
config.read("script.config")


# global project variables
directory = config.get("DEFAULT", "directory")
projectName = ""
projectType = ""
editor = config.get("DEFAULT", "editor")
defproj = config.get("DEFAULT", "defaultproj")


# global GitHub credentials
repoName = ""
username = config.get("DEFAULT", "username")
password = config.get("DEFAULT", "password")
private = config.get("DEFAULT", "private")


# runs the proccess to run based on the type of project
def RunProjectProcess(projectType):
    project_types.Init(projectName, repoName, directory)
    project_types.types[projectType]()


# gets user input to update GitHub credentials
def GetCredentials():
    global repoName
    global private
    global username
    global password

    if repoName == "":
        repoName = input("Enter a name for the GitHub repository: ")
    if private == "":
        private = input("Private GitHub repository (y/n): ")
    while private != False and private != True:
        if private == "y":
            private = True
        elif private == "n":
            private = False
        else:
            print("{}Invalid value.{}".format(Fore.YELLOW, Fore.WHITE))
            private = input("Private GitHub repository (y/n): ")
    if username == "":
        username = input("Enter your GitHub username: ")
    if username == "" or password == "":
        password = getpass.getpass("Enter your GitHub password: ")


# creates GitHub repo if credentials are valid
def CreateGitHubRepo():
    global repoName
    global private
    global username
    global password
    GetCredentials()
    try:
        user = Github(username, password).get_user()
        user.create_repo(repoName, private=private)
        return True
    except Exception as e:
        repoName = ""
        username = ""
        password = ""
        private = ""
        print(Fore.RED + str(e) + Fore.WHITE)
        return False


def DeleteGitHubRepo():
    global repoName
    global username
    global password
    try:
        user = Github(username, password)
        repo = user.get_repo("{}/{}".format(username, repoName))
        repo.delete()
    except Exception as e:
        print(str(e))
        print("{}Could not delete new repository \'{}\'. Please delete it online.{}".format(
            Fore.RED, repoName, Fore.WHITE))


# loops until there is a valid file path
if not os.path.isdir(directory):
    print("{}Invalid string for the directory option in script.config; please make sure the directory in script.config exists to stop seeing this message in the future.{}".format(
        Fore.RED, Fore.WHITE))
    directory = input("Enter valid local path: ")
    while not os.path.isdir(directory):
        print("{}Invalid local path; please try again.{}".format(
            Fore.YELLOW, Fore.WHITE))
        directory = input("Enter valid local path: ")


# requests user for project name
projectName = input("Project name: ")
repoName = projectName


# loops until there is a valid project name
while os.path.isdir(directory + "\\" + projectName):
    print("{}Project name already exists; please try again.{}".format(
        Fore.YELLOW, Fore.WHITE))
    projectName = input("Project name: ")


# decide project type
if defproj is not "none":
    projectType = defproj
else:
    projectType = input("Project type: ")

# loops until project type is valid
while projectType not in project_types.types:
    print("{}Invalid project type; please try again.{}".format(
        Fore.YELLOW, Fore.WHITE))
    print("Valid project types: ")
    for key, value in project_types.types.items():
        print(Fore.BLUE + key + Fore.WHITE)
    projectType = input("Project type: ")


# loops until GitHub repo has been created successfully
while CreateGitHubRepo() == False:
    print("{}Something went wrong when creating the GitHub repo. See above for more details.{}".format(
        Fore.YELLOW, Fore.WHITE))


try:
    # changes into correct directory and runs the project proccess for the declared project type
    os.chdir(directory)
    RunProjectProcess(projectType)

    # git proccesses
    subprocess.call("git init", shell=True)
    subprocess.call("git add .", shell=True)
    subprocess.call("git commit -m \"initial commit\"", shell=True)
    subprocess.call("git remote add origin https://github.com/{}/{}".format(username, repoName),
                    shell=True)
    subprocess.call("git push -u origin master", shell=True)

    # opens project in editor
    if editor is not "none":
        try:
            subprocess.call("{} .".format(editor), shell=True)
        except Exception as e:
            print("{}No editor found:{} {}".format(
                Fore.RED, Fore.WHITE, str(e)))
    else:
        print("{}No editor selected.{}".format(Fore.YELLOW, Fore.WHITE))
    print("{}Project created succesfully!{}".format(Fore.GREEN, Fore.WHITE))

    # starts a dev server for certain project types
    if projectType == "react" or projectType == "react-ts":
        subprocess.call("npm start", shell=True)
    elif projectType == "laravel":
        webbrowser.open("http://localhost:8000/")
        subprocess.call("php artisan serve", shell=True)
    elif projectType == "vue":
        webbrowser.open("http://localhost:8080/")
        subprocess.call("npm run serve", shell=True)
    elif projectType == "html":
        webbrowser.open("{}\\{}\\index.html".format(directory, projectName))
except Exception as e:
    print("{}There was an error when creating the project:{} {}".format(
        Fore.RED, Fore.WHITE, str(e)))
    DeleteGitHubRepo()
