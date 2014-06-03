<<<<<<< HEAD
# coding: UTF-8
# 求解八码游戏 A*算法 练习
__author__ = 'Noah'

import numpy as np


# 目标状态
targetStat = np.arange(9).reshape((3, 3))


def isComplete(stat):
    """
     是否达到目标状态
    """
    return np.all(stat == targetStat)  # 全为真时返回true


def getIndex(num, stat):
    """
    获得数字的位置
    """
    for colum in range(len(stat)):
        for row in range(len(stat[colum])):
            if num == stat[colum][row]:
                return row, colum
    raise Exception('not find:' + num)


def swapElement(stat, fromX, fromY, toX, toY):
    """
    交换元素位置
    """
    temp = stat[fromX][fromY]
    stat[fromX][fromY] = stat[toX][toY]
    stat[toX][toY] = temp
    return stat


def getNextMove(curNode):
    """
    得到可以移动的动作
    """
    toStatNodes = []
    zeroX, zeroY = getIndex(0, curNode.stat)
    if zeroY < 2:
        stat = swapElement(np.copy(curNode.stat), zeroY, zeroX, zeroY + 1, zeroX)
        toStatNodes.append(Node([zeroX, zeroY + 1, "move up"], curNode,
                                stat,
                                getHn(stat)))  # 可上移
    if zeroY > 0:
        stat = swapElement(np.copy(curNode.stat), zeroY, zeroX, zeroY - 1, zeroX)
        toStatNodes.append(Node([zeroX, zeroY - 1, "move down"], curNode,
                                stat, getHn(stat)))  # 可下移
    if zeroX < 2:
        stat = swapElement(np.copy(curNode.stat), zeroY, zeroX + 1, zeroY, zeroX)
        toStatNodes.append(Node([zeroX + 1, zeroY, "move left"], curNode,
                                stat, getHn(stat)))  # 可左移
    if zeroX > 0:
        stat = swapElement(np.copy(curNode.stat), zeroY, zeroX - 1, zeroY, zeroX)
        toStatNodes.append(Node([zeroX - 1, zeroY, "move right"], curNode, stat, getHn(stat)))  # 可右移
    return toStatNodes


def getMinNode(nodes):
    """
    得到估计万耗散最小结点
    """
    min = 100000
    minNode = None
    for node in nodes:
        if node.cost < min:
            min = node.cost
            minNode = node
    nodes.remove(minNode)
    return minNode


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


class Node(object):
    def __init__(self, action, parent, stat, cost):
        self.parent = parent
        self.stat = stat
        self.action = action
        self.cost = cost

    def __eq__(self, other):
        return np.all(self.stat == other.stat)


def printTrace(curNode):
    traceList = []
    while curNode.parent:
        traceList.append(curNode)
        curNode = curNode.parent
    traceList.reverse()
    trace = ""
    step = 0
    for node in traceList:
        step = step + 1
        trace += " \nstep:" + str(step) + " action: " + str(node.action) + " res:\n" + str(node.stat)
    print trace


def contain(nodeset, nodetarget):
    for node in nodeset:
        if np.all(node.stat == nodetarget.stat):
            return True
    return False


if __name__ == '__main__':
    # testStat = np.arange(9)
    # np.random.shuffle(testStat)
    # testStat = np.reshape(testStat, (3, 3))
    # testStat = np.array([[1, 2, 0], [3, 4, 5], [6, 7, 8]]) # 有些情况是无解的!
    testStat = np.array([[7, 2, 4], [5, 0, 6], [8, 3, 1]])
    print "testStat\n" + str(testStat)
    walkedNodes = []
    exploredNodes = []
    curNode = Node("XXXX", None, testStat, getHn(testStat))
    while not isComplete(curNode.stat):
        walkedNodes.append(curNode)
        nextNodes = getNextMove(curNode)
        exploredNodes.extend([node for node in nextNodes if not contain(walkedNodes, node) ])
        nextNode = getMinNode(exploredNodes)  # 跑到hn值最小的那个状态
        curNode = nextNode
    printTrace(curNode)


