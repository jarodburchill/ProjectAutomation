# Project Automation

Python script for creating new projects in the desired local directory, with a GitHub origin.

Contact us [on Discord.](https://discord.gg/eqWstJu)

## Requirements:

#### Universal

- [Python 3.4+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- A text editor i.e. [VS Code](https://code.visualstudio.com/), [Atom](https://atom.io/), etc. (Optional but recommended.)

#### React/Node.js/Express.js

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

#### \$USER = your machine's username. YOU MUST CHANGE THIS!

---

The `editor` option takes a string to determine what editor new projects will be opened in after creation.

```
editor = <editor>
```

Any editor that is installed on your local machine is supported (provided it has a command line command to open). Set to `none` if you don't wish to open the repo in an editor.

#### See EDITORS.md for a list of editors.

---

The `username` option is blank by default. If a correct GitHub username is entered into this option, the script will not prompt you to enter a username on each run.

```
username = <username>
```

---

The `password` option is blank by default. If a correct GitHub password is entered into this option and the username option has also been provided, the script will not prompt you to enter a password on each run.

```
password = <password>
```

---

The `private` option is blank by default. If it is set to `y` all repos will be made private by default. If it is set to `n` all repos will be set to public by default.

```
private = <y/n>
```

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
| `react` | Create-react-app |
| `react-ts` | Create-react-app with TypeScript |
| `node` | Node.js project |
| `express` | Express.js project |
| `laravel` | Laravel project |
| `vue` | Vue project |
| `python` | pyscaffold project |

#### For lots of python config options, [see the pyscaffold README.](https://github.com/pyscaffold/pyscaffold#configuration--packaging)

## Contributors:

<a href="https://github.com/jarodburchill"><img src="https://avatars.githubusercontent.com/u/37840393?v=3" title="jarodburchill" width="80" height="80"></a>
<a href="https://github.com/ajnieset"><img src="https://avatars.githubusercontent.com/u/40476295?v=3" title="ajnieset" width="80" height="80"></a>
<a href="https://github.com/rexogamer"><img src="https://avatars.githubusercontent.com/u/42586271?v=3" title="rexogamer" width="80" height="80"></a>
<a href="https://github.com/misterwhopper"><img src="https://avatars.githubusercontent.com/u/25962309?v=3" title="misterwhopper" width="80" height="80"></a>

## License:

MIT © [Jarod Burchill](http://burchilldevelopment.com)
