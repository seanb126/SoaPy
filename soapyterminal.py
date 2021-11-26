
from tkinter import *
from tkinter.scrolledtext import ScrolledText



class SoaPyTerminal():
    def __init__(self, root):
        global output_window, spyTerminal

        # SoaPy terminal version
        SOAPY_TERMINAL_VERSION = '1.0.0'

        self.root = root
        output_window = ScrolledText(root, height=10)
        output_window.pack(fill=BOTH, expand=1)
        
        output_window.configure(background='black', foreground='white', font=("Helvetica", 10))
        output_window.insert(1.0, f'SoaPy Terminal - Version {SOAPY_TERMINAL_VERSION}\n')
        output_window.configure(state='disabled')
    def InsertData(output, error):
        output = output
        error = error
        output_window.config(state='normal')
        output_window.insert(END, '\n')
        output_window.insert(END, output) # needs fixing
        # insert the error text in output_windows
        # if there is error
        output_window.insert(1.0, error)
        output_window.update()
        output_window.config(state='disabled')