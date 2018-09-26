# -*- coding: utf-8 -*-
"""
创建时间 Wed Sep 26 11:41:04 2018
描述:
作者:PM.liugang
"""

'''属性变化代码'''
import pandas as pd

ifile = 'discdata.xls'
ofile = 'discdata_processed.xls'

data = pd.read_excel(ifile)
data = data[data['TARGET_ID'] == 184].copy()
dataGroup = data.groupby('COLLECTTIME')


def attrTrans(x):
    '''
    param x 数据集 DataFrame
    return
    '''
    result = pd.Series(index=['SYS_NAME',
                              'CWXT_DB:184:C:\\',
                              'CWXT_DB:184:D:\\',
                              'COLLECTTIME'])

    result['SYS_NAME'] = x['SYS_NAME'].iloc[0]
    result['COLLECTTIME'] = x['COLLECTTIME'].iloc[0]
    result['CWXT_DB:184:C:\\'] = x['VALUE'].iloc[0]
    result['CWXT_DB:184:D:\\'] = x['VALUE'].iloc[1]
    return result


dataProcessed = dataGroup.apply(attrTrans)
print(dataProcessed)

'''平稳性检验代码'''
# 参数初始化
dfile = 'discdata_processed.xls'
data = pd.read_excel(dfile)
data = data.iloc[:len(data)-5]

# 平稳性检验
from statsmodels.tsa.stattools import adfuller as ADF
diff = 0
adf = ADF(data['CWXT_DB:184:D:\\'])

while adf[1] >= 0.05:
    diff = diff + 1
    adf = ADF(data['CWXT_DB:184:D:\\'].diff(diff).dropna())

print('原始序列经过%s阶差分后归于平稳.P值为%s' % (diff, adf[1]))

'''白噪声检验代码'''
# 白噪声检验
from statsmodels.stats.diagnostic import acorr_ljungbox
[[lb], [p]] = acorr_ljungbox(data['CWXT_DB:184:D:\\'], lags=1)
if p < 0.05:
    print('原始序列为非白噪声序列，对应的P值为: %s' % p)
else:
    print('原始序列为白噪声序列，对应的P值为: %s' % p)

[[lb], [p]] = acorr_ljungbox(data['CWXT_DB:184:D:\\'].diff().dropna(),
                             lags=1)
if p < 0.05:`
    print('原始序列为非白噪声序列，对应的P值为: %s' % p)
else:
    print('原始序列为白噪声序列，对应的P值为: %s' % p)
