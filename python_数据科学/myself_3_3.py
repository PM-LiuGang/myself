# IPython log file

get_ipython().run_line_magic('cd', 'c')
get_ipython().run_line_magic('bookmark', '-l')
get_ipython().run_line_magic('bookmark', 'c c:/python/python_数据科学手册/')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('bookmark', '-l')
get_ipython().run_line_magic('pwd', '')
#[Out]# 'C:\\Users\\Administrator'
get_ipython().run_line_magic('cd', 'c')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('pwd', '')
#[Out]# 'c:\\python\\python_数据科学手册'
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', 'myself_x/')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('logstart', 'myself_3_3.py')
get_ipython().run_line_magic('logstart', '-o myself_3_3.py')
get_ipython().run_line_magic('logstop', '')
import pandas as pd
import numpy as np
df1 = pd.DataFrame({'employee':['Bob','Jake','Lisa','Sue'],'group':['Accounting','Engineering','Engineering','HR']})
df1
#[Out]#   employee        group
#[Out]# 0      Bob   Accounting
#[Out]# 1     Jake  Engineering
#[Out]# 2     Lisa  Engineering
#[Out]# 3      Sue           HR
df2 = pd.DataFrame({'employee':['Bob','Jake','Lisa','Sue'],'group':[2004,2008,2012,2014]})
pd.merge(df1,df2,on='employee')
#[Out]#   employee      group_x  group_y
#[Out]# 0      Bob   Accounting     2004
#[Out]# 1     Jake  Engineering     2008
#[Out]# 2     Lisa  Engineering     2012
#[Out]# 3      Sue           HR     2014
df3 = pd.DataFrame({'employee':['Bob','Jake','Lisa','Sue'],'salary':[70000,80000,120000,90000]})
pd.merge(df1,df3,left_on='employee',right_on='name')
df3 = pd.DataFrame({'name':['Bob','Jake','Lisa','Sue'],'salary':[70000,80000,120000,90000]})
pd.merge(df1,df3,left_on='employee',right_on='name')
#[Out]#   employee        group  name  salary
#[Out]# 0      Bob   Accounting   Bob   70000
#[Out]# 1     Jake  Engineering  Jake   80000
#[Out]# 2     Lisa  Engineering  Lisa  120000
#[Out]# 3      Sue           HR   Sue   90000
pd.merge(df1,df3,left_on='employee',right_on='name').drop('name',axis=1)
#[Out]#   employee        group  salary
#[Out]# 0      Bob   Accounting   70000
#[Out]# 1     Jake  Engineering   80000
#[Out]# 2     Lisa  Engineering  120000
#[Out]# 3      Sue           HR   90000
df1a = df1.set_index('employee')
df1
#[Out]#   employee        group
#[Out]# 0      Bob   Accounting
#[Out]# 1     Jake  Engineering
#[Out]# 2     Lisa  Engineering
#[Out]# 3      Sue           HR
df1a
#[Out]#                 group
#[Out]# employee             
#[Out]# Bob        Accounting
#[Out]# Jake      Engineering
#[Out]# Lisa      Engineering
#[Out]# Sue                HR
df2a = df2.set_index('employee')
df2a
#[Out]#           group
#[Out]# employee       
#[Out]# Bob        2004
#[Out]# Jake       2008
#[Out]# Lisa       2012
#[Out]# Sue        2014
pd.merge(df1a,df2a,left_index=True,right_index=True)
#[Out]#               group_x  group_y
#[Out]# employee                      
#[Out]# Bob        Accounting     2004
#[Out]# Jake      Engineering     2008
#[Out]# Lisa      Engineering     2012
#[Out]# Sue                HR     2014
df1a
#[Out]#                 group
#[Out]# employee             
#[Out]# Bob        Accounting
#[Out]# Jake      Engineering
#[Out]# Lisa      Engineering
#[Out]# Sue                HR
df2a
#[Out]#           group
#[Out]# employee       
#[Out]# Bob        2004
#[Out]# Jake       2008
#[Out]# Lisa       2012
#[Out]# Sue        2014
df1a.join(df2a)
df1a
#[Out]#                 group
#[Out]# employee             
#[Out]# Bob        Accounting
#[Out]# Jake      Engineering
#[Out]# Lisa      Engineering
#[Out]# Sue                HR
df2a
#[Out]#           group
#[Out]# employee       
#[Out]# Bob        2004
#[Out]# Jake       2008
#[Out]# Lisa       2012
#[Out]# Sue        2014
df2a.columns = 'hire_date'
df2a.columns = ['hire_date']
df1a.join(df2a)
#[Out]#                 group  hire_date
#[Out]# employee                        
#[Out]# Bob        Accounting       2004
#[Out]# Jake      Engineering       2008
#[Out]# Lisa      Engineering       2012
#[Out]# Sue                HR       2014
df1
#[Out]#   employee        group
#[Out]# 0      Bob   Accounting
#[Out]# 1     Jake  Engineering
#[Out]# 2     Lisa  Engineering
#[Out]# 3      Sue           HR
df3
#[Out]#    name  salary
#[Out]# 0   Bob   70000
#[Out]# 1  Jake   80000
#[Out]# 2  Lisa  120000
#[Out]# 3   Sue   90000
df1a
#[Out]#                 group
#[Out]# employee             
#[Out]# Bob        Accounting
#[Out]# Jake      Engineering
#[Out]# Lisa      Engineering
#[Out]# Sue                HR
df3
#[Out]#    name  salary
#[Out]# 0   Bob   70000
#[Out]# 1  Jake   80000
#[Out]# 2  Lisa  120000
#[Out]# 3   Sue   90000
pd.merge(df1a,df3,left_index=True,right_on='name')
#[Out]#          group  name  salary
#[Out]# 0   Accounting   Bob   70000
#[Out]# 1  Engineering  Jake   80000
#[Out]# 2  Engineering  Lisa  120000
#[Out]# 3           HR   Sue   90000
df6 = pd.DataFrame({'name':['Peter','Paul','Mary'].'food':['fish','beans','bread']},columns=['name','food'])
df6 = pd.DataFrame({'name':['Peter','Paul','Mary'],'food':['fish','beans','bread']},columns=['name','food'])
df7 = pd.DataFrame({'name':['Mary','Joseph',],'drink':['wine','beer']},columns=['name','drink'])
df6
#[Out]#     name   food
#[Out]# 0  Peter   fish
#[Out]# 1   Paul  beans
#[Out]# 2   Mary  bread
df7
#[Out]#      name drink
#[Out]# 0    Mary  wine
#[Out]# 1  Joseph  beer
pd.merge(df6,df7)
#[Out]#    name   food drink
#[Out]# 0  Mary  bread  wine
pd.merge(df6,df7,how='inner')
#[Out]#    name   food drink
#[Out]# 0  Mary  bread  wine
pd.merge(df6,df7,how='outer')
#[Out]#      name   food drink
#[Out]# 0   Peter   fish   NaN
#[Out]# 1    Paul  beans   NaN
#[Out]# 2    Mary  bread  wine
#[Out]# 3  Joseph    NaN  beer
pd.merge(df6,df7,how='left')
#[Out]#     name   food drink
#[Out]# 0  Peter   fish   NaN
#[Out]# 1   Paul  beans   NaN
#[Out]# 2   Mary  bread  wine
df6
#[Out]#     name   food
#[Out]# 0  Peter   fish
#[Out]# 1   Paul  beans
#[Out]# 2   Mary  bread
df7
#[Out]#      name drink
#[Out]# 0    Mary  wine
#[Out]# 1  Joseph  beer
pd.merge(df6,df7,how='right')
#[Out]#      name   food drink
#[Out]# 0    Mary  bread  wine
#[Out]# 1  Joseph    NaN  beer
df8 = pd.DataFrame({'name':['Bob','Jake','Lisa','Sue'],'rank':[1,2,3,4]})
df9 = pd.DataFrame({'name':['Bob','Jake','Lisa','Sue'],'rank':[3,1,4,2]})
df8
#[Out]#    name  rank
#[Out]# 0   Bob     1
#[Out]# 1  Jake     2
#[Out]# 2  Lisa     3
#[Out]# 3   Sue     4
df9
#[Out]#    name  rank
#[Out]# 0   Bob     3
#[Out]# 1  Jake     1
#[Out]# 2  Lisa     4
#[Out]# 3   Sue     2
pd.merge(df8,df9,on='name')
#[Out]#    name  rank_x  rank_y
#[Out]# 0   Bob       1       3
#[Out]# 1  Jake       2       1
#[Out]# 2  Lisa       3       4
#[Out]# 3   Sue       4       2
pd.merge(df8,df9,on='name',suffixes=['_L','_R'])
#[Out]#    name  rank_L  rank_R
#[Out]# 0   Bob       1       3
#[Out]# 1  Jake       2       1
#[Out]# 2  Lisa       3       4
#[Out]# 3   Sue       4       2
pop = pd.read_csv('state-population.csv')
areas = pd.read_csv('state-areas.csv')
abbrevs = pd.read_csv('state-abbrevs.csv')
pop
#[Out]#      state/region     ages  year   population
#[Out]# 0              AL  under18  2012    1117489.0
#[Out]# 1              AL    total  2012    4817528.0
#[Out]# 2              AL  under18  2010    1130966.0
#[Out]# 3              AL    total  2010    4785570.0
#[Out]# 4              AL  under18  2011    1125763.0
#[Out]# 5              AL    total  2011    4801627.0
#[Out]# 6              AL    total  2009    4757938.0
#[Out]# 7              AL  under18  2009    1134192.0
#[Out]# 8              AL  under18  2013    1111481.0
#[Out]# 9              AL    total  2013    4833722.0
#[Out]# 10             AL    total  2007    4672840.0
#[Out]# 11             AL  under18  2007    1132296.0
#[Out]# 12             AL    total  2008    4718206.0
#[Out]# 13             AL  under18  2008    1134927.0
#[Out]# 14             AL    total  2005    4569805.0
#[Out]# 15             AL  under18  2005    1117229.0
#[Out]# 16             AL    total  2006    4628981.0
#[Out]# 17             AL  under18  2006    1126798.0
#[Out]# 18             AL    total  2004    4530729.0
#[Out]# 19             AL  under18  2004    1113662.0
#[Out]# 20             AL    total  2003    4503491.0
#[Out]# 21             AL  under18  2003    1113083.0
#[Out]# 22             AL    total  2001    4467634.0
#[Out]# 23             AL  under18  2001    1120409.0
#[Out]# 24             AL    total  2002    4480089.0
#[Out]# 25             AL  under18  2002    1116590.0
#[Out]# 26             AL  under18  1999    1121287.0
#[Out]# 27             AL    total  1999    4430141.0
#[Out]# 28             AL    total  2000    4452173.0
#[Out]# 29             AL  under18  2000    1122273.0
#[Out]# ...           ...      ...   ...          ...
#[Out]# 2514          USA  under18  1999   71946051.0
#[Out]# 2515          USA    total  2000  282162411.0
#[Out]# 2516          USA  under18  2000   72376189.0
#[Out]# 2517          USA    total  1999  279040181.0
#[Out]# 2518          USA    total  2001  284968955.0
#[Out]# 2519          USA  under18  2001   72671175.0
#[Out]# 2520          USA    total  2002  287625193.0
#[Out]# 2521          USA  under18  2002   72936457.0
#[Out]# 2522          USA    total  2003  290107933.0
#[Out]# 2523          USA  under18  2003   73100758.0
#[Out]# 2524          USA    total  2004  292805298.0
#[Out]# 2525          USA  under18  2004   73297735.0
#[Out]# 2526          USA    total  2005  295516599.0
#[Out]# 2527          USA  under18  2005   73523669.0
#[Out]# 2528          USA    total  2006  298379912.0
#[Out]# 2529          USA  under18  2006   73757714.0
#[Out]# 2530          USA    total  2007  301231207.0
#[Out]# 2531          USA  under18  2007   74019405.0
#[Out]# 2532          USA    total  2008  304093966.0
#[Out]# 2533          USA  under18  2008   74104602.0
#[Out]# 2534          USA  under18  2013   73585872.0
#[Out]# 2535          USA    total  2013  316128839.0
#[Out]# 2536          USA    total  2009  306771529.0
#[Out]# 2537          USA  under18  2009   74134167.0
#[Out]# 2538          USA  under18  2010   74119556.0
#[Out]# 2539          USA    total  2010  309326295.0
#[Out]# 2540          USA  under18  2011   73902222.0
#[Out]# 2541          USA    total  2011  311582564.0
#[Out]# 2542          USA  under18  2012   73708179.0
#[Out]# 2543          USA    total  2012  313873685.0
#[Out]# 
#[Out]# [2544 rows x 4 columns]
pop.shape
#[Out]# (2544, 4)
areas.head()
#[Out]#         state  area (sq. mi)
#[Out]# 0     Alabama          52423
#[Out]# 1      Alaska         656425
#[Out]# 2     Arizona         114006
#[Out]# 3    Arkansas          53182
#[Out]# 4  California         163707
abbrevs.head()
#[Out]#         state abbreviation
#[Out]# 0     Alabama           AL
#[Out]# 1      Alaska           AK
#[Out]# 2     Arizona           AZ
#[Out]# 3    Arkansas           AR
#[Out]# 4  California           CA
merged = pd.merge(pop,abbrevs,how='outer',left_on ='state/region',right_on='abbreviation')
merged.head()
#[Out]#   state/region     ages  year  population    state abbreviation
#[Out]# 0           AL  under18  2012   1117489.0  Alabama           AL
#[Out]# 1           AL    total  2012   4817528.0  Alabama           AL
#[Out]# 2           AL  under18  2010   1130966.0  Alabama           AL
#[Out]# 3           AL    total  2010   4785570.0  Alabama           AL
#[Out]# 4           AL  under18  2011   1125763.0  Alabama           AL
pop.head()
#[Out]#   state/region     ages  year  population
#[Out]# 0           AL  under18  2012   1117489.0
#[Out]# 1           AL    total  2012   4817528.0
#[Out]# 2           AL  under18  2010   1130966.0
#[Out]# 3           AL    total  2010   4785570.0
#[Out]# 4           AL  under18  2011   1125763.0
abbrevs.head()
#[Out]#         state abbreviation
#[Out]# 0     Alabama           AL
#[Out]# 1      Alaska           AK
#[Out]# 2     Arizona           AZ
#[Out]# 3    Arkansas           AR
#[Out]# 4  California           CA
pop.shape
#[Out]# (2544, 4)
abbrevs.shape
#[Out]# (51, 2)
merged.shape
#[Out]# (2544, 6)
abbrevs.value_counts()
abbrevs['abbreviation'].value_counts()
#[Out]# VT    1
#[Out]# MD    1
#[Out]# AR    1
#[Out]# PA    1
#[Out]# MT    1
#[Out]# IA    1
#[Out]# VA    1
#[Out]# RI    1
#[Out]# NC    1
#[Out]# OK    1
#[Out]# IN    1
#[Out]# ID    1
#[Out]# SD    1
#[Out]# GA    1
#[Out]# HI    1
#[Out]# OH    1
#[Out]# CA    1
#[Out]# UT    1
#[Out]# LA    1
#[Out]# KY    1
#[Out]# AL    1
#[Out]# TN    1
#[Out]# MN    1
#[Out]# AK    1
#[Out]# SC    1
#[Out]# MO    1
#[Out]# MI    1
#[Out]# MS    1
#[Out]# AZ    1
#[Out]# CT    1
#[Out]# NJ    1
#[Out]# NY    1
#[Out]# IL    1
#[Out]# KS    1
#[Out]# ND    1
#[Out]# ME    1
#[Out]# FL    1
#[Out]# NV    1
#[Out]# NH    1
#[Out]# NE    1
#[Out]# MA    1
#[Out]# OR    1
#[Out]# WV    1
#[Out]# TX    1
#[Out]# NM    1
#[Out]# DC    1
#[Out]# WY    1
#[Out]# WI    1
#[Out]# WA    1
#[Out]# CO    1
#[Out]# DE    1
#[Out]# Name: abbreviation, dtype: int64
merged.isnull().any()
#[Out]# state/region    False
#[Out]# ages            False
#[Out]# year            False
#[Out]# population       True
#[Out]# state            True
#[Out]# abbreviation     True
#[Out]# dtype: bool
merged.columns
#[Out]# Index(['state/region', 'ages', 'year', 'population', 'state', 'abbreviation'], dtype='object')
merged = merged.drop('abbreviation',axis=1)
merged
#[Out]#      state/region     ages  year   population    state
#[Out]# 0              AL  under18  2012    1117489.0  Alabama
#[Out]# 1              AL    total  2012    4817528.0  Alabama
#[Out]# 2              AL  under18  2010    1130966.0  Alabama
#[Out]# 3              AL    total  2010    4785570.0  Alabama
#[Out]# 4              AL  under18  2011    1125763.0  Alabama
#[Out]# 5              AL    total  2011    4801627.0  Alabama
#[Out]# 6              AL    total  2009    4757938.0  Alabama
#[Out]# 7              AL  under18  2009    1134192.0  Alabama
#[Out]# 8              AL  under18  2013    1111481.0  Alabama
#[Out]# 9              AL    total  2013    4833722.0  Alabama
#[Out]# 10             AL    total  2007    4672840.0  Alabama
#[Out]# 11             AL  under18  2007    1132296.0  Alabama
#[Out]# 12             AL    total  2008    4718206.0  Alabama
#[Out]# 13             AL  under18  2008    1134927.0  Alabama
#[Out]# 14             AL    total  2005    4569805.0  Alabama
#[Out]# 15             AL  under18  2005    1117229.0  Alabama
#[Out]# 16             AL    total  2006    4628981.0  Alabama
#[Out]# 17             AL  under18  2006    1126798.0  Alabama
#[Out]# 18             AL    total  2004    4530729.0  Alabama
#[Out]# 19             AL  under18  2004    1113662.0  Alabama
#[Out]# 20             AL    total  2003    4503491.0  Alabama
#[Out]# 21             AL  under18  2003    1113083.0  Alabama
#[Out]# 22             AL    total  2001    4467634.0  Alabama
#[Out]# 23             AL  under18  2001    1120409.0  Alabama
#[Out]# 24             AL    total  2002    4480089.0  Alabama
#[Out]# 25             AL  under18  2002    1116590.0  Alabama
#[Out]# 26             AL  under18  1999    1121287.0  Alabama
#[Out]# 27             AL    total  1999    4430141.0  Alabama
#[Out]# 28             AL    total  2000    4452173.0  Alabama
#[Out]# 29             AL  under18  2000    1122273.0  Alabama
#[Out]# ...           ...      ...   ...          ...      ...
#[Out]# 2514          USA  under18  1999   71946051.0      NaN
#[Out]# 2515          USA    total  2000  282162411.0      NaN
#[Out]# 2516          USA  under18  2000   72376189.0      NaN
#[Out]# 2517          USA    total  1999  279040181.0      NaN
#[Out]# 2518          USA    total  2001  284968955.0      NaN
#[Out]# 2519          USA  under18  2001   72671175.0      NaN
#[Out]# 2520          USA    total  2002  287625193.0      NaN
#[Out]# 2521          USA  under18  2002   72936457.0      NaN
#[Out]# 2522          USA    total  2003  290107933.0      NaN
#[Out]# 2523          USA  under18  2003   73100758.0      NaN
#[Out]# 2524          USA    total  2004  292805298.0      NaN
#[Out]# 2525          USA  under18  2004   73297735.0      NaN
#[Out]# 2526          USA    total  2005  295516599.0      NaN
#[Out]# 2527          USA  under18  2005   73523669.0      NaN
#[Out]# 2528          USA    total  2006  298379912.0      NaN
#[Out]# 2529          USA  under18  2006   73757714.0      NaN
#[Out]# 2530          USA    total  2007  301231207.0      NaN
#[Out]# 2531          USA  under18  2007   74019405.0      NaN
#[Out]# 2532          USA    total  2008  304093966.0      NaN
#[Out]# 2533          USA  under18  2008   74104602.0      NaN
#[Out]# 2534          USA  under18  2013   73585872.0      NaN
#[Out]# 2535          USA    total  2013  316128839.0      NaN
#[Out]# 2536          USA    total  2009  306771529.0      NaN
#[Out]# 2537          USA  under18  2009   74134167.0      NaN
#[Out]# 2538          USA  under18  2010   74119556.0      NaN
#[Out]# 2539          USA    total  2010  309326295.0      NaN
#[Out]# 2540          USA  under18  2011   73902222.0      NaN
#[Out]# 2541          USA    total  2011  311582564.0      NaN
#[Out]# 2542          USA  under18  2012   73708179.0      NaN
#[Out]# 2543          USA    total  2012  313873685.0      NaN
#[Out]# 
#[Out]# [2544 rows x 5 columns]
merged.isnull().any()
#[Out]# state/region    False
#[Out]# ages            False
#[Out]# year            False
#[Out]# population       True
#[Out]# state            True
#[Out]# dtype: bool
merged[merged['population'].isnull()].head()
#[Out]#      state/region     ages  year  population state
#[Out]# 2448           PR  under18  1990         NaN   NaN
#[Out]# 2449           PR    total  1990         NaN   NaN
#[Out]# 2450           PR    total  1991         NaN   NaN
#[Out]# 2451           PR  under18  1991         NaN   NaN
#[Out]# 2452           PR    total  1993         NaN   NaN
merged.loc[merged['state'].isnull(),'state/region'].unique()
#[Out]# array(['PR', 'USA'], dtype=object)
merged.loc[merged['state'].isnull(),'state/region']
#[Out]# 2448     PR
#[Out]# 2449     PR
#[Out]# 2450     PR
#[Out]# 2451     PR
#[Out]# 2452     PR
#[Out]# 2453     PR
#[Out]# 2454     PR
#[Out]# 2455     PR
#[Out]# 2456     PR
#[Out]# 2457     PR
#[Out]# 2458     PR
#[Out]# 2459     PR
#[Out]# 2460     PR
#[Out]# 2461     PR
#[Out]# 2462     PR
#[Out]# 2463     PR
#[Out]# 2464     PR
#[Out]# 2465     PR
#[Out]# 2466     PR
#[Out]# 2467     PR
#[Out]# 2468     PR
#[Out]# 2469     PR
#[Out]# 2470     PR
#[Out]# 2471     PR
#[Out]# 2472     PR
#[Out]# 2473     PR
#[Out]# 2474     PR
#[Out]# 2475     PR
#[Out]# 2476     PR
#[Out]# 2477     PR
#[Out]#        ... 
#[Out]# 2514    USA
#[Out]# 2515    USA
#[Out]# 2516    USA
#[Out]# 2517    USA
#[Out]# 2518    USA
#[Out]# 2519    USA
#[Out]# 2520    USA
#[Out]# 2521    USA
#[Out]# 2522    USA
#[Out]# 2523    USA
#[Out]# 2524    USA
#[Out]# 2525    USA
#[Out]# 2526    USA
#[Out]# 2527    USA
#[Out]# 2528    USA
#[Out]# 2529    USA
#[Out]# 2530    USA
#[Out]# 2531    USA
#[Out]# 2532    USA
#[Out]# 2533    USA
#[Out]# 2534    USA
#[Out]# 2535    USA
#[Out]# 2536    USA
#[Out]# 2537    USA
#[Out]# 2538    USA
#[Out]# 2539    USA
#[Out]# 2540    USA
#[Out]# 2541    USA
#[Out]# 2542    USA
#[Out]# 2543    USA
#[Out]# Name: state/region, Length: 96, dtype: object
type(merged)
#[Out]# pandas.core.frame.DataFrame
merged.loc[merged['state'].isnull()]
#[Out]#      state/region     ages  year   population state
#[Out]# 2448           PR  under18  1990          NaN   NaN
#[Out]# 2449           PR    total  1990          NaN   NaN
#[Out]# 2450           PR    total  1991          NaN   NaN
#[Out]# 2451           PR  under18  1991          NaN   NaN
#[Out]# 2452           PR    total  1993          NaN   NaN
#[Out]# 2453           PR  under18  1993          NaN   NaN
#[Out]# 2454           PR  under18  1992          NaN   NaN
#[Out]# 2455           PR    total  1992          NaN   NaN
#[Out]# 2456           PR  under18  1994          NaN   NaN
#[Out]# 2457           PR    total  1994          NaN   NaN
#[Out]# 2458           PR    total  1995          NaN   NaN
#[Out]# 2459           PR  under18  1995          NaN   NaN
#[Out]# 2460           PR  under18  1996          NaN   NaN
#[Out]# 2461           PR    total  1996          NaN   NaN
#[Out]# 2462           PR  under18  1998          NaN   NaN
#[Out]# 2463           PR    total  1998          NaN   NaN
#[Out]# 2464           PR    total  1997          NaN   NaN
#[Out]# 2465           PR  under18  1997          NaN   NaN
#[Out]# 2466           PR    total  1999          NaN   NaN
#[Out]# 2467           PR  under18  1999          NaN   NaN
#[Out]# 2468           PR    total  2000    3810605.0   NaN
#[Out]# 2469           PR  under18  2000    1089063.0   NaN
#[Out]# 2470           PR    total  2001    3818774.0   NaN
#[Out]# 2471           PR  under18  2001    1077566.0   NaN
#[Out]# 2472           PR    total  2002    3823701.0   NaN
#[Out]# 2473           PR  under18  2002    1065051.0   NaN
#[Out]# 2474           PR    total  2004    3826878.0   NaN
#[Out]# 2475           PR  under18  2004    1035919.0   NaN
#[Out]# 2476           PR    total  2003    3826095.0   NaN
#[Out]# 2477           PR  under18  2003    1050615.0   NaN
#[Out]# ...           ...      ...   ...          ...   ...
#[Out]# 2514          USA  under18  1999   71946051.0   NaN
#[Out]# 2515          USA    total  2000  282162411.0   NaN
#[Out]# 2516          USA  under18  2000   72376189.0   NaN
#[Out]# 2517          USA    total  1999  279040181.0   NaN
#[Out]# 2518          USA    total  2001  284968955.0   NaN
#[Out]# 2519          USA  under18  2001   72671175.0   NaN
#[Out]# 2520          USA    total  2002  287625193.0   NaN
#[Out]# 2521          USA  under18  2002   72936457.0   NaN
#[Out]# 2522          USA    total  2003  290107933.0   NaN
#[Out]# 2523          USA  under18  2003   73100758.0   NaN
#[Out]# 2524          USA    total  2004  292805298.0   NaN
#[Out]# 2525          USA  under18  2004   73297735.0   NaN
#[Out]# 2526          USA    total  2005  295516599.0   NaN
#[Out]# 2527          USA  under18  2005   73523669.0   NaN
#[Out]# 2528          USA    total  2006  298379912.0   NaN
#[Out]# 2529          USA  under18  2006   73757714.0   NaN
#[Out]# 2530          USA    total  2007  301231207.0   NaN
#[Out]# 2531          USA  under18  2007   74019405.0   NaN
#[Out]# 2532          USA    total  2008  304093966.0   NaN
#[Out]# 2533          USA  under18  2008   74104602.0   NaN
#[Out]# 2534          USA  under18  2013   73585872.0   NaN
#[Out]# 2535          USA    total  2013  316128839.0   NaN
#[Out]# 2536          USA    total  2009  306771529.0   NaN
#[Out]# 2537          USA  under18  2009   74134167.0   NaN
#[Out]# 2538          USA  under18  2010   74119556.0   NaN
#[Out]# 2539          USA    total  2010  309326295.0   NaN
#[Out]# 2540          USA  under18  2011   73902222.0   NaN
#[Out]# 2541          USA    total  2011  311582564.0   NaN
#[Out]# 2542          USA  under18  2012   73708179.0   NaN
#[Out]# 2543          USA    total  2012  313873685.0   NaN
#[Out]# 
#[Out]# [96 rows x 5 columns]
merged.loc[merged['state'].isnull(),'state/region']
#[Out]# 2448     PR
#[Out]# 2449     PR
#[Out]# 2450     PR
#[Out]# 2451     PR
#[Out]# 2452     PR
#[Out]# 2453     PR
#[Out]# 2454     PR
#[Out]# 2455     PR
#[Out]# 2456     PR
#[Out]# 2457     PR
#[Out]# 2458     PR
#[Out]# 2459     PR
#[Out]# 2460     PR
#[Out]# 2461     PR
#[Out]# 2462     PR
#[Out]# 2463     PR
#[Out]# 2464     PR
#[Out]# 2465     PR
#[Out]# 2466     PR
#[Out]# 2467     PR
#[Out]# 2468     PR
#[Out]# 2469     PR
#[Out]# 2470     PR
#[Out]# 2471     PR
#[Out]# 2472     PR
#[Out]# 2473     PR
#[Out]# 2474     PR
#[Out]# 2475     PR
#[Out]# 2476     PR
#[Out]# 2477     PR
#[Out]#        ... 
#[Out]# 2514    USA
#[Out]# 2515    USA
#[Out]# 2516    USA
#[Out]# 2517    USA
#[Out]# 2518    USA
#[Out]# 2519    USA
#[Out]# 2520    USA
#[Out]# 2521    USA
#[Out]# 2522    USA
#[Out]# 2523    USA
#[Out]# 2524    USA
#[Out]# 2525    USA
#[Out]# 2526    USA
#[Out]# 2527    USA
#[Out]# 2528    USA
#[Out]# 2529    USA
#[Out]# 2530    USA
#[Out]# 2531    USA
#[Out]# 2532    USA
#[Out]# 2533    USA
#[Out]# 2534    USA
#[Out]# 2535    USA
#[Out]# 2536    USA
#[Out]# 2537    USA
#[Out]# 2538    USA
#[Out]# 2539    USA
#[Out]# 2540    USA
#[Out]# 2541    USA
#[Out]# 2542    USA
#[Out]# 2543    USA
#[Out]# Name: state/region, Length: 96, dtype: object
merged.loc[merged['state/region']='PR','state'] = 'Puerto Rico'

