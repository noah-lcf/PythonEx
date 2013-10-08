# coding: UTF-8
__author__ = 'Noah'
from collections import defaultdict
import numpy as np


class A(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


a = A("aaa")
a1 = A("aaa")
print a == a1
b = A("bbb")
b1 = A("bbb")
print a == b
aSet = {a, a1,a}
print aSet
aSet.remove(a)
print aSet

def contain(list, target):
    for i in list:
        if np.all(i == target):
            return True
    return False


def remove(list, target):
    for i in range(len(list)):
        if np.all(list[i] == target):
            del list[i]


def addUnique(list, listToAdd):
    for i in listToAdd:
        if not contain(list, i):
            list.extend(i)


b = []
b.extend([[[1, 2], "a"], [[1, 3], "a"]])
print b
b.remove([[1, 2], "a"])
print b

targetStat = np.arange(9).reshape((3, 3))
a = []
c = []
testStat = np.arange(9)
np.random.shuffle(testStat)
testStat = np.reshape(testStat, (3, 3))
a.append(testStat)
c.append(testStat)
addUnique(a, c)
print a
a.append(targetStat)
c.append(targetStat)
addUnique(a, c)
print a


class Factorial(dict):
    def __missing__(self, k):
        if k > 1:
            return k * self[k - 1]
        else:
            return 1


def testFact():
    counts = defaultdict(lambda: 10)
    print counts
    counts['foo'] += 1
    print counts
    factorial = Factorial(counts)

    print factorial.get(10)

