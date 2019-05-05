from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from _view import View
from _coordObj import Coord
from _cBtn import *
import _menu
import random
import time

class Game(View):

    def __init__(self, parent=None):
        if parent != None:
            super().__init__(parent)
        else:
            super().__init__()
        self.timerS = time.time()
        self.mineCoordList = []
        self.btnList = MSButtonList()
        self.setScreen()
        self.start()

    #   Uses _view.py funtions to clear the current Frame and calls _menu.Menu()
    #       while maintaining the original root Tk() window
    def endGame(self):
        self.clear()
        m = _menu.Menu(self.root)

    #   On Game win, notate the time it took to complete and add player information
    #       to _scores.txt for tracking.
    def win(self):
        self.timerE = time.time()
        self.time = (self.timerE - self.timerS)
        a = simpledialog.askstring("Minesweeper",
                                   "Congratulations, you won!\nPlease enter your name:",
                                   parent=self.screen)
        if a is not None:
            with open('_scores.txt', 'a+') as file:
                file.write(a +'\t' + str(int(round(self.time))) + '\t' + str(self.diff) + '\t\n')
            file.close()
        self.endGame()

    #   Checks for un-checked buttons, if the only remaining are mines - call win(),
    #       else return to calling function - btnClick()
    def checkWin(self):
        for i in range(self.height):
            for j in range(self.width):
                c = Coord(j, i)
                mb = self.btnList.getMSBtn(c)
                if(mb.check == False):
                    if c in self.mineCoordList:
                        continue
                    else:
                        return
                else:
                    continue
        self.win()

    #   Returns list of all coordinates immediately surrounding a given coordinate
    def getImmediateCoordList(self, coord):
        imCoords = []
        for i in range(3):
            c = Coord(coord.x-1, coord.y-1+i)
            imCoords.append(c)
        for i in range(3):
            c = Coord(coord.x+1, coord.y-1+i)
            imCoords.append(c)
        imCoords.append(Coord(coord.x, coord.y-1))
        imCoords.append(Coord(coord.x, coord.y+1))
        return imCoords

    #   Returns count of all mines immediately surrounding a given coordinate
    def getImmediateMineCount(self, coord):
        surroundingMines = 0
        for i in range(3):
            if(self.btnList.get(coord.x-1, coord.y-1+i) == 'M'):
                surroundingMines += 1
        for i in range(3):
            if(self.btnList.get(coord.x+1, coord.y-1+i) == 'M'):
                surroundingMines += 1
        if(self.btnList.get(coord.x, coord.y-1) == 'M'):
            surroundingMines += 1
        if(self.btnList.get(coord.x, coord.y+1) == 'M'):
            surroundingMines += 1
        return surroundingMines

    #   Handles left-click for a given coordinate (which represents a button)
    def btnClick(self, c):
        v = self.btnList.get(c)
        b = self.btnList.getBtn(c)
        mb = self.btnList.getMSBtn(c)
        if(mb.check == False):
            mb.check = True
            if v == 'M':
                b.config(bg="red")
                messagebox.showinfo("Minesweeper", "Y O U\tD I E D")
                with open('_dc.txt', 'r') as file:
                    dc = int(file.readline())
                file.close()
                with open('_dc.txt', 'w+') as file:
                    file.write(str(dc+1))
                file.close()
                self.endGame()
            elif v != 'NIL':
                b.config(bg="#aaaaaa", text=str(v))
            else:
                b.config(bg="#aaaaaa")
                vCoords = self.getImmediateCoordList(c)
                for spot in vCoords:
                    if(self.btnList.exists(spot)):
                        self.btnClick(spot)
                    else:
                        continue
        self.checkWin()

    #   Handles right-click for a given coordinate
    def flag(self, c):
        b = self.btnList.getBtn(c)
        mb = self.btnList.getMSBtn(c)
        if not mb.check:
            mb.flagged = not mb.flagged
            if mb.flagged:
                b.config(bg="yellow")
            elif not mb.flagged:
                b.config(bg="#cccccc")
        
    #   Randomly generates a list of coordinates representative of mine locations
    def generateMines(self, sideW, sideH, c):
        while True:
            rndm = Coord(random.randint(0, sideW), random.randint(0, sideH))
            if rndm in self.mineCoordList:
                continue
            else:
                self.mineCoordList.append(rndm)
                if(c == 0):
                    break
                else:
                    c = c-1
                    continue

    #   Initializes a button for each given coordinate value (dependant on selected difficulty)
    #       and adds this to a custom object list which allows for easy access and manipulation
    #       of each button via its coordinate value (see _cBtn.py for more details)
    def createTiles(self, sideW, sideH):
        for i in range(sideH):
            for j in range(sideW):
                c = Coord(j, i)
                b = Button(self.screen)
                b.bind('<Button-1>', lambda event, c=c: self.btnClick(c))
                b.bind('<Button-3>', lambda event, c=c: self.flag(c))
                b.config(bg="#cccccc", width=2, height=1)
                if c in self.mineCoordList:
                    m = MSButton(b, 'M', c)
                else:
                    m = MSButton(b, '-', c)
                m.show()
                self.btnList.add(m)
        #   Option for an Exit button from mid-game. Opted out of this for this particular
        #       project for other features. Code below is for future implementation.
        '''
        btn = ttk.Button(self.screen, text="Exit", command=self.endGame).grid(row=self.height-1, column=self.width+2)
        '''
        for i in range(sideH):
            for j in range(sideW):
                c = Coord(j, i)
                if self.btnList.get(c) == '-':
                    m = self.getImmediateMineCount(c)
                    if m == 0:
                        self.btnList.setVal('NIL', c)
                    else:
                        self.btnList.setVal(m, c)

    #   Fetches difficulty determined in _diff.py, if this is unavailable it will default to 0
    def getDiff(self):
        with open('_settings.txt', 'r') as file:
            for line in file:
                if "Difficulty:" in line:
                    ln = line.split('\t')
                    self.diff = int(ln[1])
            if self.diff == None:
                self.diff = 0
        file.close()

    #   Determines coordinate and mine settings based off difficulty and uses this to call more in-depth functions
    def setScreen(self):
        self.getDiff()
        if self.diff == 0:
            self.mineCt = 10
            self.width = 9
            self.height = 9
        elif self.diff == 1:
            self.mineCt = 40
            self.width = 16
            self.height = 16
        else:
            self.mineCt = 100
            self.width = 16
            self.height = 30
        self.generateMines(self.width, self.height, self.mineCt)
        self.createTiles(self.width, self.height)
