# IPython log file

get_ipython().run_line_magic('cd', 'c')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', '..')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', 'PythonDataScienceHandbook-master/')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', 'notebooks/')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', 'data/')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', 'c')
get_ipython().system('curl -o FremontBridge.csv')
curl --help
get_ipython().system('curl --help')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('pwd', '')
#[Out]# 'c:\\python\\python_数据科学手册\\myself_x'
try:
    recipes = pd.read_json('recipeitems-latest.json')
excep:
try:
    recipes = pd.read_json('recipeitems-latest.json')
except:
    print('ValueError:
try:
    recipes = pd.read_json('recipeitems-latest.json')
except:
    print('ValueError:',e)
    
try:
    recipes = pd.read_json('recipeitems-latest.json')
except ValueError as e
    print('ValueError:',e)
    
import pandas as pd
import numpy as np
try:
    recipes = pd.read_json('recipeitems-latest.json')
except ValueError as e:
    print('ValueError:',e)
    
recipes = pd.read_json('recipeitems-latest.json')
get_ipython().run_line_magic('ls', '')
data = pd.read_csv('Fremont_Bridge_Hourly_Bicycle_Counts_by_Month_October_2012_to_present.csv',parse_dates=True)
data.head()
#[Out]#                      Date  Fremont Bridge West Sidewalk  \
#[Out]# 0  10/03/2012 12:00:00 AM                           4.0   
#[Out]# 1  10/03/2012 01:00:00 AM                           4.0   
#[Out]# 2  10/03/2012 02:00:00 AM                           1.0   
#[Out]# 3  10/03/2012 03:00:00 AM                           2.0   
#[Out]# 4  10/03/2012 04:00:00 AM                           6.0   
#[Out]# 
#[Out]#    Fremont Bridge East Sidewalk  
#[Out]# 0                           9.0  
#[Out]# 1                           6.0  
#[Out]# 2                           1.0  
#[Out]# 3                           3.0  
#[Out]# 4                           1.0  
data.columns
#[Out]# Index(['Date', 'Fremont Bridge West Sidewalk', 'Fremont Bridge East Sidewalk'], dtype='object')
data = pd.read_csv('Fremont_Bridge_Hourly_Bicycle_Counts_by_Month_October_2012_to_present.csv',parse_dates=True,index_col='Date')
data.columns
#[Out]# Index(['Fremont Bridge West Sidewalk', 'Fremont Bridge East Sidewalk'], dtype='object')
data.columns = ['West','East']
data['Tatal'] = data.eval('West+East') # eval ??
get_ipython().run_line_magic('pinfo', 'data.eval')
data['Total'].head()
data['Tatal'] = data.eval('West+East') # eval ??
data['Tatal'].head()
#[Out]# Date
#[Out]# 2012-10-03 00:00:00    13.0
#[Out]# 2012-10-03 01:00:00    10.0
#[Out]# 2012-10-03 02:00:00     2.0
#[Out]# 2012-10-03 03:00:00     5.0
#[Out]# 2012-10-03 04:00:00     7.0
#[Out]# Name: Tatal, dtype: float64
data.head()
#[Out]#                      West  East  Tatal
#[Out]# Date                                  
#[Out]# 2012-10-03 00:00:00   4.0   9.0   13.0
#[Out]# 2012-10-03 01:00:00   4.0   6.0   10.0
#[Out]# 2012-10-03 02:00:00   1.0   1.0    2.0
#[Out]# 2012-10-03 03:00:00   2.0   3.0    5.0
#[Out]# 2012-10-03 04:00:00   6.0   1.0    7.0
data.dropna()
#[Out]#                       West   East  Tatal
#[Out]# Date                                    
#[Out]# 2012-10-03 00:00:00    4.0    9.0   13.0
#[Out]# 2012-10-03 01:00:00    4.0    6.0   10.0
#[Out]# 2012-10-03 02:00:00    1.0    1.0    2.0
#[Out]# 2012-10-03 03:00:00    2.0    3.0    5.0
#[Out]# 2012-10-03 04:00:00    6.0    1.0    7.0
#[Out]# 2012-10-03 05:00:00   21.0   10.0   31.0
#[Out]# 2012-10-03 06:00:00  105.0   50.0  155.0
#[Out]# 2012-10-03 07:00:00  257.0   95.0  352.0
#[Out]# 2012-10-03 08:00:00  291.0  146.0  437.0
#[Out]# 2012-10-03 09:00:00  172.0  104.0  276.0
#[Out]# 2012-10-03 10:00:00   72.0   46.0  118.0
#[Out]# 2012-10-03 11:00:00   10.0   32.0   42.0
#[Out]# 2012-10-03 12:00:00   35.0   41.0   76.0
#[Out]# 2012-10-03 13:00:00   42.0   48.0   90.0
#[Out]# 2012-10-03 14:00:00   77.0   51.0  128.0
#[Out]# 2012-10-03 15:00:00   72.0   92.0  164.0
#[Out]# 2012-10-03 16:00:00  133.0  182.0  315.0
#[Out]# 2012-10-03 17:00:00  192.0  391.0  583.0
#[Out]# 2012-10-03 18:00:00  122.0  258.0  380.0
#[Out]# 2012-10-03 19:00:00   59.0   69.0  128.0
#[Out]# 2012-10-03 20:00:00   29.0   51.0   80.0
#[Out]# 2012-10-03 21:00:00   25.0   38.0   63.0
#[Out]# 2012-10-03 22:00:00   24.0   25.0   49.0
#[Out]# 2012-10-03 23:00:00    5.0   12.0   17.0
#[Out]# 2012-10-04 00:00:00    7.0   11.0   18.0
#[Out]# 2012-10-04 01:00:00    3.0    0.0    3.0
#[Out]# 2012-10-04 02:00:00    3.0    6.0    9.0
#[Out]# 2012-10-04 03:00:00    0.0    3.0    3.0
#[Out]# 2012-10-04 04:00:00    7.0    1.0    8.0
#[Out]# 2012-10-04 05:00:00   15.0   11.0   26.0
#[Out]# ...                    ...    ...    ...
#[Out]# 2018-04-29 18:00:00   25.0   36.0   61.0
#[Out]# 2018-04-29 19:00:00   27.0   30.0   57.0
#[Out]# 2018-04-29 20:00:00   23.0   29.0   52.0
#[Out]# 2018-04-29 21:00:00   16.0    7.0   23.0
#[Out]# 2018-04-29 22:00:00    3.0   12.0   15.0
#[Out]# 2018-04-29 23:00:00    3.0    8.0   11.0
#[Out]# 2018-04-30 00:00:00    1.0    1.0    2.0
#[Out]# 2018-04-30 01:00:00    1.0    1.0    2.0
#[Out]# 2018-04-30 02:00:00    4.0    0.0    4.0
#[Out]# 2018-04-30 03:00:00    1.0    1.0    2.0
#[Out]# 2018-04-30 04:00:00    1.0    6.0    7.0
#[Out]# 2018-04-30 05:00:00   17.0   14.0   31.0
#[Out]# 2018-04-30 06:00:00   80.0   65.0  145.0
#[Out]# 2018-04-30 07:00:00  224.0  165.0  389.0
#[Out]# 2018-04-30 08:00:00  272.0  269.0  541.0
#[Out]# 2018-04-30 09:00:00  121.0  138.0  259.0
#[Out]# 2018-04-30 10:00:00   38.0   56.0   94.0
#[Out]# 2018-04-30 11:00:00   28.0   38.0   66.0
#[Out]# 2018-04-30 12:00:00   27.0   28.0   55.0
#[Out]# 2018-04-30 13:00:00   31.0   32.0   63.0
#[Out]# 2018-04-30 14:00:00   33.0   48.0   81.0
#[Out]# 2018-04-30 15:00:00   39.0   79.0  118.0
#[Out]# 2018-04-30 16:00:00   81.0  207.0  288.0
#[Out]# 2018-04-30 17:00:00  130.0  491.0  621.0
#[Out]# 2018-04-30 18:00:00  115.0  295.0  410.0
#[Out]# 2018-04-30 19:00:00   49.0  147.0  196.0
#[Out]# 2018-04-30 20:00:00   34.0   64.0   98.0
#[Out]# 2018-04-30 21:00:00   21.0   25.0   46.0
#[Out]# 2018-04-30 22:00:00    9.0   14.0   23.0
#[Out]# 2018-04-30 23:00:00    2.0    6.0    8.0
#[Out]# 
#[Out]# [48856 rows x 3 columns]
data.dropna().describe()
#[Out]#                West          East         Tatal
#[Out]# count  48856.000000  48856.000000  48856.000000
#[Out]# mean      54.440294     55.199218    109.639512
#[Out]# std       72.805279     79.947734    138.729253
#[Out]# min        0.000000      0.000000      0.000000
#[Out]# 25%        7.000000      7.000000     15.000000
#[Out]# 50%       29.000000     28.000000     59.000000
#[Out]# 75%       71.000000     67.000000    143.000000
#[Out]# max      854.000000    717.000000   1165.000000
data.shape
#[Out]# (48864, 3)
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('pylab', '')
data,plot()
#[Out]# (                      West   East  Tatal
#[Out]#  Date                                    
#[Out]#  2012-10-03 00:00:00    4.0    9.0   13.0
#[Out]#  2012-10-03 01:00:00    4.0    6.0   10.0
#[Out]#  2012-10-03 02:00:00    1.0    1.0    2.0
#[Out]#  2012-10-03 03:00:00    2.0    3.0    5.0
#[Out]#  2012-10-03 04:00:00    6.0    1.0    7.0
#[Out]#  2012-10-03 05:00:00   21.0   10.0   31.0
#[Out]#  2012-10-03 06:00:00  105.0   50.0  155.0
#[Out]#  2012-10-03 07:00:00  257.0   95.0  352.0
#[Out]#  2012-10-03 08:00:00  291.0  146.0  437.0
#[Out]#  2012-10-03 09:00:00  172.0  104.0  276.0
#[Out]#  2012-10-03 10:00:00   72.0   46.0  118.0
#[Out]#  2012-10-03 11:00:00   10.0   32.0   42.0
#[Out]#  2012-10-03 12:00:00   35.0   41.0   76.0
#[Out]#  2012-10-03 13:00:00   42.0   48.0   90.0
#[Out]#  2012-10-03 14:00:00   77.0   51.0  128.0
#[Out]#  2012-10-03 15:00:00   72.0   92.0  164.0
#[Out]#  2012-10-03 16:00:00  133.0  182.0  315.0
#[Out]#  2012-10-03 17:00:00  192.0  391.0  583.0
#[Out]#  2012-10-03 18:00:00  122.0  258.0  380.0
#[Out]#  2012-10-03 19:00:00   59.0   69.0  128.0
#[Out]#  2012-10-03 20:00:00   29.0   51.0   80.0
#[Out]#  2012-10-03 21:00:00   25.0   38.0   63.0
#[Out]#  2012-10-03 22:00:00   24.0   25.0   49.0
#[Out]#  2012-10-03 23:00:00    5.0   12.0   17.0
#[Out]#  2012-10-04 00:00:00    7.0   11.0   18.0
#[Out]#  2012-10-04 01:00:00    3.0    0.0    3.0
#[Out]#  2012-10-04 02:00:00    3.0    6.0    9.0
#[Out]#  2012-10-04 03:00:00    0.0    3.0    3.0
#[Out]#  2012-10-04 04:00:00    7.0    1.0    8.0
#[Out]#  2012-10-04 05:00:00   15.0   11.0   26.0
#[Out]#  ...                    ...    ...    ...
#[Out]#  2018-04-29 18:00:00   25.0   36.0   61.0
#[Out]#  2018-04-29 19:00:00   27.0   30.0   57.0
#[Out]#  2018-04-29 20:00:00   23.0   29.0   52.0
#[Out]#  2018-04-29 21:00:00   16.0    7.0   23.0
#[Out]#  2018-04-29 22:00:00    3.0   12.0   15.0
#[Out]#  2018-04-29 23:00:00    3.0    8.0   11.0
#[Out]#  2018-04-30 00:00:00    1.0    1.0    2.0
#[Out]#  2018-04-30 01:00:00    1.0    1.0    2.0
#[Out]#  2018-04-30 02:00:00    4.0    0.0    4.0
#[Out]#  2018-04-30 03:00:00    1.0    1.0    2.0
#[Out]#  2018-04-30 04:00:00    1.0    6.0    7.0
#[Out]#  2018-04-30 05:00:00   17.0   14.0   31.0
#[Out]#  2018-04-30 06:00:00   80.0   65.0  145.0
#[Out]#  2018-04-30 07:00:00  224.0  165.0  389.0
#[Out]#  2018-04-30 08:00:00  272.0  269.0  541.0
#[Out]#  2018-04-30 09:00:00  121.0  138.0  259.0
#[Out]#  2018-04-30 10:00:00   38.0   56.0   94.0
#[Out]#  2018-04-30 11:00:00   28.0   38.0   66.0
#[Out]#  2018-04-30 12:00:00   27.0   28.0   55.0
#[Out]#  2018-04-30 13:00:00   31.0   32.0   63.0
#[Out]#  2018-04-30 14:00:00   33.0   48.0   81.0
#[Out]#  2018-04-30 15:00:00   39.0   79.0  118.0
#[Out]#  2018-04-30 16:00:00   81.0  207.0  288.0
#[Out]#  2018-04-30 17:00:00  130.0  491.0  621.0
#[Out]#  2018-04-30 18:00:00  115.0  295.0  410.0
#[Out]#  2018-04-30 19:00:00   49.0  147.0  196.0
#[Out]#  2018-04-30 20:00:00   34.0   64.0   98.0
#[Out]#  2018-04-30 21:00:00   21.0   25.0   46.0
#[Out]#  2018-04-30 22:00:00    9.0   14.0   23.0
#[Out]#  2018-04-30 23:00:00    2.0    6.0    8.0
#[Out]#  
#[Out]#  [48864 rows x 3 columns], [])
data.head()
#[Out]#                      West  East  Tatal
#[Out]# Date                                  
#[Out]# 2012-10-03 00:00:00   4.0   9.0   13.0
#[Out]# 2012-10-03 01:00:00   4.0   6.0   10.0
#[Out]# 2012-10-03 02:00:00   1.0   1.0    2.0
#[Out]# 2012-10-03 03:00:00   2.0   3.0    5.0
#[Out]# 2012-10-03 04:00:00   6.0   1.0    7.0
import seaborn
seaborn.set()
data.plot()
#[Out]# <matplotlib.axes._subplots.AxesSubplot at 0x203e759a940>
plt.ylabel('Hourly Bicycle Count')
#[Out]# Text(0,0.5,'Hourly Bicycle Count')
data.plot()
#[Out]# <matplotlib.axes._subplots.AxesSubplot at 0x203e9e76160>
plt.ylabel('Hourly Bicycle Count')
#[Out]# Text(20.75,0.5,'Hourly Bicycle Count')
weekly = data.resample('W').sum()
weekly.plot(style=[';','--','-'])
weekly.head()
#[Out]#               West    East    Tatal
#[Out]# Date                               
#[Out]# 2012-10-07  7297.0  6995.0  14292.0
#[Out]# 2012-10-14  8679.0  8116.0  16795.0
#[Out]# 2012-10-21  7946.0  7563.0  15509.0
#[Out]# 2012-10-28  6901.0  6536.0  13437.0
#[Out]# 2012-11-04  6408.0  5786.0  12194.0
weekly.plot(style=['--','-'])
#[Out]# <matplotlib.axes._subplots.AxesSubplot at 0x203ed741c50>
plt.ylabel('Weekly bicycle count')
#[Out]# Text(34.5,0.5,'Weekly bicycle count')
daily = data.resample('D').sum()
daily.head()
#[Out]#               West    East   Tatal
#[Out]# Date                              
#[Out]# 2012-10-03  1760.0  1761.0  3521.0
#[Out]# 2012-10-04  1708.0  1767.0  3475.0
#[Out]# 2012-10-05  1558.0  1590.0  3148.0
#[Out]# 2012-10-06  1080.0   926.0  2006.0
#[Out]# 2012-10-07  1191.0   951.0  2142.0
data.head()
#[Out]#                      West  East  Tatal
#[Out]# Date                                  
#[Out]# 2012-10-03 00:00:00   4.0   9.0   13.0
#[Out]# 2012-10-03 01:00:00   4.0   6.0   10.0
#[Out]# 2012-10-03 02:00:00   1.0   1.0    2.0
#[Out]# 2012-10-03 03:00:00   2.0   3.0    5.0
#[Out]# 2012-10-03 04:00:00   6.0   1.0    7.0
daily.rolling(30,center=True).mean().plot(style=['--','-*'])
#[Out]# <matplotlib.axes._subplots.AxesSubplot at 0x203f0102160>
plt.ylabel('mean of 30 days count')
#[Out]# Text(20.875,0.5,'mean of 30 days count')
daily.head()
#[Out]#               West    East   Tatal
#[Out]# Date                              
#[Out]# 2012-10-03  1760.0  1761.0  3521.0
#[Out]# 2012-10-04  1708.0  1767.0  3475.0
#[Out]# 2012-10-05  1558.0  1590.0  3148.0
#[Out]# 2012-10-06  1080.0   926.0  2006.0
#[Out]# 2012-10-07  1191.0   951.0  2142.0
