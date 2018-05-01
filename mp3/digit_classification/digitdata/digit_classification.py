import numpy as np
import math
from matplotlib import pyplot as plt


class digit_clasification:

    def __init__(self, trainningfile, testingfile, k):
        self.str1 = "hello mp3"
        self.trainningfile = trainningfile
        self.testingfile = testingfile
        self.k = k

    def readData(self, filename):
        images = []
        image = []
        labels = []
        linecounter = 0
        with open(filename, 'r') as f:
            for line in f:
                if linecounter != 32:
                    linecounter += 1
                    imageline = line.rstrip()
                    image.append(list(map(int, imageline)))
                else:
                    linecounter = 0
                    labels.append(int(line.rstrip()))
                    images.append(image)
                    image = []
        images = np.asarray(images)
        labels = np.asarray(labels).reshape(-1, 1)
        return images, labels

    def getPriors(self, labels):
        labelsnum = labels.shape[0] * labels.shape[1]
        labelcountdict = {}
        priors = {}
        labels = labels.flatten().tolist()
        for label in labels:
            if label not in labelcountdict.keys():
                labelcountdict[label] = 1
            else:
                labelcountdict[label] += 1
        for k, v in labelcountdict.items():
            priors[k] = v / labelsnum

        return labelcountdict, priors

    def getLikelyhoods(self, images, labels, priors, labelscount):
        labelindex = self.getLabelIndex(labels)
        imagesnum = labels.shape[0] * labels.shape[1]
        count = np.zeros((10, 32, 32))
        likelyhoods = np.zeros((10, 32, 32))
        for digit in range(0, 10):
            labelnum = labelscount[digit]
            for i in range(0, 32):
                for j in range(0, 32):
                    for k in labelindex[digit]:
                        if images[k][i][j] == 1:
                            count[digit][i][j] += 1
            # print(count[digit].shape)
            count[digit] = (count[digit] + self.k) / \
                (labelnum + 2 * self.k)
            # print(count[digit])

        for digit in range(0, 10):
            likelyhoods[digit] = count[digit] * priors[digit]
        return likelyhoods

    def getLabelIndex(self, labels):
        labelindex = {}
        labels = labels.flatten().tolist()
        for index, label in enumerate(labels):
            if label not in labelindex.keys():
                # labellist = list(index)
                labellist = []
                labellist.append(index)
                labelindex[label] = labellist
            else:
                labelindex[label].append(index)

        return labelindex

    def getLabelNum(self, labels):
        labnum = {}
        labels = labels.flatten().tolist()
        # print(labels)
        for label in labels:
            if label not in labnum:
                labnum[label] = 1
            else:
                labnum[label] += 1
        return labnum

    def trainning(self):
        trainningimgs, trainninglabs = self.readData(self.trainningfile)
        labelscount, priors = self.getPriors(trainninglabs)
        likelyhoods = self.getLikelyhoods(
            trainningimgs, trainninglabs, priors, labelscount)
        return priors, likelyhoods

    def testing(self, priors, likelyhoods):
        testingimgs, testinglabs = self.readData(self.testingfile)
        imgnum = testinglabs.shape[0] * testinglabs.shape[1]
        testresult = np.zeros((imgnum, 10))
        likelyhoods0 = 1 - likelyhoods
        # MAP = np.zeros((imgnum, 1))
        for imgidx, image in enumerate(testingimgs):
            for c in range(0, 10):
                lh = np.absolute(likelyhoods0[c] - image)
                testresult[imgidx][c] += math.log(priors[c])
                # print(testresult[imgidx][c])
                loglikelyhoods_helper = np.log(lh)
                # print(np.sum(loglikelyhoods_helper))
                testresult[imgidx][c] += np.sum(loglikelyhoods_helper)
                # print(testresult[imgidx][c])
        # print(testresult)
        MAP = np.argmax(testresult, axis=1).reshape(-1, 1)
        return testresult, MAP, testinglabs

    def evaluation(self, testinglabels, MAP, testresult):
        confusionmatrix = np.zeros((10, 10))
        labidx = self.getLabelIndex(testinglabels)
        labsnum = self.getLabelNum(testinglabels)
        # countsum = 0
        # print('type of labsnum', type(labsnum))
        for c in range(0, 10):
            c_num = labsnum[c]
            c_idxs = labidx[c]

            for i in range(0, 10):
                count = 0
                for c_idx in c_idxs:
                    if MAP[c_idx][0] == i:
                        count += 1
                        # countsum += 1
                confusionmatrix[c][i] = count / c_num

        posteriorprob = np.zeros((10, 2))
        for c in range(0, 10):
            c_idxs = labidx[c]
            highest = -math.inf
            lowest = math.inf
            highestid = 0
            lowestid = 0
            for c_idx in c_idxs:
                if testresult[c_idx][c] > highest:
                    highest = testresult[c_idx][c]
                    highestid = c_idx
                if testresult[c_idx][c] < lowest:
                    lowest = testresult[c_idx][c]
                    lowestid = c_idx
            posteriorprob[c][0] = highestid
            posteriorprob[c][1] = lowestid

        imgnum = testinglabs.shape[0] * testinglabs.shape[1]
        countsum = 0
        for idx in range(imgnum):
            if MAP[idx][0] == testinglabels[idx][0]:
                countsum += 1

        overall_accuracy = countsum / imgnum

        return confusionmatrix, posteriorprob, overall_accuracy

    def getOdds_ratio(self, likelyhoods, confusionmatrix):
        new_cm = np.copy(confusionmatrix)
        oddsratios = []
        for i in range(0, 10):
            new_cm[i][i] = 0
        new_cm = new_cm.flatten()
        ind = np.argpartition(new_cm, -4)[-4:]
        for j in range(0, 4):
            label1 = ind[j] // 10
            label2 = ind[j] % 10
            img1 = likelyhoods[label1]
            img2 = likelyhoods[label2]
            # print('likelyhoods of ',label1, ': \n',img1)
            np.savetxt('outfile1.csv', img1, fmt='%1.3e', delimiter=",")
            # print('likelyhoods of ',label2, ': \n',img2)
            np.savetxt('outfile2.csv', img2, fmt='%1.3e', delimiter=",")

            plot1 = np.asarray(img1)
            plt.imshow(plot1, interpolation='nearest')
            plt.xlabel(label1)
            plt.ylabel('pair' + str(j))
            plt.show()
            plot2 = np.asarray(img2)
            plt.imshow(plot2, interpolation='nearest')
            plt.xlabel(label2)
            plt.ylabel('pair' + str(j))
            plt.show()

            oddsratio = np.zeros((32, 32))
            for row in range(0, 32):
                for col in range(0, 32):
                    # oddsratio[row][col] = likelyhoods[label1][
                    #     row][col] / likelyhoods[label2][row][col]
                    oddsratio[row][col] = math.log(likelyhoods[label1][
                        row][col] / likelyhoods[label2][row][col])
            plt.imshow(oddsratio, interpolation='nearest')
            plt.show()
            oddsratio = oddsratio.tolist()
            oddsratios.append(oddsratio)
        return oddsratios