=======
# coding: UTF-8
# 求解八码游戏 A*算法 练习
#test commit
__author__ = 'Noah'

import numpy as np


# 目标状态
targetStat = np.arange(9).reshape((3, 3))


def isComplete(stat):
    """
     是否达到目标状态
    """
    return np.all(stat == targetStat)  # 全为真时返回true


def getIndex(num, stat):
    """
    获得数字的位置
    """
    for colum in range(len(stat)):
        for row in range(len(stat[colum])):
            if num == stat[colum][row]:
                return row, colum
    raise Exception('not find:' + num)


def swapElement(stat, fromX, fromY, toX, toY):
    """
    交换元素位置
    """
    temp = stat[fromX][fromY]
    stat[fromX][fromY] = stat[toX][toY]
    stat[toX][toY] = temp
    return stat


def getNextMove(curNode):
    """
    得到可以移动的动作
    """
    toStatNodes = []
    zeroX, zeroY = getIndex(0, curNode.stat)
    if zeroY < 2:
        stat = swapElement(np.copy(curNode.stat), zeroY, zeroX, zeroY + 1, zeroX)
        toStatNodes.append(Node([zeroX, zeroY + 1, "move up"], curNode,
                                stat,
                                getHn(stat)))  # 可上移
    if zeroY > 0:
        stat = swapElement(np.copy(curNode.stat), zeroY, zeroX, zeroY - 1, zeroX)
        toStatNodes.append(Node([zeroX, zeroY - 1, "move down"], curNode,
                                stat, getHn(stat)))  # 可下移
    if zeroX < 2:
        stat = swapElement(np.copy(curNode.stat), zeroY, zeroX + 1, zeroY, zeroX)
        toStatNodes.append(Node([zeroX + 1, zeroY, "move left"], curNode,
                                stat, getHn(stat)))  # 可左移
    if zeroX > 0:
        stat = swapElement(np.copy(curNode.stat), zeroY, zeroX - 1, zeroY, zeroX)
        toStatNodes.append(Node([zeroX - 1, zeroY, "move right"], curNode, stat, getHn(stat)))  # 可右移
    return toStatNodes


def getMinNode(nodes):
    """
    得到估计万耗散最小结点
    """
    min = 100000
    minNode = None
    for node in nodes:
        if node.cost < min:
            min = node.cost
            minNode = node
    nodes.remove(minNode)
    return minNode


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


class Node(object):
    def __init__(self, action, parent, stat, cost):
        self.parent = parent
        self.stat = stat
        self.action = action
        self.cost = cost

    def __eq__(self, other):
        return np.all(self.stat == other.stat)


def printTrace(curNode):
    traceList = []
    while curNode.parent:
        traceList.append(curNode)
        curNode = curNode.parent
    traceList.reverse()
    trace = ""
    step = 0
    for node in traceList:
        step = step + 1
        trace += " \nstep:" + str(step) + " action: " + str(node.action) + " res:\n" + str(node.stat)
    print trace


def contain(nodeset, nodetarget):
    for node in nodeset:
        if np.all(node.stat == nodetarget.stat):
            return True
    return False


if __name__ == '__main__':
    # testStat = np.arange(9)
    # np.random.shuffle(testStat)
    # testStat = np.reshape(testStat, (3, 3))
    # testStat = np.array([[1, 2, 0], [3, 4, 5], [6, 7, 8]]) # 有些情况是无解的!
    testStat = np.array([[7, 2, 4], [5, 0, 6], [8, 3, 1]])
    print "testStat\n" + str(testStat)
    walkedNodes = []
    exploredNodes = []
    curNode = Node("XXXX", None, testStat, getHn(testStat))
    while not isComplete(curNode.stat):
        walkedNodes.append(curNode)
        nextNodes = getNextMove(curNode)
        exploredNodes.extend([node for node in nextNodes if not contain(walkedNodes, node) ])
        nextNode = getMinNode(exploredNodes)  # 跑到hn值最小的那个状态
        curNode = nextNode
    printTrace(curNode)


>>>>>>> 06851892dc9a7ed9caf1aa019ad706e8f3034bc4
