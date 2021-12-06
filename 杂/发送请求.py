import urllib.request
 
#定义保存函数
def saveFile(data):
    path = "D:\学习\work\py"
    f = open(path,'wb')
    f.write(data)
    f.close()
 
#网址
url = "https://www.bilibili.com"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.63 Safari/537.36'}
req = urllib.request.Request(url=url,headers=headers)
 
res = urllib.request.urlopen(req)
 
data = res.read()
 
#也可以把爬取的内容保存到文件中
saveFile(data)
 
data = data.decode('utf-8')
#打印抓取的内容
print(data)
 
 
#打印爬取网页的各类信息
print(type(res))
print(res.geturl())
print(res.info())
print(res.getcode())
