# IPython log file

get_ipython().run_line_magic('cd', 'c')
get_ipython().run_line_magic('pwd', '')
#[Out]# 'c:\\python\\python_数据科学手册\\myself_x'
get_ipython().run_line_magic('ls', '')
import numpy as np
import pandas as pd
import seaborn as sns
titanic = sns.load_dataset('titanic')
titanic = sns.load_dataset('titanic')
titanic = sns.load_dataset('titanic')titanic = sns.load_dataset('titanic')
titanic = sns.load_dataset('titanic')
get_ipython().run_line_magic('ls', '')
data = pd.read_csv('titanic_dataset.csv')
data.columns
#[Out]# Index(['survived', 'pclass', 'name', 'sex', 'age', 'sibsp', 'parch', 'ticket',
#[Out]#        'fare'],
#[Out]#       dtype='object')
titanic.groupby('sex')[['survived']].mean()
data.groupby('sex')[['survived']].mean()
#[Out]#         survived
#[Out]# sex             
#[Out]# female  0.727468
#[Out]# male    0.190985
data.groupby(['sex','class'])['survived'].aggregate('mean').unstack()
data.columns
#[Out]# Index(['survived', 'pclass', 'name', 'sex', 'age', 'sibsp', 'parch', 'ticket',
#[Out]#        'fare'],
#[Out]#       dtype='object')
data['pclass'][:5]
#[Out]# 0    1
#[Out]# 1    1
#[Out]# 2    1
#[Out]# 3    1
#[Out]# 4    1
#[Out]# Name: pclass, dtype: int64
data['pclass'].value_counts()
#[Out]# 3    709
#[Out]# 1    323
#[Out]# 2    277
#[Out]# Name: pclass, dtype: int64
data.groupby(['sex','pclass'])['survived'].aggregate('mean').unstack()
#[Out]# pclass         1         2         3
#[Out]# sex                                 
#[Out]# female  0.965278  0.886792  0.490741
#[Out]# male    0.340782  0.146199  0.152130
data.groupby(['sex','pclass'])['survived'].aggregate('mean')
#[Out]# sex     pclass
#[Out]# female  1         0.965278
#[Out]#         2         0.886792
#[Out]#         3         0.490741
#[Out]# male    1         0.340782
#[Out]#         2         0.146199
#[Out]#         3         0.152130
#[Out]# Name: survived, dtype: float64
data.groupby(['sex','pclass'])['survived']
#[Out]# <pandas.core.groupby.SeriesGroupBy object at 0x000001FFE6E73B70>
data.groupby(['sex','pclass'])['survived'].sum()
#[Out]# sex     pclass
#[Out]# female  1         139
#[Out]#         2          94
#[Out]#         3         106
#[Out]# male    1          61
#[Out]#         2          25
#[Out]#         3          75
#[Out]# Name: survived, dtype: int64
data.groupby(['sex','pclass'])['survived'].value_counts()
#[Out]# sex     pclass  survived
#[Out]# female  1       1           139
#[Out]#                 0             5
#[Out]#         2       1            94
#[Out]#                 0            12
#[Out]#         3       0           110
#[Out]#                 1           106
#[Out]# male    1       0           118
#[Out]#                 1            61
#[Out]#         2       0           146
#[Out]#                 1            25
#[Out]#         3       0           418
#[Out]#                 1            75
#[Out]# Name: survived, dtype: int64
data.pivot_table('survived',index='sex',columns='class')
data.pivot_table('survived',index='sex',columns='pclass')
#[Out]# pclass         1         2         3
#[Out]# sex                                 
#[Out]# female  0.965278  0.886792  0.490741
#[Out]# male    0.340782  0.146199  0.152130
data.groupby(['sex','pclass'])['survived'].aggregate('mean').unstack()
#[Out]# pclass         1         2         3
#[Out]# sex                                 
#[Out]# female  0.965278  0.886792  0.490741
#[Out]# male    0.340782  0.146199  0.152130
age = pd.cut(data['age'],[0,18,80])
#data.pivot_table('survived',['sex','age'],'pclass')
age
#[Out]# 0       (18, 80]
#[Out]# 1        (0, 18]
#[Out]# 2        (0, 18]
#[Out]# 3       (18, 80]
#[Out]# 4       (18, 80]
#[Out]# 5       (18, 80]
#[Out]# 6       (18, 80]
#[Out]# 7       (18, 80]
#[Out]# 8       (18, 80]
#[Out]# 9       (18, 80]
#[Out]# 10      (18, 80]
#[Out]# 11       (0, 18]
#[Out]# 12      (18, 80]
#[Out]# 13      (18, 80]
#[Out]# 14      (18, 80]
#[Out]# 15           NaN
#[Out]# 16      (18, 80]
#[Out]# 17      (18, 80]
#[Out]# 18      (18, 80]
#[Out]# 19      (18, 80]
#[Out]# 20      (18, 80]
#[Out]# 21      (18, 80]
#[Out]# 22      (18, 80]
#[Out]# 23      (18, 80]
#[Out]# 24      (18, 80]
#[Out]# 25      (18, 80]
#[Out]# 26      (18, 80]
#[Out]# 27      (18, 80]
#[Out]# 28      (18, 80]
#[Out]# 29      (18, 80]
#[Out]#           ...   
#[Out]# 1279     (0, 18]
#[Out]# 1280    (18, 80]
#[Out]# 1281    (18, 80]
#[Out]# 1282         NaN
#[Out]# 1283         NaN
#[Out]# 1284         NaN
#[Out]# 1285    (18, 80]
#[Out]# 1286    (18, 80]
#[Out]# 1287    (18, 80]
#[Out]# 1288     (0, 18]
#[Out]# 1289    (18, 80]
#[Out]# 1290    (18, 80]
#[Out]# 1291         NaN
#[Out]# 1292         NaN
#[Out]# 1293         NaN
#[Out]# 1294    (18, 80]
#[Out]# 1295    (18, 80]
#[Out]# 1296    (18, 80]
#[Out]# 1297         NaN
#[Out]# 1298    (18, 80]
#[Out]# 1299    (18, 80]
#[Out]# 1300     (0, 18]
#[Out]# 1301    (18, 80]
#[Out]# 1302         NaN
#[Out]# 1303         NaN
#[Out]# 1304     (0, 18]
#[Out]# 1305         NaN
#[Out]# 1306    (18, 80]
#[Out]# 1307    (18, 80]
#[Out]# 1308    (18, 80]
#[Out]# Name: age, Length: 1309, dtype: category
#[Out]# Categories (2, interval[int64]): [(0, 18] < (18, 80]]
data.pivot_table('survived',['sex','age'],'pclass')
#[Out]# pclass                 1         2         3
#[Out]# sex    age                                  
#[Out]# female 0.0000   1.000000  0.666667  0.531250
#[Out]#        0.1667        NaN       NaN  1.000000
#[Out]#        0.7500        NaN       NaN  1.000000
#[Out]#        0.9167        NaN  1.000000       NaN
#[Out]#        1.0000        NaN  1.000000  0.750000
#[Out]#        2.0000   0.000000  1.000000  0.200000
#[Out]#        3.0000        NaN  1.000000  0.000000
#[Out]#        4.0000        NaN  1.000000  1.000000
#[Out]#        5.0000        NaN  1.000000  1.000000
#[Out]#        6.0000        NaN  1.000000  0.000000
#[Out]#        7.0000        NaN  1.000000       NaN
#[Out]#        8.0000        NaN  1.000000  0.000000
#[Out]#        9.0000        NaN       NaN  0.200000
#[Out]#        10.0000       NaN       NaN  0.000000
#[Out]#        11.0000       NaN       NaN  0.000000
#[Out]#        12.0000       NaN  1.000000       NaN
#[Out]#        13.0000       NaN  1.000000  1.000000
#[Out]#        14.0000  1.000000  1.000000  0.500000
#[Out]#        14.5000       NaN       NaN  0.000000
#[Out]#        15.0000  1.000000  1.000000  1.000000
#[Out]#        16.0000  1.000000       NaN  0.800000
#[Out]#        17.0000  1.000000  1.000000  0.500000
#[Out]#        18.0000  1.000000  0.666667  0.500000
#[Out]#        18.5000       NaN       NaN  0.000000
#[Out]#        19.0000  1.000000  1.000000  0.750000
#[Out]#        20.0000       NaN  1.000000  0.000000
#[Out]#        21.0000  1.000000  1.000000  0.200000
#[Out]#        22.0000  1.000000  0.750000  0.666667
#[Out]#        23.0000  1.000000  1.000000  0.600000
#[Out]#        24.0000  1.000000  0.900000  0.666667
#[Out]# ...                  ...       ...       ...
#[Out]# male   45.5000  0.000000       NaN  0.000000
#[Out]#        46.0000  0.000000  0.000000       NaN
#[Out]#        47.0000  0.000000  0.000000  0.000000
#[Out]#        48.0000  0.750000  0.000000  0.000000
#[Out]#        49.0000  0.600000  0.000000  0.000000
#[Out]#        50.0000  0.200000  0.000000  0.000000
#[Out]#        51.0000  0.500000  0.000000  0.000000
#[Out]#        52.0000  0.500000  0.000000       NaN
#[Out]#        53.0000  1.000000       NaN       NaN
#[Out]#        54.0000  0.333333  0.000000       NaN
#[Out]#        55.0000  0.000000       NaN       NaN
#[Out]#        55.5000       NaN       NaN  0.000000
#[Out]#        56.0000  0.333333       NaN       NaN
#[Out]#        57.0000  0.000000  0.000000       NaN
#[Out]#        58.0000  0.000000       NaN       NaN
#[Out]#        59.0000       NaN  0.000000  0.000000
#[Out]#        60.0000  0.500000  0.000000       NaN
#[Out]#        60.5000       NaN       NaN  0.000000
#[Out]#        61.0000  0.000000  0.000000  0.000000
#[Out]#        62.0000  0.000000  0.500000       NaN
#[Out]#        63.0000       NaN  0.000000       NaN
#[Out]#        64.0000  0.000000       NaN       NaN
#[Out]#        65.0000  0.000000       NaN  0.000000
#[Out]#        66.0000       NaN  0.000000       NaN
#[Out]#        67.0000  0.000000       NaN       NaN
#[Out]#        70.0000  0.000000  0.000000       NaN
#[Out]#        70.5000       NaN       NaN  0.000000
#[Out]#        71.0000  0.000000       NaN       NaN
#[Out]#        74.0000       NaN       NaN  0.000000
#[Out]#        80.0000  1.000000       NaN       NaN
#[Out]# 
#[Out]# [168 rows x 3 columns]
age = pd.cut(data['age'],[0,18,80])
age
#[Out]# 0       (18, 80]
#[Out]# 1        (0, 18]
#[Out]# 2        (0, 18]
#[Out]# 3       (18, 80]
#[Out]# 4       (18, 80]
#[Out]# 5       (18, 80]
#[Out]# 6       (18, 80]
#[Out]# 7       (18, 80]
#[Out]# 8       (18, 80]
#[Out]# 9       (18, 80]
#[Out]# 10      (18, 80]
#[Out]# 11       (0, 18]
#[Out]# 12      (18, 80]
#[Out]# 13      (18, 80]
#[Out]# 14      (18, 80]
#[Out]# 15           NaN
#[Out]# 16      (18, 80]
#[Out]# 17      (18, 80]
#[Out]# 18      (18, 80]
#[Out]# 19      (18, 80]
#[Out]# 20      (18, 80]
#[Out]# 21      (18, 80]
#[Out]# 22      (18, 80]
#[Out]# 23      (18, 80]
#[Out]# 24      (18, 80]
#[Out]# 25      (18, 80]
#[Out]# 26      (18, 80]
#[Out]# 27      (18, 80]
#[Out]# 28      (18, 80]
#[Out]# 29      (18, 80]
#[Out]#           ...   
#[Out]# 1279     (0, 18]
#[Out]# 1280    (18, 80]
#[Out]# 1281    (18, 80]
#[Out]# 1282         NaN
#[Out]# 1283         NaN
#[Out]# 1284         NaN
#[Out]# 1285    (18, 80]
#[Out]# 1286    (18, 80]
#[Out]# 1287    (18, 80]
#[Out]# 1288     (0, 18]
#[Out]# 1289    (18, 80]
#[Out]# 1290    (18, 80]
#[Out]# 1291         NaN
#[Out]# 1292         NaN
#[Out]# 1293         NaN
#[Out]# 1294    (18, 80]
#[Out]# 1295    (18, 80]
#[Out]# 1296    (18, 80]
#[Out]# 1297         NaN
#[Out]# 1298    (18, 80]
#[Out]# 1299    (18, 80]
#[Out]# 1300     (0, 18]
#[Out]# 1301    (18, 80]
#[Out]# 1302         NaN
#[Out]# 1303         NaN
#[Out]# 1304     (0, 18]
#[Out]# 1305         NaN
#[Out]# 1306    (18, 80]
#[Out]# 1307    (18, 80]
#[Out]# 1308    (18, 80]
#[Out]# Name: age, Length: 1309, dtype: category
#[Out]# Categories (2, interval[int64]): [(0, 18] < (18, 80]]
data.pivot_table('survived',['sex','age'],'pclass')
#[Out]# pclass                 1         2         3
#[Out]# sex    age                                  
#[Out]# female 0.0000   1.000000  0.666667  0.531250
#[Out]#        0.1667        NaN       NaN  1.000000
#[Out]#        0.7500        NaN       NaN  1.000000
#[Out]#        0.9167        NaN  1.000000       NaN
#[Out]#        1.0000        NaN  1.000000  0.750000
#[Out]#        2.0000   0.000000  1.000000  0.200000
#[Out]#        3.0000        NaN  1.000000  0.000000
#[Out]#        4.0000        NaN  1.000000  1.000000
#[Out]#        5.0000        NaN  1.000000  1.000000
#[Out]#        6.0000        NaN  1.000000  0.000000
#[Out]#        7.0000        NaN  1.000000       NaN
#[Out]#        8.0000        NaN  1.000000  0.000000
#[Out]#        9.0000        NaN       NaN  0.200000
#[Out]#        10.0000       NaN       NaN  0.000000
#[Out]#        11.0000       NaN       NaN  0.000000
#[Out]#        12.0000       NaN  1.000000       NaN
#[Out]#        13.0000       NaN  1.000000  1.000000
#[Out]#        14.0000  1.000000  1.000000  0.500000
#[Out]#        14.5000       NaN       NaN  0.000000
#[Out]#        15.0000  1.000000  1.000000  1.000000
#[Out]#        16.0000  1.000000       NaN  0.800000
#[Out]#        17.0000  1.000000  1.000000  0.500000
#[Out]#        18.0000  1.000000  0.666667  0.500000
#[Out]#        18.5000       NaN       NaN  0.000000
#[Out]#        19.0000  1.000000  1.000000  0.750000
#[Out]#        20.0000       NaN  1.000000  0.000000
#[Out]#        21.0000  1.000000  1.000000  0.200000
#[Out]#        22.0000  1.000000  0.750000  0.666667
#[Out]#        23.0000  1.000000  1.000000  0.600000
#[Out]#        24.0000  1.000000  0.900000  0.666667
#[Out]# ...                  ...       ...       ...
#[Out]# male   45.5000  0.000000       NaN  0.000000
#[Out]#        46.0000  0.000000  0.000000       NaN
#[Out]#        47.0000  0.000000  0.000000  0.000000
#[Out]#        48.0000  0.750000  0.000000  0.000000
#[Out]#        49.0000  0.600000  0.000000  0.000000
#[Out]#        50.0000  0.200000  0.000000  0.000000
#[Out]#        51.0000  0.500000  0.000000  0.000000
#[Out]#        52.0000  0.500000  0.000000       NaN
#[Out]#        53.0000  1.000000       NaN       NaN
#[Out]#        54.0000  0.333333  0.000000       NaN
#[Out]#        55.0000  0.000000       NaN       NaN
#[Out]#        55.5000       NaN       NaN  0.000000
#[Out]#        56.0000  0.333333       NaN       NaN
#[Out]#        57.0000  0.000000  0.000000       NaN
#[Out]#        58.0000  0.000000       NaN       NaN
#[Out]#        59.0000       NaN  0.000000  0.000000
#[Out]#        60.0000  0.500000  0.000000       NaN
#[Out]#        60.5000       NaN       NaN  0.000000
#[Out]#        61.0000  0.000000  0.000000  0.000000
#[Out]#        62.0000  0.000000  0.500000       NaN
#[Out]#        63.0000       NaN  0.000000       NaN
#[Out]#        64.0000  0.000000       NaN       NaN
#[Out]#        65.0000  0.000000       NaN  0.000000
#[Out]#        66.0000       NaN  0.000000       NaN
#[Out]#        67.0000  0.000000       NaN       NaN
#[Out]#        70.0000  0.000000  0.000000       NaN
#[Out]#        70.5000       NaN       NaN  0.000000
#[Out]#        71.0000  0.000000       NaN       NaN
#[Out]#        74.0000       NaN       NaN  0.000000
#[Out]#        80.0000  1.000000       NaN       NaN
#[Out]# 
#[Out]# [168 rows x 3 columns]
data.pivot_table('survived',['sex',age],'pclass')
#[Out]# pclass                  1         2         3
#[Out]# sex    age                                   
#[Out]# female (0, 18]   0.923077  0.952381  0.534483
#[Out]#        (18, 80]  0.966667  0.878049  0.436170
#[Out]# male   (0, 18]   0.750000  0.523810  0.208333
#[Out]#        (18, 80]  0.328671  0.087591  0.158845
get_ipython().run_line_magic('pinfo', 'data.pivot_table')
data.pivot_table('survived',index=['sex',age],columns='pclass')
#[Out]# pclass                  1         2         3
#[Out]# sex    age                                   
#[Out]# female (0, 18]   0.923077  0.952381  0.534483
#[Out]#        (18, 80]  0.966667  0.878049  0.436170
#[Out]# male   (0, 18]   0.750000  0.523810  0.208333
#[Out]#        (18, 80]  0.328671  0.087591  0.158845
data.pivot_table(values='survived',index=['sex',age],columns='pclass')
#[Out]# pclass                  1         2         3
#[Out]# sex    age                                   
#[Out]# female (0, 18]   0.923077  0.952381  0.534483
#[Out]#        (18, 80]  0.966667  0.878049  0.436170
#[Out]# male   (0, 18]   0.750000  0.523810  0.208333
#[Out]#        (18, 80]  0.328671  0.087591  0.158845
'fare' in data.columns
#[Out]# True
fare = pd.qcut(data['fare'],2)
fare
#[Out]# 0       (14.454, 512.329]
#[Out]# 1       (14.454, 512.329]
#[Out]# 2       (14.454, 512.329]
#[Out]# 3       (14.454, 512.329]
#[Out]# 4       (14.454, 512.329]
#[Out]# 5       (14.454, 512.329]
#[Out]# 6       (14.454, 512.329]
#[Out]# 7        (-0.001, 14.454]
#[Out]# 8       (14.454, 512.329]
#[Out]# 9       (14.454, 512.329]
#[Out]# 10      (14.454, 512.329]
#[Out]# 11      (14.454, 512.329]
#[Out]# 12      (14.454, 512.329]
#[Out]# 13      (14.454, 512.329]
#[Out]# 14      (14.454, 512.329]
#[Out]# 15      (14.454, 512.329]
#[Out]# 16      (14.454, 512.329]
#[Out]# 17      (14.454, 512.329]
#[Out]# 18      (14.454, 512.329]
#[Out]# 19      (14.454, 512.329]
#[Out]# 20      (14.454, 512.329]
#[Out]# 21      (14.454, 512.329]
#[Out]# 22      (14.454, 512.329]
#[Out]# 23      (14.454, 512.329]
#[Out]# 24      (14.454, 512.329]
#[Out]# 25      (14.454, 512.329]
#[Out]# 26      (14.454, 512.329]
#[Out]# 27      (14.454, 512.329]
#[Out]# 28      (14.454, 512.329]
#[Out]# 29      (14.454, 512.329]
#[Out]#               ...        
#[Out]# 1279     (-0.001, 14.454]
#[Out]# 1280     (-0.001, 14.454]
#[Out]# 1281     (-0.001, 14.454]
#[Out]# 1282     (-0.001, 14.454]
#[Out]# 1283     (-0.001, 14.454]
#[Out]# 1284     (-0.001, 14.454]
#[Out]# 1285     (-0.001, 14.454]
#[Out]# 1286     (-0.001, 14.454]
#[Out]# 1287     (-0.001, 14.454]
#[Out]# 1288     (-0.001, 14.454]
#[Out]# 1289     (-0.001, 14.454]
#[Out]# 1290     (-0.001, 14.454]
#[Out]# 1291     (-0.001, 14.454]
#[Out]# 1292     (-0.001, 14.454]
#[Out]# 1293     (-0.001, 14.454]
#[Out]# 1294    (14.454, 512.329]
#[Out]# 1295     (-0.001, 14.454]
#[Out]# 1296     (-0.001, 14.454]
#[Out]# 1297     (-0.001, 14.454]
#[Out]# 1298     (-0.001, 14.454]
#[Out]# 1299     (-0.001, 14.454]
#[Out]# 1300     (-0.001, 14.454]
#[Out]# 1301     (-0.001, 14.454]
#[Out]# 1302     (-0.001, 14.454]
#[Out]# 1303    (14.454, 512.329]
#[Out]# 1304     (-0.001, 14.454]
#[Out]# 1305     (-0.001, 14.454]
#[Out]# 1306     (-0.001, 14.454]
#[Out]# 1307     (-0.001, 14.454]
#[Out]# 1308     (-0.001, 14.454]
#[Out]# Name: fare, Length: 1309, dtype: category
#[Out]# Categories (2, interval[float64]): [(-0.001, 14.454] < (14.454, 512.329]]
fare.last_valid_index
#[Out]# <bound method Series.last_valid_index of 0       (14.454, 512.329]
#[Out]# 1       (14.454, 512.329]
#[Out]# 2       (14.454, 512.329]
#[Out]# 3       (14.454, 512.329]
#[Out]# 4       (14.454, 512.329]
#[Out]# 5       (14.454, 512.329]
#[Out]# 6       (14.454, 512.329]
#[Out]# 7        (-0.001, 14.454]
#[Out]# 8       (14.454, 512.329]
#[Out]# 9       (14.454, 512.329]
#[Out]# 10      (14.454, 512.329]
#[Out]# 11      (14.454, 512.329]
#[Out]# 12      (14.454, 512.329]
#[Out]# 13      (14.454, 512.329]
#[Out]# 14      (14.454, 512.329]
#[Out]# 15      (14.454, 512.329]
#[Out]# 16      (14.454, 512.329]
#[Out]# 17      (14.454, 512.329]
#[Out]# 18      (14.454, 512.329]
#[Out]# 19      (14.454, 512.329]
#[Out]# 20      (14.454, 512.329]
#[Out]# 21      (14.454, 512.329]
#[Out]# 22      (14.454, 512.329]
#[Out]# 23      (14.454, 512.329]
#[Out]# 24      (14.454, 512.329]
#[Out]# 25      (14.454, 512.329]
#[Out]# 26      (14.454, 512.329]
#[Out]# 27      (14.454, 512.329]
#[Out]# 28      (14.454, 512.329]
#[Out]# 29      (14.454, 512.329]
#[Out]#               ...        
#[Out]# 1279     (-0.001, 14.454]
#[Out]# 1280     (-0.001, 14.454]
#[Out]# 1281     (-0.001, 14.454]
#[Out]# 1282     (-0.001, 14.454]
#[Out]# 1283     (-0.001, 14.454]
#[Out]# 1284     (-0.001, 14.454]
#[Out]# 1285     (-0.001, 14.454]
#[Out]# 1286     (-0.001, 14.454]
#[Out]# 1287     (-0.001, 14.454]
#[Out]# 1288     (-0.001, 14.454]
#[Out]# 1289     (-0.001, 14.454]
#[Out]# 1290     (-0.001, 14.454]
#[Out]# 1291     (-0.001, 14.454]
#[Out]# 1292     (-0.001, 14.454]
#[Out]# 1293     (-0.001, 14.454]
#[Out]# 1294    (14.454, 512.329]
#[Out]# 1295     (-0.001, 14.454]
#[Out]# 1296     (-0.001, 14.454]
#[Out]# 1297     (-0.001, 14.454]
#[Out]# 1298     (-0.001, 14.454]
#[Out]# 1299     (-0.001, 14.454]
#[Out]# 1300     (-0.001, 14.454]
#[Out]# 1301     (-0.001, 14.454]
#[Out]# 1302     (-0.001, 14.454]
#[Out]# 1303    (14.454, 512.329]
#[Out]# 1304     (-0.001, 14.454]
#[Out]# 1305     (-0.001, 14.454]
#[Out]# 1306     (-0.001, 14.454]
#[Out]# 1307     (-0.001, 14.454]
#[Out]# 1308     (-0.001, 14.454]
#[Out]# Name: fare, Length: 1309, dtype: category
#[Out]# Categories (2, interval[float64]): [(-0.001, 14.454] < (14.454, 512.329]]>
fare = pd.qcut(data['fare'],2)
fare
#[Out]# 0       (14.454, 512.329]
#[Out]# 1       (14.454, 512.329]
#[Out]# 2       (14.454, 512.329]
#[Out]# 3       (14.454, 512.329]
#[Out]# 4       (14.454, 512.329]
#[Out]# 5       (14.454, 512.329]
#[Out]# 6       (14.454, 512.329]
#[Out]# 7        (-0.001, 14.454]
#[Out]# 8       (14.454, 512.329]
#[Out]# 9       (14.454, 512.329]
#[Out]# 10      (14.454, 512.329]
#[Out]# 11      (14.454, 512.329]
#[Out]# 12      (14.454, 512.329]
#[Out]# 13      (14.454, 512.329]
#[Out]# 14      (14.454, 512.329]
#[Out]# 15      (14.454, 512.329]
#[Out]# 16      (14.454, 512.329]
#[Out]# 17      (14.454, 512.329]
#[Out]# 18      (14.454, 512.329]
#[Out]# 19      (14.454, 512.329]
#[Out]# 20      (14.454, 512.329]
#[Out]# 21      (14.454, 512.329]
#[Out]# 22      (14.454, 512.329]
#[Out]# 23      (14.454, 512.329]
#[Out]# 24      (14.454, 512.329]
#[Out]# 25      (14.454, 512.329]
#[Out]# 26      (14.454, 512.329]
#[Out]# 27      (14.454, 512.329]
#[Out]# 28      (14.454, 512.329]
#[Out]# 29      (14.454, 512.329]
#[Out]#               ...        
#[Out]# 1279     (-0.001, 14.454]
#[Out]# 1280     (-0.001, 14.454]
#[Out]# 1281     (-0.001, 14.454]
#[Out]# 1282     (-0.001, 14.454]
#[Out]# 1283     (-0.001, 14.454]
#[Out]# 1284     (-0.001, 14.454]
#[Out]# 1285     (-0.001, 14.454]
#[Out]# 1286     (-0.001, 14.454]
#[Out]# 1287     (-0.001, 14.454]
#[Out]# 1288     (-0.001, 14.454]
#[Out]# 1289     (-0.001, 14.454]
#[Out]# 1290     (-0.001, 14.454]
#[Out]# 1291     (-0.001, 14.454]
#[Out]# 1292     (-0.001, 14.454]
#[Out]# 1293     (-0.001, 14.454]
#[Out]# 1294    (14.454, 512.329]
#[Out]# 1295     (-0.001, 14.454]
#[Out]# 1296     (-0.001, 14.454]
#[Out]# 1297     (-0.001, 14.454]
#[Out]# 1298     (-0.001, 14.454]
#[Out]# 1299     (-0.001, 14.454]
#[Out]# 1300     (-0.001, 14.454]
#[Out]# 1301     (-0.001, 14.454]
#[Out]# 1302     (-0.001, 14.454]
#[Out]# 1303    (14.454, 512.329]
#[Out]# 1304     (-0.001, 14.454]
#[Out]# 1305     (-0.001, 14.454]
#[Out]# 1306     (-0.001, 14.454]
#[Out]# 1307     (-0.001, 14.454]
#[Out]# 1308     (-0.001, 14.454]
#[Out]# Name: fare, Length: 1309, dtype: category
#[Out]# Categories (2, interval[float64]): [(-0.001, 14.454] < (14.454, 512.329]]
data.pivot_table('survived',['sex',age],[fare,'class'])
data.pivot_table('survived',['sex',age],[fare,'pclass'])
#[Out]# fare            (-0.001, 14.454]                     (14.454, 512.329]  \
#[Out]# pclass                         1         2         3                 1   
#[Out]# sex    age                                                               
#[Out]# female (0, 18]               NaN  0.750000  0.666667          0.923077   
#[Out]#        (18, 80]              NaN  0.866667  0.437500          0.966667   
#[Out]# male   (0, 18]               NaN  0.000000  0.264706          0.750000   
#[Out]#        (18, 80]              0.2  0.119048  0.153527          0.333333   
#[Out]# 
#[Out]# fare                                 
#[Out]# pclass                  2         3  
#[Out]# sex    age                           
#[Out]# female (0, 18]   1.000000  0.392857  
#[Out]#        (18, 80]  0.884615  0.433333  
#[Out]# male   (0, 18]   0.687500  0.157895  
#[Out]#        (18, 80]  0.037736  0.194444  
data.pivot_table(values='survived',index=['sex',age],columns=[fare,'pclass'])
#[Out]# fare            (-0.001, 14.454]                     (14.454, 512.329]  \
#[Out]# pclass                         1         2         3                 1   
#[Out]# sex    age                                                               
#[Out]# female (0, 18]               NaN  0.750000  0.666667          0.923077   
#[Out]#        (18, 80]              NaN  0.866667  0.437500          0.966667   
#[Out]# male   (0, 18]               NaN  0.000000  0.264706          0.750000   
#[Out]#        (18, 80]              0.2  0.119048  0.153527          0.333333   
#[Out]# 
#[Out]# fare                                 
#[Out]# pclass                  2         3  
#[Out]# sex    age                           
#[Out]# female (0, 18]   1.000000  0.392857  
#[Out]#        (18, 80]  0.884615  0.433333  
#[Out]# male   (0, 18]   0.687500  0.157895  
#[Out]#        (18, 80]  0.037736  0.194444  
data.pivot_table(index='sex',columns='class',aggfunc={'survived':sum,'fare':'mean'})
data.pivot_table(index='sex',columns='pclass',aggfunc={'survived':sum,'fare':'mean'})
#[Out]#               fare                       survived         
#[Out]# pclass           1          2          3        1   2    3
#[Out]# sex                                                       
#[Out]# female  109.412385  23.234827  15.324250      139  94  106
#[Out]# male     69.888385  19.904946  12.406294       61  25   75
data['fare'][:5]
#[Out]# 0    211.3375
#[Out]# 1    151.5500
#[Out]# 2    151.5500
#[Out]# 3    151.5500
#[Out]# 4    151.5500
#[Out]# Name: fare, dtype: float64
data['fare'][:10]
#[Out]# 0    211.3375
#[Out]# 1    151.5500
#[Out]# 2    151.5500
#[Out]# 3    151.5500
#[Out]# 4    151.5500
#[Out]# 5     26.5500
#[Out]# 6     77.9583
#[Out]# 7      0.0000
#[Out]# 8     51.4792
#[Out]# 9     49.5042
#[Out]# Name: fare, dtype: float64
data.pivot_table('survived',index='sex',columns='pclass',margins_name='all')
#[Out]# pclass         1         2         3
#[Out]# sex                                 
#[Out]# female  0.965278  0.886792  0.490741
#[Out]# male    0.340782  0.146199  0.152130
data.pivot_table('survived',index='sex',columns='pclass',margins)
data.pivot_table('survived',index='sex',columns='pclass',margins)
data.pivot_table('survived',index='sex',columns='pclass',margins='all')
#[Out]# pclass         1         2         3       All
#[Out]# sex                                           
#[Out]# female  0.965278  0.886792  0.490741  0.727468
#[Out]# male    0.340782  0.146199  0.152130  0.190985
#[Out]# All     0.619195  0.429603  0.255289  0.381971
get_ipython().run_line_magic('ls', '')
births = pd.read_csv('births.csv')
births.head()
#[Out]#    year  month  day gender  births
#[Out]# 0  1969      1  1.0      F    4046
#[Out]# 1  1969      1  1.0      M    4440
#[Out]# 2  1969      1  2.0      F    4454
#[Out]# 3  1969      1  2.0      M    4548
#[Out]# 4  1969      1  3.0      F    4548
births.head()
#[Out]#    year  month  day gender  births
#[Out]# 0  1969      1  1.0      F    4046
#[Out]# 1  1969      1  1.0      M    4440
#[Out]# 2  1969      1  2.0      F    4454
#[Out]# 3  1969      1  2.0      M    4548
#[Out]# 4  1969      1  3.0      F    4548
births.shape
#[Out]# (15547, 5)
births['decade'] = 10 * (births['year'] //10)
births.head()
#[Out]#    year  month  day gender  births  decade
#[Out]# 0  1969      1  1.0      F    4046    1960
#[Out]# 1  1969      1  1.0      M    4440    1960
#[Out]# 2  1969      1  2.0      F    4454    1960
#[Out]# 3  1969      1  2.0      M    4548    1960
#[Out]# 4  1969      1  3.0      F    4548    1960
births.pivot_table('birth',index='decade',columns='gender',aggfunc='sum')
births.pivot_table('births',index='decade',columns='gender',aggfunc='sum')
births.pivot_table('births',index='decade',columns='gender',aggfunc='sum')
#[Out]# gender         F         M
#[Out]# decade                    
#[Out]# 1960     1753634   1846572
#[Out]# 1970    16263075  17121550
#[Out]# 1980    18310351  19243452
#[Out]# 1990    19479454  20420553
#[Out]# 2000    18229309  19106428
births.pivot_table(births,index='decade',columns='gender',aggfunc='sum')
#[Out]#           births                day           month            year         
#[Out]# gender         F         M        F        M      F      M        F        M
#[Out]# decade                                                                      
#[Out]# 1960     1753634   1846572   7140.0   7140.0   2496   2496   756096   756096
#[Out]# 1970    16263075  17121550  69896.0  69710.0  24828  24832  7524768  7516855
#[Out]# 1980    18310351  19243452  56976.0  56877.0  21842  21845  6652359  6650377
#[Out]# 1990    19479454  20420553      0.0      0.0    780    780   239340   239340
#[Out]# 2000    18229309  19106428      0.0      0.0    702    702   216432   216432
births.columns
#[Out]# Index(['year', 'month', 'day', 'gender', 'births', 'decade'], dtype='object')
births['births']
#[Out]# 0          4046
#[Out]# 1          4440
#[Out]# 2          4454
#[Out]# 3          4548
#[Out]# 4          4548
#[Out]# 5          4994
#[Out]# 6          4440
#[Out]# 7          4520
#[Out]# 8          4192
#[Out]# 9          4198
#[Out]# 10         4710
#[Out]# 11         4850
#[Out]# 12         4646
#[Out]# 13         5092
#[Out]# 14         4800
#[Out]# 15         4934
#[Out]# 16         4592
#[Out]# 17         4842
#[Out]# 18         4852
#[Out]# 19         5190
#[Out]# 20         4580
#[Out]# 21         4598
#[Out]# 22         4126
#[Out]# 23         4324
#[Out]# 24         4758
#[Out]# 25         5076
#[Out]# 26         5070
#[Out]# 27         5296
#[Out]# 28         4798
#[Out]# 29         5096
#[Out]#           ...  
#[Out]# 15517    180912
#[Out]# 15518    189157
#[Out]# 15519    173513
#[Out]# 15520    180814
#[Out]# 15521    173787
#[Out]# 15522    181426
#[Out]# 15523    174255
#[Out]# 15524    182789
#[Out]# 15525    165669
#[Out]# 15526    173434
#[Out]# 15527    172053
#[Out]# 15528    179129
#[Out]# 15529    169585
#[Out]# 15530    177399
#[Out]# 15531    173141
#[Out]# 15532    182294
#[Out]# 15533    169958
#[Out]# 15534    179267
#[Out]# 15535    183391
#[Out]# 15536    192714
#[Out]# 15537    182713
#[Out]# 15538    191315
#[Out]# 15539    179696
#[Out]# 15540    188964
#[Out]# 15541    175314
#[Out]# 15542    183219
#[Out]# 15543    158939
#[Out]# 15544    165468
#[Out]# 15545    173215
#[Out]# 15546    181235
#[Out]# Name: births, Length: 15547, dtype: int64
births.pivot_table('births',index='decade',columns='gender',aggfunc='sum')
#[Out]# gender         F         M
#[Out]# decade                    
#[Out]# 1960     1753634   1846572
#[Out]# 1970    16263075  17121550
#[Out]# 1980    18310351  19243452
#[Out]# 1990    19479454  20420553
#[Out]# 2000    18229309  19106428
import matplotlib.pyplot as plt
sns.set()
births.pivot_table('births',index='year',columns='gender',aggfunc='sum')
#[Out]# gender        F        M
#[Out]# year                    
#[Out]# 1969    1753634  1846572
#[Out]# 1970    1819164  1918636
#[Out]# 1971    1736774  1826774
#[Out]# 1972    1592347  1673888
#[Out]# 1973    1533102  1613023
#[Out]# 1974    1543005  1627626
#[Out]# 1975    1535546  1618010
#[Out]# 1976    1547613  1628863
#[Out]# 1977    1623363  1708796
#[Out]# 1978    1626324  1711976
#[Out]# 1979    1705837  1793958
#[Out]# 1980    1762459  1855522
#[Out]# 1981    1772037  1863478
#[Out]# 1982    1797239  1888218
#[Out]# 1983    1775299  1867522
#[Out]# 1984    1791802  1881766
#[Out]# 1985    1834774  1930290
#[Out]# 1986    1833708  1926987
#[Out]# 1987    1860111  1953105
#[Out]# 1988    1909210  2004583
#[Out]# 1989    1973712  2071981
#[Out]# 1990    2030966  2131951
#[Out]# 1991    2011601  2103741
#[Out]# 1992    1985118  2084310
#[Out]# 1993    1953456  2051067
#[Out]# 1994    1932234  2024691
#[Out]# 1995    1904871  1998141
#[Out]# 1996    1902664  1992210
#[Out]# 1997    1896928  1987401
#[Out]# 1998    1927106  2018086
#[Out]# 1999    1934510  2028955
#[Out]# 2000    1984255  2079568
#[Out]# 2001    1970770  2060761
#[Out]# 2002    1966519  2060857
#[Out]# 2003    1999387  2096705
#[Out]# 2004    2010710  2108197
#[Out]# 2005    2022892  2122727
#[Out]# 2006    2084957  2188268
#[Out]# 2007    2111890  2212118
#[Out]# 2008    2077929  2177227
plt.ylabel('total births per year')
#[Out]# Text(0,0.5,'total births per year')
plt.show()
get_ipython().run_line_magic('hist', '')
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('pylab', '')
import matplotlib.pyplot as plt
sns.set()
births.pivot_table('births',index='year',columns='gender',aggfunc='sum')
#[Out]# gender        F        M
#[Out]# year                    
#[Out]# 1969    1753634  1846572
#[Out]# 1970    1819164  1918636
#[Out]# 1971    1736774  1826774
#[Out]# 1972    1592347  1673888
#[Out]# 1973    1533102  1613023
#[Out]# 1974    1543005  1627626
#[Out]# 1975    1535546  1618010
#[Out]# 1976    1547613  1628863
#[Out]# 1977    1623363  1708796
#[Out]# 1978    1626324  1711976
#[Out]# 1979    1705837  1793958
#[Out]# 1980    1762459  1855522
#[Out]# 1981    1772037  1863478
#[Out]# 1982    1797239  1888218
#[Out]# 1983    1775299  1867522
#[Out]# 1984    1791802  1881766
#[Out]# 1985    1834774  1930290
#[Out]# 1986    1833708  1926987
#[Out]# 1987    1860111  1953105
#[Out]# 1988    1909210  2004583
#[Out]# 1989    1973712  2071981
#[Out]# 1990    2030966  2131951
#[Out]# 1991    2011601  2103741
#[Out]# 1992    1985118  2084310
#[Out]# 1993    1953456  2051067
#[Out]# 1994    1932234  2024691
#[Out]# 1995    1904871  1998141
#[Out]# 1996    1902664  1992210
#[Out]# 1997    1896928  1987401
#[Out]# 1998    1927106  2018086
#[Out]# 1999    1934510  2028955
#[Out]# 2000    1984255  2079568
#[Out]# 2001    1970770  2060761
#[Out]# 2002    1966519  2060857
#[Out]# 2003    1999387  2096705
#[Out]# 2004    2010710  2108197
#[Out]# 2005    2022892  2122727
#[Out]# 2006    2084957  2188268
#[Out]# 2007    2111890  2212118
#[Out]# 2008    2077929  2177227
births.pivot_table('births',index='year',columns='gender',aggfunc='sum').head()
#[Out]# gender        F        M
#[Out]# year                    
#[Out]# 1969    1753634  1846572
#[Out]# 1970    1819164  1918636
#[Out]# 1971    1736774  1826774
#[Out]# 1972    1592347  1673888
#[Out]# 1973    1533102  1613023
dataplt = births.pivot_table('births',index='year',columns='gender',aggfunc='sum').head()
plt.plot(dataplt)
#[Out]# [<matplotlib.lines.Line2D at 0x1ffe7c56860>,
#[Out]#  <matplotlib.lines.Line2D at 0x1ffe7c569e8>]
plt.legend()
#[Out]# <matplotlib.legend.Legend at 0x1ffe5e96b70>
plt.plot(births['year'],dataplt)
plt.plot(births['year'],births['gender'])
#[Out]# [<matplotlib.lines.Line2D at 0x1ffe7c5e080>]
plt.plot(dataplt)
#[Out]# [<matplotlib.lines.Line2D at 0x1ffe678dfd0>,
#[Out]#  <matplotlib.lines.Line2D at 0x1ffe3021da0>]
plt.show()
plt.plot(dataplt)
#[Out]# [<matplotlib.lines.Line2D at 0x1ffe83d6dd8>,
#[Out]#  <matplotlib.lines.Line2D at 0x1ffe83d6f60>]
dataplt.columns
#[Out]# Index(['F', 'M'], dtype='object', name='gender')
dataplt.index
#[Out]# Int64Index([1969, 1970, 1971, 1972, 1973], dtype='int64', name='year')
births.pivot_table('births',index='year',columns='gender',aggfunc='sum').head()
#[Out]# gender        F        M
#[Out]# year                    
#[Out]# 1969    1753634  1846572
#[Out]# 1970    1819164  1918636
#[Out]# 1971    1736774  1826774
#[Out]# 1972    1592347  1673888
#[Out]# 1973    1533102  1613023
births.pivot_table('births',index='year',columns='gender',aggfunc='sum')
#[Out]# gender        F        M
#[Out]# year                    
#[Out]# 1969    1753634  1846572
#[Out]# 1970    1819164  1918636
#[Out]# 1971    1736774  1826774
#[Out]# 1972    1592347  1673888
#[Out]# 1973    1533102  1613023
#[Out]# 1974    1543005  1627626
#[Out]# 1975    1535546  1618010
#[Out]# 1976    1547613  1628863
#[Out]# 1977    1623363  1708796
#[Out]# 1978    1626324  1711976
#[Out]# 1979    1705837  1793958
#[Out]# 1980    1762459  1855522
#[Out]# 1981    1772037  1863478
#[Out]# 1982    1797239  1888218
#[Out]# 1983    1775299  1867522
#[Out]# 1984    1791802  1881766
#[Out]# 1985    1834774  1930290
#[Out]# 1986    1833708  1926987
#[Out]# 1987    1860111  1953105
#[Out]# 1988    1909210  2004583
#[Out]# 1989    1973712  2071981
#[Out]# 1990    2030966  2131951
#[Out]# 1991    2011601  2103741
#[Out]# 1992    1985118  2084310
#[Out]# 1993    1953456  2051067
#[Out]# 1994    1932234  2024691
#[Out]# 1995    1904871  1998141
#[Out]# 1996    1902664  1992210
#[Out]# 1997    1896928  1987401
#[Out]# 1998    1927106  2018086
#[Out]# 1999    1934510  2028955
#[Out]# 2000    1984255  2079568
#[Out]# 2001    1970770  2060761
#[Out]# 2002    1966519  2060857
#[Out]# 2003    1999387  2096705
#[Out]# 2004    2010710  2108197
#[Out]# 2005    2022892  2122727
#[Out]# 2006    2084957  2188268
#[Out]# 2007    2111890  2212118
#[Out]# 2008    2077929  2177227
dataplt = births.pivot_table('births',index='year',columns='gender',aggfunc='sum')
plt.plot(dataplt)
#[Out]# [<matplotlib.lines.Line2D at 0x1ffe8344128>,
#[Out]#  <matplotlib.lines.Line2D at 0x1ffe8344208>]
plt.show()
plt.legend()
#[Out]# <matplotlib.legend.Legend at 0x1ffe82406d8>
plt.xlabel('total births per year')
#[Out]# Text(0.5,27.5,'total births per year')
plt.show()
plt.ylabel('total births per year')
#[Out]# Text(32.625,0.5,'total births per year')
plt.show(['F','M'])
plt.legend(['F','M'])
#[Out]# <matplotlib.legend.Legend at 0x1ffee605710>
dataplt = births.pivot_table('births',index='year',columns='gender',aggfunc='sum')
plt.legend(['F','M'])
#[Out]# <matplotlib.legend.Legend at 0x1ffee6175f8>
plt.show(['F','M'])
plt.show(['F','M'])
plt.show()
plt.show()
dataplt = births.pivot_table('births',index='year',columns='gender',aggfunc='sum')
plt.show()
plt.plot(dataplt)
#[Out]# [<matplotlib.lines.Line2D at 0x1ffee5c3048>,
#[Out]#  <matplotlib.lines.Line2D at 0x1ffee5c31d0>]
plt.legend(['F','M'])
#[Out]# <matplotlib.legend.Legend at 0x1ffee61d2b0>
plt.xlabel('total births per year')
#[Out]# Text(0.5,15.625,'total births per year')
quartiles = np.percentile(births['births'],[20,50,75])
nu = quartiles[1]
sig = 0.74 * (quartiles[2]-quartiles[0])
quartiles
#[Out]# array([4262. , 4814. , 5289.5])
births['births']
#[Out]# 0          4046
#[Out]# 1          4440
#[Out]# 2          4454
#[Out]# 3          4548
#[Out]# 4          4548
#[Out]# 5          4994
#[Out]# 6          4440
#[Out]# 7          4520
#[Out]# 8          4192
#[Out]# 9          4198
#[Out]# 10         4710
#[Out]# 11         4850
#[Out]# 12         4646
#[Out]# 13         5092
#[Out]# 14         4800
#[Out]# 15         4934
#[Out]# 16         4592
#[Out]# 17         4842
#[Out]# 18         4852
#[Out]# 19         5190
#[Out]# 20         4580
#[Out]# 21         4598
#[Out]# 22         4126
#[Out]# 23         4324
#[Out]# 24         4758
#[Out]# 25         5076
#[Out]# 26         5070
#[Out]# 27         5296
#[Out]# 28         4798
#[Out]# 29         5096
#[Out]#           ...  
#[Out]# 15517    180912
#[Out]# 15518    189157
#[Out]# 15519    173513
#[Out]# 15520    180814
#[Out]# 15521    173787
#[Out]# 15522    181426
#[Out]# 15523    174255
#[Out]# 15524    182789
#[Out]# 15525    165669
#[Out]# 15526    173434
#[Out]# 15527    172053
#[Out]# 15528    179129
#[Out]# 15529    169585
#[Out]# 15530    177399
#[Out]# 15531    173141
#[Out]# 15532    182294
#[Out]# 15533    169958
#[Out]# 15534    179267
#[Out]# 15535    183391
#[Out]# 15536    192714
#[Out]# 15537    182713
#[Out]# 15538    191315
#[Out]# 15539    179696
#[Out]# 15540    188964
#[Out]# 15541    175314
#[Out]# 15542    183219
#[Out]# 15543    158939
#[Out]# 15544    165468
#[Out]# 15545    173215
#[Out]# 15546    181235
#[Out]# Name: births, Length: 15547, dtype: int64
quartiles
#[Out]# array([4262. , 4814. , 5289.5])
births['births'].head()
#[Out]# 0    4046
#[Out]# 1    4440
#[Out]# 2    4454
#[Out]# 3    4548
#[Out]# 4    4548
#[Out]# Name: births, dtype: int64
births['births'].tail()
#[Out]# 15542    183219
#[Out]# 15543    158939
#[Out]# 15544    165468
#[Out]# 15545    173215
#[Out]# 15546    181235
#[Out]# Name: births, dtype: int64
quartiles
#[Out]# array([4262. , 4814. , 5289.5])
quartiles.sum()
#[Out]# 14365.5
births.shape
#[Out]# (15547, 6)
(births.isnull()).counts()
(births.isnull()).counts
(births.isnull()).sum
#[Out]# <bound method DataFrame.sum of         year  month    day  gender  births  decade
#[Out]# 0      False  False  False   False   False   False
#[Out]# 1      False  False  False   False   False   False
#[Out]# 2      False  False  False   False   False   False
#[Out]# 3      False  False  False   False   False   False
#[Out]# 4      False  False  False   False   False   False
#[Out]# 5      False  False  False   False   False   False
#[Out]# 6      False  False  False   False   False   False
#[Out]# 7      False  False  False   False   False   False
#[Out]# 8      False  False  False   False   False   False
#[Out]# 9      False  False  False   False   False   False
#[Out]# 10     False  False  False   False   False   False
#[Out]# 11     False  False  False   False   False   False
#[Out]# 12     False  False  False   False   False   False
#[Out]# 13     False  False  False   False   False   False
#[Out]# 14     False  False  False   False   False   False
#[Out]# 15     False  False  False   False   False   False
#[Out]# 16     False  False  False   False   False   False
#[Out]# 17     False  False  False   False   False   False
#[Out]# 18     False  False  False   False   False   False
#[Out]# 19     False  False  False   False   False   False
#[Out]# 20     False  False  False   False   False   False
#[Out]# 21     False  False  False   False   False   False
#[Out]# 22     False  False  False   False   False   False
#[Out]# 23     False  False  False   False   False   False
#[Out]# 24     False  False  False   False   False   False
#[Out]# 25     False  False  False   False   False   False
#[Out]# 26     False  False  False   False   False   False
#[Out]# 27     False  False  False   False   False   False
#[Out]# 28     False  False  False   False   False   False
#[Out]# 29     False  False  False   False   False   False
#[Out]# ...      ...    ...    ...     ...     ...     ...
#[Out]# 15517  False  False   True   False   False   False
#[Out]# 15518  False  False   True   False   False   False
#[Out]# 15519  False  False   True   False   False   False
#[Out]# 15520  False  False   True   False   False   False
#[Out]# 15521  False  False   True   False   False   False
#[Out]# 15522  False  False   True   False   False   False
#[Out]# 15523  False  False   True   False   False   False
#[Out]# 15524  False  False   True   False   False   False
#[Out]# 15525  False  False   True   False   False   False
#[Out]# 15526  False  False   True   False   False   False
#[Out]# 15527  False  False   True   False   False   False
#[Out]# 15528  False  False   True   False   False   False
#[Out]# 15529  False  False   True   False   False   False
#[Out]# 15530  False  False   True   False   False   False
#[Out]# 15531  False  False   True   False   False   False
#[Out]# 15532  False  False   True   False   False   False
#[Out]# 15533  False  False   True   False   False   False
#[Out]# 15534  False  False   True   False   False   False
#[Out]# 15535  False  False   True   False   False   False
#[Out]# 15536  False  False   True   False   False   False
#[Out]# 15537  False  False   True   False   False   False
#[Out]# 15538  False  False   True   False   False   False
#[Out]# 15539  False  False   True   False   False   False
#[Out]# 15540  False  False   True   False   False   False
#[Out]# 15541  False  False   True   False   False   False
#[Out]# 15542  False  False   True   False   False   False
#[Out]# 15543  False  False   True   False   False   False
#[Out]# 15544  False  False   True   False   False   False
#[Out]# 15545  False  False   True   False   False   False
#[Out]# 15546  False  False   True   False   False   False
#[Out]# 
#[Out]# [15547 rows x 6 columns]>
(births['births'].isnull()).sum
#[Out]# <bound method Series.sum of 0        False
#[Out]# 1        False
#[Out]# 2        False
#[Out]# 3        False
#[Out]# 4        False
#[Out]# 5        False
#[Out]# 6        False
#[Out]# 7        False
#[Out]# 8        False
#[Out]# 9        False
#[Out]# 10       False
#[Out]# 11       False
#[Out]# 12       False
#[Out]# 13       False
#[Out]# 14       False
#[Out]# 15       False
#[Out]# 16       False
#[Out]# 17       False
#[Out]# 18       False
#[Out]# 19       False
#[Out]# 20       False
#[Out]# 21       False
#[Out]# 22       False
#[Out]# 23       False
#[Out]# 24       False
#[Out]# 25       False
#[Out]# 26       False
#[Out]# 27       False
#[Out]# 28       False
#[Out]# 29       False
#[Out]#          ...  
#[Out]# 15517    False
#[Out]# 15518    False
#[Out]# 15519    False
#[Out]# 15520    False
#[Out]# 15521    False
#[Out]# 15522    False
#[Out]# 15523    False
#[Out]# 15524    False
#[Out]# 15525    False
#[Out]# 15526    False
#[Out]# 15527    False
#[Out]# 15528    False
#[Out]# 15529    False
#[Out]# 15530    False
#[Out]# 15531    False
#[Out]# 15532    False
#[Out]# 15533    False
#[Out]# 15534    False
#[Out]# 15535    False
#[Out]# 15536    False
#[Out]# 15537    False
#[Out]# 15538    False
#[Out]# 15539    False
#[Out]# 15540    False
#[Out]# 15541    False
#[Out]# 15542    False
#[Out]# 15543    False
#[Out]# 15544    False
#[Out]# 15545    False
#[Out]# 15546    False
#[Out]# Name: births, Length: 15547, dtype: bool>
(births['births'].isnull()).sum()
#[Out]# 0
mu 
mu = quartiles[1]
mu
#[Out]# 4814.0
sig = 0.74 * (quartiles[2] - quartiles[0])
sig
#[Out]# 760.35
sig = 0.74 * (quartiles[2] - quartiles[0]) # 0.74标准正太分布的分位数间距
sig
#[Out]# 760.35
births = births.query('(births > @muu -5 *@sig) & (births < @mu +5 *@sig)')
births = births.query('(births > @mu -5 *@sig) & (births < @mu +5 *@sig)')
births
#[Out]#        year  month   day gender  births  decade
#[Out]# 0      1969      1   1.0      F    4046    1960
#[Out]# 1      1969      1   1.0      M    4440    1960
#[Out]# 2      1969      1   2.0      F    4454    1960
#[Out]# 3      1969      1   2.0      M    4548    1960
#[Out]# 4      1969      1   3.0      F    4548    1960
#[Out]# 5      1969      1   3.0      M    4994    1960
#[Out]# 6      1969      1   4.0      F    4440    1960
#[Out]# 7      1969      1   4.0      M    4520    1960
#[Out]# 8      1969      1   5.0      F    4192    1960
#[Out]# 9      1969      1   5.0      M    4198    1960
#[Out]# 10     1969      1   6.0      F    4710    1960
#[Out]# 11     1969      1   6.0      M    4850    1960
#[Out]# 12     1969      1   7.0      F    4646    1960
#[Out]# 13     1969      1   7.0      M    5092    1960
#[Out]# 14     1969      1   8.0      F    4800    1960
#[Out]# 15     1969      1   8.0      M    4934    1960
#[Out]# 16     1969      1   9.0      F    4592    1960
#[Out]# 17     1969      1   9.0      M    4842    1960
#[Out]# 18     1969      1  10.0      F    4852    1960
#[Out]# 19     1969      1  10.0      M    5190    1960
#[Out]# 20     1969      1  11.0      F    4580    1960
#[Out]# 21     1969      1  11.0      M    4598    1960
#[Out]# 22     1969      1  12.0      F    4126    1960
#[Out]# 23     1969      1  12.0      M    4324    1960
#[Out]# 24     1969      1  13.0      F    4758    1960
#[Out]# 25     1969      1  13.0      M    5076    1960
#[Out]# 26     1969      1  14.0      F    5070    1960
#[Out]# 27     1969      1  14.0      M    5296    1960
#[Out]# 28     1969      1  15.0      F    4798    1960
#[Out]# 29     1969      1  15.0      M    5096    1960
#[Out]# ...     ...    ...   ...    ...     ...     ...
#[Out]# 15037  1988     12  17.0      F    4270    1980
#[Out]# 15038  1988     12  17.0      M    4486    1980
#[Out]# 15039  1988     12  18.0      F    4211    1980
#[Out]# 15040  1988     12  18.0      M    4220    1980
#[Out]# 15041  1988     12  19.0      F    5651    1980
#[Out]# 15042  1988     12  19.0      M    6065    1980
#[Out]# 15043  1988     12  20.0      F    6092    1980
#[Out]# 15044  1988     12  20.0      M    6343    1980
#[Out]# 15045  1988     12  21.0      F    5462    1980
#[Out]# 15046  1988     12  21.0      M    5861    1980
#[Out]# 15047  1988     12  22.0      F    5219    1980
#[Out]# 15048  1988     12  22.0      M    5510    1980
#[Out]# 15049  1988     12  23.0      F    4887    1980
#[Out]# 15050  1988     12  23.0      M    5110    1980
#[Out]# 15051  1988     12  24.0      F    4024    1980
#[Out]# 15052  1988     12  24.0      M    4269    1980
#[Out]# 15053  1988     12  25.0      F    3874    1980
#[Out]# 15054  1988     12  25.0      M    3961    1980
#[Out]# 15055  1988     12  26.0      F    4274    1980
#[Out]# 15056  1988     12  26.0      M    4409    1980
#[Out]# 15057  1988     12  27.0      F    5633    1980
#[Out]# 15058  1988     12  27.0      M    5895    1980
#[Out]# 15059  1988     12  28.0      F    5858    1980
#[Out]# 15060  1988     12  28.0      M    5989    1980
#[Out]# 15061  1988     12  29.0      F    5760    1980
#[Out]# 15062  1988     12  29.0      M    5944    1980
#[Out]# 15063  1988     12  30.0      F    5742    1980
#[Out]# 15064  1988     12  30.0      M    6095    1980
#[Out]# 15065  1988     12  31.0      F    4435    1980
#[Out]# 15066  1988     12  31.0      M    4698    1980
#[Out]# 
#[Out]# [14610 rows x 6 columns]
births['day'] = births['day'].astyep(int)
births['day'] = births['day'].astype(int)
births.columns
#[Out]# Index(['year', 'month', 'day', 'gender', 'births', 'decade'], dtype='object')
births.index = pd.to_datetime(10000*birth.year+100*births.month+births.day,format='%Y%m%d')
births.index = pd.to_datetime(10000*births.year+100*births.month+births.day,format='%Y%m%d')
births['dayofweek'] = births.index.dayofweek
births.columns
#[Out]# Index(['year', 'month', 'day', 'gender', 'births', 'decade', 'dayofweek'], dtype='object')
births['dayofweek'].head()
#[Out]# 1969-01-01    2
#[Out]# 1969-01-01    2
#[Out]# 1969-01-02    3
#[Out]# 1969-01-02    3
#[Out]# 1969-01-03    4
#[Out]# Name: dayofweek, dtype: int64
get_ipython().run_line_magic('pinfo', 'briths.index.dayofweek')
births.index
#[Out]# DatetimeIndex(['1969-01-01', '1969-01-01', '1969-01-02', '1969-01-02',
#[Out]#                '1969-01-03', '1969-01-03', '1969-01-04', '1969-01-04',
#[Out]#                '1969-01-05', '1969-01-05',
#[Out]#                ...
#[Out]#                '1988-12-27', '1988-12-27', '1988-12-28', '1988-12-28',
#[Out]#                '1988-12-29', '1988-12-29', '1988-12-30', '1988-12-30',
#[Out]#                '1988-12-31', '1988-12-31'],
#[Out]#               dtype='datetime64[ns]', length=14610, freq=None)
import matplotlib as mpl
births.pivot_table('births',index='dayofweek',columns='decade',aggfunc='mean').plot()
#[Out]# <matplotlib.axes._subplots.AxesSubplot at 0x1ffeed13da0>
plt.gca().set_xticklabels(['Mon','Tues','Wed','Tue','Fri','Sat','Sun'])
#[Out]# [Text(0,0,'Mon'),
#[Out]#  Text(0,0,'Tues'),
#[Out]#  Text(1,0,'Wed'),
#[Out]#  Text(2,0,'Tue'),
#[Out]#  Text(3,0,'Fri'),
#[Out]#  Text(4,0,'Sat'),
#[Out]#  Text(5,0,'Sun')]
plt.ylabel('mean births by day')
#[Out]# Text(20.75,0.5,'mean births by day')
births_by_date = births.pivot_table('births',[births.index.month,births.index.day])
births_by_date.head()
#[Out]#        births
#[Out]# 1 1  4009.225
#[Out]#   2  4247.400
#[Out]#   3  4500.900
#[Out]#   4  4571.350
#[Out]#   5  4603.625
births_by_date.index = [pd.datetime(2012,month,day) for (month,day) in births_by_date.index]
births_by_date.head()
#[Out]#               births
#[Out]# 2012-01-01  4009.225
#[Out]# 2012-01-02  4247.400
#[Out]# 2012-01-03  4500.900
#[Out]# 2012-01-04  4571.350
#[Out]# 2012-01-05  4603.625
fig,ax = plt.subplot(figzise=(12,4))
births_by_data.plot(ax=ax)
births_by_date.plot(ax=ax)
get_ipython().run_line_magic('pinfo', 'ax')
births_by_date.plot(ax)
fig,ax = plt.subplot(figzise=(12,4))
fig,ax = plt.subplots(figzise=(12,4))
fig,ax = plt.subplots(figzise=(12,4))
get_ipython().run_line_magic('pinfo', 'plt.subplot')
get_ipython().run_line_magic('pinfo', 'plt.subplots')
fig,ax = plt.subplots()#subplots!!!!
births_by_date.plot(ax=ax)
#[Out]# <matplotlib.axes._subplots.AxesSubplot at 0x1ffeefd9fd0>
get_ipython().run_line_magic('logstop', '')
