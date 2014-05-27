# coding: UTF-8
__author__ = 'Noah'
from numpy import *
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [2, 1], [4, 0.1]])
    labels = ['A', 'B', 'C', 'D']
    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector



#归一化第一列数值，使之分布在0-1之间
def autoNorm(dataSet):
    print dataSet[:,0]
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))dataSet
    m = dataSet.shape[0]
    #tile生成一个最小值矩阵和范围矩阵
    normDataSet = dataSet - tile(minVals, (m, 1))
    #这里不是矩阵相除，特征值相除
    normDataSet = normDataSet / tile(ranges, (m, 1))   #element wise divide
    print normDataSet[:,0]
    return normDataSet, ranges, minVals


def datingClassTest():
    hoRatio = 0.50      #hold out 10%
    datingDataMat, datingLabels = file2matrix('../datingTestSet2.txt')       #load data setfrom file
    # print datingDataMat[:0]
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        # print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print "the total error rate is: %f" % (errorCount / float(numTestVecs))
    print errorCount


datingClassTest()
# group, label = createDataSet()
# print classify0([0.1,0.1],group, label, 1)
datingDataMat, datingLabels = file2matrix("../datingTestSet2.txt")
# print datingDataMat

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
# plt.show()
# print(autoNorm(datingDataMat))