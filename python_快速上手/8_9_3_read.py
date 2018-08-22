#coding=utf-8
#python
#
import re,os,fileinput
#找到一个文件中所有txt文件
pwd = input('Enter a pwd:')

rex = re.compile(r'\d{1,2}\.\sWhat.+')
#便利的时候不能赋值，因为赋值为空
#os.getcwd(pwd)
for i in os.listdir(pwd):
	if i[-4:] == '.txt':
		print('cur file is :',i)
		file = open(i)
		files = file.readlines()
		for file in files:
			if len(file) > 25:
				print(rex.findall(file))
		'''
		with fileinput.input(i) as lines:
			for line in lines:
				#无法加入正则表达式进行判断
				#空的列表
				if 'What' in line:
					print('No:',fileinput.filelineno(),'Line:',line)
		'''



#输出正则表达式
#与正则表达式的行打在屏幕上
#将结果保存另一个文件中