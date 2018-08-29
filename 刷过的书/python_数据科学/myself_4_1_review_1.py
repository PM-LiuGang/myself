# IPython log file

get_ipython().run_line_magic('cd', 'c')
get_ipython().run_line_magic('ls', '')
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import pandas as pd
import numpy as np
rng = np.random.RandomState(0)
get_ipython().run_line_magic('pylab', '')
ax1 = plt.axes()
ax2 = plt.axes([0.65,0.65,0.2,0.2])
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.5,0.8,0.4],xtickslabels=[],ylim=(-1.2,1.2))
ax1 = fig.add_axes([0.1,0.5,0.8,0.4],xticklabels=[],ylim=(-1.2,1.2))
ax2 = fig.add_axes([0.1,0.1,0.8,0.4],ylim=(-1.2,1.2))
x = np.linspace(0,10)
ax1.plot(np.sin(x))
#[Out]# [<matplotlib.lines.Line2D at 0x236b88e40b8>]
ax2.plot(np.cos(x))
#[Out]# [<matplotlib.lines.Line2D at 0x236b8a36860>]
for i in range(1,7):
    plt.subplot(2,3,i)
    plt.text(0.5,0.5,str((2,3,i)),fontsize=18,ha='center')
    
fig.
fig = plt.figure()
fig.subplots_adjust(hspace=0.4,wspace=0.4)
for i in range(1,7):
    ax = fig.add_subplot(2,3,i)
    ax.text(0.5,0.5,str((2,3,i)),fontsize=18,ha='center')
    
