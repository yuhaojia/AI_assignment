


class Component(object):
    def __init__(self, Cname):
        self.name = Cname
        #self.numC = -1
        numC = -1
        if Cname == "A":
            numC = 0
        else:
            numC = ord(Cname) - ord("A")

        N_FACTORY = 5

        distanceMatrix = [[0, 1064, 673, 1401, 277],
                          [1064, 0, 958, 1934, 337],
                          [673, 958, 0, 1001, 399],
                          [1401, 1934, 1001, 0, 387],
                          [277, 337, 399, 387, 0]]

        distanceT = []
        for i in range(N_FACTORY):
            distanceT.append(distanceMatrix[numC][i])
        distanceMark = []
        for i in range(N_FACTORY):
            for j in range(N_FACTORY):
                for k in range(N_FACTORY):
                    if distanceMatrix[i][j]>distanceMatrix[i][k]+distanceMatrix[j][k]:
                        kkww = 1


        self.distance = distanceT


