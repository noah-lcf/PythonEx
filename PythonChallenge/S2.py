# coding: UTF-8
'''
Created on 2013年11月27日

@author: NOAH
'''

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

dict = [i for i in "abcdefghijklmnopqrstuvwxyz"]

import string
table = string.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
print s.translate(table)

def getLoc(i):
    for j in range(0, len(dict)):
        if i == dict[j]:
            return j
    return -1

print getLoc("a")

res = ""
for i in s:
    j = getLoc(i)
    if j != -1:
        if j == len(dict) - 1:
            res += dict[1]
        elif j == len(dict) - 2:
            res += dict[0]
        else:
            res += dict[j + 2]
    else:
        res += i

print res
if __name__ == '__main__':
    pass