# trainningfile = '/Users/haowenjiang/Doc/cs/uiuc/AI/assignment/mp3/digit_classification/digitdata/optdigits-orig_train.txt'
# testingfile = '/Users/haowenjiang/Doc/cs/uiuc/AI/assignment/mp3/digit_classification/digitdata/optdigits-orig_test.txt'
trainningfile = 'optdigits-orig_train.txt'
testingfile = 'optdigits-orig_test.txt'
# k = 0
# while k < 1.0:
#     k = k + 0.1
#     c = digit_clasification(trainningfile, testingfile, k)
#     priors, likelyhoods = c.trainning()
#     testresult, MAP, testinglabs = c.testing(priors, likelyhoods)
#     confusionmatrix, posteriorprob, overall_accuracy = c.evaluation(
#         testinglabs, MAP, testresult)
#     print('k value is ', k, 'overall_accuracy is ', overall_accuracy)
# oddsratio = c.getOdds_ratio(likelyhoods, confusionmatrix)

k = 0.1
c = digit_clasification(trainningfile, testingfile, k)
priors, likelyhoods = c.trainning()
testresult, MAP, testinglabs = c.testing(priors, likelyhoods)
confusionmatrix, posteriorprob, overall_accuracy = c.evaluation(
    testinglabs, MAP, testresult)
# print('k value is ', k, 'overall_accuracy is ', overall_accuracy)
# print(confusionmatrix)
# for i in range(10):
#     print(confusionmatrix[i][i])
# np.savetxt('outfile.txt', confusionmatrix, fmt='%1.3e')
# print(posteriorprob)
# print(likelyhoods)
oddsratio = c.getOdds_ratio(likelyhoods, confusionmatrix)
np_odds = np.asarray(oddsratio)
# print(np_odds.shape)
for i in range(4):
    temp = np_odds[i]
    file = '{}{}{}'.format('outfile', i, '.csv')
    np.savetxt(file, temp, fmt='%1.3e', delimiter=",")
