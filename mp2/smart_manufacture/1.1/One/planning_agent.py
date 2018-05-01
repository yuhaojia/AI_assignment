

from State import *
import sys
import heapq
from copy import deepcopy
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import numpy as np
from itertools import combinations


#from scipy.sparse import csr_matrix.getnnz

def miles(Start):
    Widgets = [['A', 'E', 'D', 'C', 'A', '*'],
               ['B', 'E', 'A', 'C', 'D', '*'],
               ['B', 'A', 'B', 'C', 'E', '*'],
               ['D', 'A', 'D', 'B', 'D', '*'],
               ['B', 'E', 'C', 'B', 'D', '*']]
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
    NUMBERN = 6
    openlist = []
    unvisitedelement = list(Widgets)
    count = 0
    # step_sum = 0
    # distance = []
    # iter = [0, 0, 0, 0, 0]
    unvisited = ['A', 'B', 'C', 'D', 'E']
    # visited = []
    remainNum = [0, 0, 0, 0, 0]
    for i in range(KindOfElement):
        for j in range(KindOfElement):
            k = ord(Widgets[i][j]) - ord("A")
            remainNum[k] += 1
    print(remainNum)
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
    distanceMatrixCharTree = []
    for ii in range(len(unvisited)):
        listT = []
        for jj in range(len(unvisited)):
            listT.append(0)
        distanceMatrixCharTree.append(listT)

    ##print(distanceMatrixCharTree)
    for chara in unvisited:
        iChar = ord(chara)-ord('A')
        for numCh in unvisited:
            inumChar = ord(numCh)-ord('A')
            #if iChar == inumChar:
            #    distanceMatrixCharTree[][]=0
            if iChar > inumChar:
                distanceMatrixCharTree[inumChar][iChar] = distanceMatrix[inumChar][iChar]
            else:
                distanceMatrixCharTree[iChar][inumChar] = distanceMatrix[iChar][inumChar]
    ##print(distanceMatrixCharTree)
    distanceMatrixCharTree_csr_matrix = csr_matrix(distanceMatrixCharTree)
    #print(distanceMatrixCharTree_csr_matrix)
    Tcsr = minimum_spanning_tree(distanceMatrixCharTree_csr_matrix)
    TcsrArray = Tcsr.toarray().astype(int)

    Sum = np.sum(TcsrArray)
    ##print(TcsrArray)
    ##print(Sum)

    startState.H = Sum
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
        surroundPossible = []
        elems = deepcopy(curState.remainelements)
        if surroundPossible:
            surroundPossible.pop()
        for iikkii in range(KindOfElement):
            PossibleName = chr(ord('A') + iikkii)
            for elem in elems:
                if PossibleName == elem[0]:
                    surroundPossible.append(PossibleName)

        ##print("Surround")
        for i in range(KindOfElement):
            NextName = chr(ord('A') + i)
            # print(curState.name)
            Nextremainelements = deepcopy(curState.remainelements)
            # print(Nextremainelements)
            NextremainNum = deepcopy(curState.remainNum)
            Nextremaintype = deepcopy(curState.remaintype)
            Newpath = deepcopy(curState.path)
            if NextName in surroundPossible and NextName != curState.name and NextName in curState.remaintype and curState.remainNum[i] > 0:

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
        nameChar = curState.name
        ihahaha = ord(nameChar) - ord('A')
        #elementsAlways = ['A', 'B', 'C', 'D', 'E']

        for nextstate in surround:
            leastH = math.inf
            jhahaha = ord(nextstate.name) - ord('A')

            #if distanceMatrixCharTreeT:
            #    distanceMatrixCharTreeT.pop()
            elementsTest = deepcopy(nextstate.remaintype)
            visitedList = []
            combinationsList = []
            for element in elementsAlways:
                if element not in elementsTest:
                    visitedList.append(element)
            for numSelect in range(len(visitedList)):

                comb = combinations(visitedList, numSelect)
                for i in list(comb):
                    combinationsList.append(list(i))

            for numberOfSear in range(len(combinationsList) + 1):
                distanceMatrixCharTreeT = []
                if distanceMatrixCharTreeT:
                    distanceMatrixCharTreeT.pop()
                TreeList = deepcopy(nextstate.remaintype)
                if numberOfSear != len(combinationsList):
                    EleTobeadd = combinationsList[numberOfSear]
                    for elementToBeAdded in EleTobeadd:
                        TreeList.append(elementToBeAdded)

                if distanceMatrixCharTreeT:
                    distanceMatrixCharTreeT.pop()
                numTreeList = len(TreeList)
                print(numTreeList)
                for iij in range(numTreeList):
                    listTT = []
                    if listTT:
                        listTT.pop()
                    for jjj in range(numTreeList):
                        listTT.append(0)
                    distanceMatrixCharTreeT.append(listTT)
                print("AAAAA")
                print(distanceMatrixCharTreeT)

                ##print(distanceMatrixCharTreeT)
                BigI = 0
                ListRemain1 = deepcopy(TreeList)
                ListRemain2 = deepcopy(TreeList)
                for charaT in ListRemain1:
                    iCharT = ord(charaT) - ord('A')

                    BigJ = 0
                    for numChT in ListRemain2:
                        inumCharT = ord(numChT) - ord('A')
                        # if iChar == inumChar:
                        #    distanceMatrixCharTree[][]=0
                        if BigI > BigJ:
                            distanceMatrixCharTreeT[BigJ][BigI] = distanceMatrix[inumCharT][iCharT]
                        else:
                            distanceMatrixCharTreeT[BigI][BigJ] = distanceMatrix[iCharT][inumCharT]
                        BigJ += 1
                    BigI += 1
                # print("distanceMatrixCharTreeT")
                # print(distanceMatrixCharTreeT)
                if distanceMatrixCharTreeT:
                    distanceMatrixCharTree_csr_matrixT = csr_matrix(distanceMatrixCharTreeT)
                    #print(distanceMatrixCharTree_csr_matrix)
                    #print("AA")
                    print(distanceMatrixCharTreeT)
                    print(distanceMatrixCharTree_csr_matrixT.shape)
                    TcsrT = minimum_spanning_tree(distanceMatrixCharTree_csr_matrixT)
                    TcsrArrayT = TcsrT.toarray().astype(int)

                    SumT = np.sum(TcsrArrayT)
                else:
                    SumT = 0
                if SumT < leastH:
                    leastH = SumT

                if distanceMatrixCharTreeT:
                    distanceMatrixCharTreeT.pop()
            ##print(TcsrArrayT)
            ##print(SumT)

            nextstate.G = curState.G + distanceMatrix[ihahaha][jhahaha]
            nextstate.H = SumT
            # len(nextstate.remaintype)
            nextstate.updateF()
            heapq.heappush(openlist, nextstate)

    pass

