# coding: UTF-8
__author__ = 'Noah'
import numpy as np

CHESS_MARK = "-1"


def getBlankChessBoard():
    board = np.reshape(np.arange(0, 64), (8, 8))
    for i in range(0, len(board)):
        if (i & 1) == 1:
            board[i] += 1
    return board & 1


def getBoradStatus(array):
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

def findCells2Match(posX,posY):
    cells=[]


if __name__ == '__main__':
    # testStat = np.arange(1, 9)
    # np.random.shuffle(testStat)
    testStat = [3, 6, 1, 7, 5, 4, 2, 8]
    print testStat
    print printPrettyBoard(getBoradStatus(testStat))