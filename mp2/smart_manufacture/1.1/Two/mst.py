# surroundT = list(surrounds)

        nameChar = curState.name
        i = ord(nameChar)-ord('A')
        elementsAlways = ['A', 'B', 'C', 'D', 'E']

        for nextstate in surround:
            leastH = math.inf
            j = ord(nextstate.name)-ord('A')
            distanceMatrixCharTreeT = []
            elementsTest = deepcopy(nextstate.remaintype)
            visitedList = []
            combinationsList = []
            for element in elementsAlways:
                if element not in elementsTest:
                    visitedList.append(element)
            for numSelect in range():
                comb = combinations(visitedList, numSelect)
                for i in list(comb):
                    combinationsList.append(list(i))


            for numberOfSear in range(len(combinationsList)+1):
                TreeList = deepcopy(nextstate.remaintype)
                if numberOfSear != len(combinationsList):
                    EleTobeadd = combinationsList[numberOfSear]
                    for elementToBeAdded in EleTobeadd:
                        TreeList.append(elementToBeAdded)

                #numberOfSear+=1

                if distanceMatrixCharTreeT:
                    distanceMatrixCharTreeT.pop()
                for ii in range(len(TreeList)):
                    listTT = []
                    for jj in range(len(TreeList)):
                        listTT.append(0)
                    distanceMatrixCharTreeT.append(listTT)

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
                #print("distanceMatrixCharTreeT")
                #print(distanceMatrixCharTreeT)
                if distanceMatrixCharTreeT:
                    distanceMatrixCharTree_csr_matrixT = csr_matrix(distanceMatrixCharTreeT)
                # print(distanceMatrixCharTree_csr_matrix)
                    TcsrT = minimum_spanning_tree(distanceMatrixCharTree_csr_matrixT)
                    TcsrArrayT = TcsrT.toarray().astype(int)

                    SumT = np.sum(TcsrArrayT)
                else:
                    SumT = 0
                if SumT < leastH:
                    leastH = SumT


            ##print(TcsrArrayT)
            ##print(SumT)

            nextstate.G = curState.G + distanceMatrix[i][j]
            nextstate.H = SumT
                #len(nextstate.remaintype)
            nextstate.updateF()
            heapq.heappush(openlist, nextstate)