#!/usr/bin/python  
# encoding: utf-8
from cStringIO import StringIO
import glob
import os
import time

from PIL import Image
import requests
from pyquery import PyQuery as pq
from string import strip
from requests.exceptions import ConnectionError

'''

使用requests,pyquery 从网站上抓取验证图片 

用户验证后获取数据

'''

domain = "http://xxxxxxx:8085"
login_url = domain + "/proxy/login.aspx"
code_url = domain + "/VerifyCodeImage.aspx"


save_path = os.path.join(os.path.dirname(__file__), '../static/image').replace('\\', '/')
files_path = os.path.join(os.path.dirname(__file__), '../static/files').replace('\\', '/')

http_proxy = "http://127.0.0.1:8888/"
https_proxy = http_proxy
ftp_proxy = http_proxy

myProxyDict = {  }


user_name = "xxx"
user_pwd = "xxxxxxxx"

headers = {"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}

s = requests.Session()

    
def clearImage():
	pic_files = glob.glob(save_path + '//*.png')
# 	print "find "+str(len(pic_files))+" images"
    map(os.remove,pic_files)
	
def init(use_proxy=False, clear_image=True):
	if clear_image:clearImage()
# 	monkey_patch()
	if  use_proxy:
		global myProxyDict
		myProxyDict = { "http"  : http_proxy, "https" : https_proxy, "ftp"   : ftp_proxy }
	

def get(url, params={}):
    try:
	       r = s.get(url, headers=headers, allow_redirects=True, proxies=myProxyDict, params=params)
    except ConnectionError:
        return "{}"
    return r.text

def post(url, data):
    try:
	       r = s.post(url, data=data, headers=headers, allow_redirects=True, proxies=myProxyDict)
    except ConnectionError:
        return None
    return r.text

def getPic():
    try:
        name = str(long(time.time() * 1000)) + ".png"
        get(login_url)
        r = s.get(code_url, headers=headers, proxies=myProxyDict)
        i = Image.open(StringIO(r.content))
        i.save(save_path + "//" + name)
        print "pic saved:" + save_path + "//" + name
        return name
    except ConnectionError:
        return ""
    
def isUserLogin():
    main_res=get(domain+"/Proxy/Main.aspx")
    d = pq(main_res)
    if d("#" + login_page_mark):
       return False
    return True    

def dologin(code,pic=""):
    logininfo = {'txtAdminName':user_name, 'txtAdminPassWord':user_pwd, 'txtCode':code, "btnAdminLogin":"", "__VIEWSTATE":"/wEPDwUJNjkyMTgwMTQ3ZGQ="}
    post(login_url, logininfo)
    if pic:
        os.remove(save_path+"/"+pic)
    if isUserLogin():
        return 1
    return None

def logout():
	s.close()	

def login():
	getPic()
	code = raw_input("input code please:\n")
	print "your input: " + code
	dologin(code)

api_url = domain + '/API/DLOrderHandler.ashx';

# uGParent 标识用户ID
# isSub    是否包含子集（1：否，0：是）
# type     {loadZSSOrderSell:卖出，loadZSSOrderBuy：买入。}
zs_form_template = {'type':'loadZSSOrderSell', 'uGParent':260, 'isSub':1, 'pageIndex':1, 'pageSize':100, 'productId':'', 'userName':'', 'startDate':'', 'endDate':''}


def getData(command_type, uGParent=260):  
	zs_form_template['type'] = command_type
	zs_form_template['uGParent'] = uGParent
	return post(api_url, zs_form_template)

def getSellData():
    return getData("loadZSSOrderSell")

def getBuyData():
	return getData("loadZSSOrderBuy")

def getTotal():
	totalForm = {'type':'loadZSSOrderTotle', 'productId':'', 'startDate':'', 'startDate':'', 'uGParent':260, 'isSub':1}
	return post(api_url, totalForm)



login_page_mark = "txtAdminName"



filter_users = ["li"]

def parseUserList(d):
    user_list = []
    for tr in d('body .datalist table tr'):
        i = 0
        user = {}
        for td in pq(tr).children("td"):
            if i == 0:
                user['userid'] = strip(pq(td).find("span").html())
            if i == 1:
                user['username'] = pq(td).html()
            if i == 2:
                user['agent'] = pq(td).html()
            if i == 3:
                user['count'] = pq(td).find("span").html()
            if i == 4:
                user['opentime'] = pq(td).html()
            i = i + 1
        if user.has_key('userid') and user['username'] not in filter_users:
            user_list.append(user)
    return user_list




# 交易会员列表r
def getUserList():
    user_list_url = domain + "/Proxy/User/UserList.aspx"
    user_html = get(user_list_url, {"pageindex":str(1)})
    d = pq(user_html)
    # need login
    if d("#" + login_page_mark):
        return -1
    user_list = []
#     d=pq(filename=files_path+"/userlist.html")
    user_list.extend(parseUserList(d))
    pageIndex = 2
    while d(".page-next"):
        user_html = get(user_list_url, {"pageindex":str(pageIndex)})
        d = pq(user_html)
        user_list.extend(parseUserList(d))
        pageIndex += 1
    return user_list



def parseTradeHis(d):
    summaryList = []
    trIndex = 0
    for tr in d(".horder_list_tab tr"):
        tdIndex = 1
        summary = {}
        for td in pq(tr).children("td"):
            if trIndex == 0 or trIndex == 1:
                if tdIndex == 2:
                    summary["code"] = pq(td).html() 
                elif tdIndex == 4:
                    summary["tradeMount"] = pq(td).html() 
                elif tdIndex == 6:
                    summary["unTradeMount"] = pq(td).html()
                elif tdIndex == 8:
                    summary["charge"] = pq(td).html()
                elif tdIndex == 10:
                    summary["profitLoss"] = pq(td).html()
            if trIndex == 2:
                summary["code"] = ''
                if tdIndex == 3:
                    summary["tradeMount"] = pq(td).html() 
                elif tdIndex == 5:
                    summary["unTradeMount"] = pq(td).html()
                elif tdIndex == 7:
                    summary["charge"] = pq(td).html()
                elif tdIndex == 9:
                    summary["profitLoss"] = pq(td).html()
            tdIndex += 1
        summaryList.append(summary)
        trIndex += 1     
    detailList = []
    trIndex = 0
    for tr in d(".datalist tr"):
        if trIndex == 0:
            trIndex += 1
            continue
        detail = {}
        tdIndex = 0
        for td in pq(tr).children("td"):
            if tdIndex == 0:
                detail["id"] = pq(td).html()
            if tdIndex == 1:
                detail["no"] = pq(td).html()
            if tdIndex == 2:
                detail["username"] = pq(td).html()
            if tdIndex == 3:
                detail["code"] = pq(td).html()
            if tdIndex == 4:
                detail["time"] = pq(td).html()
            if tdIndex == 5:
                detail["type"] = pq(td).html()
            if tdIndex == 6:
                detail["count"] = pq(td).html()
            if tdIndex == 7:
                detail["price"] = pq(td).html()
            if tdIndex == 8:
                detail["left"] = pq(td).html()
            if tdIndex == 9:
                detail["charge"] = pq(td).html()
            if tdIndex == 10:
                detail["addOrSub"] = pq(td).html()
            if tdIndex == 11:
                detail["profit"] = pq(td).html()
            if tdIndex == 12:
                detail["leftMoney"] = pq(td).html()
            if tdIndex == 13:
                detail["dealType"] = pq(td).html()
            tdIndex += 1
        detailList.append(detail)
        trIndex += 1   
    return summaryList, detailList      

def getTradeHis(startDate="2014-04-01 00:00:00", endDate=""):
    if not endDate:
        endDate = time.strftime('%Y-%m-%d', time.localtime(time.time())) + " 23:59:59"
    sell_his_url = domain + '''/Proxy/maker/horderlist.aspx?
                        adverse=-1&issub=1&type=-1&uGParent=260&&pagesize=40'''
    trade_his_html = get(sell_his_url, {"startDate":startDate, "endDate":endDate})
    d = pq(trade_his_html)
#     d=pq(filename=files_path+"/tradehis.htm")
    if d("#" + login_page_mark):
        return None,None
    totalList,detailList =parseTradeHis(d)
    pageIndex = 2
    while d(".page-next"):
        trade_his_html = get(sell_his_url, {"startDate":startDate, "endDate":endDate,"pageindex":str(pageIndex)})
        d = pq(trade_his_html)
        totalListTmp,detailListTmp =parseTradeHis(d) 
        detailList.extend(detailListTmp)
        pageIndex += 1
    return totalList,detailList
    
    

def main():
	init(use_proxy=False, clear_image=True)
	login()
# 	print getTotal()
# 	getSellData()
# 	print getTotal()
#     print getTotal()
	logout()



if __name__ == '__main__':
#     main()
    print getTradeHis()
#     print get("http://42.96.149.95:8085/Proxy/maker/horderlist.aspx?adverse=-1&issub=1&type=-1&uGParent=260&startDate=2014-04-01+00%3a00%3a00&endDate=2014-04-12+23%3a59%3a59&pagesize=40")

