# ProjectAutomation
Python script for creating new projects in the desired local directory, with a GitHub origin.  
  
Contact us [on Discord.](https://discord.gg/eqWstJu)
## Requirements:
#### Universal
- Python 3.4+
- Git
- A text editor i.e. VS Code, Atom, etc. (Optional but recommended.)
#### React/Node.js/Express.js
- npm
#### Laravel
- Laravel
- Composer
- PHP
- serve
#### Vue
- Vue CLI
- serve
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
All configuration options can be found in the `script.config` file.
### Options and Defaults:
The `directory` option takes a file path string to determine where new local repositories will be created.  
  
Default path for Windows users, change as required:
```
directory = C:/Projects/
```
Linux users must change the local path:
```
directory = /home/$USER/Projects/
```
Mac users must change the local path:
```
directory = /Users/$USER/Projects/
```
#### $USER = your machine's username. YOU MUST CHANGE THIS!  
-----------------------------
The `editor` option takes a string to determine what editor new projects will be opened in after creation.
```
editor = <editor>
```
Any editor that is installed on your local machine is supported (provided it has a command line command to open). Set to `none` if you don't wish to open the repo in an editor.
#### See EDITORS.md for a list of editors.
-----------------------------
The `username` option is blank by default. If a correct GitHub username is entered into this option, the script will not prompt you to enter a username on each run.  
```
username = <username>
```
-----------------------------
The `password` option is blank by default. If a correct GitHub password is entered into this option and the username option has also been provided, the script will not prompt you to enter a password on each run.  
```
password = <password>
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
Node.js project:
```
node
```
#### For lots of config options, [see the pyscaffold README.](https://github.com/pyscaffold/pyscaffold#configuration--packaging)
Python project:
```
python
```
Express.js project:
```
express
```
Laravel project:
```
laravel
```
Vue project:
```
vue
```
## Contributors:
<a href="https://github.com/jarodburchill"><img src="https://avatars.githubusercontent.com/u/37840393?v=3" title="jarodburchill" width="80" height="80"></a>
<a href="https://github.com/ajnieset"><img src="https://avatars.githubusercontent.com/u/40476295?v=3" title="ajnieset" width="80" height="80"></a>
<a href="https://github.com/rexogamer"><img src="https://avatars.githubusercontent.com/u/42586271?v=3" title="rexogamer" width="80" height="80"></a>
<a href="https://github.com/misterwhopper"><img src="https://avatars.githubusercontent.com/u/25962309?v=3" title="misterwhopper" width="80" height="80"></a>
## License:
MIT © [Jarod Burchill](http://burchilldevelopment.com)
