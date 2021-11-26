# SoaPy | v1.0.1-Alpha

## Introduction
SoaPy is a piece of free and open source software (FOSS) developed in Python for Python developers.
While in the early stages of development, the longterm goal of this project is to develop a usable Python IDE that follows
the FOSS ideoligy.

A simple roadmap has been established to give a generic idea of the future features

Feel free to provide suggestions or report technical issues

## Current Issues
Line numbering re-entered however while improved it still is out of synce when writing at the end of the view, also produces a horrible out of sync glitch when redrawing line numbers. 
Current icon produces graphical error, a pure .ico file will need to be created.

## Roadmap
- Re-implement line numbers. Current approach is not only derivative, however is prone to glitches after passing the 24th line/original yview
- Terminal Selection. Allow the user to select their preferred terminal, either through a settings menu or by clicking the terminal icon
- Implement terminal commands, i.e run, ls(search files)
- Save over opened file instead of having to use save as menu
- New font(install into app directory)
- Colour tag text i.e 'print' is yellow
