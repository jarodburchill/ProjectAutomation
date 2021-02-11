import os
import subprocess
import shutil


# global variables
projectName = ""
repoName = ""
directory = ""


# gets variables from main script
def Init(project, repo, dirPath):
    global projectName
    global repoName
    global directory
    projectName = project
    repoName = repo
    directory = dirPath


# proccess for blank projects
def Blank():
    os.mkdir(projectName)
    os.chdir(projectName)
    subprocess.check_call("echo {} >> README.md".format(repoName), shell=True)


# process for html projects
def Html():
    scriptPath = os.path.dirname(os.path.realpath(__file__))
    src = "{}\\assets\\html\\".format(scriptPath)
    dst = "{}\\{}\\".format(directory, projectName)
    shutil.copytree(src, dst)
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
    try:
        import pyscaffold
    except ImportError:
        subprocess.call("pip install pyscaffold", shell=True)

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


# process for vue projects
def Vue():
    subprocess.check_call("vue create {}".format(projectName), shell=True)
    os.chdir(projectName)


# process for electron projects
def Electron():
    subprocess.check_call("npx create-electron-app {}".format(projectName), shell=True)
    os.chdir(projectName)


# project types dict with values for correct process function
types = {
    'blank': Blank,
    'html': Html,
    'react': React,
    'react-ts': ReactTS,
    'node': Node,
    'python': Python,
    'express': Express,
    'laravel': Laravel,
    'vue': Vue,
    'electron': Electron
}
