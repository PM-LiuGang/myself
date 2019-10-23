# -*- coding: utf-8 -*-
# 遗留问题 prettytable中显示 [values]
import pandas as pd

from sqlalchemy import create_engine

'''读取数据'''
engine = create_engine(
    'mysql+pymysql://root:123456@172.168.10.104:3306/test?charset=gb2312')
# create_engine(数据库格式 程序名 账号密码@地址端口 数据库名 指定编码)
sql = pd.read_sql('all_gzdata', engine, chunksize=10000)
# 表名 连接数据的引擎 分块读取（每次读取1万条记录） 返回-迭代器对象-未真正读取数据
counts = [i['fullURLId'].value_counts() for i in sql]

'''数据转换'''
counts = pd.concat(counts).groupby(level=0).sum()  # level=0 index
counts = counts.reset_index()
counts.columns = ['index', 'num']
counts['type'] = counts['index'].str.extract('(\d{3})')
counts_ = counts[['type', 'num']].groupby('type').sum()
counts_ = counts_.sort_values('num', ascending=False)
counts_['percentage'] = (counts_['num']/counts_['num'].sum())*100

'''网页类型统计'''

'''统计107类别的情况'''


def count107(i):
    '''
    param i 数据集 DataFrame/Series
    return 
    ----------------------
    示例：
    知识内容页 http://www.*****.com/info/*/数字.html 其中数字可能带有_
    知识首页 http://www.*****.com/info/*/
    知识列表页 http://www.*****.com/info/*.html
    '''
    j = i[['fullURL']][i['fullURLId'].str.contains('107')].copy()
    j['type'] = None
    j['type'][j['fullURL'].str.contains('info/.+?/')] = '知识首页'
    j['type'][j['fullURL'].str.contains('info/.+?/.+?')] = '知识列表页'
    j['type'][j['fullURL'].str.contains('/\d+?_*\d+?\.html')] = '知识内容页'
    return j['type'].value_counts()


engine = create_engine(
    'mysql+pymysql://root:123456@172.168.10.104:3306/test?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize=10000)

counts2 = [count107(i) for i in sql]
counts2 = pd.concat(counts2).groupby(level=0).sum()

'''统计点击次数'''
engine = create_engine(
    'mysql+pymysql://root:123456@172.168.10.104:3306/test?charset=gb2312')
sql = pd.read_sql('all_gzdata', engine, chunksize=10000)

c = [i['realIP'].value_counts() for i in sql]
counts3 = pd.concat(c).groupby(level=0).sum()
counts3 = pd.DataFrame(counts3)
counts3['次数'] = 1
counts3_ = counts3.groupby(0).sum()

'''数据预处理'''
# 数据清洗
import pandas as pd
engine = create_engine(
    'mysql+pymysql://root:123456@172.168.10.104:3306/test?charset=gb2312')
sql = pd.read_sql('all_gzdata', engine, chunksize=10000)

for i in sql:
    d = i[['realIP', 'fullURL']]
    d = d[d['fullURL'].str.contains('\.html')].copy()
    d.to_sql('cleaned_gzdata', engine, index=False, if_exists='append')

# 数据变换
engine = create_engine(
    'mysql+pymysql://root:123456@172.168.10.104:3306/test?charset=gb2312')
sql = pd.read_sql('all_gzdata', engine, chunksize=10000)

for i in sql:
    d = i.copy()
    d['fullURL'] = d['fullURL'].str.replace('_\d{0,2}.html', '.html')
    d = d.drop_duplicates()
    d.to_sql('changed_gzdata', engine, index=False, if_exists='append')

# 网址分类
engine = create_engine(
    'mysql+pymysql://root:123456@172.168.10.104:3306/test?charset=gb2312')
sql = pd.read_sql('all_gzdata', engine, chunksize=10000)

for i in sql:
    d = i.copy()
    d['type_l'] = d['fullURL']
    d['type_l'][d['fullURL'].str.contains('(ask)|(askzt)')] = 'zixun'
    d.to_sql('splited_gzdata',engine,index=False,if_exists='append')
    
def page199(i): #自定义统计函数
	j = i[['fullURL','pageTitle']][(i['fullURLId'].str.contains('199')) & (i['fullURL'].str.contains('\?'))]
	j['pageTitle'].fillna(u'空',inplace=True)
	j['type'] = u'其他' # 添加空列
	j['type'][j['pageTitle'].str.contains(u'法律快车-律师助手')]= u'法律快车-律师助手'
	j['type'][j['pageTitle'].str.contains(u'咨询发布成功')]= u'咨询发布成功'
	j['type'][j['pageTitle'].str.contains(u'免费发布法律咨询' )] = u'免费发布法律咨询'
	j['type'][j['pageTitle'].str.contains(u'法律快搜')] = u'快搜'
	j['type'][j['pageTitle'].str.contains(u'法律快车法律经验')] = u'法律快车法律经验'
	j['type'][j['pageTitle'].str.contains(u'法律快车法律咨询')] = u'法律快车法律咨询'
	j['type'][(j['pageTitle'].str.contains(u'_法律快车')) | (j['pageTitle'].str.contains(u'-法律快车'))] = u'法律快车'
	j['type'][j['pageTitle'].str.contains(u'空')] = u'空'
	return j


