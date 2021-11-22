#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 18:58:49 2021

@author: Seanb126
"""


from tkinter import *

root = Tk()

 
# reflects specified file name else = 'untitled'
projectName = 'Untitled'
# reflects edit status '*' if unsaved else ''
editStatus = '*'
# include change detection stream


# Window Title
root.title('SoaPy' + ' - {}{}'.format(projectName, editStatus))

# Toolbar
toolBar = Frame(root, bg='blue')
toolBar.pack(side=TOP, fill=X)
# buttons
openFile = Button(toolBar, text='Open File')
openFile.pack(side=LEFT, padx=2, pady= 10)

# text field
textField = Text(root, padx=3, pady=50, wrap='word',undo=True)
textField.pack(expand='yes', fill='both')




root.mainloop()

