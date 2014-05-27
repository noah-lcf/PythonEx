# coding: UTF-8
__author__ = 'Noah'
from numpy import *
import operator
"""
  机器学习实战第一章的列子,加了一些地方的注释，最后有与scipy现成算法的一个比较--scipy正确性要高
  
  优势：
  简单有效 
  


  劣势：

  K邻近算法必须保存全部数据，占空间
  必须计算每个点的距离 ，耗时（scipy 会构建KD-tree或ball-tree，缩小搜索范围 Todo:kd-tree ball-tree区别？）
  无法给点数据的基础结构信息



"""

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [2, 1], [4, 0.1]])
    labels = ['A', 'B', 'C', 'D']
    return group, labels

#计算所有点与当前点的欧式距离，返回最近顺序为K的样本的类别（其实这里可以直接返回最小）
def classify0(inX, dataSet, labels, k):
    """
    inX:待分类向量
    dataSet:全部样本
    lables:全部样本标签
    k:返回最近顺序为K的样本类别
    """
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
    """
    这里可以直接用numpy自带的方法,再把数据和标签截出来
    np.genfromtxt(filename, delimiter=',')
    data=data[:,:-1]
    label=data[:,-1]
    """
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



def autoNorm(dataSet):
    """
    归一化第一列数值，使之分布在0-1之间
    """
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    #tile生成一个最小值矩阵和范围矩阵
    normDataSet = dataSet - tile(minVals, (m, 1))  
    normDataSet = normDataSet / tile(ranges, (m, 1))   #element wise divide
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


def printDateScatter():
    datingDataMat, datingLabels = file2matrix("../datingTestSet2.txt")
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
    plt.show()

#用scipy改写
def classifyWithScipy():
    hoRatio = 0.50 
    from sklearn import neighbors
    #详见： http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier
    clf = neighbors.KNeighborsClassifier() 
    datingDataMat, datingLabels = file2matrix("../datingTestSet2.txt")
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        clf.fit(normMat[numTestVecs:m, :], datingLabels[numTestVecs:m])
        classifierResult=clf.predict(normMat[i, :])
        # print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print "the total error rate is: %f" % (errorCount / float(numTestVecs))
    print errorCount

    

# group, label = createDataSet()
# print classify0([0.1,0.2],group, label, 1)

datingClassTest()
classifyWithScipy()
# datingClassTest()



