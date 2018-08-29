#coding=utf-8
#从csv文件删除表头

import os,csv 

os.makedirs('headeremoved',exist_ok = True)

newcsvfile = open('newcsvfile.csv','w',newline='')
newcsvwriter= csv.writer(newcsvfile)

for i in os.listdir('.'):
	#如果文件不是以.csv结尾，跳到for开始
	if not i.endswith('.csv'):
		continue
	print('removing header from ' + i + '...')

	csvrows = []
	csvfileobj = open(i)#打开带表头的文件
	readerobj = csv.reader(csvfileobj)#将csv的内容读取到reader对象里
	#readerobj=[[],[],[],[]]
	#遍历各行[]
	for row in readerobj:
		#如果是文件的第一行，跳到for开始
		if readerobj.line_num == 1:
			continue
		#csvfileobj=[[],[],[]]
		csvrows.append(row)
	csvfileobj.close()#关闭带表头的文件
	#默认从本路径下打开文件夹和i
	csvfileobj = open(os.path.join('headeremoved',i),'w',newline='')
	csvwriter = csv.writer(csvfileobj)
	for row in csvrows:
		#写入时，也是列表的列表中第一个列表
		csvwriter.writerow(row)
	csvfileobj.close()

'''
	csvfileobj.close()

		csvfile = open(i)
		csvreader = csv.reader(csvfile)

		if csvreader.line_num != 1:
			for line in csvreader:
				newcsvwriter.writerow(line)


newcsvfile.close()
csvfile.close()
'''