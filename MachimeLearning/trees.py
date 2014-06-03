# coding: UTF-8
__author__ = 'Noah'
from math import log
import operator
import matplotlib.pyplot as plt
import numpy as np

'''
机器学习实战第3章例子-决策树

最后使用scikit改写


scipy默认使用 gini不纯度评估

书中使用熵评估,这个例子也是基于这个来计算

http://scikit-learn.org/stable/modules/tree.html

优点：
    计算复杂度不高，缺失不敏感


缺点：
    产生过度匹配问题:
    一个假设在训练数据上能够获得比其他假设更好的拟合，但是在训练数据外的数据集上却不能很好的拟合数据。此时我们就叫这个假设出现了overfitting的现象。
    出现这种现象的主要原因是训练数据中存在噪音或者训练数据太少。
    而解决overfit的方法主要有两种：提前停止树的增长或者对已经生成的树按照一定的规则进行后剪枝。

适用范围：

数值型和标称型 




'''

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


def calcShannonEnt(dataSet): 
    """
        计算香农熵，只与各目标特征出现的概率有关，与具体属性无关
        熵越高，混合的数据越多，可以在数据集中添加更多的分类 
    """
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
        shannonEnt -= prob * log(prob, 2)# log(prob, 2):信息定义  prob * log(prob, 2): 信息期望值  这里是计算所有类别可能性对应信息量的和（香农熵）
    print "shannonEnt:%d for dataSet:%s" % (shannonEnt,dataSet)
    return shannonEnt


def createDataSet():
    dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'yes'], [0, 1, 'no'], [0, 1, 'no']]
    # dataSet = [[1, 1, 1], [1, 1, 1], [1, 0, 1], [0, 1, 0], [0, 1, 0]]labels
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


def splitDataSet(dataSet, axis, value):  # 根据给定维的值切分小成小的数据集集合
    """
     Parameters
     ----------
       dataSet:需要分割的数据集
       axis:   切分属性轴（X坐标）
       value:  属性切分值
    """
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduccedFeatVec = featVec[:axis]
            reduccedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reduccedFeatVec)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):  
    """
        选择信息增益最大的维度
    """
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
            print 'newEntropy %f, for axis %d,value %s' % ( newEntropy,  i,value)
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
    if classList.count(classList[0]) == len(classList):  # 类别全部相同停止继续划分子树
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


def classify(inputTree,featLabels,testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict): 
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else: classLabel = valueOfFeat
    return classLabel

from sklearn import tree
import StringIO
import pydot 
def classfyWithScipy(dataSet,labels,dataToClassfy):
    clf = tree.DecisionTreeClassifier(criterion="entropy").fit(dataSet,labels)
    dot_data = StringIO.StringIO() 
    tree.export_graphviz(clf, out_file=dot_data) 
    graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
    graph.write_pdf("entropy.pdf") 
    return clf.predict(dataToClassfy)


from sklearn.datasets import load_iris
dataSet, labels = createDataSet()
print dataSet,labels
print calcShannonEnt(dataSet)
print splitDataSet(dataSet, 0, 1)
print splitDataSet(dataSet, 0, 0)
print chooseBestFeatureToSplit(dataSet)
tree=createTree(dataSet, labels)

orgData=np.array(dataSet)[:,:2]
classes=np.array(dataSet)[:,2]

# classes= np.reshape(classes,(len(classes),1))
print classfyWithScipy(orgData,classes,[[0,0]])
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
dot_data = StringIO.StringIO() 
tree.export_graphviz(clf, out_file=dot_data) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("iris2.pdf") 

# createPlot()

