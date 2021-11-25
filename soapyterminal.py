
from tkinter import *
from tkinter.scrolledtext import ScrolledText


class SoaPyTerminal():
    def __init__(self, root):
        # global root
        # self.output_window = output_window
        self.root = root
        output_window = ScrolledText(root, height=10)
        output_window.pack(fill=BOTH, expand=1)
        
        output_window.configure(background='black', foreground='white', font=("Helvetica", 10))
        output_window.insert(1.0, 'SoaPy Terminal - Version 1.0.0\n')
        output_window.configure(state='disabled')