#!/usr/bin/python
# coding: UTF-8
"""
  hive MR嵌入脚本，计算两点之间距离
  
"""
import sys,os,time
from datetime import * 
import traceback 
import math
sys.path.append(os.getcwd())

EMPTY_ROW=""


EARTH_RADIUS = 6378.138;

def rad(d):
	return d * math.pi / 180.0;

def calcDistance(lat1,lng1,lat2,lng2):
		radLat1 = rad(lat1)
		radLat2 = rad(lat2)
		a = radLat1 - radLat2
		b = rad(lng1) - rad(lng2)
		s = 2 * math.asin(math.sqrt(math.pow(math.sin(a / 2), 2) + math.cos(radLat1) * math.cos(radLat2)* math.pow(math.sin(b / 2), 2)))
		s = s * EARTH_RADIUS
		s = round(s * 10000) / 10
		return s


#print calcDistance(22.576344,113.88294,22.590181,113.8736)

try:
	for line in sys.stdin:
		line=line.strip()
		props= line.split("\t")
		if(len(props)!=6):sys.stderr.write("parse error,line:"+line+"\n") 
		else:
			try:
				obj_id=props[0]
				day=props[1]
				lat1,lng1,lat2,lng2 = map(float,props[2:])
				dis=calcDistance(lat1,lng1,lat2,lng2)
				print obj_id+"\t"+day+"\t"+`dis`
			except ValueError:
				sys.stderr.write("parse error,line:"+line+"\n")
except:  
    traceback.print_exc(file=sys.stderr) 
