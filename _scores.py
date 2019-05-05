from tkinter import *
from tkinter import ttk
from _view import View
import _menu
import operator

class Scores(View):
    
    def __init__(self, parent=None):
        if parent != None:
            super().__init__(parent)
        else:
            super().__init__()
        self.setScreen()
        self.start()

    #   Exits view and calls Menu() with parent Tk()
    def returnCmd(self):
        self.clear()
        m = _menu.Menu(self.root)

    #   Gets, sorts, and returns top 10 times (and corresponding names) for the current difficulty
    def getInfo(self):
        intVal = None
        # could use error handling if no file is present, if "Difficulty:" is empty, etc.
        with open('_settings.txt', 'r') as inputFile:
            for line in inputFile:
                if "Difficulty:" in line:
                    ln = line.split('\t')
                    intVal = int(ln[1])
                else:
                    continue
        if(intVal == None):
            intVal = 0
        inputFile.close()
        with open('_scores.txt', 'r') as inputFile:
            coll = dict()
            for line in inputFile:
                ln = line.split('\t')
                if(int(ln[2]) != intVal):
                    continue
                else:
                    if coll.get(ln[0]) != None and coll.get(ln[0]) < int(ln[1]):
                        continue
                    else:
                        coll[ln[0]] = int(ln[1])
        inputFile.close()
        # this section could be improved via peridocial data cleansing and/or more efficient algorithms
        #   The below line was obtained from https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
        _coll = sorted(coll.items(), key=operator.itemgetter(1))
        _coll = _coll[:10]
        return _coll

    #   Simple view to display information returned from getInfo()
    def setScreen(self):
        collection = self.getInfo()
        highscr = Label(self.screen, text="HIGH SCORES").grid(row=1, column=2)
        names = Label(self.screen, text="Name").grid(row=3, column=1)
        scores = Label(self.screen, text="Time").grid(row=3, column=3)
        for i in range(len(collection)):
            nm = Label(self.screen, text=collection[i][0]).grid(row=4+i, column=1)
            tm = Label(self.screen, text=str(collection[i][1])).grid(row=4+i, column=3)
        ex = ttk.Button(self.screen, text="OK", command=self.returnCmd).grid(row=(len(collection)+5), column=2)
        for i in range(5):
            self.screen.grid_columnconfigure(i, minsize=20)
        for i in range((len(collection) + 7)):
            self.screen.grid_rowconfigure(i, minsize=20)                

