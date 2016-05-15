#coding:utf-8

import urllib2

"""
	将数据写入到文件当中
"""
def writeToFile (dest, data):
	try:
		page_file = open (dest, 'w')
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
	writeToFile('page.data', html)	



###以下为主函数
getPage('http://www.dianping.com/search/category/1/10/g113r801')