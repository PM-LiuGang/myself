# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 21:00:00 2018
Python时间序列分析
@author: 刘刚
"""

import pandas as pd 
import numpy as np

from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.arima_model import ARMA
import matplotlib.pyplot as plt 
import prettytable
import os 
import warnings
warnings.filterwarnings('ignore')
os.chdir('d:\\python\\python_数据分析与数据化运营\\chapter4')

def pre_table(table_name,table_rows):
	'''
	:param table_name 表格名称
	:param table_rows 表格内容，嵌套列表
	:return 展示表格内容
	'''
	table = prettytable.PrettyTable()
	table.field_names = table_name
	for i in table_rows:
		table.add_row(i)
	return table
	
def get_best_log(ts,max_log=5,rule1=True,rule2=True):
	'''
	:param ts 时间序列数据，Series类型
	:param max_log 最大log处理的次数，int类型
	:param rule1 规则布尔值，布尔型
	:param rule2 规则布尔值，布尔型
	:return 达到平稳处理的最佳次数值和处理后的时间序列
	'''
	if rule1 and rule2:
		return 0,ts
	else:
		for i in range(1,max_log):
			ts = np.log(ts)
			lbvalue,pvalue2 = acorr_ljungbox(ts,lags=1)
			adf,pvalue1,usedlag,nobs,critical_value,icbest = adfuller(ts)
			rule_1 = (adf < critical_value['1%'] and adf < critical_value['5%'] and adf < critical_value['10%'] and pvalue1 < 0.01)
			rule_2 = pvalue2 < 0.05
			rule_3 = i < 5 
			if rule_1 and rule_2 and rule_3:
				print('The best log n is: {0}'.format(i))
				return i,ts
				
def recover_log(ts,log_n):
	'''
	:function 还原经过平稳处理的数据
	:param ts 经过log方法平稳处理的时间序列，series类型
	:param log_n log方法处理的次数，int类型
	:return 还原后的时间序列
	'''
	for i in range(1,log_n + 1):
		ts = np.exp(ts)
	return ts 
	
def adf_val(ts,ts_title,acf_title,pacf_title):
	'''
	:function 平稳性检验
	:param ts 时间序列数据，Series类型
	:param ts_title 时间序列图的标题名称，字符串
	:param acf_title 自相关图的标题名称，字符串
	:param pacf_title 偏相关图的标题名称，字符串
	:return adf值，adf的p值，三种状态的检验值
	'''
	plt.figure()
	plt.plot(ts)
	plt.title(ts_title)
	plt.show()
	plot_acf(ts,lags=20,title=acf_title).show()
	plot_pacf(ts,lags=20,title=pacf_title).show()
	adf,pvalue,usedlag,nobs,critical_value,icbest = adfuller(ts)
	table_name = ['adf','pvalue','usedlag','nobs','critical_value','icbest']
	table_rows = [[adf,pvalue,usedlag,nobs,critical_value,icbest]]
	adf_table = pre_table(table_name,table_rows)
	print('stationarity')
	print(adf_table)
	return adf,pvalue,critical_value
	
def acorr_val(ts):
	'''
	:function 白噪声
	:param ts 时间序列数据，Series类型
	:return 白噪声检验的p值和展示数据表格对象
	'''
	lbvalue,pvalue = acorr_ljungbox(ts,lags=1)
	table_name = ['lbvalue','pvalue']
	table_rows = [[lbvalue,pvalue]]
	acorr_ljungbox_table = pre_table(table_name,table_rows)
	print('atationarity score')
	print(acorr_ljungbox_table)
	return pvalue
	
def arma_fit(ts):
	'''
	:function arma最优模型训练
	:param ts 时间序列数据，Series类型
	:return 最优状态下的p，q，arma模型对象，pdq数据框和展示参数表格对象
	'''
	max_count = int(len(ts)/10)
	bic = float('inf')
	tmp_score = []
	for tmp_p in range(max_count + 1):
		for tmp_q in range(max_count + 1):
			model = ARMA(ts,order=(tmp_p,tmp_q))
			try:
				results_ARMA = model.fit(disp=-1,method='css')
			except:
				continue
			finally:
				tmp_aic = results_ARMA.aic
				tmp_bic = results_ARMA.bic 
				tmp_hqic = results_ARMA.hqic
				tmp_score.append([tmp_p,tmp_q,tmp_aic,tmp_bic,tmp_hqic])
				if tmp_bic < bic:
					p = tmp_p
					q = tmp_q 
					model_arma = results_ARMA
					aic = tmp_bic
					bic = tmp_bic
					hqic = tmp_bic
	pdq_metrix = np.array(tmp_score)
	pdq_pd = pd.DataFrame(pdq_metrix,columns=['p','q','aic','bic','hqic'])
	table_name = ['p','q','aic','bic','hqic']
	table_rows = [[p,q,aic,bic,hqic]]
	parameter_table = pre_table(table_name,table_rows)
	print('each p/q training record')
	print(pdq_pd)
	print('best p and q'.title())
	print(parameter_table)
	return model_arma
	
def train_test(model_arma,ts,log_n,rule1=True,rule2=True):
	'''
	:param model_arma 最优ARMA模型对象
	:param ts 时间序列数据，Series类型
	:param log_n 平稳性处理的log次数，int型
	:param rule1 
	:param rule2 
	:return 还原后的时间序列 
	'''
	train_predict = model_arma.predict()
	if not (rule1 and rule2):
		train_predict = recover_log(train_predict,log_n)
		ts = recover_log(ts,log_n)
	ts_data_new = ts[train_predict.index]
	RMSE = np.sqrt(np.sum((train_predict - ts_data_new) ** 2) / ts_data_new.size)
	plt.figure()
	train_predict.plot(label='predicted_data',style='--')
	ts_data_new.plot(label='raw data')
	plt.legend(loc='best')
	plt.title('raw data and predicted data with RMSE of %.2f' % RMSE)
	plt.show()
	return ts 

def predict_data(model_arma,ts,log_n,start,end,rule1=True,rule2=True):
	'''
	:function 预测未来指定时间项的数据
	:param model_arma 最优ARMA模型对象
	:param ts 时间序列数据，Series类型
	:param log_n 平稳性处理的log次数，int型
	:param rule1 
	:param rule2
	:param start 要预测数据的开始时间索引
	:param end 要预测数据的结束时间索引
	:return  
	'''
	predict_ts = model_arma.predict(start=start,end=end)
	print('-----------Predict Data--------------')
	if not (rule1 and rule2):
		predict_ts = recover_log(predict_ts,log_n)
	print(predict_ts)
	plt.figure()
	ts.plot(label='Raw Time Series')
	predict_ts.plot(label='Predict_data',style='--')
	plt.legend(loc='best')
	plt.title('Predicted Time Series')
	plt.show()
	
date_parser = lambda dates:pd.datetime.strptime(dates,'%m-%d-%Y')
df = pd.read_table('time_series.txt',delimiter='\t',index_col='date',date_parser=date_parser)
ts_data = df['number'].astype('float32')
print('data summary')
print(ts_data.describe())

adf,pvalue1,critical_value = adf_val(ts_data,'Raw Time Series','Raw acf','Raw Pacf')
pvalue2 = acorr_val(ts_data)

rule_1 = (adf < critical_value['1%'] and adf < critical_value['5%'] and adf < critical_value['10%'] and pvalue1 < 0.01)
rule_2 = (pvalue2[0,] < 0.05)

log_n,ts_data = get_best_log(ts_data,max_log=5,rule1=rule_1,rule2=rule_2)
adf,pvalue1,critical_value = adf_val(ts_data,'final time series','final acf','final pacf')
pvalue2 = acorr_val(ts_data)

model_arma = arma_fit(ts_data)
ts_data = train_test(model_arma,ts_data,log_n,rule1=rule_1,rule2=rule_2)

start = '1991-07-28'
end = '1991-08-02'
predict_data(model_arma,ts_data,log_n,start,end,rule1=rule_1,rule2=rule_2)

