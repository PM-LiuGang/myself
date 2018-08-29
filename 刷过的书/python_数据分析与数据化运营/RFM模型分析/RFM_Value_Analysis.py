# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 06:21:35 2018
基于RFM的用户价值分析
@author: 刘刚
特征变量数：4（用户ID 订单日期 订单ID 浮点数据的订单金额）
数据记录数：86135
是否有NA值：有
是否有异常值：有
"""

import pandas as pd 
import time
import numpy as np
import mysql.connector
import os

os.chdir(r'D:\python\python_数据分析与数据化运营')

dtypes = {'ORDERDATE':object, 'ORDERID':object, 'AMOUNTINFO':np.float32}
'''路径不能有中文，如果有，报错，初始化失败'''
raw_data = pd.read_csv('D:\\python\\sales.csv',dtype=dtypes,index_col='USERID')
'''数据总体情况'''
print('Data Overview')
print(raw_data.head(4))
print('-'*30)
print('Data DESC')
print(raw_data.describe())
print('-'*60)
'''缺失值情况'''
na_cols = raw_data.isnull().any(axis=0)#数据框里有空值就置为True，只返回True
print('NA Cols')
print(na_cols)
print('-'*30)
na_lines = raw_data.isnull().any(axis=1)#返回多行，每行都有是True或False的结果
print('Na Recors')
print('Total number of NA lines is : {0}'.format(na_lines.sum()))#有10行是空行
print(raw_data[na_lines])#
print('-'*60)
'''异常值处理'''
sales_data = raw_data.dropna()#含有null行就丢弃
sales_data = sales_data[sales_data['AMOUNTINFO']>1]
'''日期格式转换'''
sales_data['ORDERDATE'] = pd.to_datetime(sales_data['ORDERDATE'],format='%Y-%m-%d')
print('Raw Dtypes')
print(sales_data.dtypes)
print('-'*60)
'''数据转换，每个用户id的r f m值'''
recency_value = sales_data['ORDERDATE'].groupby(sales_data.index).max()
frequency_value = sales_data.ORDERDATE.groupby(sales_data.index).count()
monetary_value = sales_data.AMOUNTINFO.groupby(sales_data.index).sum()
'''R F M scores'''
deadline_date = pd.datetime(2017,1,1)
#deadline_date-recency_value timedelta64 dt.day获得天的数值 int
r_interval = (deadline_date-recency_value).dt.days
r_score = pd.cut(r_interval,5,labels=[5,4,3,2,1])
f_score = pd.cut(frequency_value,5,labels=[1,2,3,4,5])
m_score = pd.cut(monetary_value,5,labels=[1,2,3,4,5])
'''RFM数据合并'''
rfm_list = [r_score,f_score,m_score]
rfm_cols = ['r_score','f_score','m_score']
'''pd.cut->array([[4, 2, 3, ..., 1, 4, 1]'''
rfm_pd = pd.DataFrame(np.array(rfm_list).T,dtype=np.int32,columns=rfm_cols,index=frequency_value.index)
print('RFM Score Overview:')
print(rfm_pd.head(4))
print('-'*60)
'''计算RFM总得分'''
rfm_pd['rfm_wscore'] = rfm_pd['r_score'] * 0.6 + rfm_pd['f_score'] * 0.3 + rfm_pd['m_score'] * 0.1

rfm_pd_tmp = rfm_pd.copy()
rfm_pd_tmp['r_score'] = rfm_pd_tmp['r_score'].astype(str)#修改源码中的astype('string')，报错，unknow style
rfm_pd_tmp['f_score'] = rfm_pd_tmp['f_score'].astype(str)
rfm_pd_tmp['m_score'] = rfm_pd_tmp['m_score'].astype(str)
rfm_pd['rfm_comb'] = rfm_pd_tmp['r_score'].str.cat(rfm_pd_tmp['f_score']).str.cat(rfm_pd_tmp['m_score'])

print('Final RFM Score Overview: ')
print(rfm_pd.head(4))
print('-' * 30)
print('Final RFM Scores DESC: ')
print(rfm_pd.describe())
rfm_pd.to_csv('my_sales_rfm_score.csv')
'''将信息写入到数据中'''
table_name = 'sales_rfm_score'
config = {'host':'127.0.0.1',
          'user':'root',
          'password':'123456',
          'port':3306,
          'database':'python_data',
          'buffered':True,
          'charset':'gb2312'}
con = mysql.connector.connect(**config)
cursor = con.cursor()
cursor.execute('show tables')
table_object = cursor.fetchall()#通过fetchall方法获得所有数据，表名
table_list = []
for t in table_object:#循环读出所有库
    table_list.append(t[0])
if not table_name in table_list:
    cursor.execute('''
    CREATE TABLE %s (
    userid     VARCHAR(20),
    r_score int(2),
    f_score int(2),
    m_score int(2),
    rfm_wscore DECIMAL(10,2),
    rfm_comb VARCHAR(10),
    insert_date VARCHAR(20))ENGINE=InnoDB DEFAULT CHARSET=gb2312''' % table_name)
    
user_id = rfm_pd.index
rfm_wscore = rfm_pd['rfm_wscore']
rfm_comb = rfm_pd['rfm_comb']
timestamp = time.strftime('%Y-%m-%d',time.localtime(time.time()))#转换本地时间到指定格式
print('Begin to insert data into table {0}...'.format(table_name))
for i in range(rfm_pd.shape[0]):
    insert_sql = "INSERT INTO `%s` VALUES ('%s',%s,%s,%s,%s,'%s','%s')" % (table_name,user_id[i],r_score.iloc[i],f_score.iloc[i],\
                                         m_score.iloc[i],rfm_wscore.iloc[i],rfm_comb.iloc[i],timestamp)#timestamp取的哪个时间
    cursor.execute(insert_sql)
    con.commit()#执行sql语句，execute中必须用“”
cursor.close()
con.close()
print('Finish inserting,total records is : %d' % (i+1))
