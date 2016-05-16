#coding:utf-8

import urllib2
import re

mainUrl = "http://www.dianping.com"		# uri的主体

"""
	将数据写入到文件当中
"""
def writeToFile (dest, data):
	try:
		page_file = open (dest, 'a')
		page_file.write (data)	#将文件写入到dest
	except IOError:
		print ('io error')
	finally:
		if 'page_file' in locals(): # 查看你要写入的文件是否成功打开，若是则关闭
			page_file.close()

"""
	通过url获取网页上的所有数据
"""
def getPage(url):
	header = {
		'User-Agent':
			'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	# 模拟浏览器的头信息

	hostUrl = url
	urlRequest = urllib2.Request(hostUrl,'', header)
	response = urllib2.urlopen(urlRequest)
	html = response.read ()
	# writeToFile('page.data', html)
	return html


"""
	通过正则表达式过滤出页面中想要的那一部分数据
"""
def getContentByPattern (pattern, string):
	result = re.findall (pattern, string)
	return result


def listConvertStr (list):
	return "\r\n".join(list) 

###以下为主函数
html =  getPage('http://www.dianping.com/search/category/1/10/g113r801')	#获取网页的所有内容

patternCat = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"			#分类的pattern
data = getContentByPattern (patternCat, html)						# 正则表达式过滤后的内容
# print (data)
writeToFile ("./page.data", listConvertStr(data))										# j将过滤后的内容存储到文件中
