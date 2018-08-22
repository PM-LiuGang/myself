#coding=utf-8
#编写一个程序，对给定的网页URL，下载该页面所有链接的页面。
#程序应该标记出所有具有404“Not Found”状态码的页面，将它们作为坏链接输出。

import requests
import bs4

url = 'http://ifeve.com/'#并发程序网
response = requests.get(url)#下载该界面的内容
#获取bs4文本对象,解析器lxml
soup = bs4.BeautifulSoup(response.text, "lxml")
#<a href="http://ifeve.com/java-concurrent/">并发基础</a></li>
#css选择器，返回列表对象
a_list = soup.select('a')
#遍历列表
playfile = open('hrefaddress.txt','w')

for a in a_list:
    a_url = a.get('href')#获取链接的url
#    assert type(a_url) == type(''),'a_url must be str'
    playfile.write(str(a_url)+'\n')
    try:
        response = requests.get(a_url)#下载链接的url
        #如果res对象的响应吗是没有发现，给出提示，否则打印链接，给出提示
        if response.status_code == requests.codes.not_found:
            print("Page %s is broken link" % a_url)
        else:
            print("Page %s is other type link" % a_url)
        response.raise_for_status()#下载如果没有成功，转到except
    except:
        print("Page %s is Error" % a_url)

playfile.close()