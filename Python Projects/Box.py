class box:
    
    def __init__ (self, h, w, d):

        self.height = h
        self.width = w
        self.depth = d

    def getVolume( self ):

        return self.height * self.width * self.depth

    def getSurfaceArea( self ):

        return 2 * (self.depth * self.width + self.depth * self.height + self.width * self.height)

    def setDimensions(self, h, w, d):
        self.height = h
        self.width = w
        self.depth = d

    def __repr__ ( self ):

        return f"height: {self.height}, width: {self.width}, depth: {self.depth}"
