import re
import numpy as np
import math
import heapq
from SearchAgent import *
from State import *
from Point import *

class BasicGraph(object):
    def __init__(self, filename):
        self.filename = filename
        self.directionRow = [1, 0, -1, 0]
        self.directionCol = [0, 1, 0, -1]
        self.vistedPoint = {}
        self.graph = []
        self.graph_n = None


    def initGraph(self):
        with open(self.filename) as f:
            lines = f.readlines()

        for line in lines:
            line = line.rstrip()
            row = list(line)
            self.graph.append(row)
        self.graph_n = np.array(self.graph)
        # print(graph)

    def dirAvai(self, point):
        if self.graph[point.row][point.col] == "%":
            return False
        else:
            return True

    def move(self, curPos):
        nextPoss = []
        for m in range(4):
            nextPos = Point(curPos.row + self.directionRow[m],
                          curPos.col + self.directionCol[m])
            if self.dirAvai(nextPos) is True:
                nextPoss.append(nextPos)
        return nextPoss

    def findP(self, gn, P):
        p_n = np.where(gn == P)
        # p_n = zip(*np.where(gn == P))

        point = Point(int(p_n[0]), int(p_n[1]))
        return point

    def findTarget(self, gn, target):

        points = []
        pairs = zip(*np.where(gn == target))
        pairs = list(pairs)
        for pair in pairs:
            point = Point(pair[0], pair[1])
            points.append(point)
        return points


    # the type of pair here is tuple
    def getCloseDict(self, gn, target = '%'):
        points = {}
        pairs = zip(*np.where(gn == target))
        pairs = list(pairs)
        for pair in pairs:
            points[pair] = True
        return points


    def getCloseList(self, gn, target = '%'):
        points = []
        pairs = zip(*np.where(gn == target))
        pairs = list(pairs)
        for pair in pairs:
            points.append(Point(pair[0], pair[1]))
        return points

    def getCloseStateList(self, gn, target = '%'):
        states = []
        pairs = zip(*np.where(gn == target))
        pairs = list(pairs)
        for pair in pairs:
            states.append(State(pair[0], pair[1], []))

        return states


    def isClosePoint(self):
        pass

    def surround(self, curPos):
        nextPoss = []
        for m in range(4):
            nextPos = Point(curPos.row + self.directionRow[m],
                            curPos.col + self.directionCol[m])
            nextPoss.append(nextPos)
        return nextPoss

    def surroundState(self, curstate):
        nextstates = []
        for m in range(4):
            nextstate = State(curstate.row + self.directionRow[m],
                              curstate.col + self.directionCol[m],
                              curstate.remaintargets)
            point = Point(curstate.row + self.directionRow[m],
                            curstate.col + self.directionCol[m])
            if not self.dirAvai(point):
                continue
            nextstate.updateRemainTargets()
            nextstates.append(nextstate)
        return nextstates