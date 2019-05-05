from tkinter import *

class Root():

    #   Super class method for initialzing main window
    def __init__(self):
        self.root = Tk()

    #   Super class method for getting rid of main window
    def close(self):
        self.root.destroy()
        exit()
