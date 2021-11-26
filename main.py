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
        save_file()
    elif opt == 'c':
        print('Run operation cancelled')
    msg_box.destroy()

# message box for when attempting to run a non-saved file
def check_run(): 
    global msg_box
    msg_box = Toplevel(root) # places at top level of main window
    msg_box.title('Run Operation Warning')
    msg_box.geometry('300x100')
    msg_box.resizable(height=False, width=False)
    msg_box_label = Label(msg_box, text='You must first save this file \n in order to run it')
    msg_box_label.configure(font=('nimbus sans',12))
    msg_box_label.pack(pady=10)
    msg_box_frame = Frame(msg_box)
    msg_box_frame.pack(pady=5)

    saveButton = Button(msg_box_frame, text='Save', 
    command=lambda: choice('s'))
    saveButton.grid(row=0, column=0)

    cancelButton = Button(msg_box_frame, text='Cancel', 
    command=lambda: choice('c'))
    cancelButton.grid(row=0, column=1)

# Reveals SoaPy information window
def AppInfo(): 
    global INFO_APP_ICON, spyTerminal

    # window settings
    appInfo = Toplevel(root)
    appInfo.title('SoaPy IDE')
    appInfo.geometry('300x200')
    appInfo.resizable(height=False, width=False)

    # App image
    appImage = Label(appInfo, image = INFO_APP_ICON)
    appImage.pack(pady=5)

    # App name + version label
    appName = Label(appInfo, text=f'SoaPy IDE {SOAPY_VERSION}')
    appName.config(font=('nimbus sans',15, 'bold'))
    appName.pack(pady= 5)

    # Developer info label
    devName = Label(appInfo, text=f'Developed by {DEVELOPER_NAMES}')
    devName.config(font=('nimbus sans',10))
    devName.pack(pady= 5)

# Function for opening files
def open_file():
    try:
        global path
        # Open file dialog settings
        file = fd.askopenfilename(title='Open Python File',
        filetypes=(('Python Files', '*.py'),('Text Files', '*.txt'), 
        ('All Files', '*.*')))

        # File contents become readable
        file = open(file, 'r')
        data = file.read()

        # Extracts files path and name
        filePath = os.path.realpath(str(file.name))
        print(filePath)
        fileName = os.path.basename(str(file.name))

        # Updates main window title
        root.title(f'SoaPy - {fileName}')
        # Updates global path var
        path = f'{filePath}'

        # Deletes current textField content and inserts data from file
        textField.delete('1.0', END)
        textField.insert(END, data)
        file.close()
    except:
        print('! Error opening file !')
        print('i: Likely operation was cancelled by user')

# Function fo saving file as
def save_file():
    global path, root
    # save file operation
    if '.' not in path: # executes if no file previously opened
    # Save file as dialog settings
        pyFile = fd.asksaveasfilename(
            defaultextension='.*',
            title='Save File',
            filetypes=(('Python Files', '*.py'),('Text Files', '*.txt'), 
        ('All Files', '*.*'))
        )
        if pyFile:
            # extracts file path and name
            filePath = os.path.dirname(str(pyFile))
            fileName = os.path.basename(str(pyFile))
            path = f'{filePath}' # updates global path value
            root.title(f'SoaPy - {fileName}') # updates main window title

            pyFile = open(pyFile, 'w') # opens file in write mode
            pyFile.write(textField.get(1.0, END)) # writes data to file
            pyFile.close() 
    elif '.' in path: # executes if a file has been opened into SoaPy
        # saves file without dialog
        file = open(path, 'w')
        file.write(textField.get(1.0, END)) # writes data to file
        file.close()


# Function for starting a new file
def new_file():
    global path
    textField.delete('1.0', END)
    root.title('SoaPy - untitled*')
    path = ''

# Function to pre-load all required app images
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
    INFO_APP_ICON = PhotoImage(file =r'icons/appIcon32.png')
 
# Sets main window settings
def window_settings(): # could be class?
    global root
    root.geometry('500x600')
    root.title('SoaPy' + ' - {}{}'.format(projectName, editStatus))
    root.tk.call('wm', 'iconphoto', root._w, APP_ICON)


# Class for tool bar icons
class ToolBarIcon():
    def __init__(self, toolBar, image, side, command):

        self.toolBar = toolBar # inherit tool bar frame
        self.image = image # inherit icon image 
        self.side = side # side of tool bar
        self.command = command # select a command to execute

        # Icon object settings
        button = Button(toolBar, 
        height=20, width=20, image=image,
        highlightthickness = 0, bd = 0, bg = '#F8F6F0',
        command=command)
        button.pack(side=side, padx=5, pady= 10)

# Class for top toolbar widget
class ToolBar():
    def __init__(self, root):
        self.root = root
        
        # Establish tool bar frame
        toolBar = Frame(root, bg='#F8F6F0')
        toolBar.pack(side=TOP, fill=X)

        # Left side
        ToolBarIcon(toolBar, image=OPEN_FILE_ICON, side=LEFT, command=open_file) # open file
        ToolBarIcon(toolBar, image=FILE_NEW_IMAGE, side=LEFT, command=new_file) # new file
        ToolBarIcon(toolBar, image=SAVE_FILE_IMAGE, side=LEFT, command=save_file) # save file as
        
        # Right side
        ToolBarIcon(toolBar, image=APP_INFO_IMAGE, side=RIGHT, command=AppInfo) # open app info
        ToolBarIcon(toolBar, image=RUN_FILE_ICON, side=RIGHT, command=runOperation) # run script

# Class for text field widget
class TextField():
    def __init__(self, root):
        global textField
        self.root = root
        # Establish text frame
        # important when implementing line numbers
        TEXT_FRAME = Frame(root)
        TEXT_FRAME.pack(fill=BOTH)

        # Establish text field
        textField = Text(TEXT_FRAME,undo=True)
        textField.pack(expand='true', fill=BOTH)
        textField.pack_propagate(False)
        textField.configure(font=('nimbus sans', 10))
        textField.config(wrap='none')

# Class for Terminal Bar
class TerminalBar():
    def __init__(self, root):
        global termType
        self.root = root
        
        termBar =Frame(root, bg='#F8F6F0')
        termBar.pack(fill=X)
        termLabel = Label(termBar, image = TERMINAL_IMAGE, background='#F8F6F0')
        termLabel.pack(pady=5, padx=5, fill='both', side=LEFT)

        # terminal label
        termType = Label(termBar, text=f'Terminal: ({termEnv})', background='#F8F6F0')
        termType.pack(pady=5, padx=5, fill='both', side=LEFT)

# Class for embedding the terminal
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

# Call function to run scripts
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

# ensures file is saved before attempting to run script
def runOperation(event=None):
    # path check
    if '.' not in path:
        check_run() # checks if file is saved
        if '.' not in path:
            pass
        else:
            run() # executes script
    else:
        run()


# bootstrap
if __name__ == '__main__':

    # root for Tkinter application
    root = Tk() # move to class
    
    # initial variables / could be added to class if needs be
    path = ''
    USER_SYSTEM = platform.system() # finds users system (i.e Windows, Linux)
    projectName = 'untitled'
    editStatus = '*'
    termEnv = '' # change based on loadup function
    SOAPY_VERSION = '1.0.0' # current SoaPy version
    DEVELOPER_NAMES = 'Seanb126' # developer names

    # Setup Functions
    load_images() 
    window_settings()

    # Widgets
    ToolBar(root)
    TextField(root)
    TerminalBar(root)
    LoadTerminal(root)

    root.mainloop()

