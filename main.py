#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 18:58:49 2021

@author: Seanb126
"""


from tkinter import *
from tkinter import filedialog as fd

root = Tk()

def openPy():
    file = fd.askopenfilename(title='Open Python File')
    file = open(file, 'r')
    data = file.read()

    textField.insert(END, data)
    file.close()



 
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

# Open File
openIcon = PhotoImage(file = r'icons/openFree.png')

openFile = Button(toolBar, 
height=20, width=20, image=openIcon,
highlightthickness = 0, bd = 0, bg = '#F8F6F0')

openFile.pack(side=LEFT, padx=2, pady= 10)
# Save File
saveIcon = PhotoImage(file = r'icons/saveFile20x20.png')

saveFile = Button(toolBar, 
height=20, width=20, image=saveIcon,
highlightthickness = 0, bd = 0, bg = '#F8F6F0')

saveFile.pack(side=LEFT, padx=2, pady= 10)
# Run File
runIcon = PhotoImage(file = r'icons/playFile.png')
runFile = Button(toolBar, 
height=20, width=20, image=runIcon,
highlightthickness = 0, bd = 0, bg = '#F8F6F0')

runFile.pack(side=RIGHT, padx=2, pady= 10)

# text field
textField = Text(root, padx=3, pady=5, wrap='word',undo=True)
textField.pack(expand='yes', fill='both')




root.mainloop()

