# -*- coding:UTF-8 -*-
import statsmodels.api as sm
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
from statsmodels.sandbox.regression.predstd import wls_prediction_std

def linearmodel(data):
	features = ['x']
	label = ['y']
	y = data[label]
	#添加一个常数，这个常数是b，固定成本
	#为什么参数是data[features]
	x = sm.add_constant(data[features])
	re = trainmodel(x,y)
	modelsummary(re)

	resnew = trainmodel(data[features],y)
	print(resnew.summary())
	visualizemodel(resnew,data,features,label)

def trainmodel(x,y):
	#创建一个线性回归模型，OLS=普通最小二乘模型
	model = sm.OLS(y,x)
	re = model.fit()
	return re 

def modelsummary(re):
	#整体统计分析结果
	#这个相当于t_test的结果，t_test只能做单个变量的假设检验
	print(re.summary())
	#用f test检测x对应的系数是否显著
	#条件用字符串表示
	#f_test能做单个变量和多个变量的检验
	print("检验假设x的系数等于0：")
	print(re.f_test('x=0'))

	#用f test检测常量b是否显著
	print("检测假设const的系数等于0：")
	print(re.f_test('const=0'))

	# 用f test检测a=1, b=0同时成立的显著性
	print("检测假设x的系数等于1和const的系数等于0同时成立：")
	print(re.f_test(['x=1','const=0']))

def visualizemodel(re,data,features,label):
	#预测结果的标准差，置信区间的上边界和下边界
	prstd,prelow,preup = wls_prediction_std(re,alpha=0.05)
	plt.rcParams['font.sans-serif']=['SimHei']
	fig = plt.figure(figsize=(6,6),dpi=80)
	ax = fig.add_subplot(111)
	ax.set_title('%s' % '线性回归统计示例')
	ax.set_xlabel('$x$')
	ax.set_ylabel('$y$')
	ax.scatter(data[features], data[label], color='b',label='%s: $y = x + \epsilon$' % "真实值")
	ax.plot(data[features], preup, "r--", label='%s' % "95%置信区间")
	ax.plot(data[features], re.predict(data[features]), color='r',label=u'%s: $y = %.3fx$'% ("预测值", re.params[features]))
	ax.plot(data[features],prelow,'r--')
	legend = plt.legend(shadow=True)
	legend.get_frame().set_facecolor('#6F93AE')

if __name__ == '__main__':
	data = pd.read_csv('simple_example.csv')
	linearmodel(data)

