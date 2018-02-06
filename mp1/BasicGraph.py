import re
import numpy as np
import math

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
        # p_n = np.where(gn == target)
        # p_n = np.array(p_n)
        # pairs1 = p_n[0]
        # pairs2 = p_n[1]
        # pairs = zip(pairs1, pairs2)
        points = []
        pairs = zip(*np.where(gn == target))
        pairs = list(pairs)
        for pair in pairs:
            point = Point(pair[0], pair[1])
            points.append(point)
        return points

    def getCloseDict(self, gn, target = '%'):
        points = {}
        pairs = zip(*np.where(gn == target))
        pairs = list(pairs)
        for pair in pairs:
            points[pair] = True
            # print(points[pair])
        return points

    def isClosePoint(self):


class Point(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.last = None
        self.F = 0
        self.G = math.inf

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

    def getTurple(self):
        t = (self.row, self.col)
        return t

    def isInDict(self, dict):
        t = (self.row, self.col)
        try:
            result = dict[t]
        except:
            result = False

        return result
