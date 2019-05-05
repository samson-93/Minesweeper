from tkinter import *
from _root import Root

class View(Root):
    
    def __init__(self, parent=None):
        if parent != None:
            self.root = parent
        else:
            super().__init__()
        self.root.title("Minesweeper")
        #   Below 2 lines are from https://stackoverflow.com/questions
        #   /18537918/set-window-icon
        imgicon = PhotoImage(file='_logo.gif')
        self.root.tk.call('wm', 'iconphoto', self.root._w, imgicon)  
        self.screen = Frame(self.root)

    #   Produces and sets up content for current
    #       view and calls mainloop() for parent Tk()
    def start(self):
        self.screen.grid()
        self.root.mainloop()

    #   Wipes current frame from parent Tk()
    def clear(self):
        self.screen.grid_forget()
        self.screen.destroy()

    #   Wipes current frame from parent Tk() and calls
    #       super() to begin kill sequence for the parent Tk() itself
    def close(self):
        self.screen.grid_forget()
        self.screen.destroy()
        super().close()

