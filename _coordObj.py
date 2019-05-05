class Coord():
    
    def __init__(self, x, y = None):
        #   Handles casting x-y coords in a string to Coord()
        if(y == None):
            if(isinstance(x, str)):
                ln = x.split(', ')
                newX = int(ln[0][1:])
                newY = int(ln[1][:-1])
                self.x = newX
                self.y = newY
            else:
                self.x = x
                self.y = 0
        else:
            self.x = x
            self.y = y

    #   Returns Coord()
    def getCoord(self):
        return self

    #   Returns x-value of Coord()
    def getX(self):
        return self.x

    #   Returns y-value of Coord()
    def getY(self):
        return self.y

    #   Returns string representation of Coord()
    def __str__(self):
        return "{" + str(self.x) + ", " + str(self.y) + "}"

    #   Returns boolean as representing if two Coord()s are equal or not
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

