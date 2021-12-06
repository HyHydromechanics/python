import requests
import re
 
url='https://music.163.com/#/artist?id=46361128'
 
def get_html(url):
 
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.63 Safari/537.36'
               }
    params = {
        'id': '9272'
             }
 
    #通过Request()方法构造一个请求对象
    response = requests.get(url, headers=headers,params=params)
    html=response.text
    print(type(html))   #str
    return html
 
def parse_html(html):
 
    #<a href="/song?id=287035">遇见</a>
    pattern=re.compile('<a href="/song\?id=\d+">(.*?)</a>')
    names=re.findall(pattern,html)
    print(len(names))
    for name in names:
         print(name)
 
if __name__ == '__main__':
    html=get_html(url)
    f = open("out.txt","w",encoding='utf-8') #添加encoding='utf-8'可以解决'gbk' codec can't encode character '\xa9'
    f.write(html)      #将html写入txt文件
    parse_html(html)