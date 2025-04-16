import math as m
class sphere:
    def __init__ (self, r):

        self.radius = r

    def getVolume(self):

        return 4/3 * m.pi * self.radius ** 3

    def getSurfaceArea(self):

        return 4 * m.pi * self.radius ** 2

    def setRadius(self, r):

        self.radius = r

    def __repr__(self):

        return f"{self.radius}"