import matplotlib as mpl
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', 'data/')
get_ipython().run_line_magic('ls', '')
births = pd.read_csv('births.csv')
births.columns
#[Out]# Index(['year', 'month', 'day', 'gender', 'births'], dtype='object')
quartiles = np.percentile(births['births'],[25,50,75])
mu,sig = quartiles[1],0.74 * (quartiles[2]-quartiles[0])
births = births.query('(births > @mu -5 * @sig) & (births < @mu + 5 * @sig)
births = births.query('(births > @mu -5 * @sig) & (births < @mu + 5 * @sig))
births = births.query('(births > @mu -5 * @sig) & (births < @mu + 5 * @sig)')
births['day'] = births['day'].astype(int)
births.columns
#[Out]# Index(['year', 'month', 'day', 'gender', 'births'], dtype='object')
births['day'].dtype()
births['day'].dtype
#[Out]# dtype('int32')
births['year'].dtype
#[Out]# dtype('int64')
births['month'].dtype
#[Out]# dtype('int64')
births.head)_
births.head()
#[Out]#    year  month  day gender  births
#[Out]# 0  1969      1    1      F    4046
#[Out]# 1  1969      1    1      M    4440
#[Out]# 2  1969      1    2      F    4454
#[Out]# 3  1969      1    2      M    4548
#[Out]# 4  1969      1    3      F    4548
births.year * 10000
#[Out]# 0        19690000
#[Out]# 1        19690000
#[Out]# 2        19690000
#[Out]# 3        19690000
#[Out]# 4        19690000
#[Out]# 5        19690000
#[Out]# 6        19690000
#[Out]# 7        19690000
#[Out]# 8        19690000
#[Out]# 9        19690000
#[Out]# 10       19690000
#[Out]# 11       19690000
#[Out]# 12       19690000
#[Out]# 13       19690000
#[Out]# 14       19690000
#[Out]# 15       19690000
#[Out]# 16       19690000
#[Out]# 17       19690000
#[Out]# 18       19690000
#[Out]# 19       19690000
#[Out]# 20       19690000
#[Out]# 21       19690000
#[Out]# 22       19690000
#[Out]# 23       19690000
#[Out]# 24       19690000
#[Out]# 25       19690000
#[Out]# 26       19690000
#[Out]# 27       19690000
#[Out]# 28       19690000
#[Out]# 29       19690000
#[Out]#            ...   
#[Out]# 15037    19880000
#[Out]# 15038    19880000
#[Out]# 15039    19880000
#[Out]# 15040    19880000
#[Out]# 15041    19880000
#[Out]# 15042    19880000
#[Out]# 15043    19880000
#[Out]# 15044    19880000
#[Out]# 15045    19880000
#[Out]# 15046    19880000
#[Out]# 15047    19880000
#[Out]# 15048    19880000
#[Out]# 15049    19880000
#[Out]# 15050    19880000
#[Out]# 15051    19880000
#[Out]# 15052    19880000
#[Out]# 15053    19880000
#[Out]# 15054    19880000
#[Out]# 15055    19880000
#[Out]# 15056    19880000
#[Out]# 15057    19880000
#[Out]# 15058    19880000
#[Out]# 15059    19880000
#[Out]# 15060    19880000
#[Out]# 15061    19880000
#[Out]# 15062    19880000
#[Out]# 15063    19880000
#[Out]# 15064    19880000
#[Out]# 15065    19880000
#[Out]# 15066    19880000
#[Out]# Name: year, Length: 14610, dtype: int64
births.index = pd.to_datetime(10000*births.year + 100 * births.month + births.day,format='%Y%m%d')
births.index
#[Out]# DatetimeIndex(['1969-01-01', '1969-01-01', '1969-01-02', '1969-01-02',
#[Out]#                '1969-01-03', '1969-01-03', '1969-01-04', '1969-01-04',
#[Out]#                '1969-01-05', '1969-01-05',
#[Out]#                ...
#[Out]#                '1988-12-27', '1988-12-27', '1988-12-28', '1988-12-28',
#[Out]#                '1988-12-29', '1988-12-29', '1988-12-30', '1988-12-30',
#[Out]#                '1988-12-31', '1988-12-31'],
#[Out]#               dtype='datetime64[ns]', length=14610, freq=None)
births_by_date = births.pivot_table('births',[births.index.month,births.index.day])
get_ipython().run_line_magic('pinfo', 'births.pivot_table')
births.index
#[Out]# DatetimeIndex(['1969-01-01', '1969-01-01', '1969-01-02', '1969-01-02',
#[Out]#                '1969-01-03', '1969-01-03', '1969-01-04', '1969-01-04',
#[Out]#                '1969-01-05', '1969-01-05',
#[Out]#                ...
#[Out]#                '1988-12-27', '1988-12-27', '1988-12-28', '1988-12-28',
#[Out]#                '1988-12-29', '1988-12-29', '1988-12-30', '1988-12-30',
#[Out]#                '1988-12-31', '1988-12-31'],
#[Out]#               dtype='datetime64[ns]', length=14610, freq=None)
births.index.year
#[Out]# Int64Index([1969, 1969, 1969, 1969, 1969, 1969, 1969, 1969, 1969, 1969,
#[Out]#             ...
#[Out]#             1988, 1988, 1988, 1988, 1988, 1988, 1988, 1988, 1988, 1988],
#[Out]#            dtype='int64', length=14610)
births.index.day
#[Out]# Int64Index([ 1,  1,  2,  2,  3,  3,  4,  4,  5,  5,
#[Out]#             ...
#[Out]#             27, 27, 28, 28, 29, 29, 30, 30, 31, 31],
#[Out]#            dtype='int64', length=14610)
births['births']
#[Out]# 1969-01-01    4046
#[Out]# 1969-01-01    4440
#[Out]# 1969-01-02    4454
#[Out]# 1969-01-02    4548
#[Out]# 1969-01-03    4548
#[Out]# 1969-01-03    4994
#[Out]# 1969-01-04    4440
#[Out]# 1969-01-04    4520
#[Out]# 1969-01-05    4192
#[Out]# 1969-01-05    4198
#[Out]# 1969-01-06    4710
#[Out]# 1969-01-06    4850
#[Out]# 1969-01-07    4646
#[Out]# 1969-01-07    5092
#[Out]# 1969-01-08    4800
#[Out]# 1969-01-08    4934
#[Out]# 1969-01-09    4592
#[Out]# 1969-01-09    4842
#[Out]# 1969-01-10    4852
#[Out]# 1969-01-10    5190
#[Out]# 1969-01-11    4580
#[Out]# 1969-01-11    4598
#[Out]# 1969-01-12    4126
#[Out]# 1969-01-12    4324
#[Out]# 1969-01-13    4758
#[Out]# 1969-01-13    5076
#[Out]# 1969-01-14    5070
#[Out]# 1969-01-14    5296
#[Out]# 1969-01-15    4798
#[Out]# 1969-01-15    5096
#[Out]#               ... 
#[Out]# 1988-12-17    4270
#[Out]# 1988-12-17    4486
#[Out]# 1988-12-18    4211
#[Out]# 1988-12-18    4220
#[Out]# 1988-12-19    5651
#[Out]# 1988-12-19    6065
#[Out]# 1988-12-20    6092
#[Out]# 1988-12-20    6343
#[Out]# 1988-12-21    5462
#[Out]# 1988-12-21    5861
#[Out]# 1988-12-22    5219
#[Out]# 1988-12-22    5510
#[Out]# 1988-12-23    4887
#[Out]# 1988-12-23    5110
#[Out]# 1988-12-24    4024
#[Out]# 1988-12-24    4269
#[Out]# 1988-12-25    3874
#[Out]# 1988-12-25    3961
#[Out]# 1988-12-26    4274
#[Out]# 1988-12-26    4409
#[Out]# 1988-12-27    5633
#[Out]# 1988-12-27    5895
#[Out]# 1988-12-28    5858
#[Out]# 1988-12-28    5989
#[Out]# 1988-12-29    5760
#[Out]# 1988-12-29    5944
#[Out]# 1988-12-30    5742
#[Out]# 1988-12-30    6095
#[Out]# 1988-12-31    4435
#[Out]# 1988-12-31    4698
#[Out]# Name: births, Length: 14610, dtype: int64
births_by_date
#[Out]#          births
#[Out]# 1  1   4009.225
#[Out]#    2   4247.400
#[Out]#    3   4500.900
#[Out]#    4   4571.350
#[Out]#    5   4603.625
#[Out]#    6   4668.150
#[Out]#    7   4706.925
#[Out]#    8   4629.650
#[Out]#    9   4537.775
#[Out]#    10  4591.700
#[Out]#    11  4675.150
#[Out]#    12  4700.800
#[Out]#    13  4730.050
#[Out]#    14  4816.200
#[Out]#    15  4733.650
#[Out]#    16  4665.025
#[Out]#    17  4654.650
#[Out]#    18  4707.325
#[Out]#    19  4731.525
#[Out]#    20  4767.525
#[Out]#    21  4790.250
#[Out]#    22  4742.800
#[Out]#    23  4666.750
#[Out]#    24  4653.200
#[Out]#    25  4698.000
#[Out]#    26  4715.900
#[Out]#    27  4747.025
#[Out]#    28  4771.800
#[Out]#    29  4702.300
#[Out]#    30  4644.225
#[Out]# ...         ...
#[Out]# 12 2   4830.300
#[Out]#    3   4758.500
#[Out]#    4   4718.725
#[Out]#    5   4734.675
#[Out]#    6   4683.050
#[Out]#    7   4704.325
#[Out]#    8   4803.800
#[Out]#    9   4793.825
#[Out]#    10  4785.325
#[Out]#    11  4738.500
#[Out]#    12  4791.300
#[Out]#    13  4676.675
#[Out]#    14  4792.100
#[Out]#    15  4920.800
#[Out]#    16  4968.100
#[Out]#    17  4951.600
#[Out]#    18  4936.375
#[Out]#    19  4962.925
#[Out]#    20  4877.025
#[Out]#    21  4816.100
#[Out]#    22  4661.925
#[Out]#    23  4466.675
#[Out]#    24  4126.250
#[Out]#    25  3844.450
#[Out]#    26  4383.525
#[Out]#    27  4850.150
#[Out]#    28  5044.200
#[Out]#    29  5120.150
#[Out]#    30  5172.350
#[Out]#    31  4859.200
#[Out]# 
#[Out]# [366 rows x 1 columns]
births_by_date_valication = births.pivot_table(values='births',index=[births.index.month,births.index.day])
births_by_date_valication
#[Out]#          births
#[Out]# 1  1   4009.225
#[Out]#    2   4247.400
#[Out]#    3   4500.900
#[Out]#    4   4571.350
#[Out]#    5   4603.625
#[Out]#    6   4668.150
#[Out]#    7   4706.925
#[Out]#    8   4629.650
#[Out]#    9   4537.775
#[Out]#    10  4591.700
#[Out]#    11  4675.150
#[Out]#    12  4700.800
#[Out]#    13  4730.050
#[Out]#    14  4816.200
#[Out]#    15  4733.650
#[Out]#    16  4665.025
#[Out]#    17  4654.650
#[Out]#    18  4707.325
#[Out]#    19  4731.525
#[Out]#    20  4767.525
#[Out]#    21  4790.250
#[Out]#    22  4742.800
#[Out]#    23  4666.750
#[Out]#    24  4653.200
#[Out]#    25  4698.000
#[Out]#    26  4715.900
#[Out]#    27  4747.025
#[Out]#    28  4771.800
#[Out]#    29  4702.300
#[Out]#    30  4644.225
#[Out]# ...         ...
#[Out]# 12 2   4830.300
#[Out]#    3   4758.500
#[Out]#    4   4718.725
#[Out]#    5   4734.675
#[Out]#    6   4683.050
#[Out]#    7   4704.325
#[Out]#    8   4803.800
#[Out]#    9   4793.825
#[Out]#    10  4785.325
#[Out]#    11  4738.500
#[Out]#    12  4791.300
#[Out]#    13  4676.675
#[Out]#    14  4792.100
#[Out]#    15  4920.800
#[Out]#    16  4968.100
#[Out]#    17  4951.600
#[Out]#    18  4936.375
#[Out]#    19  4962.925
#[Out]#    20  4877.025
#[Out]#    21  4816.100
#[Out]#    22  4661.925
#[Out]#    23  4466.675
#[Out]#    24  4126.250
#[Out]#    25  3844.450
#[Out]#    26  4383.525
#[Out]#    27  4850.150
#[Out]#    28  5044.200
#[Out]#    29  5120.150
#[Out]#    30  5172.350
#[Out]#    31  4859.200
#[Out]# 
#[Out]# [366 rows x 1 columns]
births_by_date.index = [pd.datetime(2012,month,day) for (month,day) in births_by_date.index]
births_by_date.index
#[Out]# DatetimeIndex(['2012-01-01', '2012-01-02', '2012-01-03', '2012-01-04',
#[Out]#                '2012-01-05', '2012-01-06', '2012-01-07', '2012-01-08',
#[Out]#                '2012-01-09', '2012-01-10',
#[Out]#                ...
#[Out]#                '2012-12-22', '2012-12-23', '2012-12-24', '2012-12-25',
#[Out]#                '2012-12-26', '2012-12-27', '2012-12-28', '2012-12-29',
#[Out]#                '2012-12-30', '2012-12-31'],
#[Out]#               dtype='datetime64[ns]', length=366, freq=None)
births.index
#[Out]# DatetimeIndex(['1969-01-01', '1969-01-01', '1969-01-02', '1969-01-02',
#[Out]#                '1969-01-03', '1969-01-03', '1969-01-04', '1969-01-04',
#[Out]#                '1969-01-05', '1969-01-05',
#[Out]#                ...
#[Out]#                '1988-12-27', '1988-12-27', '1988-12-28', '1988-12-28',
#[Out]#                '1988-12-29', '1988-12-29', '1988-12-30', '1988-12-30',
#[Out]#                '1988-12-31', '1988-12-31'],
#[Out]#               dtype='datetime64[ns]', length=14610, freq=None)
fig,ax = plt.subplots(figsize=(12,4))
births_by_date.plot(ax=ax)
#[Out]# <matplotlib.axes._subplots.AxesSubplot at 0x236b9c6aeb8>
get_ipython().run_line_magic('pinfo', 'births_by_date.plot')
style = dict(size=10,color='gray')
style
#[Out]# {'color': 'gray', 'size': 10}
ax.text('2012-1-1',3950,"New year Day',**style)
ax.text('2012-1-1',3950,'New year Day',**style)
get_ipython().run_line_magic('pinfo', 'ax')
ax
#[Out]# <matplotlib.axes._subplots.AxesSubplot at 0x236b9c6aeb8>
births_by_date.index
#[Out]# DatetimeIndex(['2012-01-01', '2012-01-02', '2012-01-03', '2012-01-04',
#[Out]#                '2012-01-05', '2012-01-06', '2012-01-07', '2012-01-08',
#[Out]#                '2012-01-09', '2012-01-10',
#[Out]#                ...
#[Out]#                '2012-12-22', '2012-12-23', '2012-12-24', '2012-12-25',
#[Out]#                '2012-12-26', '2012-12-27', '2012-12-28', '2012-12-29',
#[Out]#                '2012-12-30', '2012-12-31'],
#[Out]#               dtype='datetime64[ns]', length=366, freq=None)
ax.text('2012-7-4',4250,'Independence Day',ha='center',**style)
get_ipython().run_line_magic('pinfo', 'ax.text')
ax.text('2012-9-4',4850,'Labor Day',ha='center',**style)
ax.text('2012-10-31',4600,'Halloween',ha='right',**style)
ax.set(title='USA births  by day of year (1969-1988)',ylabel = 'average daily births')
#[Out]# [Text(108.708,0.5,'average daily births'),
#[Out]#  Text(0.5,1,'USA births  by day of year (1969-1988)')]
ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
ax.xaxis.set_minor_locator(mpl.dates.MonthLocator()(bymonthday=15))
ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=15))
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter('%h'))
fig,ax = plt.subplots(facecolor='lightgray')
ax.axis([0,10,0,10])
#[Out]# [0, 10, 0, 10]
ax.text(1,5,'.Data:(1,5)',transform=ax.transData)
#[Out]# Text(1,5,'.Data:(1,5)')
ax.text(0.5,0.1,'.Data:(1,5)',transform=ax.transAxes)
#[Out]# Text(0.5,0.1,'.Data:(1,5)')
ax.text(0.2,0.2,'Figure:(0.2,0.2)',transform=fig.transFigure)
#[Out]# Text(0.2,0.2,'Figure:(0.2,0.2)')
tranData以x轴y轴标签作为数据坐标
ax.set(xlim=(0,2),ylim=(-6,6))
#[Out]# [(-6, 6), (0, 2)]
fig,ax = plt.subplots()
x = np.linspace(0,20,1000)
ax.plot(x,np.cos(x))
#[Out]# [<matplotlib.lines.Line2D at 0x236b8a7a5c0>]
ax.axis('equal')
#[Out]# (-1.0, 21.0, -1.0999987378908789, 1.0999999398995657)
ax.annotate('local maximum',xy=(6.28,1),xytext=(10,4),arrowprops=dict(facecolor='black',shrink=0.05))
#[Out]# Text(10,4,'local maximum')
ax.annotate('local minimum',xy=(5*np.pi,-1),xytext=(2,-6),arrowprops=dict(arrowstyle='->',connectionstyle='angle3,angelA=0,angleB=-90))
ax.annotate('local minimum',xy=(5*np.pi,-1),xytext=(2,-6),arrowprops=dict(arrowstyle='->',connectionstyle='angle3,angelA=0,angleB=-90'))
ax.annotate('local minimum',xy=(5*np.pi,-1),xytext=(2,-6),arrowprops=dict(arrowstyle='->',connectionstyle='angle3,angleA=0,angleB=-90'))
#[Out]# Text(2,-6,'local minimum')
fig.savefig('Figure_4_1_review_2.png')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', '..')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', 'data/')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', '..')
get_ipython().run_line_magic('cd', 'image/')
get_ipython().run_line_magic('ls', '')
fig.savefig('Figure_4_1_review_2.png')
fig,ax = plt.subplots(figsize=(12,4))
births_by_date.plot(ax=ax)
#[Out]# <matplotlib.axes._subplots.AxesSubplot at 0x236bc9ca9b0>
ax.annotate('New Year Day',xy=('2012-1-1',4100),xycoords='data',xytext=(50,-30),textcoords='offset points',arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=-0.2'))
#[Out]# Text(50,-30,'New Year Day')
get_ipython().run_line_magic('pinfo', 'ax.annotate')
plt.style.use('seaborn-whitegrid')
ax = plt.axes(xscale='log',yscale='log')
ax = plt.axes(xscale='log',yscale='log')
ax = plt.axes(xscale='log',yscale='log')
print(ax.xaxis.get_major_locator())
ax = plt.axes()
ax.plot(np.random.rand(50))
#[Out]# [<matplotlib.lines.Line2D at 0x236bb83a0f0>]
ax.yaxis.set_major_locator(plt.NullLocator())
ax.plot(np.random.rand(50))
#[Out]# [<matplotlib.lines.Line2D at 0x236bb8b25f8>]
ax = plt.axes()
ax.yaxis.set_major_locator(plt.NullLocator())
ax.plot(np.random.rand(50))
#[Out]# [<matplotlib.lines.Line2D at 0x236c16b3588>]
ax.yaxis.set_major_locator(plt.NullLocator())
ax.xaxis.set_major_formatter(plt.NullLocator())
ax.xaxis.set_major_formatter(plt.NullLocator())
ax.xaxis.set_major_formatter(plt.NullFormatter())
fig,ax = plt.subplots()
x = np.linspace(0,3*np.pi,1000)
ax.plot(x,np.sin(x),lw=3,label='Sine')
#[Out]# [<matplotlib.lines.Line2D at 0x236c10dfda0>]
ax.plot(x,np.cos(x),lw=3,label='Cosine')
#[Out]# [<matplotlib.lines.Line2D at 0x236bd355358>]
ax.grid(True)
ax.legend(frameon=False)
#[Out]# <matplotlib.legend.Legend at 0x236bcfdc898>
ax.axis('equal')
#[Out]# (-0.47123889803846897, 9.896016858807847, -1.1, 1.1)
ax.set_xlim(0,3*np.pi)
#[Out]# (0, 9.42477796076938)
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi/2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi/4))
def format_func(value,tick_number):
    n = int(np.round(2 * value /np.pi))
    if n==0:
        return '0'
    elif n==1:
        return r'$\pi/2$'
    elif n % 2 >0:
        return r'${0}\pi/2$'.format(n)
    else:
        return r'${0}\pi$'.format(n//2)
    
ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
plt.style.use('classic')
x = np.random.randn(1000)
plt.hist(x)
#[Out]# (array([  1.,   1.,  36.,  76., 185., 236., 251., 142.,  55.,  17.]),
#[Out]#  array([-3.97222136, -3.30061122, -2.62900108, -1.95739094, -1.2857808 ,
#[Out]#         -0.61417066,  0.05743949,  0.72904963,  1.40065977,  2.07226991,
#[Out]#          2.74388005]),
#[Out]#  <a list of 10 Patch objects>)
ax = plt.axes(axisbg='#E6E6E6')
ax.set_axisbelow(True)
plt.grid(color='w',linestyle='solid')
for spine in ax.spines.values():
    spine.set_visible(False)
    
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()
ax.tick_params(color='gray',direction='out')
for tick in ax.get_xticklabels():
    tick.set_color('gray')
    
for tick in ax.get_yticklabels():
    tick.set_color('gray')
    
ax.hist(x,edgecolor='#E6E6E6',color='EE6666')
ax.hist(x,edgecolor='#E6E6E6',color='#EE6666')
#[Out]# (array([  1.,   1.,  36.,  76., 185., 236., 251., 142.,  55.,  17.]),
#[Out]#  array([-3.97222136, -3.30061122, -2.62900108, -1.95739094, -1.2857808 ,
#[Out]#         -0.61417066,  0.05743949,  0.72904963,  1.40065977,  2.07226991,
#[Out]#          2.74388005]),
#[Out]#  <a list of 10 Patch objects>)
get_ipython().run_line_magic('pwd', '')
#[Out]# 'c:\\python\\python_数据科学手册\\myself_x\\image'
get_ipython().run_line_magic('ls', '')
fig.savefig('Figure_4_1_review_3.png')
get_ipython().run_line_magic('pinfo', 'plt.style')
plt.style.available[:5]
#[Out]# ['bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight']
get_ipython().run_line_magic('pinfo', 'plt.style.context')
plt.style.context[:5]
get_ipython().run_line_magic('logstate', '')
from mpl_toolkits import mplot3d
fig = plt.figure()
ax = plt.axes(projection='3d')
zline = np.linspace(0,15,1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline,yline,zline,'gray')
#[Out]# [<mpl_toolkits.mplot3d.art3d.Line3D at 0x236bcfdc358>]
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata,ydata,zdata,c=zdata,cmap='Greens')
#[Out]# <mpl_toolkits.mplot3d.art3d.Path3DCollection at 0x236c1d90cc0>
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import Basemap
import basemap
import Basemap
from mpl_toolkits.basemap import Basemap
get_ipython().run_line_magic('logstop', '')
