# encoding: utf-8 
__author__ = 'NOAH'


def compare(filePath1, filePath2):
    """比较文件两个文件，输出没有重复的行 """
    f1 = open(filePath1, "r")
    f2 = open(filePath2, "r")
    s1 = set(a.rstrip().decode("utf-8") for a in f1.readlines())
    s2 = set(a.rstrip().decode("utf-8") for a in f2.readlines())
    return ",".join(s1- s2)


if __name__ == '__main__':
    print compare("../cityAll.txt", "../cityPoi.txt")