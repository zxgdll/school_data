#!/usr/bin/env python
#coding=utf-8
import urllib2
import urllib
import cookielib
filename='cookie.txt' #存储校园网cookie的文件
cookie=cookielib.MozillaCookieJar(filename)
handler=urllib2.HTTPCookieProcessor(cookie)# 创建cookie处理器
opener=urllib2.build_opener(handler) #构建opener
value={'username':'2015544010','password':'ilovebs'}
data=urllib.urlencode(value)
request=urllib2.Request('http://gim.jlu.edu.cn/check.jsp',data)
response=opener.open(request)
cookie.save(ignore_discard=True,ignore_expires=True)
url1='http://gim.jlu.edu.cn/pyc/menu_stu.jsp?menu=xuanke_check'
result=opener.open(url1)
with open('res.html','w+') as f:
	f.write(result.read().decode('gb2312').encode('utf-8'))