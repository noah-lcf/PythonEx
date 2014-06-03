# encoding: utf-8 
'''
Created on 2013年12月18日

@author: NOAH

java gc日志转格式

'''



#!/usr/bin/env python  
   
import sys, os, datetime  
   
# true if string is a positive float  
def validSeconds(str_sec):  
    try:  
        return 0 < float(str_sec)  
    except ValueError:  
        return False  
   
# show usage                  
if len(sys.argv) < 2:  
    print "Usage: %s <gc.log>" % (sys.argv[0])  
    sys.exit(1)  
   
file_str = sys.argv[1]  
lastmod_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_str))  
   
file = open(file_str, 'r')  
lines = file.readlines()  
file.close()  
   
# get last elapsed time  
for line in reversed(lines):  
    parts = line.split(':')  
    if validSeconds(parts[0]):  
        break  
   
# calculate start time  
start_date = lastmod_date - datetime.timedelta(seconds=float(parts[0]))  
   
# print file prepending human readable time where appropiate    

fto = open("./gcParsed.log", "w")

for line in lines:  
    parts = line.split(':')  
    if not validSeconds(parts[0]):  
        print line.rstrip()  
        continue  
    line_date = start_date + datetime.timedelta(seconds=float(parts[0]))  
    print "%s: %s" % (line_date.isoformat(), line.rstrip()) 
    fto.write("%s: %s \n" % (line_date.isoformat(), line.rstrip())) 
    
