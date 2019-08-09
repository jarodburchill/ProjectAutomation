import os
import subprocess


# global variables
projectName = ""
repoName = ""


# gets variables from main script
def Init(project, repo):
    global projectName
    global repoName
    projectName = project
    repoName = repo


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
