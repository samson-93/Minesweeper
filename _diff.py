from tkinter import *
from tkinter import ttk
from _view import View
import _menu

class Difficulty(View):
    
    def __init__(self, parent=None):
        if parent != None:
            super().__init__(parent)
        else:
            super().__init__()
        self.setScreen()
        self.start()

    #   Sets difficulty value to be equal to the value of the selected radiobutton
    def select(self):
        self.newDiff = self.v.get()

    #   Wipes _settings.txt file, rewrites it with updated difficulty value
    def saveAndExit(self):
        with open('_settings.txt', 'w+') as file:
            file.write("Difficulty:\t" + str(self.newDiff))
        file.close()       
        self.clear()
        m = _menu.Menu(self.root)

    #   Initializes radiobuttons and functionality for easily adjusting difficulty value
    def setScreen(self):
        intVal = None
        # should implement error handling
        with open('_settings.txt', 'r') as inputFile:
            for line in inputFile:
                if "Difficulty:" in line:
                    ln = line.split('\t')
                    intVal = int(ln[1])
        inputFile.close()
        if intVal == None:
            intVal = 0
        self.newDiff = intVal
        #   The Following section uses approaches inspired by the following web pages:
        #   1)  https://www.python-course.eu/tkinter_radiobuttons.php
        #   2)  https://stackoverflow.com/questions/40900792/tkinter-radiobutton-not-updating-variable
        self.v = IntVar(self.screen)
        header = Label(self.screen, text="Choose Difficulty:").grid(row=1, column=1)
        self.easy = Radiobutton(self.screen, text="Easy", variable=self.v, value=0, command=self.select)
        self.normal = Radiobutton(self.screen, text="Normal", variable=self.v, value=1, command=self.select)
        self.hard = Radiobutton(self.screen, text="Hard", variable=self.v, value=2, command=self.select)   
        if intVal == 0:
            self.easy.select()
        elif intVal == 1:
            self.normal.select()
        else:
            self.hard.select()
        self.easy.grid(sticky="W", row=3, column=1)
        self.normal.grid(sticky="W", row=4, column=1)
        self.hard.grid(sticky="W", row=5, column=1)
        self.exit = ttk.Button(self.screen, text="OK", command=self.saveAndExit).grid(row=7, column=1)
        for i in range(9):
            self.screen.grid_rowconfigure(i, minsize=20)
        for i in range(3):
            self.screen.grid_columnconfigure(i, minsize=20)
