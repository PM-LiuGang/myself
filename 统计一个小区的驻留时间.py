# -*- coding=utf-8 -*-
'''
统计一个用户在不同小区的驻留时间
————————————————————————————————
列说明：
dtformat dt对应timestamp格式
dtdelta 当前位置的距离下次变化位置占用的小区
'''
import numpy as np 
import pandas as pd 
from datetime import datetime

def read_data(file):
	data = pd.read_csv(file)
	return data 

def stay_cell(data):
#	data有了4列，location、dt、dtformat、dtdelta
#	del data[data.columns[0]],选择指定列
	dcp = data[['location','datetime']]
#	data有了3列，location、dt、dtformat、dtdelta
	dcp['dtformat'] = np.nan
	dcp['dtdelta'] = np.nan
	#获取时间格式，传递给strptime中format
#	time_format = data.dt[0]
#	data中dtdelta赋值
#	如果不知道时间格式，怎么自动识别？
	for i,value in enumerate(dcp['datetime']):
		dcp.iloc[i,2] = datetime.strptime(value,'%Y-%m-%d %H:%M:%S')
	#计算每个小区的驻留时间
	#计算规则下一个减去上一个作为上一个小区的驻留时间
	#len(dcp)-1防越界
	for i in range(1,len(dcp)-1):
		dcp.iloc[i,3] = dcp.iloc[i+1,2] - dcp.iloc[i,2]
	#滤除缺失值
	dcp = dcp.dropna()

	print(dcp[['location','dtdelta']].groupby('location').sum())

if __name__ == '__main__':
	data = read_data('cell_stay.csv')
	stay_cell(data)

