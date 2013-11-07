# coding: UTF-8
__author__ = 'Noah'
from math import log
import operator
import matplotlib.pyplot as plt


decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")


def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords="axes fraction", xytext=centerPt, textcoords="axes fraction",
                            va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)


def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree(firstStr)
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs


def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys:
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth


    def createPlot():
        fig = plt.figure(1, facecolor="white")
        fig.clf()
        createPlot.ax1 = plt.subplot(111, frameon=False)
        plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
        plotNode('a leaf node', (0.8, .01), (0.3, 0.8), leafNode)
        plt.show()


    def calcShannonEnt(dataSet):  # 计算香农熵，与目标特征出现的概率有关
        numEntries = len(dataSet)
        labelCounts = {}
        for featVec in dataSet:
            currentLabel = featVec[-1]
            if currentLabel not in labelCounts.keys():
                labelCounts[currentLabel] = 0
            labelCounts[currentLabel] += 1
        shannonEnt = 0.0
        for key in labelCounts:
            prob = float(labelCounts[key]) / numEntries
            shannonEnt -= prob * log(prob, 2)
        return shannonEnt


    def createDataSet():
        dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'yes'], [0, 1, 'no'], [0, 1, 'no']]
        labels = ['no surfacing', 'flippers']
        return dataSet, labels


    def splitDataSet(dataSet, axis, value):  # 根据给定维的值切分小成小的数据集集合
        retDataSet = []
        for featVec in dataSet:
            if featVec[axis] == value:
                reduccedFeatVec = featVec[:axis]
                reduccedFeatVec.extend(featVec[axis + 1:])
                retDataSet.append(reduccedFeatVec)
        return retDataSet


    def chooseBestFeatureToSplit(dataSet):  # 选择信息增益最大的维度
        numFeatures = len(dataSet[0]) - 1
        baseEntropy = calcShannonEnt(dataSet)
        print "baseEntropy %f" % baseEntropy
        bestInfoGain = 0.0
        bestFeature = -1
        for i in range(numFeatures):
            featList = [example[i] for example in dataSet]
            uniqueVals = set(featList)
            newEntropy = 0.0
            for value in uniqueVals:
                subDataSet = splitDataSet(dataSet, i, value)
                prob = len(subDataSet) / float(len(dataSet))
                newEntropy += prob * calcShannonEnt(subDataSet)
            infoGain = baseEntropy - newEntropy
            print 'newEntropy %f,infoGain %f for axis %d,' % ( newEntropy, infoGain, i)
            if (infoGain > bestInfoGain):
                bestInfoGain = infoGain
                bestFeature = i
        return bestFeature


    def majorityCnt(classList):
        classCount = {}
        for vote in classList:
            if vote not in classCount.keys():
                classCount[vote] = 0
            else:
                classCount = -1
        sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0]


    def createTree(dataSet, labels):
        classList = [example[-1] for example in dataSet]

        if classList.count(classList[0]) == len(classList):  # 类别全部相同停止继续划分
            return classList[0]
        if len(dataSet[0]) == 1:  # 遍历完所有特征时返回出现次数最多的
            return majorityCnt(classList)
        bestFeat = chooseBestFeatureToSplit(dataSet)
        bestFeatLabel = labels[bestFeat]
        myTree = {bestFeatLabel: {}}
        del (labels[bestFeat])
        featValues = [example[bestFeat] for example in dataSet]
        uniqueVals = set(featValues)
        for value in uniqueVals:
            subLabels = labels[:]
            myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
        return myTree




    if __name__ == '__main__':
    # dataSet, labels = createDataSet()
    # shannonEnt = calcShannonEnt(dataSet)
    # print shannonEnt
    # splitedDataSet = splitDataSet(dataSet, 0, 1)
    # print splitedDataSet
    # splitedDataSet = splitDataSet(dataSet, 1, 0)
    # print splitedDataSet
    # print chooseBestFeatureToSplit(dataSet)
        createPlot()