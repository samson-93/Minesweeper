from tkinter import *
from _coordObj import Coord

class MSButton():
    
    def __init__(self, btn, val, coord, checked=False, flagged=False):
        self.btn = btn
        self.value = val
        self.coord = coord
        self.check = checked
        self.flagged = flagged

    #   Displays button object found inside of MSButton()
    #       per the coordinates also found in the object
    def show(self):
        self.btn.grid(row=self.coord.x, column=self.coord.y)

    #   Returns Coord() of MSButton()
    def getCoord(self):
        return self.coord

    #   Returns value of MSButton()
    def getVal(self):
        return self.value

class MSButtonList():
    
    def __init__(self):
        self.lst = []

    #   Adds MSButton() to an internal list[]
    def add(self, msbutton):
        self.lst.append(msbutton)

    #   Returns value of MSButton() that is located at a given coordinate
    def get(self,r,c=None):
        if (isinstance(r, Coord)):
            coord = r
            r = coord.x
            c = coord.y
        for msbtn in self.lst:
            if msbtn.coord.x == r and msbtn.coord.y == c:
                return str(msbtn.value) # originally was cast as string
            else:
                continue
        return None

    #   Returns Button() within MSButton() located at a given coordinate
    def getBtn(self, r, c=None):
        if (isinstance(r, Coord)):
            coord = r
            r = coord.x
            c = coord.y
        for msbtn in self.lst:
            if msbtn.coord.x == r and msbtn.coord.y == c:
                return msbtn.btn
            else:
                continue
        return None

    # Returns MSButton() located at a given coordinate
    def getMSBtn(self, r, c=None):
        if (isinstance(r, Coord)):
            coord = r
            r = coord.x
            c = coord.y
        for msbtn in self.lst:
            if msbtn.coord.x == r and msbtn.coord.y == c:
                return msbtn
            else:
                continue
        return None

    # Sets value of MSButton() at a given coordinate
    def setVal(self, newVal, r, c=None):
        if (isinstance(r, Coord)):
            coord = r
            r = coord.x
            c = coord.y
        for msbtn in self.lst:
            if msbtn.coord.x == r and msbtn.coord.y == c:
                msbtn.value = newVal
            else:
                continue

    #   Returns boolean representing the existance of a given coordinate or not
    def exists(self, r, c=None):
        if (isinstance(r, Coord)):
            coord = r
            r = coord.x
            c = coord.y
        for msbtn in self.lst:
            if msbtn.coord.x == r and msbtn.coord.y == c:
                return True
            else:
                continue
        return False
    
        

