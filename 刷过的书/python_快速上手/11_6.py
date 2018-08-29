import requests,sys,bs4,webbrowser

key = ' '.join(sys.argv[1:])

resobj = requests.get('http://www.baidu.com/s?wd='+key)

resobj.raise_for_status()

bs4obj = bs4.BeautifulSoup(resobj.text)

#bs4objelem1=bs4obj.select('.t c-gap-bottom-small a')

bs4objelem2=bs4obj.select('.t a')

#numopen1 = min(3,len(bs4objelem1))
numopen2 = min(3,len(bs4objelem2))

#for i in range(numopen1):
#	webbrowser.open(bs4objelem1[i].get('href'))

for i in range(numopen2):
	webbrowser.open(bs4objelem2[i].get('href'))

