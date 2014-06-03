#!/usr/bin/python
# coding: UTF-8
"""
  hive MR嵌入脚本，统计轨迹中每天每个小时内用了多久
  1.需要保证不会出现跨天分段（如果出现将忽略）
  2.脚本在嵌入执行时需要用dos2unix工具转换
"""
import sys,os,time
from datetime import * 
import traceback 
sys.path.append(os.getcwd())


DATE_TIME_FORMAT="%Y-%m-%d %H:%M:%S"
DATE_FORMAT="%Y-%m-%d"

sys.stderr.write("we are running at " + datetime.strftime(datetime.today(),DATE_TIME_FORMAT) + "\n")  

EMPTY_ROW="".join(["\t"]*26)

def calcHoursBetween(start,end):
	cost_dict={}
	if(start[0:10]!=end[0:10]):
		sys.stderr.write("different day in a track,start:" + start + ",end:"+end+"\n")  
		return cost_dict
	try:
		start_h=int(start[11:13])
		start_m=int(start[14:16])
		end_h=int(end[11:13])
		end_m=int(end[14:16])
	except ValueError:
		sys.stderr.write("get hour/min props error,start:"+start+" end:"+end+"\n")
		return cost_dict
	if(start_h==end_h):
		cost_dict[start_h]=end_m-start_m
	elif(start_h<end_h):
		for x in xrange(start_h,end_h+1):
			if(x==start_h):
				cost_dict[x]=60-start_m
			if(start_h<x<end_h):
				cost_dict[x]=60
			if(x==end_h):
				cost_dict[x]=end_m
	else:
		sys.stderr.write("end before start,start:" + start + ",end:"+end+" \n")  
	return cost_dict

'''
 2014年1-9月假期数据
'''
holidays=["2014-01-01","2014-01-30","2014-02-01","2014-02-02","2014-02-03","2014-02-04","2014-02-05","2014-02-06","2014-04-05","2014-04-07","2014-05-01","2014-05-02","2014-05-03","2014-06-02","2014-09-08"]

need_wrok_weekdays=['2014-01-26','2014-02-08','2014-05-04','2014-09-28']

def calcDayType(day):
	"""
	0:day为空
	1：工作日
	2：周未
	3：假日
	"""
	if not day: return 0
	if(day in holidays):
		return 3
	else: 
		weekday = datetime.strptime(day,DATE_FORMAT).isoweekday()
		if(weekday ==6 or weekday == 7):
			if day  in need_wrok_weekdays:
			 	return 1
			else:
				return 2
		else:	
			return 1

def toColumns(obj_id,day,cost_dict):
	ary=[0]*24
	for k,v in cost_dict.items():
		ary[k]=v
	dayType=calcDayType(day)
	return obj_id+"\t"+day+"\t"+str(dayType)+"\t"+"\t".join(map(str,ary))



try:
	for line in sys.stdin:
		line=line.strip()
		props= line.split("\t")
	        if(len(props)!=3):
	        	sys.stderr.write("parse error,line:"+line+"\n")
			print EMPTY_ROW
		else:
	    		obj_id,start_time,end_time = props
			day=start_time[:10]
			hour_dict=calcHoursBetween(start_time,end_time)
			if not hour_dict:
				print EMPTY_ROW
			else:
				print toColumns(obj_id,day,hour_dict)	
except:  
    traceback.print_exc(file=sys.stderr) 

# if __name__ == '__main__':
# 	cost_dict= hoursBetween("2014-11-11 11:11:11","2014-11-11 20:15:11")
# 	if not cost_dict:
# 		sys.exit()
# 	else:
# 		print toText("id111","2014-11-11",cost_dict)
	


		
