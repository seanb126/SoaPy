# SoaPy Python IDE

## Introduction
SoaPy is a functional Python IDE, which includes the ability to run your Python scripts inside an embedded terminal(SoaPy Terminal or xTerm)
or an external terminal(xTerm, Windows cmd.exe, Gnome terminal).

SoaPy was developed using Python and the Tkinter package (see requirements.txt/ or main.py)


Feel free to view/comment!

## Installation
SoaPy can be run as any other traditional Python script, by typing inside a terminal:

```linux
python main.py
```

To avoid possible permission issues when saving files, it may be best to rely on the single executable file, within the bin directory.
To run the executable on Linux, first you must 'cd' into the executables directory(bin folder if you cloned this repo)
then type:

```linux
sudo ./SoaPy
```

For Windows users, please await a commit which contains the .exe file. 
However that should be as easy to run, by just double clicking the executable file.

## Current Issues
- Current app icon produces graphical error, a pure .ico file will need to be created
- Permission exception thrown when saving outside of project folder(Linux). Exception didn't occur with pyinstaller exec'. Likely a dev issue

## Roadmap
- Re-implement line numbers
- Terminal Selection. Allow the user to select their preferred terminal, either through a settings menu or by clicking the terminal icon
- Implement SoaPy terminal commands, i.e run, ls(search files)
- New font(install into app directory)
- Colour tag text i.e 'print' is yellow in text field
- Ability to check code for syntax / Python errors
- Produce single executable (Include icon files inside exec)

## License
MIT License(see LICENSE)
