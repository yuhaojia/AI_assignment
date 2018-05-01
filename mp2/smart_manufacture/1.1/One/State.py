import math
#from BasicGraph import *

class State(object):

    def __init__(self, name, remainelements,remaintype,remainNum, path):
        self.name = name
        self.remainelements = remainelements
        self.remaintype = remaintype
        self.remainNum = remainNum
        self.path = path
        self.G = math.inf
        self.H = math.inf
        self.F = math.inf
        #self.surround = []




    def isState(self, state):
        if self.remainNum != state.remainNum or self.name != state.name or len(self.remainelements) != len(state.remainelements) or len(self.remaintype) != len(state.remaintype) :
            return False
        for i in self.remainelements:
            if i not in state.remaintargets:
                return False
        for j in self.remaintype:
            if j not in state.remaintype:
                return False
        return True

    def isInList(self, lst):
        for state in lst:
            if self.isState(state):
                return True
        return False

    def updateF(self):
        self.F = self.G + self.H

    #def updateRemainTargets(self):
        #if self.checkState():
            #self.remaintargets.remove((self.row, self.col))

    #def checkState(self):
        #for rt in self.remaintargets:
            #if rt[0] == self.row and rt[1] == self.col:
                #return True
        #return False

    def __lt__(self, other):
        return self.F < other.F
