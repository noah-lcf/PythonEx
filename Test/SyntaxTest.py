# coding: UTF-8
__author__ = 'Noah'
from collections import defaultdict

counts = defaultdict(lambda: 10)
print counts
counts['foo'] += 1
print counts


class Factorial(dict):
    def __missing__(self, k):
        if k > 1:
            return k * self[k - 1]
        else:
            return 1


factorial = Factorial(counts)
print factorial.get(10)
