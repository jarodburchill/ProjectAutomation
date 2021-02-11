# Project Automation

Python script for creating new projects in the desired local directory, with a GitHub origin.

Contact us [on Discord.](https://discord.gg/eqWstJu)

## Requirements:

#### Universal

- [Python 3.4+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- A text editor (eg. [VS Code](https://code.visualstudio.com/) or [Atom](https://atom.io/. Optional but recommended.)

#### React/Electron/Node.js/Express.js

- [npm](https://nodejs.org/)

#### Vue

- [Vue CLI](https://cli.vuejs.org/guide/installation.html)

#### Laravel

- [PHP](https://www.php.net/manual/en/install.php)
- [Composer](https://getcomposer.org/)
- [Laravel](https://laravel.com/docs/5.8/installation)

## Installation:

### Windows:

Clone the repository:

```
cd C:\
git clone https://github.com/jarodburchill/project-automation
```

Set the environment variable:

```
setx path "%path%;C:\project-automation\windows"
```

### Mac/Linux:

Clone the repository:

```
cd ~
git clone https://github.com/jarodburchill/project-automation
```

Set the environment variable:

```
PATH=$PATH:~/project-automation/mac-linux
```

Make executable:

```
cd ~/project-automation/mac-linux
chmod +x new-project
```

## Configuration:

All configuration options can be found in the `script.config` file.

### Options and Defaults:
| Name         | Description           | Usage                | Default           | 
| ------------- | --------------------- | -------------------- | ----------------- |
| `directory` | Takes a file path string to determine where new projects will be created. | `directory = <path>` | `C:/Projects`. If on Windows, change if you like. If on Mac, you must set it to `/Users/<username>/desired path`. If on Linux, you must set it to `/home/<username>/desired path`. |
| `editor` | Takes a string to determine which editor new projects will be opened in after creation. | `editor = <name of command that opens the editor/none>` (see EDITORS.md) | `code` (opens VSCode) |
| `username` | If a valid GitHub username is entered into this option, the script will not prompt for your username every run. | `username = <username>` | blank |
| `password` | If the `username` option is set, the script will not prompt for your GitHub password every run. | `password = <password>` | blank |
| `private` | Takes a string to determine if projects should have a private or public GitHub repo. | `private = <y/n>` | blank |

## Usage:

### Run in Terminal:

```
new-project
```

### Project Types:

| Type          | Description           |
| ------------- | --------------------- |
| `blank` | Blank repository with a README |
| `html` | HTML boilerplate complete with CSS and JS |
| `react` | create-react-app |
| `react-ts` | create-react-app with TypeScript |
| `node` | Node.js project |
| `express` | Express.js project |
| `laravel` | Laravel project |
| `vue` | Vue project |
| `python` | Pyscaffold project |
| `electron` | create-electron-app |

#### For lots of python config options, [see the pyscaffold README.](https://github.com/pyscaffold/pyscaffold#configuration--packaging)

## Contributors:

<a href="https://github.com/jarodburchill"><img src="https://avatars.githubusercontent.com/u/37840393?v=3" title="jarodburchill" width="80" height="80"></a>
<a href="https://github.com/ajnieset"><img src="https://avatars.githubusercontent.com/u/40476295?v=3" title="ajnieset" width="80" height="80"></a>
<a href="https://github.com/rexogamer"><img src="https://avatars.githubusercontent.com/u/42586271?v=3" title="rexogamer" width="80" height="80"></a>
<a href="https://github.com/misterwhopper"><img src="https://avatars.githubusercontent.com/u/25962309?v=3" title="misterwhopper" width="80" height="80"></a>

## License:

MIT © [Jarod Burchill](http://burchilldevelopment.com)
