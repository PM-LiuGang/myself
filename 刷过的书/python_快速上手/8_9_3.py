#coding=utf-8
#python
#
import re
#找到一个文件中所有txt文件
pwd = input('Enter a pwd:')

rex = re.compile(r'what')
#os.getcwd(pwd)
for i in os.listdir(pwd):
	if i[-4:] == '.txt':
		file = open(i)
		for h in file.readlines():
			if rex.findall(h) != []:
				print(h)

#输出正则表达式
#与正则表达式的行打在屏幕上
#将结果保存另一个文件中