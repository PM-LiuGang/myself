# -*- coding: UTF-8 -*-
"""
此脚本用于展示如何利用惩罚项解决模型幻觉的问题
"""

import os
import sys

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd

def generate_randomvar():
	np.random.seed(4873)
	return np.random.randint(2,size=20)

def train_model(x,y):
	model = sm.OLS(y,x)
	res = model.fit()
	return res

def train_regulize_model(x,y,alpha):
	model = sm.OLS(y,x)
	#正则化拟合&权重
	res = model.fit_regularized(alpha=alpha)
	return res 

def visualize_model(x,y):
#	为在Matplotlib中显示中文，设置特殊字体
	plt.rcParams['font.sans-serif']=['SimHei']
# 	正确显示负号
	plt.rcParams['axes.unicode_minus']=False
	fig = plt.figure(figsize=(6,6),dpi=80)
	#一个子图
	ax = fig.add_subplot(1,1,1)
    #np.logspace() logspace用于创建等比数列
	alphas = np.logspace(-4,-0.8,100)
    #coefs 系数
	coefs = []
	for alpha in alphas:
		res = train_regulize_model(x,y,alpha)
		#添加模型的参数
		coefs.append(res.params)

	coefs = np.array(coefs)
	#coefs[:,1],第一列，第二列，第三列
	ax.plot(alphas, coefs[:, 1], "r:",label='%s' % "x的参数a")
	ax.plot(alphas, coefs[:, 2], "g",label='%s' % "z的参数b")
	ax.plot(alphas, coefs[:, 0], "b-.",label='%s' % "const的参数c")
	legend = plt.legend(loc=4, shadow=True)
	legend.get_frame().set_facecolor("#6F93AE")
	ax.set_yticks(np.arange(-1, 1.3, 0.3))
	#ax.set_scale 把当前的图形x轴设置为对数坐标
	ax.set_xscale("log")
	ax.set_xlabel("$alpha$")
	plt.show()

def add_reg(data):
	features = ['x']
	labels = ['y']
	Y = data[labels]
	_X = data[features]
	_X['z'] = generate_randomvar()
	X = sm.add_constant(_X)
	print('加入惩罚项（权重=0.1）的估计结果：\n%s' % train_regulize_model(X,Y,0.1).params)
	visualize_model(X,Y)

def read_data(file):
	data = pd.read_csv(file)
	return data 

if __name__ == "__main__":
	data = read_data('simple_example.csv')
	add_reg(data)

