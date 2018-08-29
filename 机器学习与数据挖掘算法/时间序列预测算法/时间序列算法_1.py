# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 23:59:00 2018
来源 《python运营》
@author: 刘刚
"""
# AR模型 Xt = Φ0+Φ1Xt-1+Φ2Xt-2+。。。+ΦpXt-p + εt，以前P期的序列值Xt-1，Xt-2，，，Xt-p为自变量、随机变量Xt的取xt为因变量建立线性回归模型
# MA模型Xt=u+ε-θ1εt-1-θ2εt-2--。。。。。。-θqεt-q，随机变量Xt的取值xt与以前各期的序列值无关，建议xt与前q期的随机扰动εt-1，εt-2，εt-3，，，εt-q的线性回归模型
import pandas as pd
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')  # 忽略一些告警
# acf和pacf的展示库
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller  # 单位根平稳性检测
from statsmodels.stats.diagnostic import acorr_ljungbox  # 白噪声随机性检测
from statsmodels.tsa.arima_model import ARMA as arma  # 并没用arima，用的不是差分，用的是log
import matplotlib.pyplot as plt
import prettytable

os.chdir('C:\python\python_数据分析与数据化运营\chapter4')


def pre_table(table_name, table_rows):
    '''
    param：table_name：表格名称，字符串列表
    param：table_row：表格内容，嵌套列表
    return：表格对象
    '''
    table = prettytable.PrettyTable()
    table.field_names = table_name
    for i in table_rows:
        table.add_row(i)  # 多行数据
    return table


def get_best_log(ts, max_log=5, rule1=True, rule2=True):
    '''
    param | ts:时间序列数据，Series类型
    param | max_log：最大的log处理次数，int类型
    param | rule1：规则1，布尔类型
    param | rule2：规则2，布尔类型
    return | 到达平稳序列处理的最佳次数数值和处理后的时间序列
    '''
    if rule1 and rule2:
        return 0, ts
    else:
        for i in range(1, max_log):
            ts = np.log(ts)  # 对数处理
            lbvalue, pvalue1 = acorr_ljungbox(ts, lags=1)  # 白噪声
            adf, pvalue2, usedlag, nobs, critical_values, icbest = adfuller(
                ts)  # 单位根检验
            # 这个条件是另一本数中没有提及的 adf需要同时小于critical values的三个值
            # 白噪声的p值小于0.01，不应该是0.05么
            rule_1 = (adf < critical_values['1%'] and adf < critical_values['5%']
                      and adf < critical_values['10%'] and pvalue1 < 0.01)
            rule_2 = (pvalue2 < 0.05)
            rule_3 = (i < 5)
            if rule_1 and rule_2 and rule_3:
                print('The best log n is:{0}'.format(i))
                return i, ts


def recover_log(ts, log_n):
    '''
    |param ts:经过log方法平稳处理的时间序列，Series类型
    |param log_n:log方法处理的次数，int类型
    |return 指数操作后，还原时间序列
    '''
    for i in range(1, log_n+1):
        ts = np.exp(ts)
    return ts


def adf_val(ts, ts_title, acf_title, pacf_title):
    '''
    |param ts:时间序列数据，Series类型
    |param ts_title：时间序列图的标题名称，字符串类型
    |param acf_title：acf图的标题名称，字符串类型
    |param pacf_title：pacf图的标题名称，字符串类型
    |return adf值，adf的p值，三种状态的检验值1%,5%,10%
    '''
    plt.figure()
    plt.plot(ts)
    plt.title(ts_title)
    plt.show()
    plot_acf(ts, lags=20, title=acf_title).show()
    plot_pacf(ts, lags=20, title=pacf_title).show()
    adf, pvalue, usedlag, nobs, critical_values, icbest = adfuller(ts)
    table_name = ['adf', 'pvalue', 'usedlag',
                  'nobs', 'critical_values', 'icbest']
    table_rows = [[adf, pvalue, usedlag, nobs, critical_values, icbest]]
    adf_table = pre_table(table_name, table_rows)
    print('stochastic score')
    print(adf_table)
    # 规则1,2使用
    return adf, pvalue, critical_values


def acorr_val(ts):
    '''
    |param ts:时间序列数据，Series类型
    |return 白噪声检验的P值和展示数据表格对象
    '''
    lbvalue, pvalue = acorr_ljungbox(ts, lags=1)
    table_name = ['lbvalue', 'pvalue']
    table_rows = [[lbvalue, pvalue]]
    acorr_ljungbox_table = pre_table(table_name, table_rows)
    print('stationarity score')
    print(acorr_ljungbox_table)
    # 是否小于0.01
    return pvalue


def arma_fit(ts):
    '''
    |param ts:时间序列数据，已经经过平稳性处理，并满足平稳性和白噪音检验的序列，Series类型
    |return 最优状态下的p值，q值，arma模型对象，pdq数据框和展示参数表格对象
    '''
    max_count = int(len(ts)/10)
    bic = float('inf')  # 初始值为正无穷
    tmp_score = []
    for tmp_p in range(max_count+1):
        for tmp_q in range(max_count+1):
            model = arma(ts, order=(tmp_p, tmp_q))
            try:
                # disp=-1不打印收敛信息
                # css 控制最大似然的计算方法是条件平方和似然度最大化
                result_arma = model.fit(disp=-1, method='css')
            except:
                continue
            finally:
                tmp_aic = result_arma.aic
                tmp_bic = result_arma.bic
                tmp_hqic = result_arma.hqic
                tmp_score.append([tmp_p, tmp_q, tmp_aic, tmp_bic, tmp_hqic])
                # 循环，找一个最小的bic，然后引用
                if tmp_bic < bic:
                    p = tmp_p
                    q = tmp_q
                    model_arma = result_arma
                    # 如果判断bic的值最小的值要小，就认为是最优模型，将p q aic bic hqic 值存储下来
                    aic = tmp_bic
                    bic = tmp_bic
                    hqic = tmp_bic
    pdq_metrix = np.array(tmp_score)
    pdq_pd = pd.DataFrame(pdq_metrix, columns=['p', 'q', 'aic', 'bic', 'hqic'])
    table_name = ['p', 'q', 'aic', 'bic', 'hqic']
    table_rows = [[p, q, aic, bic, hqic]]
    parameter_table = pre_table(table_name, table_rows)
    print('each p/q traing record')
    print(pdq_pd)
    print('best p and q')
    print(parameter_table)
    return model_arma


def train_test(model_arma, ts, log_n, rule1=True, rule2=True):
    '''
    |param model_arma:最优arma模型对象
    |param ts:时间序列数据，Series类型
    |param log n：平稳性处理的log次数，int类型
    |param rule1：满足平稳性检测的条件
    |param rule2：满足白噪声检测的条件
    |return 还原后的时间序列
    '''
    train_predict = model_arma.predict()  # ?
    if not (rule1 and rule2):  # if rule1 and rule2 = False 会执行下面语句
        # 规则1和规则2是满足平稳性和白噪声的条件的2个规则
        train_predict = recover_log(train_predict, log_n)
        ts = recover_log(ts, log_n)
    ts_data_new = ts[train_predict.index]  # 保持与预测数据数量一致，用索引同意
    RMSE = np.sqrt((np.sum(train_predict-ts_data_new) ** 2) / ts_data_new.size)

    plt.figure()
    train_predict.plot(label='predicted data', style='--')
    ts_data_new.plot(label='raw data')
    plt.legend(loc='best')
    plt.title('raw data and predicted data with RMSE of %.2f' % RMSE)
    plt.show()
    return ts


def predict_data(model_arma, ts, log_n, start, end, rule1=True, rule2=True):
    '''
    param
    -----
    model_arma:最优arma的模型对象
    ts：时间序列数据
    log n：平稳性处理的log次数，int类型
    start：要预测数据的开始索引
    end:要预测数据的结束索引

    return
    ------
    null
    '''
    predict_ts = model_arma.predict(start=start, end=end)
    print('------------------predict data-----------')
    if not (rule1 and rule2):
        predict_ts = recover_log(predict_ts, log_n)
    print(predict_ts)
    plt.figure()
    ts.plot(label='raw time series')
    predict_ts.plot(label='predicted data', style='--')
    plt.legend(loc='best')
    plt.title('predicted time series')
    plt.show()


def date_parse(dates): return pd.datetime.strptime(dates, '%m-%d-%Y')


df = pd.read_table('time_series.txt', delimiter='\t',
                   index_col='date', date_parser=date_parse)
ts_data = df['number'].astype('float32')
print('data summary')
print(ts_data.describe())
adf, pvalue1, critical_values = adf_val(
    ts_data, 'raw time series', 'raw acf', 'raw pacf')
pvalue2 = acorr_val(ts_data)
rule1 = (adf < critical_values['1%'] and adf < critical_values['5%']
         and adf < critical_values['10%'] and pvalue1 < 0.01)
rule2 = (pvalue2[0, ] < 0.05)
log_n, ts_data = get_best_log(ts_data, max_log=5, rule1=rule1, rule2=rule2)
adf, pvalue1, critical_values = adf_val(
    ts_data, 'final time series', 'final acf', 'final pacf')
pvalue2 = acorr_val(ts_data)
model_arma = arma_fit(ts_data)
ts_data = train_test(model_arma, ts_data, log_n, rule1=rule1, rule2=rule2)
start = '1991-07-28'
end = '1991-08-02'
predict_data(model_arma, ts_data, log_n, start, end, rule1=rule1, rule2=rule2)
