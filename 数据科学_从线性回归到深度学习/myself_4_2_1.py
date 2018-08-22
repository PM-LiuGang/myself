# -*- coding: UTF-8 -*-


import numpy as np
import sys
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn import linear_model

'''
def readdata(path):
	data = pd.read_csv(path)
	return data
'''	
def linearmodel(data):
	'''
	用途
	###############
	参数
	-------
	参数A：
	参数B：
	参数C:
	------
	返回
	##########
	'''
	feature = ['x']
	label = ['y']
	traindata = data[:15]
	testdata = data[15:]
	#训练一个模型，需要训练数据，特征，标签，因为这里trainmodel返回一个模型
	model = trainmodel(traindata,feature,label)
	#误差和准确率的计算，需要模型，测试数据，特征，标签，添加模型用于测试数据的使用
	error,score = evaluatemodel(model,testdata,feature,label)
	#可视化结果，需要模型，数据，特征，标签，误差，准确率，模型用于预测
	visualizemodel(model,data,feature,label,error,score)
	
def trainmodel(traindata,feature,label):
	#返回一个已经训练过的模型
	model = linear_model.LinearRegression()
	model.fit(traindata[feature],traindata[label])	
	return model
	
def evaluatemodel(model,testdata,feature,label):
	# 均方差(The mean squared error)，均方差越小越好
	# (预测Y-现有Y) ** 2/n 
	#非自有，需要单独计算
	# model.score 自有属性，参数为测试特征和测试标签
	error = np.mean((model.predict(testdata[feature])-testdata[label]) ** 2)
	score = model.score(testdata[feature],testdata[label])
	return error,score
	
def visualizemodel(model,data,feature,label,error,score):
	#可视化
	#中文名称、添加图框、只添加一个图、设置图标题、设置x，y的标签名称
	plt.rcParams['font.sans-serif']=['SimHei']
	fig = plt.figure(figsize=(6, 6), dpi=80)
	ax = fig.add_subplot(111)
	ax.set_title('%s' % '线性回归示例')
	ax.set_xlabel('$x$')
	ax.set_ylabel('$y$')
	#画出数据的散点图，标签 '真实值:y = x + e(阿拉伯数字，epsilon)'
	ax.scatter(data[feature],data[label],color='b',label='%s:$y = x + \epsilon$' % '真实值')
	#画出预测数据的线图，x坐标采用原数据，y坐标采用预测后的数据，标签 '预测值:y = model.coef_ * x ± model.intercept_'
	#model.intercept_ = 0.628
	#model.coef_ = 1.012
	if model.intercept_ > 0:
		ax.plot(data[feature],model.predict(data[feature]),color='r',label='%s:$y = %.3fx$ + %.3f' % ('预测值',model.coef_,model.intercept_))
	else:
		ax.plot(data[feature],model.predict(data[feature]),color='r',label='%s:$y = %.3fx$ - %.3f' % ("预测值",model.coef_,abs(model.intercept_)))
	#图例带阴影，边框设置颜色
	legend = plt.legend(shadow=True)
	legend.get_frame().set_facecolor('#6F93AE')
	#添加文本，在图中0.99 0.01占比处添加 均方差：error 换行 决定系数：score
	#error=0.726 | score=0.828
	ax.text(0.99, 0.01, '%s%.3f\n%s%.3f'% ("均方差：", error, "决定系数：", score),style='italic', verticalalignment='bottom', horizontalalignment='right',transform=ax.transAxes, color='m', fontsize=13)


if __name__ == '__main__':
#	path = r'C:\python\python_数据科学_从线性回归到深度学习\ch04-linear\simple_example\data\simple_example.csv'
#	data = readdata(path)
	#!pd read_csv 读取路径不能有中文，报错，初始化文件失败
	data = pd.read_csv('simple_example.csv')
	#自定义函数与系统函数不能重复
	linearmodel(data)
	