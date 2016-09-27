#!/usr/bin/env python
#coding=utf-8
import urllib
import urllib2
import cookielib
import re
import string
Bi_xiu='\xe5\xbf\x85\xe4\xbf\xae\xe8\xaf\xbe'
Xuan_xiu='\xe9\x80\x89\xe4\xbf\xae\xe8\xaf\xbe'
class school:
	def __init__(self,username,password):
		self.login_url='http://gim.jlu.edu.cn/check.jsp'
		self.mark_url='http://gim.jlu.edu.cn/pyc/menu_stu.jsp?menu=xuanke_check'
		self.cookies=cookielib.MozillaCookieJar()
		self.postdata=urllib.urlencode({'username':'2015534030','password':'XXX'})
		self.opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
		self.category=[]
		self.course=[]
		self.xuefen=[]
		self.mark=[]
	def getPage(self):
		request=urllib2.Request(url=self.login_url,data=self.postdata)
		response=self.opener.open(request)
		result=self.opener.open(self.mark_url).read()
		return result.decode('gb2312').encode('utf-8')
	def s_grade(self):
		page=self.getPage()
		items=re.findall(r'<tr.*?> <td.*?> (.*?)</td>.*?<td.*?<td.*?> (.*?)</td>.*?<td.*?<td.*?<td.*?<td.*?<td.*?> (.*?)</td>.*?<td.*?<td.*?<td.*?> (.*?)</td>.*?<td.*?</tr>',page,re.S)
		for item in items:
			self.category.append(item[0])
			self.course.append(item[1])
			self.xuefen.append(item[2])
			self.mark.append(item[3])
		for i in range(1,len(self.category)):
			print('课程名称：%s 课程学分：%s 课程成绩：%s'%(self.course[i],self.xuefen[i],self.mark[i]))
	def count(self):
		for x in range(len(self.category)):
			if x==0:
				pass
			print('课程名称：%s 课程学分：%.2f 课程成绩：%.2f'%(self.course[i],self.xuefen[i],self.mark[i]))
		self.s_grade()
		sum=0.0;
		xuefen_bixiu=0.0
		i=1;
		while i<len(self.category):
			if self.category[i]==Bi_xiu and self.mark[i].isdigit():
				sum+=string.atof(str(self.xuefen[i]))*string.atof(str(self.mark[i]))
				xuefen_bixiu+=string.atof(self.xuefen[i])	
			i+=1
		average=float(sum/xuefen_bixiu)
		return sum,average
	def show_res(self):
		print('#'*50)
		for x in range(len(self.category)):
			if x==0:
				pass
			print('课程名称：%s 课程学分：%.2f 课程成绩：%.2f'%(self.course[i],self.xuefen[i],self.mark[i]))
		a,b=self.count()
		print('总分：%.2f 绩点：%.2f'%(a,b))
sdu=school(username='2015532107',password='zxg1993827')
# page=sdu.getPage()
#sdu.s_grade()
sdu.show_res()
# pattern=re.compile(r'''<tr.*?<td.*?>(.*?)</td><td.*?<td.*?>(.*?)</td><td.*?<td.*?
# 	<td.*?<td.*?<td.*?>(.*?)</td><td.*?<td.*?<td.*?>(.*?)</td><td.*?</tr>''')
# items=re.findall(r'<tr.*?<td.*?> (.*?)</td>.*?<td.*?<td.*?> (.*?)</td>.*?<td.*?<td.*?<td.*?<td.*?<td.*?> (.*?)</td>.*?<td.*?<td.*?<td.*?> (.*?)</td>.*?<td.*?</tr>',page,re.S)
# print len(items)
# for item in items:
# 	print(item[0])