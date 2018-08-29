# -*- coding: UTF-8 -*-
"""
此脚本用于随机生成线性回归模型的训练数据
添加新变量
"""
import os,sys

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn import linear_model 
from sklearn.preprocessing import PolynomialFeatures 
import statsmodels.api as sm 

def generate_data():
	#seed(int) int是随便写么？
	np.random.seed(5320)
	x = np.array(range(0,20))/2
	#正太分布 20个数 保留2位
	error = np.round(np.random.randn(20),2)
	y = 0.05 * x + error 
	#加入变量z 恒等于1
	z = np.zeros(20) + 1 
	return pd.DataFrame({'x':x,'y':y,'z':z})
'''
def visualize_data(data):
	plt.rcParams['font.sans-serif'] = ['SimHei']
	fig = plt.figure(figsize=(6,6),dpi=80)
	ax = fig.add_subplot(1,2)
	for i in range(2):
		ax[i].set_title('%s' % '线性回归示例')
		ax[i].set_xlabel('$x$')
		ax[i].set_xticks(range(10,31,5))
		ax[i].set_ylabel('$y$')
		ax[i].set_yticks(range(10,31,5))
		ax[i].scatter(data.x,data.y,label ='$y = x + \epsilon$')
	legend = plt.legend(shadow=True)
	legend.get_frame().set_facecolor('#6F93AE')
'''
def wrong_coef(data):
	#特征x z，标签 z
	features = ['x','z']
	labels = ['y']
	xx = data[features]
	yy = data[labels]
	#查看一个变量和两个变量的模型报告
	model = sm.OLS(yy,xx['x'])
	res = model.fit()
	print('--------------没有加入新变量时---------------')
	print(res.summary())
	model_1 = sm.OLS(yy,xx)
	res_1 = model_1.fit()
	print('---------------加入新变量后------------------')
	print(res_1.summary())

if __name__ == "__main__":
	data = generate_data()
#	data=readdata('simple_example.csv')
#	featurizer=PolynomialFeatures(degree=5)
	wrong_coef(data)
#	visualize_data(data)
	

