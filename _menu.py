from tkinter import *
from tkinter import ttk
from _view import View
import _game
import _diff
import _scores

class Menu(View):
    
    def __init__(self, parent=None):
        if parent != None:
            super().__init__(parent)
        else:
            super().__init__()
        self.setScreen()
        self.start()

    #   Clears current screen and initializes the game with parent TK()
    def play(self):
        self.clear()
        g = _game.Game(self.root)

    #   Clears current screen and calls view for editing difficulty
    def callDiff(self):
        self.clear()
        d = _diff.Difficulty(self.root)

    #   Clears current screen and calls view that displays high scores
    def callScores(self):
        self.clear()
        s = _scores.Scores(self.root)

    #   Calls super() to exit application
    def kill(self):
        super().close()

    #   Obtains and returns the current death count
    def getDC(self):
        with open('_dc.txt', 'r') as file:
            dc = int(file.readline())
        file.close()
        return dc

    #   Sets up menu (which calls the above functions) in current view
    def setScreen(self):
        self.header = Label(self.screen, text = "MINESWEEPER").grid(row=1, column=1)
        self.play = ttk.Button(self.screen, text = "Play", command=self.play).grid(row=3, column=1)
        self.diff = ttk.Button(self.screen, text = "Difficulty", command=self.callDiff).grid(row=4,column=1)
        self.scores = ttk.Button(self.screen, text = "High Scores", command=self.callScores).grid(row=5,column=1)
        self.exit = ttk.Button(self.screen, text = "Exit", command=self.kill).grid(row=6, column=1)
        dc = self.getDC()
        self.counter = Label(self.screen, text=("Death Count: " + str(dc))).grid(row=8, column=1)
        for i in range(3):
            self.screen.grid_columnconfigure(i, minsize=60)
        for i in range(9):
            self.screen.grid_rowconfigure(i, minsize=30)

