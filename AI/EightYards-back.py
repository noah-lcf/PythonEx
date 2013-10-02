# coding: UTF-8
#求解八码游戏 A*算法 练习
__author__ = 'Noah'

import numpy as np


# 目标状态
targetStat = np.arange(9).reshape((3, 3))


def isComplete(stat):
    """
     是否达到目标状态
    """
    return np.all(stat == targetStat)  # 全为真时返回true


def contain(list, target):
    for i in list:
        if np.all(i == target):
            return True
    return False


def remove(list, target):
    for i in range(len(list)):
        if np.all(list[i] == target):
            del list[i]
            return list


def removeAll(list, listToRemove):
    for target in listToRemove:
        remove(list, target)
    return list


def addUnique(list, listToAdd):
    for i in listToAdd:
        if not contain(list, i):
            list.append(i)


def getIndex(num, stat):
    """
    获得数字的位置
    """
    for colum in range(len(stat)):
        for row in range(len(stat[colum])):
            if num == stat[colum][row]:
                return row, colum
    raise Exception('not find:' + num)


def swapElement(stat, zeroX, zeroY, toX, toY):
    stat[zeroX][zeroY] = stat[toX][toY]
    stat[toX][toY] = 0
    return stat


def getNextMove(stat):
    toStatList = []
    stepList = []
    zeroX, zeroY = getIndex(0, stat)
    if zeroY < 2:
        toStatList.append(swapElement(np.copy(stat), zeroY, zeroX, zeroY + 1, zeroX))    # 可上移
        stepList.append([zeroX, zeroY + 1, "up"])
    if zeroY > 0:
        toStatList.append(swapElement(np.copy(stat), zeroY, zeroX, zeroY - 1, zeroX))   # 可下移
        stepList.append([zeroX, zeroY - 1, "down"])
    if zeroX < 2:
        toStatList.append(swapElement(np.copy(stat), zeroY, zeroX, zeroY, zeroX + 1))   # 可左移
        stepList.append([zeroX + 1, zeroY, "left"])
    if zeroX > 0:
        toStatList.append(swapElement(np.copy(stat), zeroY, zeroX, zeroY, zeroX - 1))   # 可右移
        stepList.append([zeroX - 1, zeroY, "right"])
    return toStatList, stepList


def getMaxHn(stats):
    min = 10000
    index = 0
    for i in range(len(stats)):
        hn = getHn(stats[i])
        if hn < min:
            min = hn
            index = i
    return stats[index]


def getHn(stat):
    """
     得到状态的估计耗散
    """
    Hn = 0
    for colum in range(len(stat)):
        for row in range(len(stat[colum])):
            rrow, rcolum = getIndex(stat[colum][row], targetStat)
            Hn += abs(rcolum - colum) + abs(rrow - row)  # 曼哈顿距离
    return Hn


class Node:
    def __init__(self, action, parent, stat):
        self.parent = parent
        self.stat = stat
        self.action = action


if __name__ == '__main__':
    # testStat = np.arange(9)
    # np.random.shuffle(testStat)
    # testStat = np.reshape(testStat, (3, 3))

    testStat = np.array([[7, 2, 4], [5, 0, 6], [8, 3, 1]])
    print "testStat\n" + str(testStat)

    walkedStats = []
    walkedSteps = []
    exploredStats = []
    exploredSteps = []
    curStat = testStat
    searchStats = []
    parent = Node("", "", curStat)
    # try:
    while not isComplete(curStat):
        walkedStats.append(curStat)
        nextStats, nextSteps = getNextMove(curStat)
        addUnique(exploredStats, nextStats)
        # addUnique(exploredSteps, nextSteps)
        nextStat = getMaxHn(removeAll(exploredStats, walkedStats))  # 跑到hn值最小的那个状态
        # searchStats = list(exploredStats)
        # while contain(walkedStats, nextStat):               # 如果已经跑过，找第二大的
        #     searchStats = remove(searchStats, nextStat)
        #     # print "skip walk to:\n" + str(nextStat)
        #     if len(nextStats) == 0: raise Exception(
        #         "'all walked!\nsteps:\n" + str(walkedSteps) + "\nstats:\n" + str(walkedStats))
        #     nextStat = getMaxHn(searchStats)
        print "walk:"  "\ncur:\n" + str(curStat) + "\nto:\n" + str(nextStat)
        curStat = nextStat
        # except  Exception,e:
    #     import sys
    #     print sys.exc_info()
    #     print "error!\n" + "steps:\n" + str(walkedSteps) + "\nstats:\n" + str(walkedStats)
    print "success!\n" + "\nstats:\n" + str(walkedStats)

