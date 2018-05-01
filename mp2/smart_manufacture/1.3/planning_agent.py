

from State import *
import sys
import heapq
from copy import deepcopy
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import numpy as np
#from scipy.sparse import csr_matrix.getnnz


#def getmiles():
#    elementsAlways = ['A', 'B', 'C', 'D', 'E']
#def getsteps():

def miles(Start, Widgets):
    #Widgets = [['A', 'E', 'D', 'C', 'A', '*'],
    #           ['B', 'E', 'A', 'C', 'D', '*'],
    #           ['B', 'A', 'B', 'C', 'E', '*'],
    #           ['D', 'A', 'D', 'B', 'D', '*'],
    #           ['B', 'E', 'C', 'B', 'D', '*']]

    #Widgets = [['E', 'C', 'A', 'E', 'A', 'D', 'E', '*'],
    #           ['E', 'A', 'C', 'B', 'A', 'D', 'B', '*'],
    #           ['B', 'C', 'A', 'C', 'B', 'E', 'C', '*'],
    #           ['A', 'E', 'C', 'D', 'C', 'B', 'D', '*'],
    #           ['D', 'E', 'C', 'B', 'A', 'C', 'D', '*']]

    elementsAlways = ['A', 'B', 'C', 'D', 'E']

    distanceMatrix = [[0, 1064, 673, 1401, 277],
                      [1064, 0, 958, 1934, 337],
                      [673, 958, 0, 1001, 399],
                      [1401, 1934, 1001, 0, 387],
                      [277, 337, 399, 387, 0]]

    distanceMatrixChar = [[0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0]]
    KindOfElement = 5
    NumberN = len(Widgets[0])-1
    openlist = []
    unvisitedelement = deepcopy(Widgets)
    count = 0
    # step_sum = 0
    # distance = []
    # iter = [0, 0, 0, 0, 0]
    unvisited = ['A', 'B', 'C', 'D', 'E']
    # visited = []
    remainNum = [0, 0, 0, 0, 0]
    for i in range(KindOfElement):
        for j in range(NumberN):
            k = ord(Widgets[i][j]) - ord("A")
            remainNum[k] += 1
    #print(remainNum)
    visitedpath = []
    ##print(unvisitedelement)
    NumSTART = len(unvisitedelement)
    if Start in unvisited and remainNum[ord(Start) - ord('A')] > 0:
        for j in range(NumSTART):
            if unvisitedelement[j][0] == Start:
                unvisitedelement[j].pop(0)
                remainNum[ord(Start) - ord('A')] -= 1
        visitedpath.append(Start)
        if remainNum[ord(Start) - ord('A')] == 0:
            unvisited.remove(Start)
    ##print(unvisitedelement)
    ##print(remainNum)
    ##print(unvisited)
    ##print(visitedpath)
    startState = State(Start, unvisitedelement, unvisited, remainNum, visitedpath)

    startState.H = 0
    startState.G = 0
    startState.updateF()
    heapq.heappush(openlist, startState)
    # openlist.append(startState)

    # for Widget in Widgets:
    # unvisited.append(Widget)

    # for i in range(len(Widget)):
    # for i in range(len(Widget)):
    while True:
        try:
            curState = heapq.heappop(openlist)
        except IndexError:
            print("No more point, no solution for this question")
            return -1
        count = count + 1
        # if not unvisited:
        # print("Found the shortest path")
        # break

        # KindOfElement = 5
        surround = []
        #surroundPossible = []
        #elems = deepcopy(curState.remainelements)
        #if surroundPossible:
        #    surroundPossible.pop()
        #for iikkii in range(KindOfElement):
        #    PossibleName = chr(ord('A') + iikkii)
        #    for elem in elems:
        #        if PossibleName == elem[0]:
        #            surroundPossible.append(PossibleName)

        ##print("Surround")
        for i in range(KindOfElement):
            NextName = chr(ord('A') + i)
            # print(curState.name)
            Nextremainelements = deepcopy(curState.remainelements)
            # print(Nextremainelements)
            NextremainNum = deepcopy(curState.remainNum)
            Nextremaintype = deepcopy(curState.remaintype)
            Newpath = deepcopy(curState.path)
            #if NextName in surroundPossible and
            if NextName != curState.name and NextName in curState.remaintype and curState.remainNum[i] > 0:

                # print(Nextremainelements)

                Num = len(Nextremainelements)
                # print(Num)

                # print(NextremainNum)
                for j in range(Num):

                    if Nextremainelements[j][0] == NextName:
                        Nextremainelements[j].pop(0)
                        NextremainNum[i] -= 1

                Newpath.append(NextName)
                if NextremainNum[i] == 0:
                    Nextremaintype.remove(NextName)

                NextState = State(NextName, Nextremainelements, Nextremaintype, NextremainNum, Newpath)
                surround.append(NextState)
                # Nextremainelements.pop()
                ##print(Nextremainelements)
        ##print(len(surround))

        # surrounds = curState.getSurr()
        if len(surround) <= 0:
            print("a_star expand points: ", count)
            kw = deepcopy(curState.remainelements)
            print("remain")
            print(kw)
            print(curState.G)
            return curState.path

        # surroundT = list(surrounds)
        leastF = math.inf
        nameChar = curState.name
        i = ord(nameChar)-ord('A')
        for nextstate in surround:
            j = ord(nextstate.name)-ord('A')


            nextstate.G = curState.G + distanceMatrix[i][j]
            nextstate.H = 0
                #len(nextstate.remaintype)
            nextstate.updateF()
            heapq.heappush(openlist, nextstate)

    pass




