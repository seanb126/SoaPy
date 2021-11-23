#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 18:58:49 2021

@author: Seanb126
"""


from tkinter import *
from tkinter import filedialog as fd
import os

root = Tk()

def openPy():
    textField.delete('1.0', END) # check if in case cancelled
    file = fd.askopenfilename(title='Open Python File',
    filetypes=(('Python Files', '*.py'),('Text Files', '*.txt'), 
    ('All Files', '*.*')))
    file = open(file, 'r')
    data = file.read()

    # fileName = file
    fileName = os.path.basename(str(file))
    # fileName = str(fileName).rpartition('/')
    fileName = fileName.rpartition('.py')
    ft = '.py'
    # fileName = fileName + ft
    fileName = fileName[0]
    root.title(f'SoaPy - {fileName}{ft}')




    textField.insert(END, data)
    file.close()

def savePy():
    t  = '3'

def newPy():
    # add if statement to determine if file is empty
    textField.delete('1.0', END)
    root.title('SoaPy - untitled*')


 
# reflects specified file name else = 'untitled'
projectName = 'Untitled'
# reflects edit status '*' if unsaved else ''
editStatus = '*'
# include change detection stream


# Window Title
root.title('SoaPy' + ' - {}{}'.format(projectName, editStatus))

# app icon
appIcon = PhotoImage(file = 'icons/appIcon32.png') # find better method
# appIcon = PhotoImage(r'icons/appIcon32.ico')

root.tk.call('wm', 'iconphoto', root._w, appIcon)
# root.iconbitmap(r'icons/appIcon32.ico')
#root.iconbitmap('icons/appIcon32.ico')

# Toolbar
toolBar = Frame(root, bg='#F8F6F0')
toolBar.pack(side=TOP, fill=X)
# ----buttons----

# current theme from remixicon.com

# Open File
openIcon = PhotoImage(file = r'icons/folder-open-fill.png')

openFile = Button(toolBar, 
height=20, width=20, image=openIcon,
highlightthickness = 0, bd = 0, bg = '#F8F6F0',
command=openPy)

openFile.pack(side=LEFT, padx=5, pady= 10)

# New File
newIcon = PhotoImage(file = r'icons/file-add-fill.png')

newFile = Button(toolBar, 
height=20, width=20, image=newIcon,
highlightthickness = 0, bd = 0, bg = '#F8F6F0',
command=newPy)

newFile.pack(side=LEFT, padx=5, pady= 10)

# Save File
saveIcon = PhotoImage(file = r'icons/save-3-line.png')

saveFile = Button(toolBar, 
height=20, width=20, image=saveIcon,
highlightthickness = 0, bd = 0, bg = '#F8F6F0')

saveFile.pack(side=LEFT, padx=5, pady= 10)
# Run File
runIcon = PhotoImage(file = r'icons/play-fill.png')
runFile = Button(toolBar, 
height=20, width=20, image=runIcon,
highlightthickness = 0, bd = 0, bg = '#F8F6F0')

runFile.pack(side=RIGHT, padx=5, pady= 10)

# text field
textField = Text(root, padx=3, pady=5, wrap='word',undo=True)
textField.pack(expand='yes', fill='both')




root.mainloop()

