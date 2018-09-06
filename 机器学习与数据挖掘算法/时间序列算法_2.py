# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 22:43:19 2018
时间序列模式
来源《数据分析与挖掘实战》
@author: 刘刚
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.arima_model import ARIMA*

file = 'arima_data.xls'
forecastnum = 5
os.chdir('D:\python\python_数据分析与挖掘实践\chapter5\demo\data')

data = pd.read_excel(file, index_col='日期')
d1 = data['销量']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
data.plot()  # 图1
plt.show()

print('Raw Seq"s adf result: ', adfuller(d1))

d_data = data.diff().dropna()
d_data.columns = ['销量差分']
d_data.plot()  # 图2
plt.show()
plot_acf(d_data).show()  # 图3
plot_pacf(d_data).show()  # 图4
print('diff Seq"s adf result: ', adfuller(d_data['销量差分']))
print('diff Seq"s acorr ljungbox result: ', acorr_ljungbox(
    d_data, lags=1))  # return stats,p value

pmax = int(len(d_data)/10)
qmax = int(len(d_data)/10)
bic_matrix = []
data['销量'] = data['销量'].astype(float)  # 不加这个报错
for p in range(pmax+1):
    tmp = []
    for q in range(qmax+1):
        try:
            tmp.append(ARIMA(data, (p, 1, q)).fit().bic)
        except:
            tmp.append(None)
    bic_matrix.append(tmp)
bic_matrix = pd.DataFrame(bic_matrix)
p, q = bic_matrix.stack().idxmin()  # bic_matrix return level index
print('BIC最小的P值和Q值为：%s,%s' % (p, q))
model = ARIMA(data, (p, 1, q)).fit()
model.summary2()
model.forecast(5)
'''
Raw Seq"s adf result: 
 (1.813771015094526, 0.9983759421514264, 10, 26, {'1%': -3.7112123008648155, '5%': -2.981246804733728, '10%': -2.6300945562130176}, 299.46989866024177)

diff Seq"s adf result:  
(-3.1560562366723537, 0.022673435440048798, 0, 35, {'1%': -3.6327426647230316, '5%': -2.9485102040816327, '10%': -2.6130173469387756}, 287.5909090780334)

diff Seq"s acorr ljungbox result: 
 (array([11.30402222]), array([0.00077339]))

BIC最小的P值和Q值为：
0,1
'''
