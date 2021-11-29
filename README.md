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
./SoaPy
```

For Windows users, please await a commit which contains the .exe file. 
However that should be as easy to run, by just double clicking the executable file.

## How-to
### SoaPy Main Window
![](/images/test_soapy.png)
The SoaPy terminal is currently set as the default medium for executing Python scripts.Largely this reason is to test and expand the utility
of the SoaPy terminal, however, also this is because it is the most operable inside of the IDE.

- To execute your Python scripts you must first ensure the file is saved
- Then you can click the green run icon in the top right of the toolbar
- Your script will run with the output visible inside the SoaPy terminal. Although, if you did not first save the file, the run operation
will warn you that the file needs to be saved first, otherwise the operation is cancelled

### SoaPy with xTerm
![](/images/test_xterm.png)
SoaPy currently restricts the user to the SoaPy terminal, however the functionality is built-in for the scripts to be run
in either xTerm, cmd.exe or Gnome-Terminal.

To enable auto-terminal selection you can uncomment the following in 'main.py' on line 237(line may of changed), or find in the LoadTerminal() class:
```python
class LoadTerminal():
    def __init__(self, root):
        global termEnv
        self.root = root
        try: 
            raise Exception # Comment this line to test SoaPy Terminal

```
Remember that if xTerm is not installed or you arent on a device that uses cmd.exe(Windows) or Gnome-Terminal(Linux + Gnome DE), then auto-selection
will utilise the SoaPy Terminal.

Currently to test the script inside of the embedded xTerm terminal, you have to type the following inside the terminal:

```linux
python3 filename.py
```
If you use the run icon to run the script, when xTerm is selected as the terminal, it will run the script in a new window.

![](/images/run_external.png)

In future releases the aim is to make this optional, with the default being that all scripts are run in the embedded terminal.

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
- Menu to check installed Python libraries and offer popular additions

## License
MIT License(see LICENSE)
