from BasicGraph import *
import math

class Point(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.last = None
        self.F = None
        self.G = math.inf
        self.H = None
        # self.state = []

    def isPoint(self, point):
        if self.row == point.row and self.col == point.col:
            return True
        else:
            return False

    def isInList(self, lst):
        for point in lst:
            if self.row == point.row and self.col == point.col:
                return True
        return False

    def getTuple(self):
        t = (self.row, self.col)
        return t

    def isInDict(self, dict):
        t = (self.row, self.col)
        try:
            result = dict[t]
        except:
            result = False

        return result

    def isClosed(self, closedict):
        t = self.getTuple()
        try:
            boo = closedict[t]
        except KeyError:
            return False
        return closedict[t]

    def __lt__(self, other):
        return self.F < other.F

    def updateF(self):
        self.F = self.G + self.H

    def setH(self, target):
        self.H = a_star_get_manh(self, target)