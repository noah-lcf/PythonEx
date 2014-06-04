def loadDataSet():
	dataMat,labelMat=[]*2
	fr = open("testSet.txt")
	for i in fr.readlines():
		lineArr=line.strip().split()
		dataMat.append()