import numpy as np
import math


class face_classification:

    def __init__(self, trainningimgsfile, trainninglabelsfile, testingimgsfile, testinglabelsfile, k):
        self.str1 = "hello mp3"
        self.trainningimgsfile = trainningimgsfile
        self.trainninglabelsfile = trainninglabelsfile
        self.testingimgsfile = testingimgsfile
        self.testinglabelsfile = testinglabelsfile
        self.k = k

    def readImages(self, filename):
        images = []
        image = []
        linecounter = 0
        with open(filename, 'r') as f:
            for line in f:
                if linecounter == 70:
                    images.append(image)
                    image = []
                    linecounter = 0
                linecounter += 1
                temp = list(line)
                imageline = temp[:60]
                for idx, element in enumerate(imageline):
                    if element == ' ':
                        imageline[idx] = 0
                    else:
                        imageline[idx] = 1
                image.append(imageline)

        images.append(image)
        images = np.asarray(images)

        return images

    # def readImages(self, imagefile):
    #     imageset = []
    #     countLine = 0
    #     image = []
    #     with open(imagefile, 'r') as infile:
    #         for line in infile:
    #             if countLine == 70:
    #                 imageset.append(image)
    #                 image = []
    #                 countLine = 0
    #             countLine += 1
    #             temp = list(line)
    #             image.append(temp[:60])
    #     imageset.append(image)
    #     imageset = np.asarray(imageset)
    #     return imageset

    def readlabels(self, filename):
        labels = []
        with open(filename, 'r') as f:
            for line in f:
                label = int(line.rstrip())
                labels.append(label)
        # labels = labels[:444]
        labels = np.asarray(labels).reshape(-1, 1)
        return labels

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
        # imagesnum = labels.shape[0] * labels.shape[1]
        count = np.zeros((2, 70, 60))
        likelyhoods = np.zeros((2, 70, 60))
        for digit in range(0, 2):
            labelnum = labelscount[digit]
            for i in range(0, 70):
                for j in range(0, 60):
                    for k in labelindex[digit]:
                        if images[k][i][j] == 1:
                            count[digit][i][j] += 1
            # print(count[digit].shape)
            count[digit] = (count[digit] + self.k) / \
                (labelnum + 2 * self.k)
            # print(count[digit])

        for digit in range(0, 2):
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
        trainningimgs = self.readImages(self.trainningimgsfile)
        trainninglabs = self.readlabels(self.trainninglabelsfile)
        labelscount, priors = self.getPriors(trainninglabs)
        likelyhoods = self.getLikelyhoods(
            trainningimgs, trainninglabs, priors, labelscount)
        return priors, likelyhoods

    def testing(self, priors, likelyhoods):
        testingimgs = self.readImages(self.testingimgsfile)
        testinglabs = self.readlabels(self.testinglabelsfile)
        imgnum = testinglabs.shape[0] * testinglabs.shape[1]
        testresult = np.zeros((imgnum, 2))
        likelyhoods0 = 1 - likelyhoods
        for imgidx, image in enumerate(testingimgs):
            for c in range(0, 2):
                lh = np.absolute(likelyhoods0[c] - image)
                testresult[imgidx][c] += math.log(priors[c])
                loglikelyhoods_helper = np.log(lh)
                # print(np.sum(loglikelyhoods_helper))
                testresult[imgidx][c] += np.sum(loglikelyhoods_helper)
                # print(testresult[imgidx][c])
        # print(testresult)
        MAP = np.argmax(testresult, axis=1).reshape(-1, 1)
        return testresult, MAP, testinglabs

    def evaluation(self, testinglabels, MAP, testresult):
        confusionmatrix = np.zeros((2, 2))
        labidx = self.getLabelIndex(testinglabels)
        labsnum = self.getLabelNum(testinglabels)
        # countsum = 0
        # print('type of labsnum', type(labsnum))
        for c in range(0, 2):
            c_num = labsnum[c]
            c_idxs = labidx[c]

            for i in range(0, 2):
                count = 0
                for c_idx in c_idxs:
                    if MAP[c_idx][0] == i:
                        count += 1
                        # countsum += 1
                confusionmatrix[c][i] = count / c_num

        # posteriorprob = np.zeros((10, 2))
        # for c in range(0, 10):
        #     c_idxs = labidx[c]
        #     highest = -math.inf
        #     lowest = math.inf
        #     for c_idx in c_idxs:
        #         if testresult[c_idx][c] > highest:
        #             highest = testresult[c_idx][c]
        #         if testresult[c_idx][c] < lowest:
        #             lowest = testresult[c_idx][c]
        #     posteriorprob[c][0] = highest
        #     posteriorprob[c][1] = lowest
        # confusionmatrix = 0
        # posteriorprob=0
        imgnum = testinglabs.shape[0] * testinglabs.shape[1]
        countsum = 0
        for idx in range(imgnum):
            if MAP[idx][0] == testinglabels[idx][0]:
                countsum += 1

        overall_accuracy = countsum / imgnum

        return confusionmatrix, overall_accuracy


trainningimgsfile = 'facedatatrain'
trainninglabelsfile = 'facedatatrainlabels'
testingimgsfile = 'facedatatest'
testinglabelsfile = 'facedatatestlabels'
k = 10
f = face_classification(trainningimgsfile, trainninglabelsfile,
                        testingimgsfile, testinglabelsfile, k)
trainimgs = f.readImages(trainningimgsfile)
trainlabels = f.readlabels(trainninglabelsfile)
testimgs = f.readImages(testingimgsfile)
testlabels = f.readlabels(testinglabelsfile)
# print(trainimgs.shape)
# print(trainlabels.shape)
# print(testimgs.shape)
# print(testlabels.shape)
priors, likelyhoods = f.trainning()
testresult, MAP, testinglabs = f.testing(priors, likelyhoods)
confusionmatrix, overall_accuracy = f.evaluation(testinglabs, MAP, testresult)
print('overall_accuracy is: ',overall_accuracy)
print('confusionmatrix is : \n', confusionmatrix)