# coding: UTF-8
#http://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F#Python
__author__ = 'Noah'
import sys
import random

lenth = 30

def qsort(arr, left, right):
    key = arr[right]
    lp = left
    rp = right
    if lp == rp:
        return
    while True:
        while (arr[lp] >= key) and (rp > lp):
            lp = lp + 1
        while (arr[rp] <= key) and (rp > lp):
            rp = rp - 1
        arr[lp], arr[rp] = arr[rp], arr[lp]
        if lp >= rp:
            break
    arr[rp], arr[right] = arr[right], arr[rp]
    if left < lp:
        qsort(arr, left, lp - 1)
    qsort(arr, rp, right)


def main():
    arr = []
    sys.setrecursionlimit(100000)
    for i in range(lenth):
        arr.append(random.randint(0, 1000))
    print arr
    qsort(arr, 0, lenth - 1)
    print arr


if __name__ == '__main__':
    for i in range(10):
        main()