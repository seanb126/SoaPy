# SoaPy | v1.0.1-Alpha

## Introduction
SoaPy is a piece of free and open source software (FOSS) developed in Python for Python developers.
While in the early stages of development, the longterm goal of this project is to develop a usable Python IDE that follows
the FOSS ideoligy.

A simple roadmap has been established to give a generic idea of the future features

Feel free to provide suggestions or report technical issues

## Current Issues
While the embedded terminal is functional, communicating through stdin or 'communicate' is not working as expected, often freezing the app. This does open the door for new oppurtunities however. The run button now opens a new terminal window based on OS and executes the code successfully, elsewhere this could encourage users to become accustomed to terminals, by providing advice on what to write in the embedded terminal i.e 'python main.py'.

The code is frankensteined together on main.py, and in desperate need of cleaning/modulerising.

Current icon produces graphical error, a pure .ico file will need to be created.

## Roadmap
- Establish basic UI (including novel icons and line numbering)
- Provide file functionality (saving, loading, etc)
- Develop and implement code analysis
- Provide access to Python environment / system terminal
- Implement Source Control through Git
- Allow for package extensions
- Automatic file backups
- Terminal recommendations
