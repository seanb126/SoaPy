#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 18:58:49 2021

@author: Seanb126
"""


from tkinter import * # change to as tk
from tkinter import filedialog as fd
from tkinter import font
from tkinter.scrolledtext import ScrolledText
import os
import sys
import subprocess
from subprocess import Popen, PIPE
import platform
from typing import ContextManager
import tkinter.font as tkf
from soapyterminal import SoaPyTerminal





# modulerise these functions
# move out of main file create window file
# move core files to 'core folder'
# create 'extended' file class for mods






# add to bootstrap
# root = Tk()
# path = ''
# load_images()

# print(tkf.families())
# root.minsize(650, 600)
# root.maxsize(650, 700)

# root.geometry('500x600')


def OnScroll(event=None):
            # widget = event.widget
            # other = textField if widget == lineNum else lineNum
            # other.yview_moveto(widget.yview()[0])
            # other.mark_set('insert', widget.index('insert'))


            lineNum.yview_moveto(textField.yview()[0])

def get_numbers(event=None):
            global textField
            output = ''
            row, col = textField.index('end').split('.')
            for i in range(1, int(row)):
                output += str(i) + '\n'

            return output

def update_numbers(event=None):
        global lineNum, lineNum_bar
        OnScroll
        # def get_numbers(event=None):
        #     output = ''
        #     row, col = textField.index('end').split('.')
        #     for i in range(1, int(row)):
        #         output += str(i) + '\n'

        #     return output
        
        lineNum_bar = get_numbers()
        lineNum.config(state='normal')
        lineNum.delete(1.0, END)
        lineNum.insert(1.0, lineNum_bar)
        lineNum.config(state='disabled')
        OnScroll
        
        

class EstablishNumbers():
    def __init__(self, parent):
        self.parent = parent
        global lineNum, lineNum_bar
        lineNum = Text(
                parent, width=4, padx=0, state='disabled',
                takefocus=0, background='grey', wrap='none'
            )
        # lineNum.tag_add('center', '1.0', 'end')
        lineNum.pack(side='left', fill='y') # uncomment for line numbering

class LineNumbers():
    def __init__(self, root):
        self.root = root
        global lineNum, lineNum_bar
        # lineNum = Text(
        #     root, width=4, padx=0, state='disabled',
        #     takefocus=0, background='grey', wrap='none'
        # )
        # lineNum.pack(side='left', fill='y') # uncomment for line numbering
        # def get_numbers(event=None):
        #     global textField
        #     output = ''
        #     row, col = textField.index('end').split('.')
        #     for i in range(1, int(row)):
        #         output += str(i) + '\n'

        #     return output
        lineNum_bar = get_numbers()
        
        lineNum.configure(font=('nimbus sans', 10)) # uncomment for line numbering

        

        textField.bind_all("<KeyRelease-Up>", OnScroll)
        textField.bind_all("<KeyRelease-Down>", OnScroll)
        lineNum.bind_all("<KeyRelease-Up>", OnScroll)
        lineNum.bind_all("<KeyRelease-Down>", OnScroll)

        for widget in (textField, lineNum):
                bindtags = list(widget.bindtags())
                bindtags.insert(2, "custom")
                widget.bindtags(tuple(bindtags))
                widget.bind_all('<Any-KeyPress>', update_numbers)
                

                widget.bind_class("custom", "<Up>", OnScroll)
                widget.bind_all('<Button-5>', OnScroll)
                widget.bind_all('<Button-4>', OnScroll)
                widget.bind_class("custom", "<Down>", OnScroll)
    
    
    # def update_numbers(event=None):
    #     global lineNum, lineNum_bar
    #     # def get_numbers(event=None):
    #     #     output = ''
    #     #     row, col = textField.index('end').split('.')
    #     #     for i in range(1, int(row)):
    #     #         output += str(i) + '\n'

    #     #     return output
    #     # lineNum_bar = get_numbers()
    #     lineNum.config(state='normal')
    #     lineNum.delete(1.0, END)
    #     lineNum.insert(1.0, lineNum_bar)
    #     lineNum.config(state='disabled')
    

    


def choice(opt): # choice operand
    if opt == 's':
        saveAsPy()
    elif opt == 'c':
        print('Run operation cancelled')
    pop.destroy()


def check_run(): # message box for when attempting to run a non-saved file
    global pop
    pop = Toplevel(root)
    pop.title('Run Operation Warning')
    pop.geometry('300x100')
    pop.resizable(height=False, width=False)
    pop_label = Label(pop, text='You must first save this file \n in order to run it')
    pop_label.configure(font=('Helvetica',12))
    pop_label.pack(pady=10)

    pop_frame = Frame(pop)
    pop_frame.pack(pady=5)

    saveButton = Button(pop_frame, text='Save', 
    command=lambda: choice('s'))
    saveButton.grid(row=0, column=0)

    cancelButton = Button(pop_frame, text='Cancel', 
    command=lambda: choice('c'))
    cancelButton.grid(row=0, column=1)
    # termAssistance() # re-activate for terminal help
    # hlpLabel.update() # re-activate for terminal help

def AppInfo(): # message box for when attempting to run a non-saved file
    # global pop2
    global INFO_APP_ICON
    appInfo = Toplevel(root)
    appInfo.title('SoaPy IDE')
    appInfo.geometry('400x200')
    appInfo.resizable(height=False, width=False)

    # resAppImage = Image.open('icons/appIcon30.png')
    # resAppImage.resize((20, 20))
    # img = ImageTk.PhotoImage(resAppImage)
    
    appImage = Label(appInfo, image = INFO_APP_ICON)
    appImage.image = 'icons/appIcon32.png'
    appImage.pack(pady=5)

    appName = Label(appInfo, text='SoaPy IDE 1.0.0')
    appName.config(font=('nimbus sans',15, 'bold'))
    appName.pack(pady= 5)


    pyv = platform.python_build
    spyTerminal = '1.0.0'
    detInfo = Label(appInfo, text=f'SoaPy Terminal: {spyTerminal}\n Developed by Seanb126')
    detInfo.config(font=('nimbus sans',12))
    detInfo.pack(pady=5)
        # termAssistance() # re-activate for terminal help
        # hlpLabel.update() # re-activate for terminal help



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
        

# class findExtention(Variable):
#     def find(Variable):
#         if '.py' in Variable:
#             print('File is a Python Script')
#             value = '.py'
#         elif '.txt' in Variable:
#             print('File is a Text File')
#             value = '.txt'
#         else:
#             print('Filetype is unregistered...')
#             print('Attempting to open')
#             value = '.???'
#         return value



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

# def find_terminal_type():
#     try:


class LoadTerminal():
    def __init__(self, root):
        global termEnv
        self.root = root
        try: 
            raise Exception # to test SoaPy Terminal
            # xterm terminal
            term = Frame(root, height=200, width=200)

            term.pack(fill='both', padx=1, pady=1)
            # expand='yes', fill='both'
            wid = term.winfo_id()
            # os.system('xterm -into %d -hold -geometry 300x10 -sb &' % wid)
            tt = subprocess.Popen(['xterm','-into',str(wid),'-geometry', '300x10'],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            termEnv = 'xterm'
            
        except:
            SoaPyTerminal(root)
            # output_window = ScrolledText(root, height=10)
            # output_window.pack(fill=BOTH, expand=1)
            # output_window.insert(1.0, 'SoaPy Terminal')
            # output_window.configure(background='black', foreground='white')
            #remove above once SoaPy Terminal has been modulerised
            termEnv = 'SoaPy'
            termType.configure(text=f'Terminal: ({termEnv})')
            termType.update()
#text field Terminal



def run():
    if termEnv == 'SoaPy':
        cmd = f'python {path}'
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=True)
        output, error =  process.communicate()
        SoaPyTerminal.InsertData(output, error)
    else: 
        if USER_SYSTEM == 'Linux':
            try:
                subprocess.Popen(['gnome-terminal', '-e', f'bash -c \"python {path}; exec bash\"'])
            except:
                print('System does not use Gnome DE')
                try:
                    subprocess.Popen(['xterm', '-e', f'bash -c \"python {path}; exec bash\"'])
                except:
                    print('Xterm is not installed on this device')
        elif USER_SYSTEM == 'Windows':
            print('Windows Testing/Development has not started')
        else:
            print('Could not identify your OS...')
            print('Attempting to open xterm')
            try:
                subprocess.Popen(['xterm', '-e', f'bash -c \"python {path}; exec bash\"'])
            except:
                print('Xterm is not installed on this device')

        cmd = f'python {path}'


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

