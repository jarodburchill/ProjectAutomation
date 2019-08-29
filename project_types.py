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
    subprocess.check_call("echo {} >> README.md".format(repoName), shell=True)


# process for react projects
def React():
    subprocess.check_call(
        "npx create-react-app {}".format(projectName), shell=True)
    os.chdir(projectName)


# process for react typescript projects
def ReactTS():
    subprocess.check_call(
        "npx create-react-app {} --typescript".format(projectName), shell=True)
    os.chdir(projectName)


# process for nodejs projects
def Node():
    Blank()
    subprocess.check_call("npm init", shell=True)


# process for python projects
def Python():
    subprocess.check_call("putup {}".format(projectName), shell=True)
    os.chdir(projectName)


# process for expressjs projects
def Express():
    Node()
    subprocess.check_call("npm install express --save", shell=True)


# process for laravel projects
def Laravel():
    subprocess.check_call("laravel new {}".format(projectName), shell=True)
    os.chdir(projectName)
    subprocess.check_call("php artisan serve", shell=True)


def Vue():
    subprocess.check_call("vue create {}".format(projectName), shell=True)
    os.chdir(projectName)
    subprocess.check_call("npm run serve", shell=True)


# project types dict with values for correct process function
types = {
    'blank': Blank,
    'react': React,
    'react-ts': ReactTS,
    'node': Node,
    'python': Python,
    'express': Express,
    'laravel': Laravel,
    'vue': Vue
}
