# -*- coding: utf-8 -*-
"""
创建时间 Wed Aug 29 10:13:50 2018
描述:
作者:PM.liugang
"""

# method 1
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine(
    'mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize=10000)

# method 2 mysql 链接
import mysql.connector
config = {'host': '127.0.0.1', 'user': 'root', 'password': '123456',
          'port': 3306, 'database': 'python_data', 'charset': 'gb2312'}
cnn = mysql.connector.connect(**config)  # 建立连接
cursor = cnn.cursor()  # 获得游标
sql = 'select * from sheet1 limit 5'  # sql语句
cursor.execute(sql)  # 执行sql语句
data = cursor.fetchall()  # 通过fetchall获得数据
for i in data[:2]:
    print(i)
cursor.close()  # 关闭游标
cnn.close()  # 关闭连接
