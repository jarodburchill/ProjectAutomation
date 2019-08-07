# ProjectAutomation

Python script for creating new projects in the desired local directory, with a GitHub origin.

## Requirements:

- Python 3.x
- Git
- npm
- Visual Studio Code (recommended)

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
git clone https://github.com/jarodburchill/ProjectAutomation
```

Set the environment variable:

```
PATH=$PATH:~/ProjectAutomation/mac-linux
```

Make executable

```
cd ~/ProjectAutomation/mac-linux
chmod +x new-project
```

## Python Packages:

Install the required python packages

`pip install -r requirements.txt`

## Configuration:

All configuration options can be found in the script.config file.

### Options and Defaults:

The localPath option takes a file path string to determine where new local repositories will be created.

```
localPath = C:/Projects/
```

Mac and Linux users change local path

```
localPath = /home/$USER/Projects/
```

> \$USER = your machines username

The vscode option takes an on or off string to determine if new projects will be opened in VS Code after creation.

```
vscode = on
```

The username option is blank by default. If a correct GitHub username is entered into this option, the script will not prompt the user to enter a username on each run.

```
username =
```

The password option is blank by default. If a correct GitHub password is entered into this option and the username option has also been provided, the script will not prompt the user to enter a password on each run.

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

## License:
