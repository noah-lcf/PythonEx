
# coding: utf-8
import sys;
import pymysql;  # mysql library (you will need to install this on the system)
import datetime, calendar
import conf_utils
from conf_utils import getConf, getConfInt
logger = conf_utils.logger




# MySQL Singleton Class with pymysql
class MySQLConnector(object):
    # 	http://famousphil.com/blog/2012/01/mysql-singleton-classes-in-php-and-python/
	_connection = None;
	_instance = None;
	# host="192.168.1.30", user="root", passwd="abcd1234", database="iov",port=30303,
	def __init__(self, host=getConf("db_url"), user=getConf("user_name"), passwd=getConf("password"), database=getConf("default_database_name"), port=getConfInt("port"), debug=False):  
		try:
			if MySQLConnector._instance == None:
				MySQLConnector._instance = self;
				self.dbhost = host
				self.dbuser = user
				self.dbpassword = passwd
				self.dbname = database
				self.port = port;
				MySQLConnector._instance.connect(debug); 
		except Exception, e:
			print "MySQL Error " + str(e);

	def instance(self):
		return MySQLConnector._instance;

	def get_connection(self):
		return MySQLConnector._connection;

	def connect(self, debug=False):
		try:
			MySQLConnector._connection = pymysql.connect(self.dbhost, self.dbuser, self.dbpassword, self.dbname, port=self.port, charset='utf8');
			logger.info("INFO: Database connection successfully established");
		except Exception, e:
			logger.error("ERROR: MySQL Connection Couldn't be created... Fatal Error! " + str(e)) ;
			sys.exit();

	def disconnect(self):
		try:
			MySQLConnector._connection.close();
		except:
			pass;  # connection not open

	# returns escaped data for insertion into mysql
	# def esc(self, esc):
	# 	return MySQLdb.escape_string(str(esc));

	# query with no result returned
	def query(self, sql):
		cur = MySQLConnector._connection.cursor();
		return cur.execute(sql);

	def tryquery(self, sql):
		try:
			cur = MySQLConnector._connection.cursor();
			return cur.execute(sql);
		except:
			return False;

	# inserts and returns the inserted row id (last row id in PHP version)
	def insert(self, sql):
		cur = MySQLConnector._connection.cursor();
		cur.execute(sql);
		return self._connection.insert_id();

	def tryinsert(self, sql):
		try:
			cur = MySQLConnector._connection.cursor();
			cur.execute(sql);
			return self._connection.insert_id();
		except:
			return -1;

	# returns the first item of data
	def queryrow(self, sql):
		cur = MySQLConnector._connection.cursor();
		cur.execute(sql);
		return cur.fetchone();

	# returns a list of data (array)
	def queryrows(self, sql):
		cur = MySQLConnector._connection.cursor();
		cur.execute(sql);
		return cur.fetchall();


conn = MySQLConnector()


def toCamal(str):
    a=str.lower()
    index=a.find("_")
    return a if index==-1 else a[0:index]+a[index+1].upper()+toCamal(a[index+2:len(a)])


typeMap={"Integer":r"^.*int$","String":r"^varchar$","Date":r"^datetime$"}

def getJavaFields(dbName,tbName):
    code_str=""
    res =  conn.queryrows("select  column_name,data_type, column_comment from information_schema.columns where table_schema ='"+dbName+"'  and table_name = '"+tbName+"';")
    for x in res:
        match = False
        for t in typeMap:
            if re.match(typeMap[t],x[1]):
                code_str+= "private "+str(t)+" " + toCamal(str(x[0])) + ";"
                if x[2]!="":code_str+= "  // "+re.sub(r"\s","",x[2])
                code_str+="\n\n"
                match = True
        if not match:
            logger.error("unknow column "+ `x`)
    return code_str

import re
if __name__ == '__main__':
    print getJavaFields("jiuche_ipad_dev","order_info").encode("utf-8")



