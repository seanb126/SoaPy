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

# Toolbar
toolBar = Frame(root, bg='#F8F6F0')
toolBar.pack(side=TOP, fill=X)
# ----buttons----

# Open File
openFile = Button(toolBar, text='Open', command=openPy)
openFile.pack(side=LEFT, padx=2, pady= 10)
# Save File
saveFile = Button(toolBar, text='Save')
saveFile.pack(side=LEFT, padx=2, pady= 10)
# Run File
runFile = Button(toolBar, text='Run')
runFile.pack(side=RIGHT, padx=2, pady= 10)

# text field
textField = Text(root, padx=3, pady=5, wrap='word',undo=True)
textField.pack(expand='yes', fill='both')




root.mainloop()

