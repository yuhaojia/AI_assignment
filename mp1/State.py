import math
from BasicGraph import *

class State(object):
    def __init__(self, row, col, remaintargets):
        self.row = row
        self.col = col
        self.remaintargets = remaintargets
        self.G = math.inf
        self.H = None
        self.F = None
        self.last = None

    def isState(self, state):
        if self.row != state.row or self.col != state.col or len(self.remaintargets) != len(state.remaintargets):
            return False
        for i in self.remaintargets:
            if i not in state.remaintargets:
                return False

        return True

    def isInList(self, lst):
        for state in lst:
            if self.isState(state):
                return True
        return False

    def updateF(self):
        self.F = self.G + self.H

    def updateRemainTargets(self):
        if self.checkState():
            self.remaintargets.remove((self.row, self.col))

    def checkState(self):
        for rt in self.remaintargets:
            if rt[0] == self.row and rt[1] == self.col:
                return True
        return False

    def __lt__(self, other):
        return self.F < other.F
