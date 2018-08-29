#coding=utf-8
#自定义函数strip

import re,sys 

text1 = input('Enter a str :')
text2 = input('Enter a octer:')
#print('enterde:','1=',text1,'2=',text2)
'''
def mystrip1(mystr):

	sstrip = re.compile(r'^\**')
	estrip = re.compile(r'\**$')

	sstripstr = sstrip.sub('!',mystr)
	print(estrip.sub('!',sstripstr))
'''
def mystrip2(mystr,octer=None):

	sstrip = re.compile(r'^\s+')
	estrip = re.compile(r'\s+$')
	ostrip = re.compile(octer)
#	print(octer != None)
#	if octer == None:
	sstripstr = sstrip.sub('',mystr)
	print(sstripstr)
	estripstr = estrip.sub('',sstripstr)
	print(estripstr)
#	if octer != None:
	print(ostrip.sub('',estripstr))
#	else:
#		print('unknow')

mystrip2(text1,text2)

'''
if len(sys.argv) == 2:	
	mystrip1(sys.argv[1])
elif len(sys.argv) == 3:
	mystrip2(sys.argv[1],sys.argv[2])
else:
	print('最多只能输入3个参数！！！')	\
'''