########################################################################################

def step(Start,Widgets):
    #Widgets = [['A', 'E', 'D', 'C', 'A', 'B', '*'],
    #           ['B', 'E', 'A', 'C', 'D', 'C','*'],
    #           ['B', 'A', 'B', 'C', 'E', 'D', '*'],
    #           ['D', 'A', 'D', 'B', 'D', 'A','*'],
    #           ['B', 'E', 'C', 'B', 'D', 'C','*']]

    #Widgets = [['E', 'C', 'A', 'E', 'A', 'D', 'E', '*'],
    #           ['E', 'A', 'C', 'B', 'A', 'D', 'B', '*'],
    #            ['B', 'C', 'A', 'C', 'B', 'E', 'C', '*'],
    #           ['A', 'E', 'C', 'D', 'C', 'B', 'D', '*'],
    #            ['D', 'E', 'C', 'B', 'A', 'C', 'D', '*']]

    #Widgets = [['A', 'E', 'D', 'C', 'A', '*'],
    #           ['B', 'E', 'A', 'C', 'D', '*'],
    #           ['B', 'A', 'B', 'C', 'E', '*'],
    #           ['D', 'A', 'D', 'B', 'D', '*'],
    #           ['B', 'E', 'C', 'B', 'D', '*']]

    KindOfElement = 5
    NumberN = len(Widgets[0])-1
    openlist = []
    unvisitedelement = deepcopy(Widgets)
    count = 0
    #step_sum = 0
    #distance = []
    #iter = [0, 0, 0, 0, 0]
    unvisited = ['A', 'B', 'C', 'D', 'E']
    #visited = []
    remainNum = [0, 0, 0, 0, 0]
    for i in range(KindOfElement):
        for j in range(NumberN):
            k = ord(Widgets[i][j])-ord("A")
            remainNum[k] += 1
    visitedpath = []
    #print(unvisitedelement)
    #print(remainNum)
    NumSTART = len(unvisitedelement)
    if Start in unvisited and remainNum[ord(Start)-ord('A')] > 0:
        for j in range(NumSTART):
            if unvisitedelement[j][0] == Start:
                unvisitedelement[j].pop(0)
                remainNum[ord(Start)-ord('A')]-=1
        visitedpath.append(Start)
        if remainNum[ord(Start)-ord('A')] == 0:
            unvisited.remove(Start)
    #print(unvisitedelement)
    #print(remainNum)
    #print(unvisited)
    #print(visitedpath)
    startState = State(Start, unvisitedelement, unvisited, remainNum, visitedpath)
    startState.H = len(unvisited)
    startState.G = 0
    startState.updateF()
    heapq.heappush(openlist, startState)
    #openlist.append(startState)

    #for Widget in Widgets:
        #unvisited.append(Widget)

    #for i in range(len(Widget)):
        #for i in range(len(Widget)):
    while True:
        try:
            curState = heapq.heappop(openlist)
        except IndexError:
            print("No more point, no solution for this question")
            return -1
        count = count + 1
        #if not unvisited:
            #print("Found the shortest path")
            #break
        #print("current")
        #print(curState.name)
        #print(curState.remainNum)
        #print(curState.remainelements)
        elems = deepcopy(curState.remainelements)
        surroundPossible = []
        if surroundPossible:
            surroundPossible.pop()
        for iikkii in range(KindOfElement):
            PossibleName = chr(ord('A') + iikkii)
            for elem in elems:
                if PossibleName == elem[0]:
                    surroundPossible.append(PossibleName)
        #KindOfElement = 5
        surround = []
        #print("Surround")
        for i in range(KindOfElement):
            NextName = chr(ord('A') + i)
            #print("Next")
            #print(NextName)
            if NextName in surroundPossible and NextName != curState.name and NextName in curState.remaintype and curState.remainNum[i] > 0:

                # print(curState.name)
                Nextremainelements = deepcopy(curState.remainelements)
                # print(Nextremainelements)
                NextremainNum = deepcopy(curState.remainNum)
                Nextremaintype = deepcopy(curState.remaintype)
                Newpath = deepcopy(curState.path)

                #print(Nextremainelements)
                Num = len(Nextremainelements)
                #print(Num)
                #print(NextremainNum)
                for j in range(Num):

                    if Nextremainelements[j][0] == NextName:
                        Nextremainelements[j].pop(0)
                        NextremainNum[i] -= 1
                Newpath.append(NextName)
                #print('Path:', end=' ')
                #print(Newpath)
                if NextremainNum[i] == 0:
                    Nextremaintype.remove(NextName)
                NextState = State(NextName, Nextremainelements, Nextremaintype, NextremainNum, Newpath)
                surround.append(NextState)
                #Nextremainelements.pop()
                #print(Nextremainelements)
        #print(len(surround))

        #surrounds = curState.getSurr()
        #if len(surround)<=0:
        #    print("a_star expand points: ", count)
        #    kw = deepcopy(curState.remainelements)
        #    print(kw)
        #    return curState.path

        if len(curState.remaintype) == 0:
            print("a_star expand points: ", count)
            #print(curState.name)
            #kw = deepcopy(curState.remaintype)
            #print("remain")
            #print(kw)
            #print("remain")
            print(Start)
            print(curState.G+1)
            return curState.path

        #surroundT = list(surrounds)
        leastF = math.inf
        for nextstate in surround:
            nextstate.G = curState.G + 1
            nextstate.H = 0
            nextstate.updateF()
            heapq.heappush(openlist, nextstate)


        #nexttarget = None

        #nextStates =

