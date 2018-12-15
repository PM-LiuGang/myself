# -*- coding: utf-8 -*-
"""
创建时间 Thu Oct 11 13:58:02 2018
描述:参考网络上的编写，将原书中所分析的内容中缺少的代码实现了 
作者:PM.liugang
create_engine(数据库格式 程序名 账号密码@地址端口 数据库名 指定编码)
read sql 表名 连接数据的引擎 分块读取 返回-生成器-未真正读取数据
"""

# 遗留问题 prettytable中显示 [values]
import pandas as pd

from sqlalchemy import create_engine

'''读取数据'''
engine = create_engine(
    'mysql+pymysql://root:123456@172.168.10.104:3306/test?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize=10000)

'''网页类型分析'''

# 统计各个网页类型所占的比例
counts1 =[i['fullURLId'].value_counts() for i in sql]
