#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 18:58:49 2021

@author: Seanb126
"""


from tkinter import *
from tkinter import filedialog as fd
from tkinter import font
from tkinter.scrolledtext import ScrolledText
import os
import sys
import subprocess
from subprocess import Popen, PIPE
import platform
from typing import ContextManager
from PIL import Image, ImageTk
import tkinter.font as tkf
from soapyterminal import SoaPyTerminal
# import soapyterminal





# modulerise these functions
# move out of main file create window file
# move core files to 'core folder'
# create 'extended' file class for mods

usrSystem = platform.system()
# print(usrSystem)





class CustomText(Text):

    def __init__(self, *args, **kwargs):
        Text.__init__(self, *args, **kwargs)

    def highlight_pattern(self, pattern, tag, start="1.0", end="end",
                          regexp=False):
        '''Apply the given tag to all text that matches the given pattern

        If 'regexp' is set to True, pattern will be treated as a regular
        expression according to Tcl's regular expression syntax.
        '''

        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        CustomText.tag_config("red", foreground = "red")
        CustomText.highlight_pattern("hello", "red")
        count = IntVar()
        while True:
            index = self.search(pattern, "matchEnd","searchLimit",
                                count=count, regexp=regexp)
            if index == "": break
            if count.get() == 0: break # degenerate pattern which matches zero-length strings
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")



root = Tk()
path = ''

# print(tkf.families())
# root.minsize(650, 600)
# root.maxsize(650, 700)

root.geometry('500x600')

def getNumbers(event=None):
    output = ''
    row, col = textField.index('end').split('.')
    for i in range(1, int(row)):
        output += str(i) + '\n'

    return output

def updtNumbers(event=None):
    lineNum_bar = getNumbers()
    lineNum.config(state='normal')
    lineNum.delete(1.0, END)
    lineNum.insert(1.0, lineNum_bar)
    lineNum.config(state='disabled')

lineNum = Text(
    root, width=4, padx=0, state='disabled',
    takefocus=0, background='grey', wrap='none'
)


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
    global img122
    appInfo = Toplevel(root)
    appInfo.title('SoaPy IDE')
    appInfo.geometry('400x200')
    appInfo.resizable(height=False, width=False)

    # resAppImage = Image.open('icons/appIcon30.png')
    # resAppImage.resize((20, 20))
    # img = ImageTk.PhotoImage(resAppImage)
    img122 = PhotoImage(file ='icons/appIcon32.png')
    appImage = Label(appInfo, image = img122)
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
        termAssistance()
        # termHelp.update() # re-activate for terminal help



def newPy():
    # add if statement to determine if file is empty
    textField.delete('1.0', END)
    root.title('SoaPy - untitled*')
    path = ''
    termAssistance()
    # termHelp.update() # re-activate for terminal help




 
# reflects specified file name else = 'untitled'
projectName = 'untitled'
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


# text field Terminal

# output_window = ScrolledText(root, height=10)
# output_window.pack(side= 'bottom',fill='x', expand=1)


# lineNum.pack(side='left', fill='y') # uncomment for line numbering

textField = Text(root, padx=5, pady=5,undo=True)
# wrap='word'

# textField.bind('<Any-KeyPress>', updtNumbers) # uncomment for line numbering

textField.pack(expand='true', pady=5, fill=BOTH)
textField.pack_propagate(False)
textField.configure(font=('nimbus sans', 10))
textField.config(wrap='none')

# lineNum.configure(font=('Helvetica', 12)) # uncomment for line numbering

# bind text fields
# def OnScroll(event):
#     widget = event.widget
#     other = textField if widget == lineNum else lineNum
#     other.yview_moveto(widget.yview()[0])
#     other.mark_set('insert', widget.index('insert'))

# textField("<KeyRelease-Up>", OnScroll)
# textField("<KeyRelease-Down>", OnScroll)
# lineNum("<KeyRelease-Up>", OnScroll)
# lineNum("<KeyRelease-Down>", OnScroll)

# for widget in (textField, lineNum):
#         bindtags = list(widget.bindtags())
#         bindtags.insert(2, "custom")
#         widget.bindtags(tuple(bindtags))

#         widget.bind_class("custom", "<Up>", OnScroll)
#         widget.bind_all('<Button-5>', OnScroll)
#         widget.bind_all('<Button-4>', OnScroll)
#         widget.bind_class("custom", "<Down>", OnScroll)




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
saveIcon = PhotoImage(file = r'icons/save-fill.png')
# original 'icons/save-3-line.png'
saveFile = Button(toolBar, 
height=20, width=20, image=saveIcon,
highlightthickness = 0, bd = 0, bg = '#F8F6F0',
command=saveAsPy)
saveFile.pack(side=LEFT, padx=5, pady= 10)

# Run File


def run():
    if termEnv == 'SoaPy':
        cmd = f'python {path}'
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=True)
        output, error =  process.communicate()
        
        # SoaPyTerminal.output_window.config(state='normal')
        # SoaPyTerminal.output_window.insert(END, '\n')
        # SoaPyTerminal.output_window.insert(END, output) # needs fixing
       
        # SoaPyTerminal.output_window.insert(1.0, error)
        # SoaPyTerminal.output_window.update()
        # SoaPyTerminal.output_window.config(state='disabled')

        SoaPyTerminal.InsertData(output, error)
    else: 

    #xterm code
    # os.system(f"xterm -hold -e sudo python {path}" % wid)
        if usrSystem == 'Linux':
            try:
                subprocess.Popen(['gnome-terminal', '-e', f'bash -c \"python {path}; exec bash\"'])
            except:
                print('System does not use Gnome DE')
                try:
                    subprocess.Popen(['xterm', '-e', f'bash -c \"python {path}; exec bash\"'])
                except:
                    print('Xterm is not installed on this device')
        elif usrSystem == 'Windows':
            print('Windows Testing/Development has not started')
        else:
            print('Could not identify your OS...')
            print('Attempting to open xterm')
            try:
                subprocess.Popen(['xterm', '-e', f'bash -c \"python {path}; exec bash\"'])
            except:
                print('Xterm is not installed on this device')

        cmd = f'python {path}'
    # tt.communicate(bytes(cmd.encode()))[0]


    # tt.stdin.write(bytes(f'bash -c \"python {path}; exec bash\"'.encode))
    # tt.communicate(f'bash -c \"python {path}; exec bash\"'.encode('utf8'))
    # tt.stdin.flush()


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

    



# App Information
infIcon = PhotoImage(file = r'icons/information-fill.png')
infFile = Button(toolBar, 
height=20, width=20, image=infIcon,
highlightthickness = 0, bd = 0, bg = '#F8F6F0',
command=AppInfo) # will open app info dialog box

infFile.pack(side=RIGHT, padx=5, pady= 10)

# run script
runIcon = PhotoImage(file = r'icons/greenRun2.png')
runFile = Button(toolBar, 
height=20, width=20, image=runIcon,
highlightthickness = 0, bd = 0, bg = '#F8F6F0',
command=runOperation)

runFile.pack(side=RIGHT, padx=5, pady= 10)

termEnv = '' # change based on loadup function

# terminal image
termBar =Frame(root, bg='#F8F6F0')
termBar.pack(fill=X)
termIcon = PhotoImage(file = r'icons/terminal.png')
termLabel = Label(termBar, image = termIcon, background='#F8F6F0')
termLabel.pack(pady=5, padx=5, fill='both', side=LEFT)

# terminal label
termType = Label(termBar, text=f'Terminal: ({termEnv})', background='#F8F6F0')
termType.pack(pady=5, padx=5, fill='both', side=LEFT)

# terminal assistance
# termHelp = Label(termBar, text='Remember to save before running script !',
# background='#F8F6F0')
# termHelp.config(font=("Courier", 10))
# termHelp.pack(pady=5, padx=5, fill='both', side=RIGHT)

# hlpIcon =PhotoImage(file = r'icons/question.png')
# hlpLabel = Label(termBar, image = hlpIcon, background='#F8F6F0')
# hlpLabel.pack(pady=5, padx=5, fill='both', side=RIGHT)

# add. updates for when changing labels



def termAssistance():
    if '.' in path:
        termHelp.configure(text=f'Type: python {path}')
    else:
        termHelp.configure(text='Remember to save before running script !')


# class SoaPyTerminal():
#     output_window = ScrolledText(root, height=10)
#     output_window.pack(fill=BOTH, expand=1)
    
#     output_window.configure(background='black', foreground='white', font=("Helvetica", 10))
#     output_window.insert(1.0, 'SoaPy Terminal - Version 1.0.0\n')
#     output_window.configure(state='disabled')
    
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



# tagging python structures
# textField.tag_config("red", foreground = "red")
# textField.highlight_pattern("hello", "red")

# Pack Order






root.mainloop()

