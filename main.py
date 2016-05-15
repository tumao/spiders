#!/D:/ProgramFiles/Python/Python35/python.exe
#coding:utf-8
import urllib.request
import string

# url = "http://www.dianping.com/search/category/1/10/g113r801"
# url = "http://cailianpress.com/"
url = "http://english.cri.cn/"
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
opener = urllib.request.build_opener()
opener.addheaders = [headers]

data = opener.open(url).read()



try:
	page_file = open ('page.html', 'w')
	print(data.decode('utf-8').encode('utf-8'), file = page_file)
	# page_file.write(data.decode('utf-8').encode('utf-8'))
except IOError:
	print ("someting wrong")
finally:
	if 'page_file' in locals(): #
		page_file.close()

# print (data)