#-*- coding:utf-8 -*-
import re
import requests

url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E6%A2%85%E9%87%8C%E9%9B%AA%E5%B1%B1'


html = requests.get(url).text
pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
i = 0
for each in pic_url:
    print (each)
    try:
        pic= requests.get(each, timeout=10)
    except requests.exceptions.ConnectionError:
        print ('【错误】当前图片无法下载')
        continue
    string = 'E:\picture\\'+str(i) + '.jpg'
    fp = open(string,'wb')
    fp.write(pic.content)
    fp.close()
    i += 1
