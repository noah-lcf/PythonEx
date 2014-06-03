
# coding: UTF-8
'''
Created on 2013年12月5日

@author: Administrator
'''
import StringIO
import urllib2

passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, "http://www.pythonchallenge.com", "huge", "file")
urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(passman)))

dict = "abcdefghijklmnopqrstuvwxyz"
dictTo = "cdefghijklmnopqrstuvwxyzab"
table=string.maketrans(dict,dictTo)

def decode(word):
    decoded = ""
    for char in word:
        match = False
        for i in range(0, len(dict)):
            if(char == dict[i]):
                match = True
                if i == 24:
                    decoded = decoded + "a"
                elif i == 25:
                    decoded = decoded + "b"
                else:
                    decoded = decoded + dict[i + 2]
        if not match:
            decoded = decoded + char
    return  decoded           
            


import re
 
def get_challenge(s):
    return urllib2.urlopen('http://www.pythonchallenge.com/pc/' + s).read()

#http://www.pythonchallenge.com/pc/def/ocr.html
def getOcr():
    src = get_challenge('def/ocr.html')
    import re
    text = re.compile('<!--((?:[^-]+|-[^-]|--[^>])*)-->', re.S).findall(src)[-1]
    counts = {}
    for c in text: counts[c] = counts.get(c, 0) + 1
    print counts

#http://www.pythonchallenge.com/pc/def/equality.html
def getEquality():
    text=get_challenge("def/equality.html")
    print re.compile("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]").findall(text)

def nextPage(p):
    url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % p
    text = urllib2.urlopen(url).read()
    print "open:"+url
    m = re.match('.*and the next nothing is ([0-9]+)', text)
    if not m or not m.group(1): print text;pass
    return m.group(1)

#http://www.pythonchallenge.com/pc/def/linkedlist.html  click the picture
def getLinkedList(p):
    for i in range(0,400):p=nextPage(p)

import pickle
#http://www.pythonchallenge.com/pc/def/peak.html
def getPeak():
    peakSrc=get_challenge("def/banner.p")
    data=pickle.loads(peakSrc)
    print '\n'.join([''.join([p[0] * p[1] for p in row]) for row in data])

import StringIO
import zipfile
#http://www.pythonchallenge.com/pc/def/channel.html
def getChannel():
    z=zipfile.ZipFile(StringIO.StringIO(get_challenge("def/channel.zip")))
    print z.namelist()
    print z.read('readme.txt')
    m=re.match('.*Next nothing is ([0-9]+)',z.read('90052.txt')).group(1)
    indexs=[m]
    while m:
        rm=re.match('.*Next nothing is ([0-9]+)',z.read(m+'.txt'))
        if not rm:print z.read(m+'.txt');break
        m=rm.group(1)
        indexs.append(m)
        continue
    print "".join([z.getinfo("%s.txt" % m).comment  for m in indexs])


import Image
def get_image(s): return Image.open(StringIO.StringIO(get_challenge(s)))

#http://www.pythonchallenge.com/pc/def/oxygen.html
def getOxygen():
    im = get_image('def/oxygen.png')
    w,h = im.size
    print ''.join([chr(im.getpixel((i, h//2))[0]) for i in range(0,w,7)]) #技巧：range 三个参数时，最后一个为二个数字差
    print ''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))

import bz2 
#http://www.pythonchallenge.com/pc/def/integrity.html   
def getIntegrity():
    un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    print bz2.BZ2Decompressor().decompress(un)
    print bz2.BZ2Decompressor().decompress(pw)


#http://www.pythonchallenge.com/pc/def/good.html
def getGood():
    first=[146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,
310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,
190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,
389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,
215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,
290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,
279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,
327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,
328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,
259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,
352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,
120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,
214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,
102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,
113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,
133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,
111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,
332,155,348,156,353,153,366,149,379,147,394,146,399]
    second=[156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,159,
157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,132,220,
125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162,
77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115,
158,121,157,128,156,134,157,136,156,136]
    print len(first),max(first),min(first)
    print len(second),max(second),min(second)
    print first[0:2]
    print first[0::2]
    print first[1::2]#技巧：x::y 以x为起点，y为间隔取值
    im = Image.new('1', (500,500), 1)
    import ImageDraw
    draw = ImageDraw.Draw(im)
    draw.line(zip(first[0::2], first[1::2]))
    draw.line(zip(second[0::2], second[1::2]))
    im.save('first+second.png')

#http://www.pythonchallenge.com/pc/return/bull.html
def getBull():
    #序列的第31位的长度 https://oeis.org/A005341
    pass




#http://www.pythonchallenge.com/pc/return/5808.html
def get5808():
    #odd even
    im = get_image('return/cave.jpg')
    w,h = im.size
    for i in range(w):
        for j in range(h):
            if (i + j) % 2 == 1:
                im.putpixel((i,j), 0)
    im.save('cave2.png')

def getEvil





 
if __name__ == '__main__':
    # findTheUrl("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
#     print decode("map")
#     print "map".translate(table)
#     str="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#     print decode(str)
#     print str.translate(table)
    # getLinkedList("8022")
    get5808()
