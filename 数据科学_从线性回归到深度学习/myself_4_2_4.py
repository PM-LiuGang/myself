# -*- coding: UTF-8 -*-
"""
此脚本用于展示过拟合问题
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures


def evaluate_model(model, testdata, features, labels, featurizer):
	# （（预测（多项式转换.测试数据（特征））- 测试数据（标签）） ** 2 ）/ n
    error = np.mean((model.predict(featurizer.fit_transform(testdata[features])) - testdata[labels]) ** 2)
    #
    score = np.mean(model.score(featurizer.fit_transform(testdata[features]), testdata[labels]))
    return error, score


def train_model(traindata, features, labels, featurizer):
	# fit_intercept 是否存在截距，默认存在 True
	# 定义评估模型，拟合数据
	model = linear_model.LinearRegression(fit_intercept=False)
	model.fit(featurizer.fit_transform(traindata[features]), traindata[labels])
	return model


def visualize_model(model, featurizer, data, features, labels, evaluation):
	plt.rcParams['font.sans-serif'] = ['SimHei']
	fig = plt.figure(figsize=(10, 10), dpi=80)
	for i in range(4):
		ax = fig.add_subplot(2, 2, i+1)
		# 4个图具体细节
		visualize_tion(ax, data, model[i], featurizer[i],evaluation[i], features, labels)
	plt.show()


def visualize_tion(ax, data, model, featurizer, evaluation, features, labels):
	# 每个子图里都包含一个散点图，一个折线图
	ax.scatter(data[features], data[labels], color='b')
	# 折线图，标签的折线图一定要用多项式拟合转换
	ax.plot(data[features], model.predict(featurizer.fit_transform(data[features])), color='r')
	#evaluation[0] = error, evaluation[1] = score
	ax.text(0.01, 0.99, '%s%.3f\n%s%.3f' % ('均方差:', evaluation[0], '决定系数:', evaluation[1]), style='italic',verticalalignment='top', horizontalalignment='left', transform=ax.transAxes, color='m', fontsize=13)


def overfitting(data):
	features = ['x']
	labels = ['y']
	traindata = data[:15]
	testdata = data[15:]
	# 为什么用列表
	featurizer = []
	overfittingmodel = []
	overfittingevaluation = []
	model = []
	evaluation = []
	for i in range(1, 11, 3):
		# i=1,4,7,10
		featurizer.append(PolynomialFeatures(degree=i))
		# 产生并训练模型，featurizer 多项式4次
		# featurizer[-1]每次取最新的featurizer列表中的最后添加的
		overfittingmodel.append(train_model(traindata, features, labels, featurizer[-1]))
		# 注意模型的训练数据data和traindata
		model.append(train_model(data, features, labels, featurizer[-1]))
		# 将模型的评估效果加到列表里
		# 两个评估，过拟合评估和普通评估
		overfittingevaluation.append(evaluate_model(overfittingmodel[-1], testdata, features, labels, featurizer[-1]))
		evaluation.append(evaluate_model(model[-1], data, features, labels, featurizer[-1]))
    # 图形化模型结果
    # 注意第一个参数和最后一个参数的不同
	visualize_model(model, featurizer, data, features, labels, evaluation)
	visualize_model(overfittingmodel, featurizer, data,features, labels, overfittingevaluation)

def readdata(path):
	data=pd.read_csv(path)
	return data

if __name__ == "__main__":
	data=readdata('simple_example.csv')
	featurizer=PolynomialFeatures(degree=5)
	overfitting(data)