merged.loc[merged['state/region']=='PR','state'] = 'Puerto Rico'
merged.loc[merged['state/region']=='USA','state'] = 'United State American'
merged.isnull().any()
#[Out]# state/region    False
#[Out]# ages            False
#[Out]# year            False
#[Out]# population       True
#[Out]# state           False
#[Out]# dtype: bool
final = pd.merge(merged,areas,on='state',how='left')
merged
#[Out]#      state/region     ages  year   population                  state
#[Out]# 0              AL  under18  2012    1117489.0                Alabama
#[Out]# 1              AL    total  2012    4817528.0                Alabama
#[Out]# 2              AL  under18  2010    1130966.0                Alabama
#[Out]# 3              AL    total  2010    4785570.0                Alabama
#[Out]# 4              AL  under18  2011    1125763.0                Alabama
#[Out]# 5              AL    total  2011    4801627.0                Alabama
#[Out]# 6              AL    total  2009    4757938.0                Alabama
#[Out]# 7              AL  under18  2009    1134192.0                Alabama
#[Out]# 8              AL  under18  2013    1111481.0                Alabama
#[Out]# 9              AL    total  2013    4833722.0                Alabama
#[Out]# 10             AL    total  2007    4672840.0                Alabama
#[Out]# 11             AL  under18  2007    1132296.0                Alabama
#[Out]# 12             AL    total  2008    4718206.0                Alabama
#[Out]# 13             AL  under18  2008    1134927.0                Alabama
#[Out]# 14             AL    total  2005    4569805.0                Alabama
#[Out]# 15             AL  under18  2005    1117229.0                Alabama
#[Out]# 16             AL    total  2006    4628981.0                Alabama
#[Out]# 17             AL  under18  2006    1126798.0                Alabama
#[Out]# 18             AL    total  2004    4530729.0                Alabama
#[Out]# 19             AL  under18  2004    1113662.0                Alabama
#[Out]# 20             AL    total  2003    4503491.0                Alabama
#[Out]# 21             AL  under18  2003    1113083.0                Alabama
#[Out]# 22             AL    total  2001    4467634.0                Alabama
#[Out]# 23             AL  under18  2001    1120409.0                Alabama
#[Out]# 24             AL    total  2002    4480089.0                Alabama
#[Out]# 25             AL  under18  2002    1116590.0                Alabama
#[Out]# 26             AL  under18  1999    1121287.0                Alabama
#[Out]# 27             AL    total  1999    4430141.0                Alabama
#[Out]# 28             AL    total  2000    4452173.0                Alabama
#[Out]# 29             AL  under18  2000    1122273.0                Alabama
#[Out]# ...           ...      ...   ...          ...                    ...
#[Out]# 2514          USA  under18  1999   71946051.0  United State American
#[Out]# 2515          USA    total  2000  282162411.0  United State American
#[Out]# 2516          USA  under18  2000   72376189.0  United State American
#[Out]# 2517          USA    total  1999  279040181.0  United State American
#[Out]# 2518          USA    total  2001  284968955.0  United State American
#[Out]# 2519          USA  under18  2001   72671175.0  United State American
#[Out]# 2520          USA    total  2002  287625193.0  United State American
#[Out]# 2521          USA  under18  2002   72936457.0  United State American
#[Out]# 2522          USA    total  2003  290107933.0  United State American
#[Out]# 2523          USA  under18  2003   73100758.0  United State American
#[Out]# 2524          USA    total  2004  292805298.0  United State American
#[Out]# 2525          USA  under18  2004   73297735.0  United State American
#[Out]# 2526          USA    total  2005  295516599.0  United State American
#[Out]# 2527          USA  under18  2005   73523669.0  United State American
#[Out]# 2528          USA    total  2006  298379912.0  United State American
#[Out]# 2529          USA  under18  2006   73757714.0  United State American
#[Out]# 2530          USA    total  2007  301231207.0  United State American
#[Out]# 2531          USA  under18  2007   74019405.0  United State American
#[Out]# 2532          USA    total  2008  304093966.0  United State American
#[Out]# 2533          USA  under18  2008   74104602.0  United State American
#[Out]# 2534          USA  under18  2013   73585872.0  United State American
#[Out]# 2535          USA    total  2013  316128839.0  United State American
#[Out]# 2536          USA    total  2009  306771529.0  United State American
#[Out]# 2537          USA  under18  2009   74134167.0  United State American
#[Out]# 2538          USA  under18  2010   74119556.0  United State American
#[Out]# 2539          USA    total  2010  309326295.0  United State American
#[Out]# 2540          USA  under18  2011   73902222.0  United State American
#[Out]# 2541          USA    total  2011  311582564.0  United State American
#[Out]# 2542          USA  under18  2012   73708179.0  United State American
#[Out]# 2543          USA    total  2012  313873685.0  United State American
#[Out]# 
#[Out]# [2544 rows x 5 columns]
areas.head()
#[Out]#         state  area (sq. mi)
#[Out]# 0     Alabama          52423
#[Out]# 1      Alaska         656425
#[Out]# 2     Arizona         114006
#[Out]# 3    Arkansas          53182
#[Out]# 4  California         163707
areas.head()
#[Out]#         state  area (sq. mi)
#[Out]# 0     Alabama          52423
#[Out]# 1      Alaska         656425
#[Out]# 2     Arizona         114006
#[Out]# 3    Arkansas          53182
#[Out]# 4  California         163707
final.head()
#[Out]#   state/region     ages  year  population    state  area (sq. mi)
#[Out]# 0           AL  under18  2012   1117489.0  Alabama        52423.0
#[Out]# 1           AL    total  2012   4817528.0  Alabama        52423.0
#[Out]# 2           AL  under18  2010   1130966.0  Alabama        52423.0
#[Out]# 3           AL    total  2010   4785570.0  Alabama        52423.0
#[Out]# 4           AL  under18  2011   1125763.0  Alabama        52423.0
merged
#[Out]#      state/region     ages  year   population                  state
#[Out]# 0              AL  under18  2012    1117489.0                Alabama
#[Out]# 1              AL    total  2012    4817528.0                Alabama
#[Out]# 2              AL  under18  2010    1130966.0                Alabama
#[Out]# 3              AL    total  2010    4785570.0                Alabama
#[Out]# 4              AL  under18  2011    1125763.0                Alabama
#[Out]# 5              AL    total  2011    4801627.0                Alabama
#[Out]# 6              AL    total  2009    4757938.0                Alabama
#[Out]# 7              AL  under18  2009    1134192.0                Alabama
#[Out]# 8              AL  under18  2013    1111481.0                Alabama
#[Out]# 9              AL    total  2013    4833722.0                Alabama
#[Out]# 10             AL    total  2007    4672840.0                Alabama
#[Out]# 11             AL  under18  2007    1132296.0                Alabama
#[Out]# 12             AL    total  2008    4718206.0                Alabama
#[Out]# 13             AL  under18  2008    1134927.0                Alabama
#[Out]# 14             AL    total  2005    4569805.0                Alabama
#[Out]# 15             AL  under18  2005    1117229.0                Alabama
#[Out]# 16             AL    total  2006    4628981.0                Alabama
#[Out]# 17             AL  under18  2006    1126798.0                Alabama
#[Out]# 18             AL    total  2004    4530729.0                Alabama
#[Out]# 19             AL  under18  2004    1113662.0                Alabama
#[Out]# 20             AL    total  2003    4503491.0                Alabama
#[Out]# 21             AL  under18  2003    1113083.0                Alabama
#[Out]# 22             AL    total  2001    4467634.0                Alabama
#[Out]# 23             AL  under18  2001    1120409.0                Alabama
#[Out]# 24             AL    total  2002    4480089.0                Alabama
#[Out]# 25             AL  under18  2002    1116590.0                Alabama
#[Out]# 26             AL  under18  1999    1121287.0                Alabama
#[Out]# 27             AL    total  1999    4430141.0                Alabama
#[Out]# 28             AL    total  2000    4452173.0                Alabama
#[Out]# 29             AL  under18  2000    1122273.0                Alabama
#[Out]# ...           ...      ...   ...          ...                    ...
#[Out]# 2514          USA  under18  1999   71946051.0  United State American
#[Out]# 2515          USA    total  2000  282162411.0  United State American
#[Out]# 2516          USA  under18  2000   72376189.0  United State American
#[Out]# 2517          USA    total  1999  279040181.0  United State American
#[Out]# 2518          USA    total  2001  284968955.0  United State American
#[Out]# 2519          USA  under18  2001   72671175.0  United State American
#[Out]# 2520          USA    total  2002  287625193.0  United State American
#[Out]# 2521          USA  under18  2002   72936457.0  United State American
#[Out]# 2522          USA    total  2003  290107933.0  United State American
#[Out]# 2523          USA  under18  2003   73100758.0  United State American
#[Out]# 2524          USA    total  2004  292805298.0  United State American
#[Out]# 2525          USA  under18  2004   73297735.0  United State American
#[Out]# 2526          USA    total  2005  295516599.0  United State American
#[Out]# 2527          USA  under18  2005   73523669.0  United State American
#[Out]# 2528          USA    total  2006  298379912.0  United State American
#[Out]# 2529          USA  under18  2006   73757714.0  United State American
#[Out]# 2530          USA    total  2007  301231207.0  United State American
#[Out]# 2531          USA  under18  2007   74019405.0  United State American
#[Out]# 2532          USA    total  2008  304093966.0  United State American
#[Out]# 2533          USA  under18  2008   74104602.0  United State American
#[Out]# 2534          USA  under18  2013   73585872.0  United State American
#[Out]# 2535          USA    total  2013  316128839.0  United State American
#[Out]# 2536          USA    total  2009  306771529.0  United State American
#[Out]# 2537          USA  under18  2009   74134167.0  United State American
#[Out]# 2538          USA  under18  2010   74119556.0  United State American
#[Out]# 2539          USA    total  2010  309326295.0  United State American
#[Out]# 2540          USA  under18  2011   73902222.0  United State American
#[Out]# 2541          USA    total  2011  311582564.0  United State American
#[Out]# 2542          USA  under18  2012   73708179.0  United State American
#[Out]# 2543          USA    total  2012  313873685.0  United State American
#[Out]# 
#[Out]# [2544 rows x 5 columns]
merged.columns
#[Out]# Index(['state/region', 'ages', 'year', 'population', 'state'], dtype='object')
final.head()
#[Out]#   state/region     ages  year  population    state  area (sq. mi)
#[Out]# 0           AL  under18  2012   1117489.0  Alabama        52423.0
#[Out]# 1           AL    total  2012   4817528.0  Alabama        52423.0
#[Out]# 2           AL  under18  2010   1130966.0  Alabama        52423.0
#[Out]# 3           AL    total  2010   4785570.0  Alabama        52423.0
#[Out]# 4           AL  under18  2011   1125763.0  Alabama        52423.0
areas.columns
#[Out]# Index(['state', 'area (sq. mi)'], dtype='object')
final.isnull().any()
#[Out]# state/region     False
#[Out]# ages             False
#[Out]# year             False
#[Out]# population        True
#[Out]# state            False
#[Out]# area (sq. mi)     True
#[Out]# dtype: bool
final['state'][final['area (sq. mi)'].isnull()].unique()
#[Out]# array(['United State American'], dtype=object)
final.head()
#[Out]#   state/region     ages  year  population    state  area (sq. mi)
#[Out]# 0           AL  under18  2012   1117489.0  Alabama        52423.0
#[Out]# 1           AL    total  2012   4817528.0  Alabama        52423.0
#[Out]# 2           AL  under18  2010   1130966.0  Alabama        52423.0
#[Out]# 3           AL    total  2010   4785570.0  Alabama        52423.0
#[Out]# 4           AL  under18  2011   1125763.0  Alabama        52423.0
final['state'][final['state']=='United State American'] = 'United States'
final['state'][final['area (sq. mi)'].isnull()].unique()
#[Out]# array(['United States'], dtype=object)
final.dropna(inplace=True)
final.head()
#[Out]#   state/region     ages  year  population    state  area (sq. mi)
#[Out]# 0           AL  under18  2012   1117489.0  Alabama        52423.0
#[Out]# 1           AL    total  2012   4817528.0  Alabama        52423.0
#[Out]# 2           AL  under18  2010   1130966.0  Alabama        52423.0
#[Out]# 3           AL    total  2010   4785570.0  Alabama        52423.0
#[Out]# 4           AL  under18  2011   1125763.0  Alabama        52423.0
data2010 = final.query("'year' ==2010 & ages=='total'")
data2010 = final.query("'year' ==2010 & ages=='total'")
data2010 = final.query("'year' ==2010 & ages=='total'")
data2010 = final[(final['year']==2010) & (final['ages'] == 'total')]
data2010
#[Out]#      state/region   ages  year  population                 state  \
#[Out]# 3              AL  total  2010   4785570.0               Alabama   
#[Out]# 91             AK  total  2010    713868.0                Alaska   
#[Out]# 101            AZ  total  2010   6408790.0               Arizona   
#[Out]# 189            AR  total  2010   2922280.0              Arkansas   
#[Out]# 197            CA  total  2010  37333601.0            California   
#[Out]# 283            CO  total  2010   5048196.0              Colorado   
#[Out]# 293            CT  total  2010   3579210.0           Connecticut   
#[Out]# 379            DE  total  2010    899711.0              Delaware   
#[Out]# 389            DC  total  2010    605125.0  District of Columbia   
#[Out]# 475            FL  total  2010  18846054.0               Florida   
#[Out]# 485            GA  total  2010   9713248.0               Georgia   
#[Out]# 570            HI  total  2010   1363731.0                Hawaii   
#[Out]# 581            ID  total  2010   1570718.0                 Idaho   
#[Out]# 666            IL  total  2010  12839695.0              Illinois   
#[Out]# 677            IN  total  2010   6489965.0               Indiana   
#[Out]# 762            IA  total  2010   3050314.0                  Iowa   
#[Out]# 773            KS  total  2010   2858910.0                Kansas   
#[Out]# 858            KY  total  2010   4347698.0              Kentucky   
#[Out]# 869            LA  total  2010   4545392.0             Louisiana   
#[Out]# 954            ME  total  2010   1327366.0                 Maine   
#[Out]# 965            MD  total  2010   5787193.0              Maryland   
#[Out]# 1050           MA  total  2010   6563263.0         Massachusetts   
#[Out]# 1061           MI  total  2010   9876149.0              Michigan   
#[Out]# 1146           MN  total  2010   5310337.0             Minnesota   
#[Out]# 1157           MS  total  2010   2970047.0           Mississippi   
#[Out]# 1242           MO  total  2010   5996063.0              Missouri   
#[Out]# 1253           MT  total  2010    990527.0               Montana   
#[Out]# 1338           NE  total  2010   1829838.0              Nebraska   
#[Out]# 1349           NV  total  2010   2703230.0                Nevada   
#[Out]# 1434           NH  total  2010   1316614.0         New Hampshire   
#[Out]# 1445           NJ  total  2010   8802707.0            New Jersey   
#[Out]# 1530           NM  total  2010   2064982.0            New Mexico   
#[Out]# 1541           NY  total  2010  19398228.0              New York   
#[Out]# 1626           NC  total  2010   9559533.0        North Carolina   
#[Out]# 1637           ND  total  2010    674344.0          North Dakota   
#[Out]# 1722           OH  total  2010  11545435.0                  Ohio   
#[Out]# 1733           OK  total  2010   3759263.0              Oklahoma   
#[Out]# 1818           OR  total  2010   3837208.0                Oregon   
#[Out]# 1829           PA  total  2010  12710472.0          Pennsylvania   
#[Out]# 1914           RI  total  2010   1052669.0          Rhode Island   
#[Out]# 1925           SC  total  2010   4636361.0        South Carolina   
#[Out]# 2010           SD  total  2010    816211.0          South Dakota   
#[Out]# 2021           TN  total  2010   6356683.0             Tennessee   
#[Out]# 2106           TX  total  2010  25245178.0                 Texas   
#[Out]# 2117           UT  total  2010   2774424.0                  Utah   
#[Out]# 2202           VT  total  2010    625793.0               Vermont   
#[Out]# 2213           VA  total  2010   8024417.0              Virginia   
#[Out]# 2298           WA  total  2010   6742256.0            Washington   
#[Out]# 2309           WV  total  2010   1854146.0         West Virginia   
#[Out]# 2394           WI  total  2010   5689060.0             Wisconsin   
#[Out]# 2405           WY  total  2010    564222.0               Wyoming   
#[Out]# 2490           PR  total  2010   3721208.0           Puerto Rico   
#[Out]# 
#[Out]#       area (sq. mi)  
#[Out]# 3           52423.0  
#[Out]# 91         656425.0  
#[Out]# 101        114006.0  
#[Out]# 189         53182.0  
#[Out]# 197        163707.0  
#[Out]# 283        104100.0  
#[Out]# 293          5544.0  
#[Out]# 379          1954.0  
#[Out]# 389            68.0  
#[Out]# 475         65758.0  
#[Out]# 485         59441.0  
#[Out]# 570         10932.0  
#[Out]# 581         83574.0  
#[Out]# 666         57918.0  
#[Out]# 677         36420.0  
#[Out]# 762         56276.0  
#[Out]# 773         82282.0  
#[Out]# 858         40411.0  
#[Out]# 869         51843.0  
#[Out]# 954         35387.0  
#[Out]# 965         12407.0  
#[Out]# 1050        10555.0  
#[Out]# 1061        96810.0  
#[Out]# 1146        86943.0  
#[Out]# 1157        48434.0  
#[Out]# 1242        69709.0  
#[Out]# 1253       147046.0  
#[Out]# 1338        77358.0  
#[Out]# 1349       110567.0  
#[Out]# 1434         9351.0  
#[Out]# 1445         8722.0  
#[Out]# 1530       121593.0  
#[Out]# 1541        54475.0  
#[Out]# 1626        53821.0  
#[Out]# 1637        70704.0  
#[Out]# 1722        44828.0  
#[Out]# 1733        69903.0  
#[Out]# 1818        98386.0  
#[Out]# 1829        46058.0  
#[Out]# 1914         1545.0  
#[Out]# 1925        32007.0  
#[Out]# 2010        77121.0  
#[Out]# 2021        42146.0  
#[Out]# 2106       268601.0  
#[Out]# 2117        84904.0  
#[Out]# 2202         9615.0  
#[Out]# 2213        42769.0  
#[Out]# 2298        71303.0  
#[Out]# 2309        24231.0  
#[Out]# 2394        65503.0  
#[Out]# 2405        97818.0  
#[Out]# 2490         3515.0  
data2010.head()
#[Out]#     state/region   ages  year  population       state  area (sq. mi)
#[Out]# 3             AL  total  2010   4785570.0     Alabama        52423.0
#[Out]# 91            AK  total  2010    713868.0      Alaska       656425.0
#[Out]# 101           AZ  total  2010   6408790.0     Arizona       114006.0
#[Out]# 189           AR  total  2010   2922280.0    Arkansas        53182.0
#[Out]# 197           CA  total  2010  37333601.0  California       163707.0
data2010.set_index('state',inplace=True)
data2010.head()
#[Out]#            state/region   ages  year  population  area (sq. mi)
#[Out]# state                                                          
#[Out]# Alabama              AL  total  2010   4785570.0        52423.0
#[Out]# Alaska               AK  total  2010    713868.0       656425.0
#[Out]# Arizona              AZ  total  2010   6408790.0       114006.0
#[Out]# Arkansas             AR  total  2010   2922280.0        53182.0
#[Out]# California           CA  total  2010  37333601.0       163707.0
density = data2010['population'] / data2010['area (sq. mi)']
density.sort_values(ascending=False,inplace=True)
density.head()
#[Out]# state
#[Out]# District of Columbia    8898.897059
#[Out]# Puerto Rico             1058.665149
#[Out]# New Jersey              1009.253268
#[Out]# Rhode Island             681.339159
#[Out]# Connecticut              645.600649
#[Out]# dtype: float64
density.tail()
#[Out]# state
#[Out]# South Dakota    10.583512
#[Out]# North Dakota     9.537565
#[Out]# Montana          6.736171
#[Out]# Wyoming          5.768079
#[Out]# Alaska           1.087509
#[Out]# dtype: float64
import time
time.now()
time.now
get_ipython().run_line_magic('pinfo', 'time')
time.gmtime
#[Out]# <function time.gmtime>
time.localtime
#[Out]# <function time.localtime>
print(time.localtime)
now
now()
import datetime
datetime.date
#[Out]# datetime.date
datetime.now
import seaborn as sns
planets = sns.load_dataset('planets')
planets.shape
#[Out]# (1035, 6)
planets.head()
#[Out]#             method  number  orbital_period   mass  distance  year
#[Out]# 0  Radial Velocity       1         269.300   7.10     77.40  2006
#[Out]# 1  Radial Velocity       1         874.774   2.21     56.95  2008
#[Out]# 2  Radial Velocity       1         763.000   2.60     19.84  2011
#[Out]# 3  Radial Velocity       1         326.030  19.40    110.62  2007
#[Out]# 4  Radial Velocity       1         516.220  10.50    119.47  2009
rng = np.random.RandomState(42)
ser = pd.Series(rng.rand(5))
ser
#[Out]# 0    0.374540
#[Out]# 1    0.950714
#[Out]# 2    0.731994
#[Out]# 3    0.598658
#[Out]# 4    0.156019
#[Out]# dtype: float64
ser.sum()
#[Out]# 2.811925491708157
ser.mean()
#[Out]# 0.5623850983416314
df = pd.DataFrame({'A':rng.rand(5),'B':rng.rand(5)}})
df = pd.DataFrame({'A':rng.rand(5),'B':rng.rand(5)})
df
#[Out]#           A         B
#[Out]# 0  0.155995  0.020584
#[Out]# 1  0.058084  0.969910
#[Out]# 2  0.866176  0.832443
#[Out]# 3  0.601115  0.212339
#[Out]# 4  0.708073  0.181825
df.mean()
#[Out]# A    0.477888
#[Out]# B    0.443420
#[Out]# dtype: float64
df.mean(axis='column')
df.mean(axis=1)
#[Out]# 0    0.088290
#[Out]# 1    0.513997
#[Out]# 2    0.849309
#[Out]# 3    0.406727
#[Out]# 4    0.444949
#[Out]# dtype: float64
planets.dropna().describe()
#[Out]#           number  orbital_period        mass    distance         year
#[Out]# count  498.00000      498.000000  498.000000  498.000000   498.000000
#[Out]# mean     1.73494      835.778671    2.509320   52.068213  2007.377510
#[Out]# std      1.17572     1469.128259    3.636274   46.596041     4.167284
#[Out]# min      1.00000        1.328300    0.003600    1.350000  1989.000000
#[Out]# 25%      1.00000       38.272250    0.212500   24.497500  2005.000000
#[Out]# 50%      1.00000      357.000000    1.245000   39.940000  2009.000000
#[Out]# 75%      2.00000      999.600000    2.867500   59.332500  2011.000000
#[Out]# max      6.00000    17337.500000   25.000000  354.000000  2014.000000
planets.first()
planets.first(axis=1)
df = pd.DataFrame({'key':['a','b','c','a','b','c'].'data':range(6)},columns=['key','data'])
df = pd.DataFrame({'key':['a','b','c','a','b','c'],'data':range(6)},columns=['key','data'])
df
#[Out]#   key  data
#[Out]# 0   a     0
#[Out]# 1   b     1
#[Out]# 2   c     2
#[Out]# 3   a     3
#[Out]# 4   b     4
#[Out]# 5   c     5
df.groupby('key')
#[Out]# <pandas.core.groupby.DataFrameGroupBy object at 0x000001D97BACAC18>
df.groupby('key').sum()
#[Out]#      data
#[Out]# key      
#[Out]# a       3
#[Out]# b       5
#[Out]# c       7
planets.groupby('method')
#[Out]# <pandas.core.groupby.DataFrameGroupBy object at 0x000001D97BB77A58>
planets.groupby('method')['orbital_period']
#[Out]# <pandas.core.groupby.SeriesGroupBy object at 0x000001D97B9CD6A0>
planets.groupby('method')['orbital_period]].median()
planets.groupby('method')['orbital_period'].median()
#[Out]# method
#[Out]# Astrometry                         631.180000
#[Out]# Eclipse Timing Variations         4343.500000
#[Out]# Imaging                          27500.000000
#[Out]# Microlensing                      3300.000000
#[Out]# Orbital Brightness Modulation        0.342887
#[Out]# Pulsar Timing                       66.541900
#[Out]# Pulsation Timing Variations       1170.000000
#[Out]# Radial Velocity                    360.200000
#[Out]# Transit                              5.714932
#[Out]# Transit Timing Variations           57.011000
#[Out]# Name: orbital_period, dtype: float64
for (method,group) in planets.groupby('method'):
    print('{0:.30s' shape = {1} '.format(method,group.shape))
for (method,group) in planets.groupby('method'):
    print('{0:.30s} shape = {1} '.format(method,group.shape))
    
planets.groupby('method')['year'].describe().unstack()
#[Out]#        method                       
#[Out]# count  Astrometry                          2.000000
#[Out]#        Eclipse Timing Variations           9.000000
#[Out]#        Imaging                            38.000000
#[Out]#        Microlensing                       23.000000
#[Out]#        Orbital Brightness Modulation       3.000000
#[Out]#        Pulsar Timing                       5.000000
#[Out]#        Pulsation Timing Variations         1.000000
#[Out]#        Radial Velocity                   553.000000
#[Out]#        Transit                           397.000000
#[Out]#        Transit Timing Variations           4.000000
#[Out]# mean   Astrometry                       2011.500000
#[Out]#        Eclipse Timing Variations        2010.000000
#[Out]#        Imaging                          2009.131579
#[Out]#        Microlensing                     2009.782609
#[Out]#        Orbital Brightness Modulation    2011.666667
#[Out]#        Pulsar Timing                    1998.400000
#[Out]#        Pulsation Timing Variations      2007.000000
#[Out]#        Radial Velocity                  2007.518987
#[Out]#        Transit                          2011.236776
#[Out]#        Transit Timing Variations        2012.500000
#[Out]# std    Astrometry                          2.121320
#[Out]#        Eclipse Timing Variations           1.414214
#[Out]#        Imaging                             2.781901
#[Out]#        Microlensing                        2.859697
#[Out]#        Orbital Brightness Modulation       1.154701
#[Out]#        Pulsar Timing                       8.384510
#[Out]#        Pulsation Timing Variations              NaN
#[Out]#        Radial Velocity                     4.249052
#[Out]#        Transit                             2.077867
#[Out]#        Transit Timing Variations           1.290994
#[Out]#                                            ...     
#[Out]# 50%    Astrometry                       2011.500000
#[Out]#        Eclipse Timing Variations        2010.000000
#[Out]#        Imaging                          2009.000000
#[Out]#        Microlensing                     2010.000000
#[Out]#        Orbital Brightness Modulation    2011.000000
#[Out]#        Pulsar Timing                    1994.000000
#[Out]#        Pulsation Timing Variations      2007.000000
#[Out]#        Radial Velocity                  2009.000000
#[Out]#        Transit                          2012.000000
#[Out]#        Transit Timing Variations        2012.500000
#[Out]# 75%    Astrometry                       2012.250000
#[Out]#        Eclipse Timing Variations        2011.000000
#[Out]#        Imaging                          2011.000000
#[Out]#        Microlensing                     2012.000000
#[Out]#        Orbital Brightness Modulation    2012.000000
#[Out]#        Pulsar Timing                    2003.000000
#[Out]#        Pulsation Timing Variations      2007.000000
#[Out]#        Radial Velocity                  2011.000000
#[Out]#        Transit                          2013.000000
#[Out]#        Transit Timing Variations        2013.250000
#[Out]# max    Astrometry                       2013.000000
#[Out]#        Eclipse Timing Variations        2012.000000
#[Out]#        Imaging                          2013.000000
#[Out]#        Microlensing                     2013.000000
#[Out]#        Orbital Brightness Modulation    2013.000000
#[Out]#        Pulsar Timing                    2011.000000
#[Out]#        Pulsation Timing Variations      2007.000000
#[Out]#        Radial Velocity                  2014.000000
#[Out]#        Transit                          2014.000000
#[Out]#        Transit Timing Variations        2014.000000
#[Out]# Length: 80, dtype: float64
planets.groupby('method')['year'].describe()
#[Out]#                                count         mean       std     min      25%  \
#[Out]# method                                                                         
#[Out]# Astrometry                       2.0  2011.500000  2.121320  2010.0  2010.75   
#[Out]# Eclipse Timing Variations        9.0  2010.000000  1.414214  2008.0  2009.00   
#[Out]# Imaging                         38.0  2009.131579  2.781901  2004.0  2008.00   
#[Out]# Microlensing                    23.0  2009.782609  2.859697  2004.0  2008.00   
#[Out]# Orbital Brightness Modulation    3.0  2011.666667  1.154701  2011.0  2011.00   
#[Out]# Pulsar Timing                    5.0  1998.400000  8.384510  1992.0  1992.00   
#[Out]# Pulsation Timing Variations      1.0  2007.000000       NaN  2007.0  2007.00   
#[Out]# Radial Velocity                553.0  2007.518987  4.249052  1989.0  2005.00   
#[Out]# Transit                        397.0  2011.236776  2.077867  2002.0  2010.00   
#[Out]# Transit Timing Variations        4.0  2012.500000  1.290994  2011.0  2011.75   
#[Out]# 
#[Out]#                                   50%      75%     max  
#[Out]# method                                                  
#[Out]# Astrometry                     2011.5  2012.25  2013.0  
#[Out]# Eclipse Timing Variations      2010.0  2011.00  2012.0  
#[Out]# Imaging                        2009.0  2011.00  2013.0  
#[Out]# Microlensing                   2010.0  2012.00  2013.0  
#[Out]# Orbital Brightness Modulation  2011.0  2012.00  2013.0  
#[Out]# Pulsar Timing                  1994.0  2003.00  2011.0  
#[Out]# Pulsation Timing Variations    2007.0  2007.00  2007.0  
#[Out]# Radial Velocity                2009.0  2011.00  2014.0  
#[Out]# Transit                        2012.0  2013.00  2014.0  
#[Out]# Transit Timing Variations      2012.5  2013.25  2014.0  
planets.columns
#[Out]# Index(['method', 'number', 'orbital_period', 'mass', 'distance', 'year'], dtype='object')
df =pd.DataFrame({'key':['a','b','c','a','b','c'],'data1':range(6),'data2':rng.randint(0,10,6)},columns=['key','data1','data2'])
df
#[Out]#   key  data1  data2
#[Out]# 0   a      0      4
#[Out]# 1   b      1      0
#[Out]# 2   c      2      9
#[Out]# 3   a      3      5
#[Out]# 4   b      4      8
#[Out]# 5   c      5      0
df.groupby('key').aggregate(['min',np.median,max])
#[Out]#     data1            data2           
#[Out]#       min median max   min median max
#[Out]# key                                  
#[Out]# a       0    1.5   3     4    4.5   5
#[Out]# b       1    2.5   4     0    4.0   8
#[Out]# c       2    3.5   5     0    4.5   9
df.groupby('key').aggregate({'data1':'min','data2':'max'})
#[Out]#      data1  data2
#[Out]# key              
#[Out]# a        0      5
#[Out]# b        1      8
#[Out]# c        2      9
def filter_func(x):
    return x['data2'].std() > 4
df.groupby('key').std()
#[Out]#        data1     data2
#[Out]# key                   
#[Out]# a    2.12132  0.707107
#[Out]# b    2.12132  5.656854
#[Out]# c    2.12132  6.363961
df.groupby('key').filter(filter_func)
#[Out]#   key  data1  data2
#[Out]# 1   b      1      0
#[Out]# 2   c      2      9
#[Out]# 4   b      4      8
#[Out]# 5   c      5      0
df.groupby('key').transform(lambda x:x-x.mean())
#[Out]#    data1  data2
#[Out]# 0   -1.5   -0.5
#[Out]# 1   -1.5   -4.0
#[Out]# 2   -1.5    4.5
#[Out]# 3    1.5    0.5
#[Out]# 4    1.5    4.0
#[Out]# 5    1.5   -4.5
L = [0,1,0,1,2,0]
df.groupby(L).sum()
#[Out]#    data1  data2
#[Out]# 0      7     13
#[Out]# 1      4      5
#[Out]# 2      4      8
df
#[Out]#   key  data1  data2
#[Out]# 0   a      0      4
#[Out]# 1   b      1      0
#[Out]# 2   c      2      9
#[Out]# 3   a      3      5
#[Out]# 4   b      4      8
#[Out]# 5   c      5      0
df.groupby(df['key']).sum()
#[Out]#      data1  data2
#[Out]# key              
#[Out]# a        3      9
#[Out]# b        5      8
#[Out]# c        7      9
df2
#[Out]#   employee  group
#[Out]# 0      Bob   2004
#[Out]# 1     Jake   2008
#[Out]# 2     Lisa   2012
#[Out]# 3      Sue   2014
df2 = df.set_index('key')
df
#[Out]#   key  data1  data2
#[Out]# 0   a      0      4
#[Out]# 1   b      1      0
#[Out]# 2   c      2      9
#[Out]# 3   a      3      5
#[Out]# 4   b      4      8
#[Out]# 5   c      5      0
df2
#[Out]#      data1  data2
#[Out]# key              
#[Out]# a        0      4
#[Out]# b        1      0
#[Out]# c        2      9
#[Out]# a        3      5
#[Out]# b        4      8
#[Out]# c        5      0
mapping = {'a','vowel','b':'consonant','c':'consonant'}
mapping = {'a','vowel','b':'consonant','c':'consonant'}
mapping = {'a':'vowel','b':'consonant','c':'consonant'}
df2.groupby(mapping).sum()
#[Out]#            data1  data2
#[Out]# consonant     12     17
#[Out]# vowel          3      9
df2.groupby(str.lower).mean()
#[Out]#    data1  data2
#[Out]# a    1.5    4.5
#[Out]# b    2.5    4.0
#[Out]# c    3.5    4.5
df2
#[Out]#      data1  data2
#[Out]# key              
#[Out]# a        0      4
#[Out]# b        1      0
#[Out]# c        2      9
#[Out]# a        3      5
#[Out]# b        4      8
#[Out]# c        5      0
df2.groupby([str.lower,mapping]).mean()
#[Out]#              data1  data2
#[Out]# a vowel        1.5    4.5
#[Out]# b consonant    2.5    4.0
#[Out]# c consonant    3.5    4.5
decade = 10 * (planets['year'] //10)
decade = decade.astype(str) + 's'
decade.name = 'decade'
planets.groupby(['method',decade])['
planets.groupby(['method',decade])['number'].sum().unstack()
#[Out]# decade                         1980s  1990s  2000s  2010s
#[Out]# method                                                   
#[Out]# Astrometry                       NaN    NaN    NaN    2.0
#[Out]# Eclipse Timing Variations        NaN    NaN    5.0   10.0
#[Out]# Imaging                          NaN    NaN   29.0   21.0
#[Out]# Microlensing                     NaN    NaN   12.0   15.0
#[Out]# Orbital Brightness Modulation    NaN    NaN    NaN    5.0
#[Out]# Pulsar Timing                    NaN    9.0    1.0    1.0
#[Out]# Pulsation Timing Variations      NaN    NaN    1.0    NaN
#[Out]# Radial Velocity                  1.0   52.0  475.0  424.0
#[Out]# Transit                          NaN    NaN   64.0  712.0
#[Out]# Transit Timing Variations        NaN    NaN    NaN    9.0
get_ipython().run_line_magic('logstop', '')
