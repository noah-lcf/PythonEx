# coding: UTF-8
# 求解Nqueen 问题 算法练习
__author__ = 'Noah'
import numpy as np

CHESS_MARK = "-1"


def getBlankChessBoard():
    board = np.reshape(np.arange(0, 64), (8, 8))
    for i in range(0, len(board)):
        if (i & 1) == 1:
            board[i] += 1
    return board & 1


def getBoardStatus(array):
    board = getBlankChessBoard()
    for i in range(0, len(array)):
        board[i][array[i] - 1] = CHESS_MARK
    return board


def printPrettyBoard(board):
    for i in range(0, len(board)):
        for j in range(len(board[i])):
            k = board[i][j]
            if (i & 1 == 1 and j & 1 == 0) or (i & 1 == 0 and j & 1 == 1):
                print '\t\033[1;34;47m',
            else:
                print '\t\033[1;37;46m',
            if k == -1:
                print "*",
            print '\t\033[0m',
        print "\n"


def findCells2MatchStraight(posX, posY):
    cells_vertical = []
    cells_horizontal = []
    for i in range(0, 8):
        if i != posX: cells_vertical.append([i, posY])
        if i != posY: cells_horizontal.append([posX, i])
    return cells_vertical, cells_horizontal


def findCells2MatchLean(posX, posY):
    '''
    得到应该计算匹配的棋盘上的点,倾斜
    '''
    cells_left = []
    cells_right = []
    #左向
    indexX = posX
    indexY = posY
    while indexX < 7 and indexY > 0:
        indexX += 1
        indexY -= 1
        cells_left.append([indexX, indexY])
    indexX = posX
    indexY = posY
    while indexX > 0 and indexY < 7:
        indexX -= 1
        indexY += 1
        cells_left.append([indexX, indexY])
        #右向
    indexX = posX
    indexY = posY
    while indexX < 7 and indexY < 7:
        indexX += 1
        indexY += 1
        cells_right.append([indexX, indexY])
    indexX = posX
    indexY = posY
    while indexX > 0 and indexY > 0:
        indexX -= 1
        indexY -= 1
        cells_right.append([indexX, indexY])
    return cells_left, cells_right


def getConfictCells(board):
    matchCells = []
    for columnIndex in range(0, len(board)):
        for rowIndex in range(0, len(board[columnIndex])):
            if board[columnIndex][rowIndex] == -1:
                matchCell = [[rowIndex, columnIndex]]
                cells_l, cells_r = findCells2MatchLean(rowIndex, columnIndex)
                cells_v, cells_h = findCells2MatchStraight(rowIndex, columnIndex)
                cells = cells_l + cells_r + cells_v + cells_h
                for cell in cells:
                    if (board[cell[1]][cell[0]]) == -1 and cell[1] > columnIndex: # 去掉右边判断，可以在find2Match里面进行判断直接不返回左边的
                        matchCell += [[cell[0], cell[1]]]
                if len(matchCell) > 1:
                    matchCells.append(matchCell)
    return matchCells


if __name__ == '__main__':
    # testStat = np.arange(1, 9)
    # np.random.shuffle(testStat)
    testStat = [3, 6, 1, 7, 5, 4, 2, 8]
    print "testStat:%s" % str(testStat)
    boardStatus = getBoardStatus(testStat)
    print printPrettyBoard(boardStatus)
    print getConfictCells(boardStatus)