# -*- coding: utf-8 -*-
"""
创建时间 Wed Sep 26 11:41:04 2018
描述:
作者:PM.liugang
"""

'''属性变化代码'''
import pandas as pd
from warnings import filterwarnings

filterwarnings('ignore')

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
print('白噪声检验...')
from statsmodels.stats.diagnostic import acorr_ljungbox
[[lb], [p]] = acorr_ljungbox(data['CWXT_DB:184:D:\\'],
                             lags=1)

if p < 0.05:
    print('原始序列为非白噪声序列，对应的P值为: %s' % p)
else:
    print('原始序列为白噪声序列，对应的P值为: %s' % p)

# 一阶差分
print('一阶差分....')

[[lb], [p]] = acorr_ljungbox(data['CWXT_DB:184:D:\\'].diff().dropna(),
                             lags=1)
if p < 0.05:
    print('原始序列为非白噪声序列，对应的P值为: %s' % p)
else:
    print('原始序列为白噪声序列，对应的P值为: %s' % p)

'''模型识别代码'''
xdata = data['CWXT_DB:184:D:\\']
from statsmodels.tsa.arima_model import ARIMA
pmax = int(len(xdata)/10)
qmax = int(len(xdata)/10)
bic_matrix = []
for p in range(pmax+1):
    tmp = []
    for q in range(qmax+1):
        try:
            tmp.append(ARIMA(xdata, (p, 1, q)).fit().bic)
        except:
            tmp.append(None)
    bic_matrix.append(tmp)

bic_matrix = pd.DataFrame(bic_matrix)

# p,q = bic_matrix.stack().idxmin(skipna=False) # Type error
p = 0
q = 1
print('BIC最小的P值和Q值为：%s %s' % (p, q))

'''模型检验代码'''
arima = ARIMA(xdata, (0, 1, 1)).fit()
xdata_pred = arima.predict(typ='levels')
pred_error = (xdata_pred-xdata).dropna()
lb,p = acorr_ljungbox(pred_error,lags=lagnum)
h = (p<0.05).sum()
if h > 0:
    print('(模型ARIMA(0,1,1) 不符合白噪声检验')
else:
    print('模型ARIMA(0,1,1) 符合白噪声检验')

'''模型预测'''

