# IPython log file

get_ipython().run_line_magic('cd', 'b')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', '..')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('bookmark', '-l')
get_ipython().run_line_magic('pwd', '')
#[Out]# 'C:\\python'
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', 'python_数据科学手册/')
pwed
get_ipython().run_line_magic('pwd', '')
#[Out]# 'C:\\python\\python_数据科学手册'
get_ipython().run_line_magic('bookmark', '-l')
get_ipython().run_line_magic('bookmark', "c 'C:\\\\python\\\\python_数据科学手册'")
get_ipython().run_line_magic('bookmark', '-l')
get_ipython().run_line_magic('cd', 'c')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', 'myself_x/')
get_ipython().run_line_magic('ls', '')
import random
a = rng.randint(10,size=(3,4))
a = random.randint(10,size=(3,4))
a = random.randint(12,size=(3,4))
a = random.randint(12).reshape((3,4))
a = random.randint(12).reshape(3,4)
a = random.randint(12,12).reshape(3,4)
a = np.random.randint(12,12).reshape(3,4)
import numpy as np
a = np.random.randint(12,12).reshape(3,4)
a = np.random.randint(12,size=(3,4))
a
#[Out]# array([[ 2,  8, 10,  7],
#[Out]#        [ 7,  6,  2,  8],
#[Out]#        [10,  7,  1, 10]])
a-a[0]
#[Out]# array([[ 0,  0,  0,  0],
#[Out]#        [ 5, -2, -8,  1],
#[Out]#        [ 8, -1, -9,  3]])
a.shape
#[Out]# (3, 4)
a[0].shape
#[Out]# (4,)
type(a)
#[Out]# numpy.ndarray
import pandas as pd
df = pd.DataFrame(a,columns=list'QRST')
df = pd.DataFrame(a,columns=list('QRST'))
df
#[Out]#     Q  R   S   T
#[Out]# 0   2  8  10   7
#[Out]# 1   7  6   2   8
#[Out]# 2  10  7   1  10
df.iloc[0]
#[Out]# Q     2
#[Out]# R     8
#[Out]# S    10
#[Out]# T     7
#[Out]# Name: 0, dtype: int32
df - df.iloc[0]
#[Out]#    Q  R  S  T
#[Out]# 0  0  0  0  0
#[Out]# 1  5 -2 -8  1
#[Out]# 2  8 -1 -9  3
df.subtract(df['R'],axis=0)
#[Out]#    Q  R  S  T
#[Out]# 0 -6  0  2 -1
#[Out]# 1  1  0 -4  2
#[Out]# 2  3  0 -6  3
df.subtract(df['R'],axis=1)
#[Out]#     Q   R   S   T   0   1   2
#[Out]# 0 NaN NaN NaN NaN NaN NaN NaN
#[Out]# 1 NaN NaN NaN NaN NaN NaN NaN
#[Out]# 2 NaN NaN NaN NaN NaN NaN NaN
df['R']
#[Out]# 0    8
#[Out]# 1    6
#[Out]# 2    7
#[Out]# Name: R, dtype: int32
df
#[Out]#     Q  R   S   T
#[Out]# 0   2  8  10   7
#[Out]# 1   7  6   2   8
#[Out]# 2  10  7   1  10
df - df.iloc[:,'R']
df - df.iloc[:,1]
#[Out]#     Q   R   S   T   0   1   2
#[Out]# 0 NaN NaN NaN NaN NaN NaN NaN
#[Out]# 1 NaN NaN NaN NaN NaN NaN NaN
#[Out]# 2 NaN NaN NaN NaN NaN NaN NaN
df
#[Out]#     Q  R   S   T
#[Out]# 0   2  8  10   7
#[Out]# 1   7  6   2   8
#[Out]# 2  10  7   1  10
df - df.loc[:,'R']
#[Out]#     Q   R   S   T   0   1   2
#[Out]# 0 NaN NaN NaN NaN NaN NaN NaN
#[Out]# 1 NaN NaN NaN NaN NaN NaN NaN
#[Out]# 2 NaN NaN NaN NaN NaN NaN NaN
df - df.iloc[1,:]
#[Out]#    Q  R  S  T
#[Out]# 0 -5  2  8 -1
#[Out]# 1  0  0  0  0
#[Out]# 2  3  1 -1  2
df.subtract(df['R'],axis=0)
#[Out]#    Q  R  S  T
#[Out]# 0 -6  0  2 -1
#[Out]# 1  1  0 -4  2
#[Out]# 2  3  0 -6  3
df.subtract(df['R'],axis=0)####????
#[Out]#    Q  R  S  T
#[Out]# 0 -6  0  2 -1
#[Out]# 1  1  0 -4  2
#[Out]# 2  3  0 -6  3
halfrow = df.iloc[0,::2]
halfrow
#[Out]# Q     2
#[Out]# S    10
#[Out]# Name: 0, dtype: int32
df
#[Out]#     Q  R   S   T
#[Out]# 0   2  8  10   7
#[Out]# 1   7  6   2   8
#[Out]# 2  10  7   1  10
df - halfrow
#[Out]#      Q   R    S   T
#[Out]# 0  0.0 NaN  0.0 NaN
#[Out]# 1  5.0 NaN -8.0 NaN
#[Out]# 2  8.0 NaN -9.0 NaN
va1 = np.array([1,None,3,4])
va1
#[Out]# array([1, None, 3, 4], dtype=object)
for dtype in ['obj','int']:
    print('dtype = ',dtype
    $%timeit np.array(1E6,dtype=dtype).sum()
for dtype in ['obj','int']:
    print('dtype = ',dtype)
    $%timeit np.array(1E6,dtype=dtype).sum()
for dtype in ['obj','int']:
    print('dtype = ',dtype)
    get_ipython().run_line_magic('timeit', 'np.array(1E6,dtype=dtype).sum()')
    print()
    
for dtype in ['object','int']:
    print('dtype = ',dtype)
    get_ipython().run_line_magic('timeit', 'np.array(1E6,dtype=dtype).sum()')
    print()
    
va1
#[Out]# array([1, None, 3, 4], dtype=object)
va1.sum()
va2 = np.array([1,np.nan,3,4])
va2.dtype
#[Out]# dtype('float64')
1 + np.nan
#[Out]# nan
0 * np.nan
#[Out]# nan
va2.sum()
#[Out]# nan
va1
#[Out]# array([1, None, 3, 4], dtype=object)
va2.min()
#[Out]# nan
va2.min
#[Out]# <function ndarray.min>
va2
#[Out]# array([ 1., nan,  3.,  4.])
va2.max)_
va2.max()
#[Out]# nan
va2.min()###???
#[Out]# nan
np.nansum(va2),np.nanmin(va2),np.nanmax(va2)
#[Out]# (8.0, 1.0, 4.0)
pd.Series([1,np.nan,2,None])
#[Out]# 0    1.0
#[Out]# 1    NaN
#[Out]# 2    2.0
#[Out]# 3    NaN
#[Out]# dtype: float64
x = pd.Series(range(2),dtype=int)
x
#[Out]# 0    0
#[Out]# 1    1
#[Out]# dtype: int32
x[0]
#[Out]# 0
x[0] = None
x
#[Out]# 0    NaN
#[Out]# 1    1.0
#[Out]# dtype: float64
#pandas中字符串类型的数据通常是用object类型存储的
print('#pandas中字符串类型的数据通常是用object类型存储的')
print('#pandas中字符串类型的数据通常是用object类型存储的')
data = pd.Series([1,np.nan,'hello',None])
data.isnull()
#[Out]# 0    False
#[Out]# 1     True
#[Out]# 2    False
#[Out]# 3     True
#[Out]# dtype: bool
data[data.notnull()]
#[Out]# 0        1
#[Out]# 2    hello
#[Out]# dtype: object
data
#[Out]# 0        1
#[Out]# 1      NaN
#[Out]# 2    hello
#[Out]# 3     None
#[Out]# dtype: object
data.dropna()
#[Out]# 0        1
#[Out]# 2    hello
#[Out]# dtype: object
df = pd.DataFrame([[1,np.nan,2],[2,3,5],[np.nan,4,6]])
df
#[Out]#      0    1  2
#[Out]# 0  1.0  NaN  2
#[Out]# 1  2.0  3.0  5
#[Out]# 2  NaN  4.0  6
df.dropna()
#[Out]#      0    1  2
#[Out]# 1  2.0  3.0  5
df.dropna(axis=1)
#[Out]#    2
#[Out]# 0  2
#[Out]# 1  5
#[Out]# 2  6
df[3] = np.nan
df
#[Out]#      0    1  2   3
#[Out]# 0  1.0  NaN  2 NaN
#[Out]# 1  2.0  3.0  5 NaN
#[Out]# 2  NaN  4.0  6 NaN
df.dropna(axis = 1,how = 'all')
#[Out]#      0    1  2
#[Out]# 0  1.0  NaN  2
#[Out]# 1  2.0  3.0  5
#[Out]# 2  NaN  4.0  6
df.dropna(axis=0,thresh=3)
#[Out]#      0    1  2   3
#[Out]# 1  2.0  3.0  5 NaN
df
#[Out]#      0    1  2   3
#[Out]# 0  1.0  NaN  2 NaN
#[Out]# 1  2.0  3.0  5 NaN
#[Out]# 2  NaN  4.0  6 NaN
df.dropna(axis=0,thresh=3)#thresh参数设置行或列中非缺失值的最小数量
#[Out]#      0    1  2   3
#[Out]# 1  2.0  3.0  5 NaN
data = pd.Series([1,np.nan,2,None,3]),index=list('abcde'))
data = pd.Series([1,np.nan,2,None,3],index=list('abcde'))
data
#[Out]# a    1.0
#[Out]# b    NaN
#[Out]# c    2.0
#[Out]# d    NaN
#[Out]# e    3.0
#[Out]# dtype: float64
data.fillna(0)
#[Out]# a    1.0
#[Out]# b    0.0
#[Out]# c    2.0
#[Out]# d    0.0
#[Out]# e    3.0
#[Out]# dtype: float64
data.fillna(method='ffill')
#[Out]# a    1.0
#[Out]# b    1.0
#[Out]# c    2.0
#[Out]# d    2.0
#[Out]# e    3.0
#[Out]# dtype: float64
data.fillna(method='bfill')
#[Out]# a    1.0
#[Out]# b    2.0
#[Out]# c    2.0
#[Out]# d    3.0
#[Out]# e    3.0
#[Out]# dtype: float64
df
#[Out]#      0    1  2   3
#[Out]# 0  1.0  NaN  2 NaN
#[Out]# 1  2.0  3.0  5 NaN
#[Out]# 2  NaN  4.0  6 NaN
df.fillna(method='ffill',axis=1)
#[Out]#      0    1    2    3
#[Out]# 0  1.0  1.0  2.0  2.0
#[Out]# 1  2.0  3.0  5.0  5.0
#[Out]# 2  NaN  4.0  6.0  6.0
df.fillna(method='ffill',axis=0)
#[Out]#      0    1  2   3
#[Out]# 0  1.0  NaN  2 NaN
#[Out]# 1  2.0  3.0  5 NaN
#[Out]# 2  2.0  4.0  6 NaN
index = [('c',2000),('c',2010),('ny',2000),('ny',2010),('t',2000),('t',2010)]
populations = [33871111,37251111,18971111,19371111,20851111,25141111]
pop = pd.Series(populations,index=index)
pop
#[Out]# (c, 2000)     33871111
#[Out]# (c, 2010)     37251111
#[Out]# (ny, 2000)    18971111
#[Out]# (ny, 2010)    19371111
#[Out]# (t, 2000)     20851111
#[Out]# (t, 2010)     25141111
#[Out]# dtype: int64
pop[('c',2010):('t',2000)]
#[Out]# (c, 2010)     37251111
#[Out]# (ny, 2000)    18971111
#[Out]# (ny, 2010)    19371111
#[Out]# (t, 2000)     20851111
#[Out]# dtype: int64
index = pd.MultiIndex.from_tuples(index)
index
#[Out]# MultiIndex(levels=[['c', 'ny', 't'], [2000, 2010]],
#[Out]#            labels=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]])
pop.index
#[Out]# Index([('c', 2000), ('c', 2010), ('ny', 2000), ('ny', 2010), ('t', 2000),
#[Out]#        ('t', 2010)],
#[Out]#       dtype='object')
pop = pop.reindex(index)
op
pop
#[Out]# c   2000    33871111
#[Out]#     2010    37251111
#[Out]# ny  2000    18971111
#[Out]#     2010    19371111
#[Out]# t   2000    20851111
#[Out]#     2010    25141111
#[Out]# dtype: int64
type(pop)
#[Out]# pandas.core.series.Series
pop[:,2010]
#[Out]# c     37251111
#[Out]# ny    19371111
#[Out]# t     25141111
#[Out]# dtype: int64
pop_df = pop.unstack()
pop_df
#[Out]#         2000      2010
#[Out]# c   33871111  37251111
#[Out]# ny  18971111  19371111
#[Out]# t   20851111  25141111
pop_df.stack()
#[Out]# c   2000    33871111
#[Out]#     2010    37251111
#[Out]# ny  2000    18971111
#[Out]#     2010    19371111
#[Out]# t   2000    20851111
#[Out]#     2010    25141111
#[Out]# dtype: int64
pop_df = pd.DataFrame({'total':pop,'under18':[926711,9284111,4687111,4318111,5906111,6879111]})
pop_df
#[Out]#             total  under18
#[Out]# c  2000  33871111   926711
#[Out]#    2010  37251111  9284111
#[Out]# ny 2000  18971111  4687111
#[Out]#    2010  19371111  4318111
#[Out]# t  2000  20851111  5906111
#[Out]#    2010  25141111  6879111
pop_df = pd.DataFrame({'total':pop,'under18':[9267111,9284111,4687111,4318111,5906111,6879111]})
pop_f
pop_df
#[Out]#             total  under18
#[Out]# c  2000  33871111  9267111
#[Out]#    2010  37251111  9284111
#[Out]# ny 2000  18971111  4687111
#[Out]#    2010  19371111  4318111
#[Out]# t  2000  20851111  5906111
#[Out]#    2010  25141111  6879111
pop_df = pd.DataFrame({'total':pop,'under18':[9267111,9284111,4687111,4318111,5906111,6879111]})#多层索引是pop的索引
pop
#[Out]# c   2000    33871111
#[Out]#     2010    37251111
#[Out]# ny  2000    18971111
#[Out]#     2010    19371111
#[Out]# t   2000    20851111
#[Out]#     2010    25141111
#[Out]# dtype: int64
f_u18 = pop_df['under18'] / pop_df['total']
f_u18
#[Out]# c   2000    0.273599
#[Out]#     2010    0.249230
#[Out]# ny  2000    0.247066
#[Out]#     2010    0.222915
#[Out]# t   2000    0.283252
#[Out]#     2010    0.273620
#[Out]# dtype: float64
pop_df['under18']
#[Out]# c   2000    9267111
#[Out]#     2010    9284111
#[Out]# ny  2000    4687111
#[Out]#     2010    4318111
#[Out]# t   2000    5906111
#[Out]#     2010    6879111
#[Out]# Name: under18, dtype: int64
pop_df['total']
#[Out]# c   2000    33871111
#[Out]#     2010    37251111
#[Out]# ny  2000    18971111
#[Out]#     2010    19371111
#[Out]# t   2000    20851111
#[Out]#     2010    25141111
#[Out]# Name: total, dtype: int64
f_u18.unstack()
#[Out]#         2000      2010
#[Out]# c   0.273599  0.249230
#[Out]# ny  0.247066  0.222915
#[Out]# t   0.283252  0.273620
df = pd.DataFrame(np.random.rand(4,2),index=[['a','a','b'],[1,2,1,2]],columns=['data1','data2'])
df = pd.DataFrame(np.random.rand(4,2),index=[['a','a','b','b'],[1,2,1,2]],columns=['data1','data2'])
df
#[Out]#         data1     data2
#[Out]# a 1  0.990516  0.155809
#[Out]#   2  0.058254  0.796521
#[Out]# b 1  0.550604  0.079334
#[Out]#   2  0.599915  0.819961
pd.MultiIndex.from_arrays([['a','a','b','b'],[1,2,1,2]])
#[Out]# MultiIndex(levels=[['a', 'b'], [1, 2]],
#[Out]#            labels=[[0, 0, 1, 1], [0, 1, 0, 1]])
pd.MultiIndex.from_tuples([('a',1),('a',2),('b',1),('b',2)])
#[Out]# MultiIndex(levels=[['a', 'b'], [1, 2]],
#[Out]#            labels=[[0, 0, 1, 1], [0, 1, 0, 1]])
pop.index.names = ['state','year']
pop
#[Out]# state  year
#[Out]# c      2000    33871111
#[Out]#        2010    37251111
#[Out]# ny     2000    18971111
#[Out]#        2010    19371111
#[Out]# t      2000    20851111
#[Out]#        2010    25141111
#[Out]# dtype: int64
index = pd.MultiIndex.from_product([[2013,2014],[1,2]],names = ['year','visit'])
colums = pd.MultiIndex.from_product([['bob','Guido','Sue'],['HR','Temp']],names=['subject','type'])
data = np.round(np.random.randn(4,6),1)
data 
#[Out]# array([[ 1.3, -0.8, -1.4,  0.2, -1.6, -1.2],
#[Out]#        [-0.6, -0.5, -0.3, -0.1, -0. ,  0.2],
#[Out]#        [ 1.7, -0.8,  1. ,  1.9,  1.1,  1. ],
#[Out]#        [-0.4, -0.1,  0.5,  0.4, -0.5, -0.2]])
data[:,::2] *= 10
data += 37
data
#[Out]# array([[50. , 36.2, 23. , 37.2, 21. , 35.8],
#[Out]#        [31. , 36.5, 34. , 36.9, 37. , 37.2],
#[Out]#        [54. , 36.2, 47. , 38.9, 48. , 38. ],
#[Out]#        [33. , 36.9, 42. , 37.4, 32. , 36.8]])
health_data = pd.DataFrame(data,index=index,columns=columns)
health_data = pd.DataFrame(data,index=index,columns=column)
colums
#[Out]# MultiIndex(levels=[['Guido', 'Sue', 'bob'], ['HR', 'Temp']],
#[Out]#            labels=[[2, 2, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1]],
#[Out]#            names=['subject', 'type'])
columns = colums
health_data = pd.DataFrame(data,index=index,columns=columns)
health_data
#[Out]# subject      bob       Guido         Sue      
#[Out]# type          HR  Temp    HR  Temp    HR  Temp
#[Out]# year visit                                    
#[Out]# 2013 1      50.0  36.2  23.0  37.2  21.0  35.8
#[Out]#      2      31.0  36.5  34.0  36.9  37.0  37.2
#[Out]# 2014 1      54.0  36.2  47.0  38.9  48.0  38.0
#[Out]#      2      33.0  36.9  42.0  37.4  32.0  36.8
health_data['Guido']
#[Out]# type          HR  Temp
#[Out]# year visit            
#[Out]# 2013 1      23.0  37.2
#[Out]#      2      34.0  36.9
#[Out]# 2014 1      47.0  38.9
#[Out]#      2      42.0  37.4
pop
#[Out]# state  year
#[Out]# c      2000    33871111
#[Out]#        2010    37251111
#[Out]# ny     2000    18971111
#[Out]#        2010    19371111
#[Out]# t      2000    20851111
#[Out]#        2010    25141111
#[Out]# dtype: int64
pop['c',2000]
#[Out]# 33871111
pop['Guido']
pop
#[Out]# state  year
#[Out]# c      2000    33871111
#[Out]#        2010    37251111
#[Out]# ny     2000    18971111
#[Out]#        2010    19371111
#[Out]# t      2000    20851111
#[Out]#        2010    25141111
#[Out]# dtype: int64
health_data['Guido']
#[Out]# type          HR  Temp
#[Out]# year visit            
#[Out]# 2013 1      23.0  37.2
#[Out]#      2      34.0  36.9
#[Out]# 2014 1      47.0  38.9
#[Out]#      2      42.0  37.4
pop.loc['c'：
pop.loc['c':'n']
#[Out]# state  year
#[Out]# c      2000    33871111
#[Out]#        2010    37251111
#[Out]# dtype: int64
pop
#[Out]# state  year
#[Out]# c      2000    33871111
#[Out]#        2010    37251111
#[Out]# ny     2000    18971111
#[Out]#        2010    19371111
#[Out]# t      2000    20851111
#[Out]#        2010    25141111
#[Out]# dtype: int64
pop.loc['c':'ny']
#[Out]# state  year
#[Out]# c      2000    33871111
#[Out]#        2010    37251111
#[Out]# ny     2000    18971111
#[Out]#        2010    19371111
#[Out]# dtype: int64
pop[:,2000]
#[Out]# state
#[Out]# c     33871111
#[Out]# ny    18971111
#[Out]# t     20851111
#[Out]# dtype: int64
pop
#[Out]# state  year
#[Out]# c      2000    33871111
#[Out]#        2010    37251111
#[Out]# ny     2000    18971111
#[Out]#        2010    19371111
#[Out]# t      2000    20851111
#[Out]#        2010    25141111
#[Out]# dtype: int64
pop[pop> 22000000]
#[Out]# state  year
#[Out]# c      2000    33871111
#[Out]#        2010    37251111
#[Out]# t      2010    25141111
#[Out]# dtype: int64
pop[['c','t']]
#[Out]# state  year
#[Out]# c      2000    33871111
#[Out]#        2010    37251111
#[Out]# t      2000    20851111
#[Out]#        2010    25141111
#[Out]# dtype: int64
health_data
#[Out]# subject      bob       Guido         Sue      
#[Out]# type          HR  Temp    HR  Temp    HR  Temp
#[Out]# year visit                                    
#[Out]# 2013 1      50.0  36.2  23.0  37.2  21.0  35.8
#[Out]#      2      31.0  36.5  34.0  36.9  37.0  37.2
#[Out]# 2014 1      54.0  36.2  47.0  38.9  48.0  38.0
#[Out]#      2      33.0  36.9  42.0  37.4  32.0  36.8
health_data['Guido','HR']
#[Out]# year  visit
#[Out]# 2013  1        23.0
#[Out]#       2        34.0
#[Out]# 2014  1        47.0
#[Out]#       2        42.0
#[Out]# Name: (Guido, HR), dtype: float64
health_data
#[Out]# subject      bob       Guido         Sue      
#[Out]# type          HR  Temp    HR  Temp    HR  Temp
#[Out]# year visit                                    
#[Out]# 2013 1      50.0  36.2  23.0  37.2  21.0  35.8
#[Out]#      2      31.0  36.5  34.0  36.9  37.0  37.2
#[Out]# 2014 1      54.0  36.2  47.0  38.9  48.0  38.0
#[Out]#      2      33.0  36.9  42.0  37.4  32.0  36.8
health_data.iloc[:2,:2]
#[Out]# subject      bob      
#[Out]# type          HR  Temp
#[Out]# year visit            
#[Out]# 2013 1      50.0  36.2
#[Out]#      2      31.0  36.5
health_data.loc[:,('bob','HR')]
#[Out]# year  visit
#[Out]# 2013  1        50.0
#[Out]#       2        31.0
#[Out]# 2014  1        54.0
#[Out]#       2        33.0
#[Out]# Name: (bob, HR), dtype: float64
idx = pd.IndexSlice
health_data.loc[idx[:,1],idx[:,'HR']]
#[Out]# subject      bob Guido   Sue
#[Out]# type          HR    HR    HR
#[Out]# year visit                  
#[Out]# 2013 1      50.0  23.0  21.0
#[Out]# 2014 1      54.0  47.0  48.0
health_data
#[Out]# subject      bob       Guido         Sue      
#[Out]# type          HR  Temp    HR  Temp    HR  Temp
#[Out]# year visit                                    
#[Out]# 2013 1      50.0  36.2  23.0  37.2  21.0  35.8
#[Out]#      2      31.0  36.5  34.0  36.9  37.0  37.2
#[Out]# 2014 1      54.0  36.2  47.0  38.9  48.0  38.0
#[Out]#      2      33.0  36.9  42.0  37.4  32.0  36.8
index = pd.MultiIndex.from_product([['a','c','b'],[1,2]])
data = pd.Series(np.random.rand(6),index=index)
data.index.names = ['char','int']
data
#[Out]# char  int
#[Out]# a     1      0.293867
#[Out]#       2      0.556014
#[Out]# c     1      0.173260
#[Out]#       2      0.753540
#[Out]# b     1      0.449921
#[Out]#       2      0.963916
#[Out]# dtype: float64
try:
    data['a':'b']
except:KeyError as e:
try:
    data['a':'b']
except KeyError as e :
    print(type(e))
    print(e)
    
try:
    data['a','b']
except KeyError as e :
    print(type(e))
    print(e)
    
    
data
#[Out]# char  int
#[Out]# a     1      0.293867
#[Out]#       2      0.556014
#[Out]# c     1      0.173260
#[Out]#       2      0.753540
#[Out]# b     1      0.449921
#[Out]#       2      0.963916
#[Out]# dtype: float64
data = data.sort_index()
data
#[Out]# char  int
#[Out]# a     1      0.293867
#[Out]#       2      0.556014
#[Out]# b     1      0.449921
#[Out]#       2      0.963916
#[Out]# c     1      0.173260
#[Out]#       2      0.753540
#[Out]# dtype: float64
try:
    data['a':'b']
except KeyError as e :
    print(type(e))
    print(e)
    
    
try:
    data['a':'b']
except KeyError as e :
    print(type(e))
    print(e)
    
    
data['a':'b']
#[Out]# char  int
#[Out]# a     1      0.293867
#[Out]#       2      0.556014
#[Out]# b     1      0.449921
#[Out]#       2      0.963916
#[Out]# dtype: float64
pop.unstack().stack()
#[Out]# state  year
#[Out]# c      2000    33871111
#[Out]#        2010    37251111
#[Out]# ny     2000    18971111
#[Out]#        2010    19371111
#[Out]# t      2000    20851111
#[Out]#        2010    25141111
#[Out]# dtype: int64
p_flat = pop.reset_indexex(name='populations')
p_flat = pop.reset_index(name='populations')
p_
_
#[Out]# state  year
#[Out]# c      2000    33871111
#[Out]#        2010    37251111
#[Out]# ny     2000    18971111
#[Out]#        2010    19371111
#[Out]# t      2000    20851111
#[Out]#        2010    25141111
#[Out]# dtype: int64
p_flat
#[Out]#   state  year  populations
#[Out]# 0     c  2000     33871111
#[Out]# 1     c  2010     37251111
#[Out]# 2    ny  2000     18971111
#[Out]# 3    ny  2010     19371111
#[Out]# 4     t  2000     20851111
#[Out]# 5     t  2010     25141111
pop
#[Out]# state  year
#[Out]# c      2000    33871111
#[Out]#        2010    37251111
#[Out]# ny     2000    18971111
#[Out]#        2010    19371111
#[Out]# t      2000    20851111
#[Out]#        2010    25141111
#[Out]# dtype: int64
populations
#[Out]# [33871111, 37251111, 18971111, 19371111, 20851111, 25141111]
pop_flat.set_index(['state','year'])
p_flat.set_index(['state','year'])
#[Out]#             populations
#[Out]# state year             
#[Out]# c     2000     33871111
#[Out]#       2010     37251111
#[Out]# ny    2000     18971111
#[Out]#       2010     19371111
#[Out]# t     2000     20851111
#[Out]#       2010     25141111
health_data
#[Out]# subject      bob       Guido         Sue      
#[Out]# type          HR  Temp    HR  Temp    HR  Temp
#[Out]# year visit                                    
#[Out]# 2013 1      50.0  36.2  23.0  37.2  21.0  35.8
#[Out]#      2      31.0  36.5  34.0  36.9  37.0  37.2
#[Out]# 2014 1      54.0  36.2  47.0  38.9  48.0  38.0
#[Out]#      2      33.0  36.9  42.0  37.4  32.0  36.8
data_mean = health_data.mean(level='year')
data_mean
#[Out]# subject   bob        Guido          Sue      
#[Out]# type       HR   Temp    HR   Temp    HR  Temp
#[Out]# year                                         
#[Out]# 2013     40.5  36.35  28.5  37.05  29.0  36.5
#[Out]# 2014     43.5  36.55  44.5  38.15  40.0  37.4
data_mean.mean(axis=1,level='type')
#[Out]# type         HR       Temp
#[Out]# year                      
#[Out]# 2013  32.666667  36.633333
#[Out]# 2014  42.666667  37.366667
ser1 = pd.Series(['A','B','C'],index=[1,2,3])
ser1 = pd.Series(['D','E','F'],index=[4,5,6])
ser1 = pd.Series(['A','B','C'],index=[1,2,3])
ser2 = pd.Series(['D','E','F'],index=[4,5,6])
pd.concat([ser1,ser2])
#[Out]# 1    A
#[Out]# 2    B
#[Out]# 3    C
#[Out]# 4    D
#[Out]# 5    E
#[Out]# 6    F
#[Out]# dtype: object
df1 = make_df('AB',[1,2])
def make_df(cols,ind):
    data = {c:[str(c) + str(i) for i in ind] for c in cols}
    return pd.DataFame(data,ind)
make_df('ABC',range(3))
def make_df(cols,ind):
    data = {c:[str(c) + str(i) for i in ind] for c in cols}
    return pd.DataFrame(data,ind)
ind
df1 = pd.DataFrame(['a1','b1','a2','b2'],columns=['A','B'])
df1 = pd.DataFrame([['a1','b1'],['a2','b2']],columns=['A','B'])
df1
#[Out]#     A   B
#[Out]# 0  a1  b1
#[Out]# 1  a2  b2
df1 = pd.DataFrame([['a3','b3'],['a4','b4']],columns=['A','B'])
df1.append(df2)
df1 = pd.DataFrame([['a1','b1'],['a2','b2']],columns=['A','B'])
= pd.DataFrame([['a1','b1'],['a2','b2']],columns=['A','B'])
df2 = pd.DataFrame([['a3','b3'],['a4','b4']],columns=['A','B'])
df1.append(df2)
#[Out]#     A   B
#[Out]# 0  a1  b1
#[Out]# 1  a2  b2
#[Out]# 0  a3  b3
#[Out]# 1  a4  b4
df1 = pd.DataFrame({'employee':{'Bob','Jake','Lisa','Sue'],'group':['Accounting','Engineering','Engineering','HR']})
df1 = pd.DataFrame({'employee':['Bob','Jake','Lisa','Sue'],'group':['Accounting','Engineering','Engineering','HR']})
df1
#[Out]#   employee        group
#[Out]# 0      Bob   Accounting
#[Out]# 1     Jake  Engineering
#[Out]# 2     Lisa  Engineering
#[Out]# 3      Sue           HR
df2 = pd.DataFrame({'emplyee':['lisa','Bob','Jake','Sue'],'hire_data':[2004,2008,2012,2014]})
df2
#[Out]#   emplyee  hire_data
#[Out]# 0    lisa       2004
#[Out]# 1     Bob       2008
#[Out]# 2    Jake       2012
#[Out]# 3     Sue       2014
df3 = pd.merge(df1,df2)
df1
#[Out]#   employee        group
#[Out]# 0      Bob   Accounting
#[Out]# 1     Jake  Engineering
#[Out]# 2     Lisa  Engineering
#[Out]# 3      Sue           HR
df2
#[Out]#   emplyee  hire_data
#[Out]# 0    lisa       2004
#[Out]# 1     Bob       2008
#[Out]# 2    Jake       2012
#[Out]# 3     Sue       2014
pd.merge(df1,df2)
df2.columns = ['employee','hire_date']
df3 = pd.merge(df1,df2)
df3
#[Out]#   employee        group  hire_date
#[Out]# 0      Bob   Accounting       2008
#[Out]# 1     Jake  Engineering       2012
#[Out]# 2      Sue           HR       2014
df1
#[Out]#   employee        group
#[Out]# 0      Bob   Accounting
#[Out]# 1     Jake  Engineering
#[Out]# 2     Lisa  Engineering
#[Out]# 3      Sue           HR
df2
#[Out]#   employee  hire_date
#[Out]# 0     lisa       2004
#[Out]# 1      Bob       2008
#[Out]# 2     Jake       2012
#[Out]# 3      Sue       2014
df4 = pd.DataFrame({'group':['Accounting','Engineering','HR'],'supervisor':['Carly','Guido','Steve']})
df3
#[Out]#   employee        group  hire_date
#[Out]# 0      Bob   Accounting       2008
#[Out]# 1     Jake  Engineering       2012
#[Out]# 2      Sue           HR       2014
df4
#[Out]#          group supervisor
#[Out]# 0   Accounting      Carly
#[Out]# 1  Engineering      Guido
#[Out]# 2           HR      Steve
pd.merge(df3,df4)
#[Out]#   employee        group  hire_date supervisor
#[Out]# 0      Bob   Accounting       2008      Carly
#[Out]# 1     Jake  Engineering       2012      Guido
#[Out]# 2      Sue           HR       2014      Steve
pd.merge(df3,df3,on='out')
get_ipython().run_line_magic('pinfo', 'pd.merge')
pd.merge(df3,df3,how='outer')
#[Out]#   employee        group  hire_date
#[Out]# 0      Bob   Accounting       2008
#[Out]# 1     Jake  Engineering       2012
#[Out]# 2      Sue           HR       2014
pd.merge(df3,df3,how='inner')
#[Out]#   employee        group  hire_date
#[Out]# 0      Bob   Accounting       2008
#[Out]# 1     Jake  Engineering       2012
#[Out]# 2      Sue           HR       2014
df3
#[Out]#   employee        group  hire_date
#[Out]# 0      Bob   Accounting       2008
#[Out]# 1     Jake  Engineering       2012
#[Out]# 2      Sue           HR       2014
df4
#[Out]#          group supervisor
#[Out]# 0   Accounting      Carly
#[Out]# 1  Engineering      Guido
#[Out]# 2           HR      Steve
get_ipython().run_line_magic('pinfo2', 'df3')
df3
#[Out]#   employee        group  hire_date
#[Out]# 0      Bob   Accounting       2008
#[Out]# 1     Jake  Engineering       2012
#[Out]# 2      Sue           HR       2014
df1
#[Out]#   employee        group
#[Out]# 0      Bob   Accounting
#[Out]# 1     Jake  Engineering
#[Out]# 2     Lisa  Engineering
#[Out]# 3      Sue           HR
df2
#[Out]#   employee  hire_date
#[Out]# 0     lisa       2004
#[Out]# 1      Bob       2008
#[Out]# 2     Jake       2012
#[Out]# 3      Sue       2014
df3 = pd.merge(df1,df2)
df3
#[Out]#   employee        group  hire_date
#[Out]# 0      Bob   Accounting       2008
#[Out]# 1     Jake  Engineering       2012
#[Out]# 2      Sue           HR       2014
df1
#[Out]#   employee        group
#[Out]# 0      Bob   Accounting
#[Out]# 1     Jake  Engineering
#[Out]# 2     Lisa  Engineering
#[Out]# 3      Sue           HR
df2
#[Out]#   employee  hire_date
#[Out]# 0     lisa       2004
#[Out]# 1      Bob       2008
#[Out]# 2     Jake       2012
#[Out]# 3      Sue       2014
df2['employee'][0] = 'Lisa'
df2
#[Out]#   employee  hire_date
#[Out]# 0     Lisa       2004
#[Out]# 1      Bob       2008
#[Out]# 2     Jake       2012
#[Out]# 3      Sue       2014
df3 = pd.merge(df1,df2)
df3
#[Out]#   employee        group  hire_date
#[Out]# 0      Bob   Accounting       2008
#[Out]# 1     Jake  Engineering       2012
#[Out]# 2     Lisa  Engineering       2004
#[Out]# 3      Sue           HR       2014
pd.merge(df3,df4)
#[Out]#   employee        group  hire_date supervisor
#[Out]# 0      Bob   Accounting       2008      Carly
#[Out]# 1     Jake  Engineering       2012      Guido
#[Out]# 2     Lisa  Engineering       2004      Guido
#[Out]# 3      Sue           HR       2014      Steve
df4
#[Out]#          group supervisor
#[Out]# 0   Accounting      Carly
#[Out]# 1  Engineering      Guido
#[Out]# 2           HR      Steve
df5 = pd.DataFrame({'group':['Accounting','Accounting','Engineering','Engineering','HR','HR']})
df5 = pd.DataFrame({'group':['Accounting','Accounting','Engineering','Engineering','HR','HR'],'skills':['math','spreadsheets','coding','spreadsheets','organization']})
df5 = pd.DataFrame({'group':['Accounting','Accounting','Engineering','Engineering','HR','HR'],'skills':['math','spreadsheets','coding','linux','spreadsheets','organization']})
df5
#[Out]#          group        skills
#[Out]# 0   Accounting          math
#[Out]# 1   Accounting  spreadsheets
#[Out]# 2  Engineering        coding
#[Out]# 3  Engineering         linux
#[Out]# 4           HR  spreadsheets
#[Out]# 5           HR  organization
pd.merge(df1,df5)
#[Out]#   employee        group        skills
#[Out]# 0      Bob   Accounting          math
#[Out]# 1      Bob   Accounting  spreadsheets
#[Out]# 2     Jake  Engineering        coding
#[Out]# 3     Jake  Engineering         linux
#[Out]# 4     Lisa  Engineering        coding
#[Out]# 5     Lisa  Engineering         linux
#[Out]# 6      Sue           HR  spreadsheets
#[Out]# 7      Sue           HR  organization
df1
#[Out]#   employee        group
#[Out]# 0      Bob   Accounting
#[Out]# 1     Jake  Engineering
#[Out]# 2     Lisa  Engineering
#[Out]# 3      Sue           HR
df2
#[Out]#   employee  hire_date
#[Out]# 0     Lisa       2004
#[Out]# 1      Bob       2008
#[Out]# 2     Jake       2012
#[Out]# 3      Sue       2014
pd.merge(df1,df2,on='employee')
#[Out]#   employee        group  hire_date
#[Out]# 0      Bob   Accounting       2008
#[Out]# 1     Jake  Engineering       2012
#[Out]# 2     Lisa  Engineering       2004
#[Out]# 3      Sue           HR       2014
df3
#[Out]#   employee        group  hire_date
#[Out]# 0      Bob   Accounting       2008
#[Out]# 1     Jake  Engineering       2012
#[Out]# 2     Lisa  Engineering       2004
#[Out]# 3      Sue           HR       2014
df3 = pd.DataFrame({'name':['Bob','Jake','Lisa','Sue'],'salary':[70000,80000,120000,90000]})
pd.merge(df1,df3,left_on='employee',right_on='name')
#[Out]#   employee        group  name  salary
#[Out]# 0      Bob   Accounting   Bob   70000
#[Out]# 1     Jake  Engineering  Jake   80000
#[Out]# 2     Lisa  Engineering  Lisa  120000
#[Out]# 3      Sue           HR   Sue   90000
pd.merge(df1,df3,left_on='employee',right_on='name').drop('name')
pd.merge(df1,df3,left_on='employee',right_on='name').drop('name',axis=1)
#[Out]#   employee        group  salary
#[Out]# 0      Bob   Accounting   70000
#[Out]# 1     Jake  Engineering   80000
#[Out]# 2     Lisa  Engineering  120000
#[Out]# 3      Sue           HR   90000
