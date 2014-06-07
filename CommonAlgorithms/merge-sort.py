#!/usr/bin/python
# coding: UTF-8
import numpy as np

"""
  归并排序练习，包括自己写的命令式和从WIKI抄来的函数式
  http://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F#Python
"""

def mergeSort(data):
	_merge_sort(data,0,len(data))
	pass

def _merge_sort(data,first,last):
	if(first<last):
		mid=int((first+last)/2)
		_merge_sort(data,first,mid)
		_merge_sort(data,mid+1,last)
		data=mergeArrays(data,first,mid+1,last)



def mergeArrays(ary,first,middle,last):
	# print "sort"+str(ary)+"  first:"+`first`+" middle:"+`middle`+" last:"+`last`
	ary1=ary[first:middle]
	#这里LAST要加1，不然会漏掉元素
	ary2=ary[middle:last+1]
	# print "ary1:"+str(ary1)
	# print "ary2"+str(ary2)
	res=[]
	idx1,idx2=0,0
	while True:
		if(len(ary1)==idx1):
			res.extend(ary2[idx2:])
			break;
		if(len(ary2)==idx2):
			res.extend(ary1[idx1:])
			break
		if ary1[idx1]<ary2[idx2]:
			res.append(ary1[idx1])
			idx1=idx1+1
		elif ary1[idx1]>ary2[idx2]:
			res.append(ary2[idx2])
			idx2=idx2+1
		else:
			res.extend([ary2[idx2]]*2)
			idx1=idx1+1
			idx2=idx2+1
	#排好序这段的写入原来的LIST
	idx=first
	for v in res:
		ary[idx]=v
		idx=idx+1
	# print "after sort:"+str(ary)
	return ary
	
	

def merge_sort_wiki(list):
  # print "wiki:"+str(list)
  if len(list) <= 1:
    return list;
 
  def merge(left, right):
    merged = []
    while len(left) > 0 and len(right) > 0:
       merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    while len(left) > 0:
       merged.append(left.pop(0))
    while len(right) > 0:
       merged.append(right.pop(0))
    return merged
 
  middle = int(len(list) / 2)
  left = merge_sort_wiki(list[:middle])
  right = merge_sort_wiki(list[middle:])
  return merge(left, right)
	
				



def main():
	data_org=np.arange(8)
	np.random.shuffle(data_org)
	tmp=data_org
	tmp2=data_org
	print "before sort: "+str(tmp)
	mergeSort(tmp)
	print "after sort: "+str(tmp)
	# mergeArrays([1,2 ,3 ,4 ,5, 2, 4 ,6, 8, 10],0,5,10)
	print "after wiki sort:"+str(merge_sort_wiki(tmp2.tolist()))


if __name__ == '__main__':
	main()




