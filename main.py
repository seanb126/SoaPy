#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 18:58:49 2021

@author: Seanb126
"""

# Import Libraries
from tkinter import *
from tkinter import filedialog as fd
import os
import subprocess
from subprocess import Popen, PIPE
import platform
import tkinter.font as tkf
from soapyterminal import SoaPyTerminal

def choice(opt): # choice operand
    if opt == 's':
        saveAsPy()
    elif opt == 'c':
        print('Run operation cancelled')
    pop.destroy()

# message box for when attempting to run a non-saved file
def check_run(): 
    global pop
    pop = Toplevel(root) # places at top level of main window
    pop.title('Run Operation Warning')
    pop.geometry('300x100')
    pop.resizable(height=False, width=False)
    pop_label = Label(pop, text='You must first save this file \n in order to run it')
    pop_label.configure(font=('nimbus sans',12))
    pop_label.pack(pady=10)
    pop_frame = Frame(pop)
    pop_frame.pack(pady=5)

    saveButton = Button(pop_frame, text='Save', 
    command=lambda: choice('s'))
    saveButton.grid(row=0, column=0)

    cancelButton = Button(pop_frame, text='Cancel', 
    command=lambda: choice('c'))
    cancelButton.grid(row=0, column=1)

def AppInfo(): # Reveals SoaPy information window
    global INFO_APP_ICON, spyTerminal
    # window settings
    appInfo = Toplevel(root)
    appInfo.title('SoaPy IDE')
    appInfo.geometry('300x200')
    appInfo.resizable(height=False, width=False)
    
    appImage = Label(appInfo, image = INFO_APP_ICON)
    appImage.pack(pady=5)

    appName = Label(appInfo, text=f'SoaPy IDE {SOAPY_VERSION}')
    appName.config(font=('nimbus sans',15, 'bold'))
    appName.pack(pady= 5)

    devName = Label(appInfo, text=f'Developed by {DEVELOPER_NAMES}')
    devName.config(font=('nimbus sans',10))
    devName.pack(pady= 5)



def openPy():
    try:
        global path
        file = fd.askopenfilename(title='Open Python File',
        filetypes=(('Python Files', '*.py'),('Text Files', '*.txt'), 
        ('All Files', '*.*')))
        file = open(file, 'r')
        data = file.read()

        filePath = os.path.realpath(str(file.name))
        print(filePath)
        fileName = os.path.basename(str(file.name))
        # print(f'Full FileName: {fileName}')
        # fileName = fileName.rpartition('.')
        # ft = '.py'
        # fileName = fileName[0]
        root.title(f'SoaPy - {fileName}')
        path = f'{filePath}'
        # print(path)
        textField.delete('1.0', END) # check if in case cancelled
        textField.insert(END, data)
        file.close()
        # termAssistance() # re-activate for terminal help
        # termHelp.update() # re-activate for terminal help
    except:
        print('! Error opening file !')
        print('i: Likely operation was cancelled by user')



def saveAsPy():
    pyFile = fd.asksaveasfilename(
        defaultextension='.*',
        title='Save File',
        filetypes=(('Python Files', '*.py'),('Text Files', '*.txt'), 
    ('All Files', '*.*'))
    )
    if pyFile:
        filePath = os.path.dirname(str(pyFile))
        fileName = os.path.basename(str(pyFile))
        # fileName = os.path.basename(str(pyFile))
        # ft = findExtention(fileName)

        # fileName = fileName.rpartition('.py')
        # # ft = '.py'
        # fileName = fileName[0]
        path = f'{filePath}'
        root.title(f'SoaPy - {fileName}')
    # save 
        pyFile = open(pyFile, 'w')
        pyFile.write(textField.get(1.0, END))
        pyFile.close()   
        # termAssistance()
        # termHelp.update() # re-activate for terminal help



def newPy():
    global path
    # add if statement to determine if file is empty
    textField.delete('1.0', END)
    root.title('SoaPy - untitled*')
    path = ''
    # termAssistance()
    # termHelp.update() # re-activate for terminal help

def load_images():
    global APP_ICON, FILE_NEW_IMAGE, OPEN_FILE_ICON,SAVE_FILE_IMAGE
    global APP_INFO_IMAGE, RUN_FILE_ICON, TERMINAL_IMAGE,INFO_APP_ICON
    APP_ICON = PhotoImage(file = r'icons/appIcon32.png')
    FILE_NEW_IMAGE = PhotoImage(file = r'icons/file-add-fill.png')
    OPEN_FILE_ICON = PhotoImage(file = r'icons/folder-open-fill.png')
    SAVE_FILE_IMAGE = PhotoImage(file = r'icons/save-fill.png')
    APP_INFO_IMAGE = PhotoImage(file = r'icons/information-fill.png')
    RUN_FILE_ICON = PhotoImage(file = r'icons/greenRun2.png')
    TERMINAL_IMAGE = PhotoImage(file = r'icons/terminal.png')
    INFO_APP_ICON = PhotoImage(file ='icons/appIcon32.png')
 

def window_settings(): # could be class?
    global root
    root.geometry('500x600')
    root.title('SoaPy' + ' - {}{}'.format(projectName, editStatus))
    root.tk.call('wm', 'iconphoto', root._w, APP_ICON)

class ToolBar():
    def __init__(self, root):
        self.root = root
        toolBar = Frame(root, bg='#F8F6F0')
        toolBar.pack(side=TOP, fill=X)
        # !could make a class for these to become reusable!
        # Left Side
        # Open File 
        openFile = Button(toolBar, 
        height=20, width=20, image=OPEN_FILE_ICON,
        highlightthickness = 0, bd = 0, bg = '#F8F6F0',
        command=openPy)
        openFile.pack(side=LEFT, padx=5, pady= 10)

        # New File
        newFile = Button(toolBar, 
        height=20, width=20, image=FILE_NEW_IMAGE,
        highlightthickness = 0, bd = 0, bg = '#F8F6F0',
        command=newPy)
        newFile.pack(side=LEFT, padx=5, pady= 10)

        # Save File As
        saveFile = Button(toolBar, 
        height=20, width=20, image=SAVE_FILE_IMAGE,
        highlightthickness = 0, bd = 0, bg = '#F8F6F0',
        command=saveAsPy)
        saveFile.pack(side=LEFT, padx=5, pady= 10)

        #Right Side
        # App Information
        infFile = Button(toolBar, 
        height=20, width=20, image=APP_INFO_IMAGE,
        highlightthickness = 0, bd = 0, bg = '#F8F6F0',
        command=AppInfo) # will open app info dialog box
        infFile.pack(side=RIGHT, padx=5, pady= 10)

        # Run Script
        runFile = Button(toolBar, 
        height=20, width=20, image=RUN_FILE_ICON,
        highlightthickness = 0, bd = 0, bg = '#F8F6F0',
        command=runOperation)
        runFile.pack(side=RIGHT, padx=5, pady= 10)

class TextField():
    def __init__(self, root):
        global textField
        self.root = root
        TEXT_FRAME = Frame(root)

        # EstablishNumbers(parent=TEXT_FRAME)
        
        TEXT_FRAME.pack(fill=BOTH)
        textField = Text(TEXT_FRAME,undo=True)
        # wrap='word'

        textField.pack(expand='true', fill=BOTH)
        textField.pack_propagate(False)
        textField.configure(font=('nimbus sans', 10))
        textField.config(wrap='none')

class TerminalBar():
    def __init__(self, root):
        global termType
        self.root = root
        # terminal image
        termBar =Frame(root, bg='#F8F6F0')
        termBar.pack(fill=X)
        termLabel = Label(termBar, image = TERMINAL_IMAGE, background='#F8F6F0')
        termLabel.pack(pady=5, padx=5, fill='both', side=LEFT)

        # terminal label
        termType = Label(termBar, text=f'Terminal: ({termEnv})', background='#F8F6F0')
        termType.pack(pady=5, padx=5, fill='both', side=LEFT)

class LoadTerminal():
    def __init__(self, root):
        global termEnv
        self.root = root
        try: 
            raise Exception # Used to test SoaPy Terminal

            # xterm terminal
            term = Frame(root, height=200, width=200)
            term.pack(fill='both', padx=1, pady=1, expand='yes')

            # Embeds terminal
            wid = term.winfo_id()
            subprocess.Popen(['xterm','-into',str(wid)],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)

            # informs program that xTerm is to be used
            termEnv = 'xTerm' 

            # Updates terminal bar label of the selected terminal
            termType.configure(text=f'Terminal: ({termEnv})')
            termType.update()
            
        except:
            SoaPyTerminal(root) # Embeds SoaPy terminal 

            # Informs program that SoaPy terminal is to be used
            termEnv = 'SoaPy'

            # Updates terminal bar label of the selected terminal
            termType.configure(text=f'Terminal: ({termEnv})')
            termType.update()



def run():
    if termEnv == 'SoaPy':
        # 
        cmd = f'python {path}'
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=True)
        output, error =  process.communicate()
        SoaPyTerminal.InsertData(output, error) # inserts data into SoaPy Terminal

        # Adapts the Run process if SoaPy Terminal isn't used
    else: 
        if USER_SYSTEM == 'Linux':
            try:
                if termEnv == 'xTerm':
                    subprocess.Popen(['xterm', '-e', f'bash -c \"python {path}; exec bash\"'])
                else:
                    subprocess.Popen(['gnome-terminal', '-e', f'bash -c \"python {path}; exec bash\"'])
            except:
                print('System does not use Gnome DE')
                try:
                    subprocess.Popen(['xterm', '-e', f'bash -c \"python {path}; exec bash\"'])
                except:
                    print('Xterm is not installed on this device')
        elif USER_SYSTEM == 'Windows':
            print('Warning: Process untested on Windows')
            try:
                subprocess.Popen(['cmd.exe', '-e', f'bash -c \"python {path}; exec bash\"'])
            except:
                try:
                    subprocess.Popen(['xterm', '-e', f'bash -c \"python {path}; exec bash\"'])
                except:
                    print('Could not find cmd.exe + xTerm is not installed on this device')
        else:
            print('Could not identify your OS...')
            print('Attempting to open xTerm')
            try:
                subprocess.Popen(['xterm', '-e', f'bash -c \"python {path}; exec bash\"'])
            except:
                print('Xterm is not installed on this device')

        cmd = f'python {path}' # remove


def runOperation(event=None):
    # path check
    if '.' not in path:
        check_run()
        if '.' not in path:
            pass
        else:
            run()
    else:
        run()



if __name__ == '__main__':
    # root for Tkinter application
    root = Tk() # move to class
    
    # initial variables
    # path for file management
    path = ''
    USER_SYSTEM = platform.system()
    projectName = 'untitled'
    editStatus = '*'
    termEnv = '' # change based on loadup function
    SOAPY_VERSION = '1.0.0'
    DEVELOPER_NAMES = 'Seanb126'

    # Setup Functions
    load_images() 
    window_settings()
    # Widgets
    ToolBar(root)
    TextField(root)
    # LineNumbers(root)
    # textField.bind_all('<Any-KeyPress>', update_numbers)
    TerminalBar(root)
    LoadTerminal(root)

    root.mainloop()

