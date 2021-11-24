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
import subprocess



# modulerise these functions
# move out of main file create window file
# move core files to 'core folder'
# create 'extended' file class for mods





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


def openPy():
    try:
        global path
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
        path = f'{fileName}{ft}'
        textField.delete('1.0', END) # check if in case cancelled
        textField.insert(END, data)
        file.close()
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
        fileName = os.path.basename(str(pyFile))
        fileName = fileName.rpartition('.py')
        ft = '.py'
        fileName = fileName[0]
        path = f'{fileName}{ft}'
        root.title(f'SoaPy - {fileName}{ft}')
    # save 
        pyFile = open(pyFile, 'w')
        pyFile.write(textField.get(1.0, END))
        pyFile.close()    



def newPy():
    # add if statement to determine if file is empty
    textField.delete('1.0', END)
    root.title('SoaPy - untitled*')
    path = ''




 
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

# text field

output_window = ScrolledText(root, height=10)
output_window.pack(side= 'bottom',fill='x', expand=1)

lineNum.pack(side='left', fill='y')
textField = CustomText(root, padx=5, pady=5, wrap='word',undo=True)
# lineNum.grid(row=0, column=0)
# textField.grid(row=0,column=1)
textField.bind('<Any-KeyPress>', updtNumbers)

textField.pack(expand='yes', fill='both')



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
# output_window = ScrolledText(root, height=10)
# output_window.pack(fill=BOTH, expand=1)

def run():
    cmd = f'python {path}'
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, shell=True)
    output, error =  process.communicate()
    # delete the previous text from
    # output_windows
    output_window.delete(1.0, END)
    # insert the new output text in
    # output_windows
    output_window.insert(1.0, output)
    # insert the error text in output_windows
    # if there is error
    output_window.insert(1.0, error)


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

    
runIcon = PhotoImage(file = r'icons/greenRun2.png')
runFile = Button(toolBar, 
height=20, width=20, image=runIcon,
highlightthickness = 0, bd = 0, bg = '#F8F6F0',
command=runOperation)

runFile.pack(side=RIGHT, padx=5, pady= 10)




# xterm terminal
# term = Frame(root, height=200, width=200)

# term.pack(fill=BOTH, expand=YES)
# wid = term.winfo_id()
# os.system('xterm -into %d -hold -geometry 300x10 -sb &' % wid)

# tagging python structures
# textField.tag_config("red", foreground = "red")
# textField.highlight_pattern("hello", "red")



root.mainloop()

