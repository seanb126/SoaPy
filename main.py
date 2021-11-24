#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 18:58:49 2021

@author: Seanb126
"""


from tkinter import *
from tkinter import filedialog as fd
import os



# modulerise these functions
# move out of main file create window file
# move core files to 'core folder'
# create 'extended' file class for mods




root = Tk()


root.geometry('500x600')

def openPy():
    textField.delete('1.0', END) # check if in case cancelled
    file = fd.askopenfilename(title='Open Python File',
    filetypes=(('Python Files', '*.py'),('Text Files', '*.txt'), 
    ('All Files', '*.*')))
    file = open(file, 'r')
    data = file.read()

    fileName = os.path.basename(str(file))
    fileName = fileName.rpartition('.py')
    ft = '.py'
    fileName = fileName[0]
    root.title(f'SoaPy - {fileName}{ft}')




    textField.insert(END, data)
    file.close()

def saveAsPy():
    pyFile = fd.asksaveasfilename(
        defaultextension='.*',
        title='Save File',
        filetypes=(('Python Files', '*.py'),('Text Files', '*.txt'), 
    ('All Files', '*.*'))
    )
    if pyFile:
        fileName = os.path.basename(str(pyFile))
        fileName = fileName.rpartition('.py')
        ft = '.py'
        fileName = fileName[0]
        root.title(f'SoaPy - {fileName}{ft}')
    # save 
        pyFile = open(pyFile, 'w')
        pyFile.write(textField.get(1.0, END))
        pyFile.close()    



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
highlightthickness = 0, bd = 0, bg = '#F8F6F0',
command=saveAsPy)
saveFile.pack(side=LEFT, padx=5, pady= 10)

# Run File
runIcon = PhotoImage(file = r'icons/greenRun2.png')
runFile = Button(toolBar, 
height=20, width=20, image=runIcon,
highlightthickness = 0, bd = 0, bg = '#F8F6F0')

runFile.pack(side=RIGHT, padx=5, pady= 10)

# text field
textField = Text(root, padx=3, pady=5, wrap='word',undo=True)
textField.pack(expand='yes', fill='both')


# terminal
term = Frame(root, height=200, width=200)

term.pack(fill=BOTH, expand=YES)
wid = term.winfo_id()
os.system('xterm -into %d -hold -geometry 300x10 -sb &' % wid)



root.mainloop()

