# Editor Help
This is a list of editors and what string to use in `script.config` for them. 
#### NOTE: IF USING ATOM, GO INTO IT, SELECT "ATOM" AND SELECT "INSTALL SCRIPT COMMANDS" BEFORE RUNNING THE SCRIPT!
Any editor, so long as it has a terminal command to open it, will work with this. If you don't want your new project to open in an editor, set the string to `"none"`. By default, it is set to open VSCode.
```
Visual Studio Code (aka VSCode): "code" (use "code-insiders" if you use VSCode Insiders)
Visual Studio Codium (aka VSCodium): "codium"
Atom: "atom" (use "atom-beta"/"atom-nightly" if you use Atom Beta/Nightly)
Vim: "vim"
Emacs: "emacs"
```
#### Special cases:
Sublime Text (and any editor with no command to open it):
1. Find the path Sublime/the editor is in.
2. Copy it.
3. Go to the start menu (or Flie Explorer), right-click This PC and select Properties.
4. Go to Advanced - Eviroment Variables - New.
5. Set the name to "editor-name .", and the value to the path where subl.exe/whichever editor is kept.
6. Click OK, then **MAKE SURE to set the editor variable in script.config to the name of the variable (without the dot).**
7. Restart the command terminal and rerun the script.

Please help by adding editors to this list!
