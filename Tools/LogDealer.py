# encoding: utf-8 
'''
Created on 2013年11月29日

@author: NOAH
'''
import re

def doWithLog(filePath):
    f = open(filePath)
    fto = open("./logRes.log", "w")
    lines = f.readlines();
    for line in lines:
        destStr=""
        if re.search(r"^java.util.concurrent.ExecutionException:.*172.20.1.\d\d:60020", line):
            ip = re.findall(r"172.20.1.\d\d:60020", line)[0]
            print ip
            destStr += ip
        if re.match(r"^2013-11-2\d\s\d\d:\d\d:\d\d,\d\d\d", line):
            date = re.findall(r"^2013-11-2\d\s\d\d:\d\d:\d\d,\d\d\d", line)[0]
            print date
            destStr +="--"+date+'\n'
        fto.write(destStr)
    
    

if __name__ == '__main__':
    testStr = "java.util.concurrent.ExecutionException: java.net.SocketTimeoutException: Call to datanode03/172.20.1.13:60020 failed on socket timeout exception: java.net.SocketTimeoutException: 60000 millis timeout while waiting for channel to be ready for read. ch : java.nio.channels.SocketChannel[connected local=/172.20.1.106:23833 remote=datanode03/172.20.1.13:60020]"
    print re.search(r"172.20.1.\d\d", testStr)
    print re.findall(r"172.20.1.\d\d", testStr)
    doWithLog("logTo.log")
    pass
