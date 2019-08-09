import os
import subprocess
import automate_project


# init automate_project module for variable use
script = automate_project


# proccess for blank projects
def Blank():
    os.mkdir(script.projectName)
    os.chdir(script.projectName)
    subprocess.run(f"echo {script.repoName} >> README.md", shell=True)


# process for react projects
def React():
    subprocess.run(f"npx create-react-app {script.projectName}", shell=True)
    os.chdir(script.projectName)


# process for react typescript projects
def ReactTS():
    subprocess.run(f"npx create-react-app {script.projectName} --typescript", shell=True)
    os.chdir(script.projectName)

    
# process for nodejs projects
def NodeJS():
    subprocess.run(f"npm init {script.projectName}", shell=True)
    od.chdir(script.projectName)

    
# project types dict with values for correct process function
types = {
    'blank': Blank,
    'react': React,
    'react-ts': ReactTS
    'node-js': NodeJS
}
