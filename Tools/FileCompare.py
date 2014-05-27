# encoding: utf-8 
__author__ = 'NOAH'



def compare(filePath1, filePath2):
    """比较文件两个文件，输出没有重复的行 """
    f1 = open(filePath1, "r")
    f2 = open(filePath2, "r")
    s1 = set(a.rstrip().decode("utf-8") for a in f1.readlines())
    s2 = set(a.rstrip().decode("utf-8") for a in f2.readlines())
    return ",".join(s1- s2)

def removeLastThreeWord(file):
     f1 = open(file, "r")
     f2 = open("../abc2.csv", "w")
     s1 = [a.rstrip().decode("utf-8") for a in f1.readlines()]
     metaAry=s1[0].split(",")
     metaAry=metaAry[0:len(metaAry)-3]
     sql=""
     for i in range(1,len(s1)):
         k=s1[i]
         ary=k.split(",")
         print ary[0]
         line=",".join(ary[0:len(ary)-3])
         print line
         f2.write(line+"\n")
         for j in range(2,len(ary[0:len(ary)-3])):
             if len(metaAry)<=j or metaAry[j].find("-")==-1:break
             year=metaAry[j].split("-")[0]
             month=metaAry[j].split("-")[1]
             sql+="insert into sale_his values(null,"+year+","+month+",'"+ary[1]+"',"+ary[j]+");\n"
     f3 = open("../brandSale.sql", "w")
     f3.write(sql)

if __name__ == '__main__':
#     a="22,大7 MPV,92,82,103,221,252,209,0,0,959"
#     print a[0:37]
#     print "22,大7 MPV,92,82,103,221,252,209,0,0,959".find(",")
#     print "22,大7 MPV,92,82,103,221,252,209,0,0,959".rfind(",")
    print removeLastThreeWord("../abc.csv")
    
   