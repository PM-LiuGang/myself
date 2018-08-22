#coding=utf-8
#在一个csv中找相同数据的行，并显示相同行位于的行数
#file='example1.csv'

import os,csv 

file = open('C:\\python\\hr\\example1.csv')
filereader = csv.reader(file)

csvrows = []

for line in filereader:
	csvrows.append(line)

for i  in csvrows:
	if csvrows.count(i) > 1:
		print(csvrows.index(i))