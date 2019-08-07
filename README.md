# ProjectAutomation
Python script for creating new projects in the desired local directory, with a GitHub origin.
## Requirements:
- Python 3.x
- Git
- npm
- Visual Studio Code or Atom (recommended)
## Installation:
### Windows:
Clone the repository:
```
cd C:\
git clone https://github.com/jarodburchill/ProjectAutomation
```
Set the environment variable:
```
setx path "%path%;C:\ProjectAutomation\windows"
```
### Mac/Linux:
Clone the repository:
```
cd ~
git clone https://github.com/jarodburchill/ProjectAutomation
```
Set the environment variable:
```
PATH=$PATH:~/ProjectAutomation/mac-linux
```
Make executable:
```
cd ~/ProjectAutomation/mac-linux
chmod +x new-project
```
## Configuration:
Rename the `script.config.example` to `script.config` and edit it according to your needs
### Options and Defaults:
The `localPath` option takes a file path string to determine where new local repositories will be created.
```
localPath = C:/Projects/
```
Mac and Linux users must change local path:
```
localPath = /home/$USER/Projects/
```
#### $USER = your machine's username.  
-----------------------------
The `editor` option takes a string to determine what editor new projects will be opened in after creation.
```
editor = <editor>
```
Currently, only Atom and VScode are supported. Set to `none` if you don't wish to open the repo in an editor.  
  
Editor types: 
``` 
vscode  
atom 
none
```
#### NOTE: If using Atom, open it, select "Atom" and choose "Install Script Commands" before running the script, or Atom will not open!
-----------------------------
The `username` option is blank by default. If a correct GitHub username is entered into this option, the script will not promt the user to enter a username on each run. 
```
username =
```
-----------------------------
The `password` option is blank by default. If a correct GitHub password is entered into this option and the username option has also been provided, the script will not promt the user to enter a password on each run. 
```
password =
```
## Usage:
### Run in Terminal:
```
new-project
```
### Project Types:
Blank repository with a README:
```
blank
```
Create-react-app:
```
react
```
Create-react-app with TypeScript:
```
react-ts
```
## Contributors:
<a href="https://github.com/jarodburchill"><img src="https://avatars.githubusercontent.com/u/37840393?v=3" title="jarodburchill" width="80" height="80"></a>
<a href="https://github.com/ajnieset"><img src="https://avatars.githubusercontent.com/u/40476295?v=3" title="ajnieset" width="80" height="80"></a>
<a href="https://github.com/rexogamer"><img src="https://avatars.githubusercontent.com/u/42586271?v=3" title="rexogamer" width="80" height="80"></a>
## License:
MIT © [Jarod Burchill](http://burchilldevelopment.com)
