# coding: utf-8
'''
Created on 2014年9月19日

@author: Administrator
'''


# -*- coding: cp936 -*-
import logging
from logging.config import fileConfig
import os


# 获取脚本文件的当前路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
fileConfig("logging.conf")

# create logger
logger = logging.getLogger("config")

class Conf(object,):
    props = {}
    def __init__(self, conf_file="conf.properties"):
        path = os.path.join(BASE_DIR, conf_file)
        lines = open(path).readlines()
        for line in lines:
            if line.strip() == "":continue 
            line = line.replace("\n", "")
            if line[0] == "#":continue  # 注释
            kvAry = line.split("=")
            if(len(kvAry) != 2):print("parse conf line:" + line + " failed,continue..");continue
            Conf.props[kvAry[0].replace("\r","")] = kvAry[1].replace("\r","")
    
    def _getOrElse(self, key, defalut_val=None):
        if(Conf.props.has_key(key)):return Conf.props[key]
        return defalut_val

conf = Conf()
logger.info("props loaded:\n" + str(Conf.props))

def getConfOrElse(key, defalut_val=None):
    return conf._getOrElse(key, defalut_val)
 
def getConf(key):
    return getConfOrElse(key, None)

def getConfInt(key, func=int):
    return func(getConfOrElse(key, None))


if __name__ == '__main__':
#     print cur_file_dir()
    host = getConf("db_url")
    user = getConf("user_name")
    passwd = getConf("password")
    database = getConf("default_database_name")
    port = getConfInt("port")
    print host, user, passwd, database, port
