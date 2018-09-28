# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 23:59:00 2018
python时间序列分析
@author: 刘刚
"""

import pandas as pd
import numpy as np
import warnings
import matplotlib.pyplot as plt
import prettytable
import time

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller  # 单位根平稳性检测
from statsmodels.stats.diagnostic import acorr_ljungbox  # 白噪声随机性检测
from statsmodels.tsa.arima_model import ARMA as arma  # 并没用arima，用的不是差分，用的是log

warnings.filterwarnings('ignore')  # 忽略一些告警

def outPreTable(table_name, table_rows):
    '''
    param  |table_name：表格名称，字符串列表
    param  |table_row：表格内容，嵌套列表
    return |表格对象
    '''
    table = prettytable.PrettyTable()
    table.field_names = table_name
    for i in table_rows:
        table.add_row(i)  # 多行数据
    return table


def getBestLogNumber(ts, max_log=5, rule1=True, rule2=True):
    '''
    param  | ts:时间序列数据，Series类型
    param  | max_log：最大的log处理次数，int类型
    param  | rule1：规则1，布尔类型
    param  | rule2：规则2，布尔类型
    return | 到达平稳序列处理的最佳次数数值和处理后的时间序列
    '''
    if rule1 and rule2: 
        return 0, ts
    else:
        for i in range(1, max_log):
            ts = np.log(ts)
            lbvalue, pvalue1 = acorr_ljungbox(ts, lags=1)
            adf, pvalue2, usedlag, nobs, critical_values, icbest = adfuller(ts)
            rule_1 = (adf < critical_values['1%'] and \
                      adf < critical_values['5%'] and \
                      adf < critical_values['10%'] and \
                      pvalue1 < 0.01)
            rule_2 = (pvalue2 < 0.05)
            rule_3 = (i < 5)
            if rule_1 and rule_2 and rule_3:
                print('The best log n is:{0}'.format(i))
                return i, ts

def logRecoverTs(ts, log_n):
    '''
    param  | ts:经过log方法平稳处理的时间序列，Series类型
    param  | log_n:log方法处理的次数，int类型
    return | 还原后的时间序列
    '''
    for i in range(1, log_n+1):
        ts = np.exp(ts)
    return ts

def adfValidate(ts, ts_title, acf_title, pacf_title):
    '''
    param  | ts:时间序列数据，Series类型
    param  | ts_title：时间序列图的标题名称，字符串类型
    param  | acf_title：acf图的标题名称，字符串类型
    param  | pacf_title：pacf图的标题名称，字符串类型
    return | adf值，adf的p值，三种状态的检验值1%,5%,10%
    '''
    plt.figure()
    plt.plot(ts)
    plt.title(ts_title)
    plt.show()
    
    plot_acf(ts, lags=20, title=acf_title).show()
    plot_pacf(ts, lags=20, title=pacf_title).show()
    
    adf, pvalue, usedlag, nobs, critical_values, icbest = adfuller(ts)
    table_name = ['adf', 
                  'pvalue', 
                  'usedlag',
                  'nobs', 
                  'critical_values', 
                  'icbest']
    table_rows = [[adf, 
                   pvalue, 
                   usedlag, 
                   nobs, 
                   critical_values, 
                   icbest]]
    adf_table = outPreTable(table_name, table_rows)
    print('Stochastic Score')
    print(adf_table)
    return adf, pvalue, critical_values

def acorrValidate(ts):
    '''
    param  | ts:时间序列数据，Series类型
    return | 白噪声检验的P值和展示数据表格对象
    '''
    lbvalue, pvalue = acorr_ljungbox(ts, lags=1)
    table_name = ['lbvalue', 'pvalue']
    table_rows = [[lbvalue, pvalue]] # note : [[]]
    acorr_ljungbox_table = outPreTable(table_name, table_rows)
    print('stationarity Score')
    print(acorr_ljungbox_table)
    return pvalue

def armaFit(ts):
    '''
    param  | ts:时间序列数据，Series类型
    return | 最优状态下的p值，q值，arma模型对象，pdq数据框和展示参数表格对象
    '''
    max_count = int(len(ts)/10)
    bic = float('inf')
    tmp_score = []
    for tmp_p in range(max_count+1):
        for tmp_q in range(max_count+1):
            model = arma(ts, order=(tmp_p, tmp_q)) 
            try:
                result_arma = model.fit(disp=-1, method='css') # ?
            except:
                continue
            finally:
                tmp_aic = result_arma.aic
                tmp_bic = result_arma.bic
                tmp_hqic = result_arma.hqic
                tmp_score.append([tmp_p, tmp_q, tmp_aic, tmp_bic, tmp_hqic])
                if tmp_bic < bic:
                    p = tmp_p
                    q = tmp_q
                    model_arma = result_arma
                    aic = tmp_bic
                    bic = tmp_bic
                    hqic = tmp_bic
    pdq_metrix = np.array(tmp_score)
    pdq_pd = pd.DataFrame(pdq_metrix, columns=['p', 'q', 'aic', 'bic', 'hqic'])
    table_name = ['p', 'q', 'aic', 'bic', 'hqic']
    table_rows = [[p, q, aic, bic, hqic]]
    parameter_table = outPreTable(table_name, table_rows)
    print('Each p/q Traing Record')
    print(pdq_pd)
    print('Best p and q')
    print(parameter_table)
    return model_arma


def trainTest(model_arma, ts, log_n, rule1=True, rule2=True):
    '''
    param  | model_arma:最优arma模型对象
    param  | ts:时间序列数据，Series类型 log处理后
    param  | log_n：平稳性处理的log次数，int类型
    param  | rule1：
    param  | rule2：
    return | 还原后的时间序列
    '''
    train_predict = model_arma.predict()  # ?
    if not (rule1 and rule2):
        train_predict = logRecoverTs(train_predict, log_n)
        ts = logRecoverTs(ts, log_n)
    ts_data_new = ts[train_predict.index]
    RMSE = np.sqrt((np.sum(train_predict-ts_data_new) ** 2) / ts_data_new.size)
    
    plt.figure()
    train_predict.plot(label='predicted data', style='--')
    ts_data_new.plot(label='raw data')
    plt.legend(loc='best')
    plt.title('raw data and predicted data with RMSE of %.2f' % RMSE)
    plt.show()
    return ts

def predictData(model_arma, ts, log_n, start, end, rule1=True, rule2=True):
    '''
    param  | model_arma:最优arma的模型对象
    param  | ts：时间序列数据
    param  | log n：平稳性处理的log次数，int类型
    param  | start：要预测数据的开始索引
    param  | end:要预测数据的结束索引
    return | null
    '''
    predict_ts = model_arma.predict(start=start, end=end)
    print('------------------predict data-----------')
    if not (rule1 and rule2):
        predict_ts = logRecoverTs(predict_ts, log_n)
    print(predict_ts)
    
    plt.figure()
    ts.plot(label='Raw Time Series')
    predict_ts.plot(label='Predicted Data', style='--')
    plt.legend(loc='best')
    plt.title('Predicted Time Series')
    plt.show()
    
date_parser = lambda dates:pd.datetime.strptime(dates,'%m-%d-%Y')
print('准备数据')
start1 = time.time()
df = pd.read_table('time_series.txt', 
                   delimiter='\t',
                   index_col='date', 
                   date_parser=date_parser)
ts_data = df['number'].astype('float32')
print('data summary')
print(ts_data.describe())
end1 = time.time()
print('准备数据用时 {0}'.format(end1-start1))

start2 = time.time()
adf, pvalue1, critical_values = adfValidate(ts_data, 
                                        'Raw Time Series', 
                                        'Raw Acf', 
                                        'Raw Pacf')
pvalue2 = acorrValidate(ts_data)
rule1 = (adf < critical_values['1%'] and \
         adf < critical_values['5%'] and \
         adf < critical_values['10%'] and \
         pvalue1 < 0.01)
rule2 = (pvalue2[0, ] < 0.05)

log_n, ts_data = getBestLogNumber(ts_data, 
                              max_log=5, 
                              rule1=rule1, 
                              rule2=rule2)
end2 = time.time()
print('获取最好的log次数为:{0},用时{1}'.format(log_n,end2-start2))

start3 = time.time()
adf, pvalue1, critical_values = adfValidate(ts_data, 
                                        'Final Time Series', 
                                        'Final Acf', 
                                        'Final Pacf')
pvalue2 = acorrValidate(ts_data)
model_arma = armaFit(ts_data)
ts_data = trainTest(model_arma, 
                     ts_data, 
                     log_n, 
                     rule1=rule1, 
                     rule2=rule2)
start = '1991-07-28'
end = '1991-08-02'
predictData(model_arma, 
            ts_data, 
            log_n, 
            start, 
            end, 
            rule1=rule1, 
            rule2=rule2)
end3 = time.time()
print('用最好的模型训练的新数据,用时{0}'.format(end3-start3))