def step(Start):
    Widgets = [['A', 'E', 'D', 'C', 'A','*'],
              ['B', 'E', 'A', 'C', 'D','*'],
              ['B', 'A', 'B', 'C', 'E','*'],
              ['D', 'A', 'D', 'B', 'D','*'],
              ['B', 'E', 'C', 'B', 'D','*']]

    #Widgets = [['A', 'E', 'D', 'C', 'A'],
    #          ['B', 'E', 'A', 'C', 'D'],
    #          ['B', 'A', 'B', 'C', 'E'],
    #          ['D', 'A', 'D', 'B', 'D'],
    #          ['B', 'E', 'C', 'B', 'D']]

    KindOfElement = 5
    NumberN = 5
    openlist = []
    unvisitedelement = list(Widgets)
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
    print(unvisitedelement)
    print(remainNum)
    NumSTART = len(unvisitedelement)
    if Start in unvisited and remainNum[ord(Start)-ord('A')] > 0:
        for j in range(NumSTART):
            if unvisitedelement[j][0] == Start:
                unvisitedelement[j].pop(0)
                remainNum[ord(Start)-ord('A')]-=1
        visitedpath.append(Start)
        if remainNum[ord(Start)-ord('A')] == 0:
            unvisited.remove(Start)
    print(unvisitedelement)
    print(remainNum)
    print(unvisited)
    print(visitedpath)
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
        print("current")
        print(curState.name)
        print(curState.remainNum)
        print(curState.remainelements)
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
        print("Surround")
        for i in range(KindOfElement):
            NextName = chr(ord('A') + i)
            print("Next")
            print(NextName)
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
                print(Newpath)
                if NextremainNum[i] == 0:
                    Nextremaintype.remove(NextName)
                NextState = State(NextName, Nextremainelements, Nextremaintype, NextremainNum, Newpath)
                surround.append(NextState)
                #Nextremainelements.pop()
                print(Nextremainelements)
        print(len(surround))

        #surrounds = curState.getSurr()
        #if len(surround)<=0:
        #    print("a_star expand points: ", count)
        #    kw = deepcopy(curState.remainelements)
        #    print(kw)
        #    return curState.path

        if len(curState.remaintype) == 0:
            print("a_star expand points: ", count)
            print(curState.name)
            kw = deepcopy(curState.remaintype)
            print("remain")
            print(kw)
            print("remain")
            print(curState.G+1)
            return curState.path

        #surroundT = list(surrounds)
        leastF = math.inf
        for nextstate in surround:
            nextstate.G = curState.G + 1
            nextstate.H = len(nextstate.remaintype)
            nextstate.updateF()
            heapq.heappush(openlist, nextstate)


        #nexttarget = None

        #nextStates =

