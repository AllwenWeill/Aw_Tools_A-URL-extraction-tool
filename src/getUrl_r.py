import urllib.request
import sqlite3
import re
import requests
import queue
import os

URL_queue = queue.Queue()

DB = sqlite3.connect("E:/gotUrl.db")
#DB = sqlite3.connect(":memory:")
cursorObj = DB.cursor()
cursorObj.execute("CREATE TABLE URLs(url text PRIMARY KEY)")

def pushDB(targetValue):
    tempPath = "REPLACE INTO URLs VALUES('%s')" % targetValue
    #print(tempPath)
    cursorObj.execute(tempPath)
    DB.commit()


#@param:需要访问的目标URL
#@function:向指定的url发送请求，并返回服务器响应的类文件对象
#@return:null
def getURLs(targetURl, proxy_ip):
    if proxy_ip != 0:
        # 代理IP对象
        proxy = urllib.request.ProxyHandler({"http": proxy_ip})
        # 建立opener对象，给该opener添加代理IP
        # 参数2：设置为HTTPHandler【固定不可改】
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        # 安装为全局opener()
        urllib.request.install_opener(opener)
    resp = urllib.request.urlopen(targetURl)
    # 类文件象支持 文件对象的操作方法，如read()方法读取文件全部内容，返回字符串
    respStr = str(resp.read())
    # print(respStr)
    res_URL = deal_allURL(respStr)
    for i in res_URL:
        URL_queue.put(i)
        pushDB(i)
    print(res_URL)

#@param:包含该页面所有内容信息的字符串
#@function:将该http网址中获取该当前页面的所有URL信息中提取有效http格式有效href
#@return:包含有效href链接的列表
def deal_allURL(str_URL):
    res_URL = []
    unhttp_Data = re.findall(r'."http://(.+?)\"', str_URL)
    for i in range(len(unhttp_Data)):
        str = "http://" + unhttp_Data[i]
        if (str[-1] == "'"):
            resStr = str[:-2]
            if exam_vaildURL(resStr):
                res_URL.append(resStr)
        else:
            if exam_vaildURL(str):
                res_URL.append(str)
    print("该页面共有", len(res_URL), "个有效URL.\n")
    print("爬虫获取中...")
    return res_URL

#@param:初步筛选的URL列表中的一个元素
#@function:利用GET请求对该URL有效性进行测试
#@return:1真0假
def exam_vaildURL(tempURL):
    try:
        respose = requests.get(url=tempURL)
        return 1
    except requests.ConnectionError as e:
        return 0

if __name__ == '__main__':
    #proxy_ip = "49.75.59.242:3128"
    proxy_ip = 0
    print("请输入目标网址：")
    getURLs(input(), proxy_ip)
    while URL_queue.empty() != None:
        getURLs(URL_queue.get(), proxy_ip)
    #chd官网  https://www.chd.edu.cn/
    #百度 http://www.baidu.com
