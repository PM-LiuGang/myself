# IPython log file

import pandas as pd
import numpy as np
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],'hire_date': [2004, 2008, 2012, 2014]})
df
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
df3 = pd.merge(df1,df2)
df3
#[Out]#   employee        group  hire_date
#[Out]# 0      Bob   Accounting       2008
#[Out]# 1     Jake  Engineering       2012
#[Out]# 2     Lisa  Engineering       2004
#[Out]# 3      Sue           HR       2014
get_ipython().run_line_magic('pinfo', 'pd.merge')
df3
#[Out]#   employee        group  hire_date
#[Out]# 0      Bob   Accounting       2008
#[Out]# 1     Jake  Engineering       2012
#[Out]# 2     Lisa  Engineering       2004
#[Out]# 3      Sue           HR       2014
pd.merge(df1,df2,how='outer')
#[Out]#   employee        group  hire_date
#[Out]# 0      Bob   Accounting       2008
#[Out]# 1     Jake  Engineering       2012
#[Out]# 2     Lisa  Engineering       2004
#[Out]# 3      Sue           HR       2014
df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],'supervisor': ['Carly', 'Guido', 'Steve']})
df3
#[Out]#   employee        group  hire_date
#[Out]# 0      Bob   Accounting       2008
#[Out]# 1     Jake  Engineering       2012
#[Out]# 2     Lisa  Engineering       2004
#[Out]# 3      Sue           HR       2014
df4
#[Out]#          group supervisor
#[Out]# 0   Accounting      Carly
#[Out]# 1  Engineering      Guido
#[Out]# 2           HR      Steve
pd.merge(df3,df4)
#[Out]#   employee        group  hire_date supervisor
#[Out]# 0      Bob   Accounting       2008      Carly
#[Out]# 1     Jake  Engineering       2012      Guido
#[Out]# 2     Lisa  Engineering       2004      Guido
#[Out]# 3      Sue           HR       2014      Steve
df5 = pd.DataFrame({'group': ['Accounting', 'Accounting','Engineering', 'Engineering', 'HR', 'HR'],'skills': ['math', 'spreadsheets', 'coding', 'linux','spreadsheets', 'organization']})
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
df5
#[Out]#          group        skills
#[Out]# 0   Accounting          math
#[Out]# 1   Accounting  spreadsheets
#[Out]# 2  Engineering        coding
#[Out]# 3  Engineering         linux
#[Out]# 4           HR  spreadsheets
#[Out]# 5           HR  organization
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
df1.columns
#[Out]# Index(['employee', 'group'], dtype='object')
df2.columns
#[Out]# Index(['employee', 'hire_date'], dtype='object')
pd.merge(df1,df2,on='employee')
#[Out]#   employee        group  hire_date
#[Out]# 0      Bob   Accounting       2008
#[Out]# 1     Jake  Engineering       2012
#[Out]# 2     Lisa  Engineering       2004
#[Out]# 3      Sue           HR       2014
get_ipython().run_line_magic('cd', 'c')
get_ipython().run_line_magic('ls', '')
df1
#[Out]#   employee        group
#[Out]# 0      Bob   Accounting
#[Out]# 1     Jake  Engineering
#[Out]# 2     Lisa  Engineering
#[Out]# 3      Sue           HR
df3
#[Out]#   employee        group  hire_date
#[Out]# 0      Bob   Accounting       2008
#[Out]# 1     Jake  Engineering       2012
#[Out]# 2     Lisa  Engineering       2004
#[Out]# 3      Sue           HR       2014
df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],'salary': [70000, 80000, 120000, 90000]})
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
pd.merge(df1,df3,left_on='employee',right_on='name')
#[Out]#   employee        group  name  salary
#[Out]# 0      Bob   Accounting   Bob   70000
#[Out]# 1     Jake  Engineering  Jake   80000
#[Out]# 2     Lisa  Engineering  Lisa  120000
#[Out]# 3      Sue           HR   Sue   90000
pd.merge(df1,df3,left_on='employee',right_on='name').drop('name',all)
pd.merge(df1,df3,left_on='employee',right_on='name').drop('name')
pd.merge(df1,df3,left_on='employee',right_on='name').drop('name',axis=1)
#[Out]#   employee        group  salary
#[Out]# 0      Bob   Accounting   70000
#[Out]# 1     Jake  Engineering   80000
#[Out]# 2     Lisa  Engineering  120000
#[Out]# 3      Sue           HR   90000
df1a
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
df1a = df1.set_index('employee')
df2a = df2.set_index('employee')
df1a
#[Out]#                 group
#[Out]# employee             
#[Out]# Bob        Accounting
#[Out]# Jake      Engineering
#[Out]# Lisa      Engineering
#[Out]# Sue                HR
df2a
#[Out]#           hire_date
#[Out]# employee           
#[Out]# Lisa           2004
#[Out]# Bob            2008
#[Out]# Jake           2012
#[Out]# Sue            2014
pd.merge(df1a,df2a,left_index=True,right_index=True)
#[Out]#                 group  hire_date
#[Out]# employee                        
#[Out]# Bob        Accounting       2008
#[Out]# Jake      Engineering       2012
#[Out]# Lisa      Engineering       2004
#[Out]# Sue                HR       2014
df1a
#[Out]#                 group
#[Out]# employee             
#[Out]# Bob        Accounting
#[Out]# Jake      Engineering
#[Out]# Lisa      Engineering
#[Out]# Sue                HR
df2a
#[Out]#           hire_date
#[Out]# employee           
#[Out]# Lisa           2004
#[Out]# Bob            2008
#[Out]# Jake           2012
#[Out]# Sue            2014
df1a.join(df2a)
#[Out]#                 group  hire_date
#[Out]# employee                        
#[Out]# Bob        Accounting       2008
#[Out]# Jake      Engineering       2012
#[Out]# Lisa      Engineering       2004
#[Out]# Sue                HR       2014
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
df6 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],'food': ['fish', 'beans', 'bread']},columns=['name', 'food'])
df7 = pd.DataFrame({'name': ['Mary', 'Joseph'],'drink': ['wine', 'beer']},columns=['name', 'drink'])
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
pd.merge(df6,df7,how='right')
#[Out]#      name   food drink
#[Out]# 0    Mary  bread  wine
#[Out]# 1  Joseph    NaN  beer
df7
#[Out]#      name drink
#[Out]# 0    Mary  wine
#[Out]# 1  Joseph  beer
df8 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],'rank': [1, 2, 3, 4]})
df9 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],'rank': [3, 1, 4, 2]})
pd.merge(df8,df9,on='name')
#[Out]#    name  rank_x  rank_y
#[Out]# 0   Bob       1       3
#[Out]# 1  Jake       2       1
#[Out]# 2  Lisa       3       4
#[Out]# 3   Sue       4       2
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
pd.merge(df8,df9,on='name',suffixes=['_L
pd.merge(df8,df9,on='name',suffixes=['_L','_R'])
#[Out]#    name  rank_L  rank_R
#[Out]# 0   Bob       1       3
#[Out]# 1  Jake       2       1
#[Out]# 2  Lisa       3       4
#[Out]# 3   Sue       4       2
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', 'data/')
get_ipython().run_line_magic('ls', '')
pop = pd.read_csv('state-population.csv')
areas = pd.read_csv('state-areas.csv')
abbrevs = pd.read_csv('state-abbrevs.csv')
pop.head()
#[Out]#   state/region     ages  year  population
#[Out]# 0           AL  under18  2012   1117489.0
#[Out]# 1           AL    total  2012   4817528.0
#[Out]# 2           AL  under18  2010   1130966.0
#[Out]# 3           AL    total  2010   4785570.0
#[Out]# 4           AL  under18  2011   1125763.0
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
pd.merge(pop,abbrevs,left_on='state/region',right_on='abbreviation',how=inner')
pd.merge(pop,abbrevs,left_on='state/region',right_on='abbreviation',how='inner')
#[Out]#      state/region     ages  year  population    state abbreviation
#[Out]# 0              AL  under18  2012   1117489.0  Alabama           AL
#[Out]# 1              AL    total  2012   4817528.0  Alabama           AL
#[Out]# 2              AL  under18  2010   1130966.0  Alabama           AL
#[Out]# 3              AL    total  2010   4785570.0  Alabama           AL
#[Out]# 4              AL  under18  2011   1125763.0  Alabama           AL
#[Out]# 5              AL    total  2011   4801627.0  Alabama           AL
#[Out]# 6              AL    total  2009   4757938.0  Alabama           AL
#[Out]# 7              AL  under18  2009   1134192.0  Alabama           AL
#[Out]# 8              AL  under18  2013   1111481.0  Alabama           AL
#[Out]# 9              AL    total  2013   4833722.0  Alabama           AL
#[Out]# 10             AL    total  2007   4672840.0  Alabama           AL
#[Out]# 11             AL  under18  2007   1132296.0  Alabama           AL
#[Out]# 12             AL    total  2008   4718206.0  Alabama           AL
#[Out]# 13             AL  under18  2008   1134927.0  Alabama           AL
#[Out]# 14             AL    total  2005   4569805.0  Alabama           AL
#[Out]# 15             AL  under18  2005   1117229.0  Alabama           AL
#[Out]# 16             AL    total  2006   4628981.0  Alabama           AL
#[Out]# 17             AL  under18  2006   1126798.0  Alabama           AL
#[Out]# 18             AL    total  2004   4530729.0  Alabama           AL
#[Out]# 19             AL  under18  2004   1113662.0  Alabama           AL
#[Out]# 20             AL    total  2003   4503491.0  Alabama           AL
#[Out]# 21             AL  under18  2003   1113083.0  Alabama           AL
#[Out]# 22             AL    total  2001   4467634.0  Alabama           AL
#[Out]# 23             AL  under18  2001   1120409.0  Alabama           AL
#[Out]# 24             AL    total  2002   4480089.0  Alabama           AL
#[Out]# 25             AL  under18  2002   1116590.0  Alabama           AL
#[Out]# 26             AL  under18  1999   1121287.0  Alabama           AL
#[Out]# 27             AL    total  1999   4430141.0  Alabama           AL
#[Out]# 28             AL    total  2000   4452173.0  Alabama           AL
#[Out]# 29             AL  under18  2000   1122273.0  Alabama           AL
#[Out]# ...           ...      ...   ...         ...      ...          ...
#[Out]# 2418           WY    total  2003    503453.0  Wyoming           WY
#[Out]# 2419           WY  under18  2003    124182.0  Wyoming           WY
#[Out]# 2420           WY    total  2004    509106.0  Wyoming           WY
#[Out]# 2421           WY  under18  2004    123974.0  Wyoming           WY
#[Out]# 2422           WY    total  2002    500017.0  Wyoming           WY
#[Out]# 2423           WY  under18  2002    125495.0  Wyoming           WY
#[Out]# 2424           WY    total  2001    494657.0  Wyoming           WY
#[Out]# 2425           WY  under18  2001    126212.0  Wyoming           WY
#[Out]# 2426           WY    total  2000    494300.0  Wyoming           WY
#[Out]# 2427           WY  under18  2000    128774.0  Wyoming           WY
#[Out]# 2428           WY    total  1999    491780.0  Wyoming           WY
#[Out]# 2429           WY  under18  1999    130793.0  Wyoming           WY
#[Out]# 2430           WY    total  1997    489452.0  Wyoming           WY
#[Out]# 2431           WY  under18  1997    134328.0  Wyoming           WY
#[Out]# 2432           WY  under18  1998    132602.0  Wyoming           WY
#[Out]# 2433           WY    total  1998    490787.0  Wyoming           WY
#[Out]# 2434           WY  under18  1996    135698.0  Wyoming           WY
#[Out]# 2435           WY    total  1996    488167.0  Wyoming           WY
#[Out]# 2436           WY    total  1995    485160.0  Wyoming           WY
#[Out]# 2437           WY  under18  1995    136785.0  Wyoming           WY
#[Out]# 2438           WY  under18  1994    137733.0  Wyoming           WY
#[Out]# 2439           WY    total  1994    480283.0  Wyoming           WY
#[Out]# 2440           WY  under18  1992    137308.0  Wyoming           WY
#[Out]# 2441           WY    total  1992    466251.0  Wyoming           WY
#[Out]# 2442           WY    total  1993    473081.0  Wyoming           WY
#[Out]# 2443           WY  under18  1993    137458.0  Wyoming           WY
#[Out]# 2444           WY    total  1991    459260.0  Wyoming           WY
#[Out]# 2445           WY  under18  1991    136720.0  Wyoming           WY
#[Out]# 2446           WY  under18  1990    136078.0  Wyoming           WY
#[Out]# 2447           WY    total  1990    453690.0  Wyoming           WY
#[Out]# 
#[Out]# [2448 rows x 6 columns]
pd.merge(pop,abbrevs,left_on='state/region',right_on='abbreviation',how='inner').drop('abbreviation',axis=1)
#[Out]#      state/region     ages  year  population    state
#[Out]# 0              AL  under18  2012   1117489.0  Alabama
#[Out]# 1              AL    total  2012   4817528.0  Alabama
#[Out]# 2              AL  under18  2010   1130966.0  Alabama
#[Out]# 3              AL    total  2010   4785570.0  Alabama
#[Out]# 4              AL  under18  2011   1125763.0  Alabama
#[Out]# 5              AL    total  2011   4801627.0  Alabama
#[Out]# 6              AL    total  2009   4757938.0  Alabama
#[Out]# 7              AL  under18  2009   1134192.0  Alabama
#[Out]# 8              AL  under18  2013   1111481.0  Alabama
#[Out]# 9              AL    total  2013   4833722.0  Alabama
#[Out]# 10             AL    total  2007   4672840.0  Alabama
#[Out]# 11             AL  under18  2007   1132296.0  Alabama
#[Out]# 12             AL    total  2008   4718206.0  Alabama
#[Out]# 13             AL  under18  2008   1134927.0  Alabama
#[Out]# 14             AL    total  2005   4569805.0  Alabama
#[Out]# 15             AL  under18  2005   1117229.0  Alabama
#[Out]# 16             AL    total  2006   4628981.0  Alabama
#[Out]# 17             AL  under18  2006   1126798.0  Alabama
#[Out]# 18             AL    total  2004   4530729.0  Alabama
#[Out]# 19             AL  under18  2004   1113662.0  Alabama
#[Out]# 20             AL    total  2003   4503491.0  Alabama
#[Out]# 21             AL  under18  2003   1113083.0  Alabama
#[Out]# 22             AL    total  2001   4467634.0  Alabama
#[Out]# 23             AL  under18  2001   1120409.0  Alabama
#[Out]# 24             AL    total  2002   4480089.0  Alabama
#[Out]# 25             AL  under18  2002   1116590.0  Alabama
#[Out]# 26             AL  under18  1999   1121287.0  Alabama
#[Out]# 27             AL    total  1999   4430141.0  Alabama
#[Out]# 28             AL    total  2000   4452173.0  Alabama
#[Out]# 29             AL  under18  2000   1122273.0  Alabama
#[Out]# ...           ...      ...   ...         ...      ...
#[Out]# 2418           WY    total  2003    503453.0  Wyoming
#[Out]# 2419           WY  under18  2003    124182.0  Wyoming
#[Out]# 2420           WY    total  2004    509106.0  Wyoming
#[Out]# 2421           WY  under18  2004    123974.0  Wyoming
#[Out]# 2422           WY    total  2002    500017.0  Wyoming
#[Out]# 2423           WY  under18  2002    125495.0  Wyoming
#[Out]# 2424           WY    total  2001    494657.0  Wyoming
#[Out]# 2425           WY  under18  2001    126212.0  Wyoming
#[Out]# 2426           WY    total  2000    494300.0  Wyoming
#[Out]# 2427           WY  under18  2000    128774.0  Wyoming
#[Out]# 2428           WY    total  1999    491780.0  Wyoming
#[Out]# 2429           WY  under18  1999    130793.0  Wyoming
#[Out]# 2430           WY    total  1997    489452.0  Wyoming
#[Out]# 2431           WY  under18  1997    134328.0  Wyoming
#[Out]# 2432           WY  under18  1998    132602.0  Wyoming
#[Out]# 2433           WY    total  1998    490787.0  Wyoming
#[Out]# 2434           WY  under18  1996    135698.0  Wyoming
#[Out]# 2435           WY    total  1996    488167.0  Wyoming
#[Out]# 2436           WY    total  1995    485160.0  Wyoming
#[Out]# 2437           WY  under18  1995    136785.0  Wyoming
#[Out]# 2438           WY  under18  1994    137733.0  Wyoming
#[Out]# 2439           WY    total  1994    480283.0  Wyoming
#[Out]# 2440           WY  under18  1992    137308.0  Wyoming
#[Out]# 2441           WY    total  1992    466251.0  Wyoming
#[Out]# 2442           WY    total  1993    473081.0  Wyoming
#[Out]# 2443           WY  under18  1993    137458.0  Wyoming
#[Out]# 2444           WY    total  1991    459260.0  Wyoming
#[Out]# 2445           WY  under18  1991    136720.0  Wyoming
#[Out]# 2446           WY  under18  1990    136078.0  Wyoming
#[Out]# 2447           WY    total  1990    453690.0  Wyoming
#[Out]# 
#[Out]# [2448 rows x 5 columns]
data1 = pd.merge(pop,abbrevs,left_on='state/region',right_on='abbreviation',how='inner').drop('abbreviation',axis=1)
data1.columns
#[Out]# Index(['state/region', 'ages', 'year', 'population', 'state'], dtype='object')
pd.merge(data1,areas,on='state')
#[Out]#      state/region     ages  year  population    state  area (sq. mi)
#[Out]# 0              AL  under18  2012   1117489.0  Alabama          52423
#[Out]# 1              AL    total  2012   4817528.0  Alabama          52423
#[Out]# 2              AL  under18  2010   1130966.0  Alabama          52423
#[Out]# 3              AL    total  2010   4785570.0  Alabama          52423
#[Out]# 4              AL  under18  2011   1125763.0  Alabama          52423
#[Out]# 5              AL    total  2011   4801627.0  Alabama          52423
#[Out]# 6              AL    total  2009   4757938.0  Alabama          52423
#[Out]# 7              AL  under18  2009   1134192.0  Alabama          52423
#[Out]# 8              AL  under18  2013   1111481.0  Alabama          52423
#[Out]# 9              AL    total  2013   4833722.0  Alabama          52423
#[Out]# 10             AL    total  2007   4672840.0  Alabama          52423
#[Out]# 11             AL  under18  2007   1132296.0  Alabama          52423
#[Out]# 12             AL    total  2008   4718206.0  Alabama          52423
#[Out]# 13             AL  under18  2008   1134927.0  Alabama          52423
#[Out]# 14             AL    total  2005   4569805.0  Alabama          52423
#[Out]# 15             AL  under18  2005   1117229.0  Alabama          52423
#[Out]# 16             AL    total  2006   4628981.0  Alabama          52423
#[Out]# 17             AL  under18  2006   1126798.0  Alabama          52423
#[Out]# 18             AL    total  2004   4530729.0  Alabama          52423
#[Out]# 19             AL  under18  2004   1113662.0  Alabama          52423
#[Out]# 20             AL    total  2003   4503491.0  Alabama          52423
#[Out]# 21             AL  under18  2003   1113083.0  Alabama          52423
#[Out]# 22             AL    total  2001   4467634.0  Alabama          52423
#[Out]# 23             AL  under18  2001   1120409.0  Alabama          52423
#[Out]# 24             AL    total  2002   4480089.0  Alabama          52423
#[Out]# 25             AL  under18  2002   1116590.0  Alabama          52423
#[Out]# 26             AL  under18  1999   1121287.0  Alabama          52423
#[Out]# 27             AL    total  1999   4430141.0  Alabama          52423
#[Out]# 28             AL    total  2000   4452173.0  Alabama          52423
#[Out]# 29             AL  under18  2000   1122273.0  Alabama          52423
#[Out]# ...           ...      ...   ...         ...      ...            ...
#[Out]# 2418           WY    total  2003    503453.0  Wyoming          97818
#[Out]# 2419           WY  under18  2003    124182.0  Wyoming          97818
#[Out]# 2420           WY    total  2004    509106.0  Wyoming          97818
#[Out]# 2421           WY  under18  2004    123974.0  Wyoming          97818
#[Out]# 2422           WY    total  2002    500017.0  Wyoming          97818
#[Out]# 2423           WY  under18  2002    125495.0  Wyoming          97818
#[Out]# 2424           WY    total  2001    494657.0  Wyoming          97818
#[Out]# 2425           WY  under18  2001    126212.0  Wyoming          97818
#[Out]# 2426           WY    total  2000    494300.0  Wyoming          97818
#[Out]# 2427           WY  under18  2000    128774.0  Wyoming          97818
#[Out]# 2428           WY    total  1999    491780.0  Wyoming          97818
#[Out]# 2429           WY  under18  1999    130793.0  Wyoming          97818
#[Out]# 2430           WY    total  1997    489452.0  Wyoming          97818
#[Out]# 2431           WY  under18  1997    134328.0  Wyoming          97818
#[Out]# 2432           WY  under18  1998    132602.0  Wyoming          97818
#[Out]# 2433           WY    total  1998    490787.0  Wyoming          97818
#[Out]# 2434           WY  under18  1996    135698.0  Wyoming          97818
#[Out]# 2435           WY    total  1996    488167.0  Wyoming          97818
#[Out]# 2436           WY    total  1995    485160.0  Wyoming          97818
#[Out]# 2437           WY  under18  1995    136785.0  Wyoming          97818
#[Out]# 2438           WY  under18  1994    137733.0  Wyoming          97818
#[Out]# 2439           WY    total  1994    480283.0  Wyoming          97818
#[Out]# 2440           WY  under18  1992    137308.0  Wyoming          97818
#[Out]# 2441           WY    total  1992    466251.0  Wyoming          97818
#[Out]# 2442           WY    total  1993    473081.0  Wyoming          97818
#[Out]# 2443           WY  under18  1993    137458.0  Wyoming          97818
#[Out]# 2444           WY    total  1991    459260.0  Wyoming          97818
#[Out]# 2445           WY  under18  1991    136720.0  Wyoming          97818
#[Out]# 2446           WY  under18  1990    136078.0  Wyoming          97818
#[Out]# 2447           WY    total  1990    453690.0  Wyoming          97818
#[Out]# 
#[Out]# [2448 rows x 6 columns]
pd.merge(data1,areas,on='state',how='outer')
#[Out]#      state/region     ages    year  population        state  area (sq. mi)
#[Out]# 0              AL  under18  2012.0   1117489.0      Alabama          52423
#[Out]# 1              AL    total  2012.0   4817528.0      Alabama          52423
#[Out]# 2              AL  under18  2010.0   1130966.0      Alabama          52423
#[Out]# 3              AL    total  2010.0   4785570.0      Alabama          52423
#[Out]# 4              AL  under18  2011.0   1125763.0      Alabama          52423
#[Out]# 5              AL    total  2011.0   4801627.0      Alabama          52423
#[Out]# 6              AL    total  2009.0   4757938.0      Alabama          52423
#[Out]# 7              AL  under18  2009.0   1134192.0      Alabama          52423
#[Out]# 8              AL  under18  2013.0   1111481.0      Alabama          52423
#[Out]# 9              AL    total  2013.0   4833722.0      Alabama          52423
#[Out]# 10             AL    total  2007.0   4672840.0      Alabama          52423
#[Out]# 11             AL  under18  2007.0   1132296.0      Alabama          52423
#[Out]# 12             AL    total  2008.0   4718206.0      Alabama          52423
#[Out]# 13             AL  under18  2008.0   1134927.0      Alabama          52423
#[Out]# 14             AL    total  2005.0   4569805.0      Alabama          52423
#[Out]# 15             AL  under18  2005.0   1117229.0      Alabama          52423
#[Out]# 16             AL    total  2006.0   4628981.0      Alabama          52423
#[Out]# 17             AL  under18  2006.0   1126798.0      Alabama          52423
#[Out]# 18             AL    total  2004.0   4530729.0      Alabama          52423
#[Out]# 19             AL  under18  2004.0   1113662.0      Alabama          52423
#[Out]# 20             AL    total  2003.0   4503491.0      Alabama          52423
#[Out]# 21             AL  under18  2003.0   1113083.0      Alabama          52423
#[Out]# 22             AL    total  2001.0   4467634.0      Alabama          52423
#[Out]# 23             AL  under18  2001.0   1120409.0      Alabama          52423
#[Out]# 24             AL    total  2002.0   4480089.0      Alabama          52423
#[Out]# 25             AL  under18  2002.0   1116590.0      Alabama          52423
#[Out]# 26             AL  under18  1999.0   1121287.0      Alabama          52423
#[Out]# 27             AL    total  1999.0   4430141.0      Alabama          52423
#[Out]# 28             AL    total  2000.0   4452173.0      Alabama          52423
#[Out]# 29             AL  under18  2000.0   1122273.0      Alabama          52423
#[Out]# ...           ...      ...     ...         ...          ...            ...
#[Out]# 2419           WY  under18  2003.0    124182.0      Wyoming          97818
#[Out]# 2420           WY    total  2004.0    509106.0      Wyoming          97818
#[Out]# 2421           WY  under18  2004.0    123974.0      Wyoming          97818
#[Out]# 2422           WY    total  2002.0    500017.0      Wyoming          97818
#[Out]# 2423           WY  under18  2002.0    125495.0      Wyoming          97818
#[Out]# 2424           WY    total  2001.0    494657.0      Wyoming          97818
#[Out]# 2425           WY  under18  2001.0    126212.0      Wyoming          97818
#[Out]# 2426           WY    total  2000.0    494300.0      Wyoming          97818
#[Out]# 2427           WY  under18  2000.0    128774.0      Wyoming          97818
#[Out]# 2428           WY    total  1999.0    491780.0      Wyoming          97818
#[Out]# 2429           WY  under18  1999.0    130793.0      Wyoming          97818
#[Out]# 2430           WY    total  1997.0    489452.0      Wyoming          97818
#[Out]# 2431           WY  under18  1997.0    134328.0      Wyoming          97818
#[Out]# 2432           WY  under18  1998.0    132602.0      Wyoming          97818
#[Out]# 2433           WY    total  1998.0    490787.0      Wyoming          97818
#[Out]# 2434           WY  under18  1996.0    135698.0      Wyoming          97818
#[Out]# 2435           WY    total  1996.0    488167.0      Wyoming          97818
#[Out]# 2436           WY    total  1995.0    485160.0      Wyoming          97818
#[Out]# 2437           WY  under18  1995.0    136785.0      Wyoming          97818
#[Out]# 2438           WY  under18  1994.0    137733.0      Wyoming          97818
#[Out]# 2439           WY    total  1994.0    480283.0      Wyoming          97818
#[Out]# 2440           WY  under18  1992.0    137308.0      Wyoming          97818
#[Out]# 2441           WY    total  1992.0    466251.0      Wyoming          97818
#[Out]# 2442           WY    total  1993.0    473081.0      Wyoming          97818
#[Out]# 2443           WY  under18  1993.0    137458.0      Wyoming          97818
#[Out]# 2444           WY    total  1991.0    459260.0      Wyoming          97818
#[Out]# 2445           WY  under18  1991.0    136720.0      Wyoming          97818
#[Out]# 2446           WY  under18  1990.0    136078.0      Wyoming          97818
#[Out]# 2447           WY    total  1990.0    453690.0      Wyoming          97818
#[Out]# 2448          NaN      NaN     NaN         NaN  Puerto Rico           3515
#[Out]# 
#[Out]# [2449 rows x 6 columns]
data2 = pd.merge(data1,areas,on='state',how='outer')
data2.dropna(axis=0)
#[Out]#      state/region     ages    year  population    state  area (sq. mi)
#[Out]# 0              AL  under18  2012.0   1117489.0  Alabama          52423
#[Out]# 1              AL    total  2012.0   4817528.0  Alabama          52423
#[Out]# 2              AL  under18  2010.0   1130966.0  Alabama          52423
#[Out]# 3              AL    total  2010.0   4785570.0  Alabama          52423
#[Out]# 4              AL  under18  2011.0   1125763.0  Alabama          52423
#[Out]# 5              AL    total  2011.0   4801627.0  Alabama          52423
#[Out]# 6              AL    total  2009.0   4757938.0  Alabama          52423
#[Out]# 7              AL  under18  2009.0   1134192.0  Alabama          52423
#[Out]# 8              AL  under18  2013.0   1111481.0  Alabama          52423
#[Out]# 9              AL    total  2013.0   4833722.0  Alabama          52423
#[Out]# 10             AL    total  2007.0   4672840.0  Alabama          52423
#[Out]# 11             AL  under18  2007.0   1132296.0  Alabama          52423
#[Out]# 12             AL    total  2008.0   4718206.0  Alabama          52423
#[Out]# 13             AL  under18  2008.0   1134927.0  Alabama          52423
#[Out]# 14             AL    total  2005.0   4569805.0  Alabama          52423
#[Out]# 15             AL  under18  2005.0   1117229.0  Alabama          52423
#[Out]# 16             AL    total  2006.0   4628981.0  Alabama          52423
#[Out]# 17             AL  under18  2006.0   1126798.0  Alabama          52423
#[Out]# 18             AL    total  2004.0   4530729.0  Alabama          52423
#[Out]# 19             AL  under18  2004.0   1113662.0  Alabama          52423
#[Out]# 20             AL    total  2003.0   4503491.0  Alabama          52423
#[Out]# 21             AL  under18  2003.0   1113083.0  Alabama          52423
#[Out]# 22             AL    total  2001.0   4467634.0  Alabama          52423
#[Out]# 23             AL  under18  2001.0   1120409.0  Alabama          52423
#[Out]# 24             AL    total  2002.0   4480089.0  Alabama          52423
#[Out]# 25             AL  under18  2002.0   1116590.0  Alabama          52423
#[Out]# 26             AL  under18  1999.0   1121287.0  Alabama          52423
#[Out]# 27             AL    total  1999.0   4430141.0  Alabama          52423
#[Out]# 28             AL    total  2000.0   4452173.0  Alabama          52423
#[Out]# 29             AL  under18  2000.0   1122273.0  Alabama          52423
#[Out]# ...           ...      ...     ...         ...      ...            ...
#[Out]# 2418           WY    total  2003.0    503453.0  Wyoming          97818
#[Out]# 2419           WY  under18  2003.0    124182.0  Wyoming          97818
#[Out]# 2420           WY    total  2004.0    509106.0  Wyoming          97818
#[Out]# 2421           WY  under18  2004.0    123974.0  Wyoming          97818
#[Out]# 2422           WY    total  2002.0    500017.0  Wyoming          97818
#[Out]# 2423           WY  under18  2002.0    125495.0  Wyoming          97818
#[Out]# 2424           WY    total  2001.0    494657.0  Wyoming          97818
#[Out]# 2425           WY  under18  2001.0    126212.0  Wyoming          97818
#[Out]# 2426           WY    total  2000.0    494300.0  Wyoming          97818
#[Out]# 2427           WY  under18  2000.0    128774.0  Wyoming          97818
#[Out]# 2428           WY    total  1999.0    491780.0  Wyoming          97818
#[Out]# 2429           WY  under18  1999.0    130793.0  Wyoming          97818
#[Out]# 2430           WY    total  1997.0    489452.0  Wyoming          97818
#[Out]# 2431           WY  under18  1997.0    134328.0  Wyoming          97818
#[Out]# 2432           WY  under18  1998.0    132602.0  Wyoming          97818
#[Out]# 2433           WY    total  1998.0    490787.0  Wyoming          97818
#[Out]# 2434           WY  under18  1996.0    135698.0  Wyoming          97818
#[Out]# 2435           WY    total  1996.0    488167.0  Wyoming          97818
#[Out]# 2436           WY    total  1995.0    485160.0  Wyoming          97818
#[Out]# 2437           WY  under18  1995.0    136785.0  Wyoming          97818
#[Out]# 2438           WY  under18  1994.0    137733.0  Wyoming          97818
#[Out]# 2439           WY    total  1994.0    480283.0  Wyoming          97818
#[Out]# 2440           WY  under18  1992.0    137308.0  Wyoming          97818
#[Out]# 2441           WY    total  1992.0    466251.0  Wyoming          97818
#[Out]# 2442           WY    total  1993.0    473081.0  Wyoming          97818
#[Out]# 2443           WY  under18  1993.0    137458.0  Wyoming          97818
#[Out]# 2444           WY    total  1991.0    459260.0  Wyoming          97818
#[Out]# 2445           WY  under18  1991.0    136720.0  Wyoming          97818
#[Out]# 2446           WY  under18  1990.0    136078.0  Wyoming          97818
#[Out]# 2447           WY    total  1990.0    453690.0  Wyoming          97818
#[Out]# 
#[Out]# [2448 rows x 6 columns]
datana = data2.dropna(axis=0)
datana.columns
#[Out]# Index(['state/region', 'ages', 'year', 'population', 'state', 'area (sq. mi)'], dtype='object')
datana.groupby('state/region','ages')
datana.groupby['state/region','ages']
datana.groupby['state/region']
datana.columns
#[Out]# Index(['state/region', 'ages', 'year', 'population', 'state', 'area (sq. mi)'], dtype='object')
datana.groupby('state/region')
#[Out]# <pandas.core.groupby.DataFrameGroupBy object at 0x000001D079CFCD68>
get_ipython().run_line_magic('pinfo', 'datana.groupby')
datana.head()
#[Out]#   state/region     ages    year  population    state  area (sq. mi)
#[Out]# 0           AL  under18  2012.0   1117489.0  Alabama          52423
#[Out]# 1           AL    total  2012.0   4817528.0  Alabama          52423
#[Out]# 2           AL  under18  2010.0   1130966.0  Alabama          52423
#[Out]# 3           AL    total  2010.0   4785570.0  Alabama          52423
#[Out]# 4           AL  under18  2011.0   1125763.0  Alabama          52423
datana.groupby(['state/region','ages'])['population'].sum()
#[Out]# state/region  ages   
#[Out]# AK            total       15508916.0
#[Out]#               under18      4480151.0
#[Out]# AL            total      107628669.0
#[Out]#               under18     26668729.0
#[Out]# AR            total       64636264.0
#[Out]#               under18     16322457.0
#[Out]# AZ            total      127070396.0
#[Out]#               under18     33133307.0
#[Out]# CA            total      824019294.0
#[Out]#               under18    218016486.0
#[Out]# CO            total      104625437.0
#[Out]#               under18     26309111.0
#[Out]# CT            total       82581666.0
#[Out]#               under18     19583558.0
#[Out]# DC            total       14089663.0
#[Out]#               under18      2693696.0
#[Out]# DE            total       19271338.0
#[Out]#               under18      4628827.0
#[Out]# FL            total      395917024.0
#[Out]#               under18     88073114.0
#[Out]# GA            total      201035593.0
#[Out]#               under18     52664609.0
#[Out]# HI            total       30142654.0
#[Out]#               under18      7207296.0
#[Out]# IA            total       70510466.0
#[Out]#               under18     17415387.0
#[Out]# ID            total       32084316.0
#[Out]#               under18      9081685.0
#[Out]# IL            total      296899117.0
#[Out]#               under18     75470606.0
#[Out]#                             ...     
#[Out]# OK            total       83757003.0
#[Out]#               under18     21460075.0
#[Out]# OR            total       83091217.0
#[Out]#               under18     19960957.0
#[Out]# PA            total      296870336.0
#[Out]#               under18     68686405.0
#[Out]# RI            total       25016239.0
#[Out]#               under18      5657732.0
#[Out]# SC            total       98916461.0
#[Out]#               under18     24429285.0
#[Out]# SD            total       18370564.0
#[Out]#               under18      4862780.0
#[Out]# TN            total      138255369.0
#[Out]#               under18     33544100.0
#[Out]# TX            total      518550295.0
#[Out]#               under18    144693347.0
#[Out]# UT            total       55705156.0
#[Out]#               under18     18023256.0
#[Out]# VA            total      173959196.0
#[Out]#               under18     41760658.0
#[Out]# VT            total       14549094.0
#[Out]#               under18      3381874.0
#[Out]# WA            total      144062186.0
#[Out]#               under18     35829119.0
#[Out]# WI            total      129553437.0
#[Out]#               under18     32265466.0
#[Out]# WV            total       43762227.0
#[Out]#               under18      9718002.0
#[Out]# WY            total       12247873.0
#[Out]#               under18      3173881.0
#[Out]# Name: population, Length: 102, dtype: float64
datana.groupby('state/region')['population'].sum()
#[Out]# state/region
#[Out]# AK    1.998907e+07
#[Out]# AL    1.342974e+08
#[Out]# AR    8.095872e+07
#[Out]# AZ    1.602037e+08
#[Out]# CA    1.042036e+09
#[Out]# CO    1.309345e+08
#[Out]# CT    1.021652e+08
#[Out]# DC    1.678336e+07
#[Out]# DE    2.390016e+07
#[Out]# FL    4.839901e+08
#[Out]# GA    2.537002e+08
#[Out]# HI    3.734995e+07
#[Out]# IA    8.792585e+07
#[Out]# ID    4.116600e+07
#[Out]# IL    3.723697e+08
#[Out]# IN    1.842422e+08
#[Out]# KS    8.177131e+07
#[Out]# KY    1.217471e+08
#[Out]# LA    1.349554e+08
#[Out]# MA    1.867770e+08
#[Out]# MD    1.611601e+08
#[Out]# ME    3.795289e+07
#[Out]# MI    2.955700e+08
#[Out]# MN    1.492092e+08
#[Out]# MO    1.690720e+08
#[Out]# MS    8.612558e+07
#[Out]# MT    2.743707e+07
#[Out]# NC    2.467548e+08
#[Out]# ND    1.952047e+07
#[Out]# NE    5.222119e+07
#[Out]# NH    3.684437e+07
#[Out]# NJ    2.508986e+08
#[Out]# NM    5.641301e+07
#[Out]# NV    6.289339e+07
#[Out]# NY    5.622154e+08
#[Out]# OH    3.398054e+08
#[Out]# OK    1.052171e+08
#[Out]# OR    1.030522e+08
#[Out]# PA    3.655567e+08
#[Out]# RI    3.067397e+07
#[Out]# SC    1.233457e+08
#[Out]# SD    2.323334e+07
#[Out]# TN    1.717995e+08
#[Out]# TX    6.632436e+08
#[Out]# UT    7.372841e+07
#[Out]# VA    2.157199e+08
#[Out]# VT    1.793097e+07
#[Out]# WA    1.798913e+08
#[Out]# WI    1.618189e+08
#[Out]# WV    5.348023e+07
#[Out]# WY    1.542175e+07
#[Out]# Name: population, dtype: float64
popsum = datana.groupby('state/region')['population'].sum()
data1.columns
#[Out]# Index(['state/region', 'ages', 'year', 'population', 'state'], dtype='object')
data2.columns
#[Out]# Index(['state/region', 'ages', 'year', 'population', 'state', 'area (sq. mi)'], dtype='object')
areasum = datana.groupby('state/region')['area(sq,mi)'].sum()
areasum = datana.groupby('state/region')['area (sq. mi)'].sum()
areasum
#[Out]# state/region
#[Out]# AK    31508400
#[Out]# AL     2516304
#[Out]# AR     2552736
#[Out]# AZ     5472288
#[Out]# CA     7857936
#[Out]# CO     4996800
#[Out]# CT      266112
#[Out]# DC        3264
#[Out]# DE       93792
#[Out]# FL     3156384
#[Out]# GA     2853168
#[Out]# HI      524736
#[Out]# IA     2701248
#[Out]# ID     4011552
#[Out]# IL     2780064
#[Out]# IN     1748160
#[Out]# KS     3949536
#[Out]# KY     1939728
#[Out]# LA     2488464
#[Out]# MA      506640
#[Out]# MD      595536
#[Out]# ME     1698576
#[Out]# MI     4646880
#[Out]# MN     4173264
#[Out]# MO     3346032
#[Out]# MS     2324832
#[Out]# MT     7058208
#[Out]# NC     2583408
#[Out]# ND     3393792
#[Out]# NE     3713184
#[Out]# NH      448848
#[Out]# NJ      418656
#[Out]# NM     5836464
#[Out]# NV     5307216
#[Out]# NY     2614800
#[Out]# OH     2151744
#[Out]# OK     3355344
#[Out]# OR     4722528
#[Out]# PA     2210784
#[Out]# RI       74160
#[Out]# SC     1536336
#[Out]# SD     3701808
#[Out]# TN     2023008
#[Out]# TX    12892848
#[Out]# UT     4075392
#[Out]# VA     2052912
#[Out]# VT      461520
#[Out]# WA     3422544
#[Out]# WI     3144144
#[Out]# WV     1163088
#[Out]# WY     4695264
#[Out]# Name: area (sq. mi), dtype: int64
popsum/areasum
#[Out]# state/region
#[Out]# AK       0.634404
#[Out]# AL      53.370896
#[Out]# AR      31.714490
#[Out]# AZ      29.275452
#[Out]# CA     132.609349
#[Out]# CO      26.203680
#[Out]# CT     383.918140
#[Out]# DC    5141.960478
#[Out]# DE     254.820934
#[Out]# FL     153.336900
#[Out]# GA      88.918774
#[Out]# HI      71.178555
#[Out]# IA      32.550085
#[Out]# ID      10.261864
#[Out]# IL     133.942860
#[Out]# IN     105.392094
#[Out]# KS      20.704030
#[Out]# KY      62.765026
#[Out]# LA      54.232430
#[Out]# MA     368.658168
#[Out]# MD     270.613563
#[Out]# ME      22.343946
#[Out]# MI      63.606122
#[Out]# MN      35.753596
#[Out]# MO      50.529093
#[Out]# MS      37.045936
#[Out]# MT       3.887257
#[Out]# NC      95.515220
#[Out]# ND       5.751817
#[Out]# NE      14.063723
#[Out]# NH      82.086515
#[Out]# NJ     599.295266
#[Out]# NM       9.665614
#[Out]# NV      11.850542
#[Out]# NY     215.012775
#[Out]# OH     157.920909
#[Out]# OK      31.358060
#[Out]# OR      21.821400
#[Out]# PA     165.351631
#[Out]# RI     413.618811
#[Out]# SC      80.285658
#[Out]# SD       6.276215
#[Out]# TN      84.922783
#[Out]# TX      51.442757
#[Out]# UT      18.091122
#[Out]# VA     105.079932
#[Out]# VT      38.851985
#[Out]# WA      52.560699
#[Out]# WI      51.466759
#[Out]# WV      45.981240
#[Out]# WY       3.284534
#[Out]# dtype: float64
consum = pd.concat(popsum,areasum)
type(popsum,areasum)
type(popsum)
#[Out]# pandas.core.series.Series
type(popsum)
#[Out]# pandas.core.series.Series
np.concatenate(popsum,areasum)
popsum.shape
#[Out]# (51,)
areasum.shape
#[Out]# (51,)
consum = pd.concat(popsum,areasum)
consum = pd.concat(popsum,areasum,axis=1)
popsum.index == areasum.index
#[Out]# array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
#[Out]#         True,  True,  True,  True,  True,  True,  True,  True,  True,
#[Out]#         True,  True,  True,  True,  True,  True,  True,  True,  True,
#[Out]#         True,  True,  True,  True,  True,  True,  True,  True,  True,
#[Out]#         True,  True,  True,  True,  True,  True,  True,  True,  True,
#[Out]#         True,  True,  True,  True,  True,  True])
popsum
#[Out]# state/region
#[Out]# AK    1.998907e+07
#[Out]# AL    1.342974e+08
#[Out]# AR    8.095872e+07
#[Out]# AZ    1.602037e+08
#[Out]# CA    1.042036e+09
#[Out]# CO    1.309345e+08
#[Out]# CT    1.021652e+08
#[Out]# DC    1.678336e+07
#[Out]# DE    2.390016e+07
#[Out]# FL    4.839901e+08
#[Out]# GA    2.537002e+08
#[Out]# HI    3.734995e+07
#[Out]# IA    8.792585e+07
#[Out]# ID    4.116600e+07
#[Out]# IL    3.723697e+08
#[Out]# IN    1.842422e+08
#[Out]# KS    8.177131e+07
#[Out]# KY    1.217471e+08
#[Out]# LA    1.349554e+08
#[Out]# MA    1.867770e+08
#[Out]# MD    1.611601e+08
#[Out]# ME    3.795289e+07
#[Out]# MI    2.955700e+08
#[Out]# MN    1.492092e+08
#[Out]# MO    1.690720e+08
#[Out]# MS    8.612558e+07
#[Out]# MT    2.743707e+07
#[Out]# NC    2.467548e+08
#[Out]# ND    1.952047e+07
#[Out]# NE    5.222119e+07
#[Out]# NH    3.684437e+07
#[Out]# NJ    2.508986e+08
#[Out]# NM    5.641301e+07
#[Out]# NV    6.289339e+07
#[Out]# NY    5.622154e+08
#[Out]# OH    3.398054e+08
#[Out]# OK    1.052171e+08
#[Out]# OR    1.030522e+08
#[Out]# PA    3.655567e+08
#[Out]# RI    3.067397e+07
#[Out]# SC    1.233457e+08
#[Out]# SD    2.323334e+07
#[Out]# TN    1.717995e+08
#[Out]# TX    6.632436e+08
#[Out]# UT    7.372841e+07
#[Out]# VA    2.157199e+08
#[Out]# VT    1.793097e+07
#[Out]# WA    1.798913e+08
#[Out]# WI    1.618189e+08
#[Out]# WV    5.348023e+07
#[Out]# WY    1.542175e+07
#[Out]# Name: population, dtype: float64
areasum
#[Out]# state/region
#[Out]# AK    31508400
#[Out]# AL     2516304
#[Out]# AR     2552736
#[Out]# AZ     5472288
#[Out]# CA     7857936
#[Out]# CO     4996800
#[Out]# CT      266112
#[Out]# DC        3264
#[Out]# DE       93792
#[Out]# FL     3156384
#[Out]# GA     2853168
#[Out]# HI      524736
#[Out]# IA     2701248
#[Out]# ID     4011552
#[Out]# IL     2780064
#[Out]# IN     1748160
#[Out]# KS     3949536
#[Out]# KY     1939728
#[Out]# LA     2488464
#[Out]# MA      506640
#[Out]# MD      595536
#[Out]# ME     1698576
#[Out]# MI     4646880
#[Out]# MN     4173264
#[Out]# MO     3346032
#[Out]# MS     2324832
#[Out]# MT     7058208
#[Out]# NC     2583408
#[Out]# ND     3393792
#[Out]# NE     3713184
#[Out]# NH      448848
#[Out]# NJ      418656
#[Out]# NM     5836464
#[Out]# NV     5307216
#[Out]# NY     2614800
#[Out]# OH     2151744
#[Out]# OK     3355344
#[Out]# OR     4722528
#[Out]# PA     2210784
#[Out]# RI       74160
#[Out]# SC     1536336
#[Out]# SD     3701808
#[Out]# TN     2023008
#[Out]# TX    12892848
#[Out]# UT     4075392
#[Out]# VA     2052912
#[Out]# VT      461520
#[Out]# WA     3422544
#[Out]# WI     3144144
#[Out]# WV     1163088
#[Out]# WY     4695264
#[Out]# Name: area (sq. mi), dtype: int64
popsum.sort_index()
#[Out]# state/region
#[Out]# AK    1.998907e+07
#[Out]# AL    1.342974e+08
#[Out]# AR    8.095872e+07
#[Out]# AZ    1.602037e+08
#[Out]# CA    1.042036e+09
#[Out]# CO    1.309345e+08
#[Out]# CT    1.021652e+08
#[Out]# DC    1.678336e+07
#[Out]# DE    2.390016e+07
#[Out]# FL    4.839901e+08
#[Out]# GA    2.537002e+08
#[Out]# HI    3.734995e+07
#[Out]# IA    8.792585e+07
#[Out]# ID    4.116600e+07
#[Out]# IL    3.723697e+08
#[Out]# IN    1.842422e+08
#[Out]# KS    8.177131e+07
#[Out]# KY    1.217471e+08
#[Out]# LA    1.349554e+08
#[Out]# MA    1.867770e+08
#[Out]# MD    1.611601e+08
#[Out]# ME    3.795289e+07
#[Out]# MI    2.955700e+08
#[Out]# MN    1.492092e+08
#[Out]# MO    1.690720e+08
#[Out]# MS    8.612558e+07
#[Out]# MT    2.743707e+07
#[Out]# NC    2.467548e+08
#[Out]# ND    1.952047e+07
#[Out]# NE    5.222119e+07
#[Out]# NH    3.684437e+07
#[Out]# NJ    2.508986e+08
#[Out]# NM    5.641301e+07
#[Out]# NV    6.289339e+07
#[Out]# NY    5.622154e+08
#[Out]# OH    3.398054e+08
#[Out]# OK    1.052171e+08
#[Out]# OR    1.030522e+08
#[Out]# PA    3.655567e+08
#[Out]# RI    3.067397e+07
#[Out]# SC    1.233457e+08
#[Out]# SD    2.323334e+07
#[Out]# TN    1.717995e+08
#[Out]# TX    6.632436e+08
#[Out]# UT    7.372841e+07
#[Out]# VA    2.157199e+08
#[Out]# VT    1.793097e+07
#[Out]# WA    1.798913e+08
#[Out]# WI    1.618189e+08
#[Out]# WV    5.348023e+07
#[Out]# WY    1.542175e+07
#[Out]# Name: population, dtype: float64
areasum.sort_index()
#[Out]# state/region
#[Out]# AK    31508400
#[Out]# AL     2516304
#[Out]# AR     2552736
#[Out]# AZ     5472288
#[Out]# CA     7857936
#[Out]# CO     4996800
#[Out]# CT      266112
#[Out]# DC        3264
#[Out]# DE       93792
#[Out]# FL     3156384
#[Out]# GA     2853168
#[Out]# HI      524736
#[Out]# IA     2701248
#[Out]# ID     4011552
#[Out]# IL     2780064
#[Out]# IN     1748160
#[Out]# KS     3949536
#[Out]# KY     1939728
#[Out]# LA     2488464
#[Out]# MA      506640
#[Out]# MD      595536
#[Out]# ME     1698576
#[Out]# MI     4646880
#[Out]# MN     4173264
#[Out]# MO     3346032
#[Out]# MS     2324832
#[Out]# MT     7058208
#[Out]# NC     2583408
#[Out]# ND     3393792
#[Out]# NE     3713184
#[Out]# NH      448848
#[Out]# NJ      418656
#[Out]# NM     5836464
#[Out]# NV     5307216
#[Out]# NY     2614800
#[Out]# OH     2151744
#[Out]# OK     3355344
#[Out]# OR     4722528
#[Out]# PA     2210784
#[Out]# RI       74160
#[Out]# SC     1536336
#[Out]# SD     3701808
#[Out]# TN     2023008
#[Out]# TX    12892848
#[Out]# UT     4075392
#[Out]# VA     2052912
#[Out]# VT      461520
#[Out]# WA     3422544
#[Out]# WI     3144144
#[Out]# WV     1163088
#[Out]# WY     4695264
#[Out]# Name: area (sq. mi), dtype: int64
consum = pd.concat(popsum,areasum,axis=1)
consum = pd.concat(popsum,areasum,axis=0)
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
areas
#[Out]#                    state  area (sq. mi)
#[Out]# 0                Alabama          52423
#[Out]# 1                 Alaska         656425
#[Out]# 2                Arizona         114006
#[Out]# 3               Arkansas          53182
#[Out]# 4             California         163707
#[Out]# 5               Colorado         104100
#[Out]# 6            Connecticut           5544
#[Out]# 7               Delaware           1954
#[Out]# 8                Florida          65758
#[Out]# 9                Georgia          59441
#[Out]# 10                Hawaii          10932
#[Out]# 11                 Idaho          83574
#[Out]# 12              Illinois          57918
#[Out]# 13               Indiana          36420
#[Out]# 14                  Iowa          56276
#[Out]# 15                Kansas          82282
#[Out]# 16              Kentucky          40411
#[Out]# 17             Louisiana          51843
#[Out]# 18                 Maine          35387
#[Out]# 19              Maryland          12407
#[Out]# 20         Massachusetts          10555
#[Out]# 21              Michigan          96810
#[Out]# 22             Minnesota          86943
#[Out]# 23           Mississippi          48434
#[Out]# 24              Missouri          69709
#[Out]# 25               Montana         147046
#[Out]# 26              Nebraska          77358
#[Out]# 27                Nevada         110567
#[Out]# 28         New Hampshire           9351
#[Out]# 29            New Jersey           8722
#[Out]# 30            New Mexico         121593
#[Out]# 31              New York          54475
#[Out]# 32        North Carolina          53821
#[Out]# 33          North Dakota          70704
#[Out]# 34                  Ohio          44828
#[Out]# 35              Oklahoma          69903
#[Out]# 36                Oregon          98386
#[Out]# 37          Pennsylvania          46058
#[Out]# 38          Rhode Island           1545
#[Out]# 39        South Carolina          32007
#[Out]# 40          South Dakota          77121
#[Out]# 41             Tennessee          42146
#[Out]# 42                 Texas         268601
#[Out]# 43                  Utah          84904
#[Out]# 44               Vermont           9615
#[Out]# 45              Virginia          42769
#[Out]# 46            Washington          71303
#[Out]# 47         West Virginia          24231
#[Out]# 48             Wisconsin          65503
#[Out]# 49               Wyoming          97818
#[Out]# 50  District of Columbia             68
#[Out]# 51           Puerto Rico           3515
abbrevs
#[Out]#                    state abbreviation
#[Out]# 0                Alabama           AL
#[Out]# 1                 Alaska           AK
#[Out]# 2                Arizona           AZ
#[Out]# 3               Arkansas           AR
#[Out]# 4             California           CA
#[Out]# 5               Colorado           CO
#[Out]# 6            Connecticut           CT
#[Out]# 7               Delaware           DE
#[Out]# 8   District of Columbia           DC
#[Out]# 9                Florida           FL
#[Out]# 10               Georgia           GA
#[Out]# 11                Hawaii           HI
#[Out]# 12                 Idaho           ID
#[Out]# 13              Illinois           IL
#[Out]# 14               Indiana           IN
#[Out]# 15                  Iowa           IA
#[Out]# 16                Kansas           KS
#[Out]# 17              Kentucky           KY
#[Out]# 18             Louisiana           LA
#[Out]# 19                 Maine           ME
#[Out]# 20               Montana           MT
#[Out]# 21              Nebraska           NE
#[Out]# 22                Nevada           NV
#[Out]# 23         New Hampshire           NH
#[Out]# 24            New Jersey           NJ
#[Out]# 25            New Mexico           NM
#[Out]# 26              New York           NY
#[Out]# 27        North Carolina           NC
#[Out]# 28          North Dakota           ND
#[Out]# 29                  Ohio           OH
#[Out]# 30              Oklahoma           OK
#[Out]# 31                Oregon           OR
#[Out]# 32              Maryland           MD
#[Out]# 33         Massachusetts           MA
#[Out]# 34              Michigan           MI
#[Out]# 35             Minnesota           MN
#[Out]# 36           Mississippi           MS
#[Out]# 37              Missouri           MO
#[Out]# 38          Pennsylvania           PA
#[Out]# 39          Rhode Island           RI
#[Out]# 40        South Carolina           SC
#[Out]# 41          South Dakota           SD
#[Out]# 42             Tennessee           TN
#[Out]# 43                 Texas           TX
#[Out]# 44                  Utah           UT
#[Out]# 45               Vermont           VT
#[Out]# 46              Virginia           VA
#[Out]# 47            Washington           WA
#[Out]# 48         West Virginia           WV
#[Out]# 49             Wisconsin           WI
#[Out]# 50               Wyoming           WY
pop.head()
#[Out]#   state/region     ages  year  population
#[Out]# 0           AL  under18  2012   1117489.0
#[Out]# 1           AL    total  2012   4817528.0
#[Out]# 2           AL  under18  2010   1130966.0
#[Out]# 3           AL    total  2010   4785570.0
#[Out]# 4           AL  under18  2011   1125763.0
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
data1 = pd.concat(pop,abbrevs,how='outer',left_on='state/region',right_on='abbreviation)
data1 = pd.concat(pop,abbrevs,how='outer',left_on='state/region',right_on='abbreviation')
data1 = pd.concat(pop,abbrevs,left_on='state/region',right_on='abbreviation',how='outter')
data1 = pd.merge(pop,abbrevs,left_on='state/region',right_on='abbreviation',how='outter')
data1 = pd.merge(pop,abbrevs,left_on='state/region',right_on='abbreviation',how='outer')
data1
#[Out]#      state/region     ages  year   population    state abbreviation
#[Out]# 0              AL  under18  2012    1117489.0  Alabama           AL
#[Out]# 1              AL    total  2012    4817528.0  Alabama           AL
#[Out]# 2              AL  under18  2010    1130966.0  Alabama           AL
#[Out]# 3              AL    total  2010    4785570.0  Alabama           AL
#[Out]# 4              AL  under18  2011    1125763.0  Alabama           AL
#[Out]# 5              AL    total  2011    4801627.0  Alabama           AL
#[Out]# 6              AL    total  2009    4757938.0  Alabama           AL
#[Out]# 7              AL  under18  2009    1134192.0  Alabama           AL
#[Out]# 8              AL  under18  2013    1111481.0  Alabama           AL
#[Out]# 9              AL    total  2013    4833722.0  Alabama           AL
#[Out]# 10             AL    total  2007    4672840.0  Alabama           AL
#[Out]# 11             AL  under18  2007    1132296.0  Alabama           AL
#[Out]# 12             AL    total  2008    4718206.0  Alabama           AL
#[Out]# 13             AL  under18  2008    1134927.0  Alabama           AL
#[Out]# 14             AL    total  2005    4569805.0  Alabama           AL
#[Out]# 15             AL  under18  2005    1117229.0  Alabama           AL
#[Out]# 16             AL    total  2006    4628981.0  Alabama           AL
#[Out]# 17             AL  under18  2006    1126798.0  Alabama           AL
#[Out]# 18             AL    total  2004    4530729.0  Alabama           AL
#[Out]# 19             AL  under18  2004    1113662.0  Alabama           AL
#[Out]# 20             AL    total  2003    4503491.0  Alabama           AL
#[Out]# 21             AL  under18  2003    1113083.0  Alabama           AL
#[Out]# 22             AL    total  2001    4467634.0  Alabama           AL
#[Out]# 23             AL  under18  2001    1120409.0  Alabama           AL
#[Out]# 24             AL    total  2002    4480089.0  Alabama           AL
#[Out]# 25             AL  under18  2002    1116590.0  Alabama           AL
#[Out]# 26             AL  under18  1999    1121287.0  Alabama           AL
#[Out]# 27             AL    total  1999    4430141.0  Alabama           AL
#[Out]# 28             AL    total  2000    4452173.0  Alabama           AL
#[Out]# 29             AL  under18  2000    1122273.0  Alabama           AL
#[Out]# ...           ...      ...   ...          ...      ...          ...
#[Out]# 2514          USA  under18  1999   71946051.0      NaN          NaN
#[Out]# 2515          USA    total  2000  282162411.0      NaN          NaN
#[Out]# 2516          USA  under18  2000   72376189.0      NaN          NaN
#[Out]# 2517          USA    total  1999  279040181.0      NaN          NaN
#[Out]# 2518          USA    total  2001  284968955.0      NaN          NaN
#[Out]# 2519          USA  under18  2001   72671175.0      NaN          NaN
#[Out]# 2520          USA    total  2002  287625193.0      NaN          NaN
#[Out]# 2521          USA  under18  2002   72936457.0      NaN          NaN
#[Out]# 2522          USA    total  2003  290107933.0      NaN          NaN
#[Out]# 2523          USA  under18  2003   73100758.0      NaN          NaN
#[Out]# 2524          USA    total  2004  292805298.0      NaN          NaN
#[Out]# 2525          USA  under18  2004   73297735.0      NaN          NaN
#[Out]# 2526          USA    total  2005  295516599.0      NaN          NaN
#[Out]# 2527          USA  under18  2005   73523669.0      NaN          NaN
#[Out]# 2528          USA    total  2006  298379912.0      NaN          NaN
#[Out]# 2529          USA  under18  2006   73757714.0      NaN          NaN
#[Out]# 2530          USA    total  2007  301231207.0      NaN          NaN
#[Out]# 2531          USA  under18  2007   74019405.0      NaN          NaN
#[Out]# 2532          USA    total  2008  304093966.0      NaN          NaN
#[Out]# 2533          USA  under18  2008   74104602.0      NaN          NaN
#[Out]# 2534          USA  under18  2013   73585872.0      NaN          NaN
#[Out]# 2535          USA    total  2013  316128839.0      NaN          NaN
#[Out]# 2536          USA    total  2009  306771529.0      NaN          NaN
#[Out]# 2537          USA  under18  2009   74134167.0      NaN          NaN
#[Out]# 2538          USA  under18  2010   74119556.0      NaN          NaN
#[Out]# 2539          USA    total  2010  309326295.0      NaN          NaN
#[Out]# 2540          USA  under18  2011   73902222.0      NaN          NaN
#[Out]# 2541          USA    total  2011  311582564.0      NaN          NaN
#[Out]# 2542          USA  under18  2012   73708179.0      NaN          NaN
#[Out]# 2543          USA    total  2012  313873685.0      NaN          NaN
#[Out]# 
#[Out]# [2544 rows x 6 columns]
_
#[Out]#      state/region     ages  year   population    state abbreviation
#[Out]# 0              AL  under18  2012    1117489.0  Alabama           AL
#[Out]# 1              AL    total  2012    4817528.0  Alabama           AL
#[Out]# 2              AL  under18  2010    1130966.0  Alabama           AL
#[Out]# 3              AL    total  2010    4785570.0  Alabama           AL
#[Out]# 4              AL  under18  2011    1125763.0  Alabama           AL
#[Out]# 5              AL    total  2011    4801627.0  Alabama           AL
#[Out]# 6              AL    total  2009    4757938.0  Alabama           AL
#[Out]# 7              AL  under18  2009    1134192.0  Alabama           AL
#[Out]# 8              AL  under18  2013    1111481.0  Alabama           AL
#[Out]# 9              AL    total  2013    4833722.0  Alabama           AL
#[Out]# 10             AL    total  2007    4672840.0  Alabama           AL
#[Out]# 11             AL  under18  2007    1132296.0  Alabama           AL
#[Out]# 12             AL    total  2008    4718206.0  Alabama           AL
#[Out]# 13             AL  under18  2008    1134927.0  Alabama           AL
#[Out]# 14             AL    total  2005    4569805.0  Alabama           AL
#[Out]# 15             AL  under18  2005    1117229.0  Alabama           AL
#[Out]# 16             AL    total  2006    4628981.0  Alabama           AL
#[Out]# 17             AL  under18  2006    1126798.0  Alabama           AL
#[Out]# 18             AL    total  2004    4530729.0  Alabama           AL
#[Out]# 19             AL  under18  2004    1113662.0  Alabama           AL
#[Out]# 20             AL    total  2003    4503491.0  Alabama           AL
#[Out]# 21             AL  under18  2003    1113083.0  Alabama           AL
#[Out]# 22             AL    total  2001    4467634.0  Alabama           AL
#[Out]# 23             AL  under18  2001    1120409.0  Alabama           AL
#[Out]# 24             AL    total  2002    4480089.0  Alabama           AL
#[Out]# 25             AL  under18  2002    1116590.0  Alabama           AL
#[Out]# 26             AL  under18  1999    1121287.0  Alabama           AL
#[Out]# 27             AL    total  1999    4430141.0  Alabama           AL
#[Out]# 28             AL    total  2000    4452173.0  Alabama           AL
#[Out]# 29             AL  under18  2000    1122273.0  Alabama           AL
#[Out]# ...           ...      ...   ...          ...      ...          ...
#[Out]# 2514          USA  under18  1999   71946051.0      NaN          NaN
#[Out]# 2515          USA    total  2000  282162411.0      NaN          NaN
#[Out]# 2516          USA  under18  2000   72376189.0      NaN          NaN
#[Out]# 2517          USA    total  1999  279040181.0      NaN          NaN
#[Out]# 2518          USA    total  2001  284968955.0      NaN          NaN
#[Out]# 2519          USA  under18  2001   72671175.0      NaN          NaN
#[Out]# 2520          USA    total  2002  287625193.0      NaN          NaN
#[Out]# 2521          USA  under18  2002   72936457.0      NaN          NaN
#[Out]# 2522          USA    total  2003  290107933.0      NaN          NaN
#[Out]# 2523          USA  under18  2003   73100758.0      NaN          NaN
#[Out]# 2524          USA    total  2004  292805298.0      NaN          NaN
#[Out]# 2525          USA  under18  2004   73297735.0      NaN          NaN
#[Out]# 2526          USA    total  2005  295516599.0      NaN          NaN
#[Out]# 2527          USA  under18  2005   73523669.0      NaN          NaN
#[Out]# 2528          USA    total  2006  298379912.0      NaN          NaN
#[Out]# 2529          USA  under18  2006   73757714.0      NaN          NaN
#[Out]# 2530          USA    total  2007  301231207.0      NaN          NaN
#[Out]# 2531          USA  under18  2007   74019405.0      NaN          NaN
#[Out]# 2532          USA    total  2008  304093966.0      NaN          NaN
#[Out]# 2533          USA  under18  2008   74104602.0      NaN          NaN
#[Out]# 2534          USA  under18  2013   73585872.0      NaN          NaN
#[Out]# 2535          USA    total  2013  316128839.0      NaN          NaN
#[Out]# 2536          USA    total  2009  306771529.0      NaN          NaN
#[Out]# 2537          USA  under18  2009   74134167.0      NaN          NaN
#[Out]# 2538          USA  under18  2010   74119556.0      NaN          NaN
#[Out]# 2539          USA    total  2010  309326295.0      NaN          NaN
#[Out]# 2540          USA  under18  2011   73902222.0      NaN          NaN
#[Out]# 2541          USA    total  2011  311582564.0      NaN          NaN
#[Out]# 2542          USA  under18  2012   73708179.0      NaN          NaN
#[Out]# 2543          USA    total  2012  313873685.0      NaN          NaN
#[Out]# 
#[Out]# [2544 rows x 6 columns]
_.isnull().any()
#[Out]# state/region    False
#[Out]# ages            False
#[Out]# year            False
#[Out]# population       True
#[Out]# state            True
#[Out]# abbreviation     True
#[Out]# dtype: bool
data1.drop('abbreviation',axis=1)
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
data1 = data1.drop('abbreviation',axis=1)
data.head()
data1.head()
#[Out]#   state/region     ages  year  population    state
#[Out]# 0           AL  under18  2012   1117489.0  Alabama
#[Out]# 1           AL    total  2012   4817528.0  Alabama
#[Out]# 2           AL  under18  2010   1130966.0  Alabama
#[Out]# 3           AL    total  2010   4785570.0  Alabama
#[Out]# 4           AL  under18  2011   1125763.0  Alabama
data1.head()
#[Out]#   state/region     ages  year  population    state
#[Out]# 0           AL  under18  2012   1117489.0  Alabama
#[Out]# 1           AL    total  2012   4817528.0  Alabama
#[Out]# 2           AL  under18  2010   1130966.0  Alabama
#[Out]# 3           AL    total  2010   4785570.0  Alabama
#[Out]# 4           AL  under18  2011   1125763.0  Alabama
data1.isnull().any()
#[Out]# state/region    False
#[Out]# ages            False
#[Out]# year            False
#[Out]# population       True
#[Out]# state            True
#[Out]# dtype: bool
data1[data1.isnull()].head()
#[Out]#   state/region ages  year  population state
#[Out]# 0          NaN  NaN   NaN         NaN   NaN
#[Out]# 1          NaN  NaN   NaN         NaN   NaN
#[Out]# 2          NaN  NaN   NaN         NaN   NaN
#[Out]# 3          NaN  NaN   NaN         NaN   NaN
#[Out]# 4          NaN  NaN   NaN         NaN   NaN
data1[data['population'].isnull()].head()
data1[data1['population'].isnull()].head()
#[Out]#      state/region     ages  year  population state
#[Out]# 2448           PR  under18  1990         NaN   NaN
#[Out]# 2449           PR    total  1990         NaN   NaN
#[Out]# 2450           PR    total  1991         NaN   NaN
#[Out]# 2451           PR  under18  1991         NaN   NaN
#[Out]# 2452           PR    total  1993         NaN   NaN
data1[data1['state/region'] == PR]['population','state']
data1[data1['state/region'] == 'PR']['population','state']
data1[data1['state/region'] == 'PR'][['population','state']]
#[Out]#       population state
#[Out]# 2448         NaN   NaN
#[Out]# 2449         NaN   NaN
#[Out]# 2450         NaN   NaN
#[Out]# 2451         NaN   NaN
#[Out]# 2452         NaN   NaN
#[Out]# 2453         NaN   NaN
#[Out]# 2454         NaN   NaN
#[Out]# 2455         NaN   NaN
#[Out]# 2456         NaN   NaN
#[Out]# 2457         NaN   NaN
#[Out]# 2458         NaN   NaN
#[Out]# 2459         NaN   NaN
#[Out]# 2460         NaN   NaN
#[Out]# 2461         NaN   NaN
#[Out]# 2462         NaN   NaN
#[Out]# 2463         NaN   NaN
#[Out]# 2464         NaN   NaN
#[Out]# 2465         NaN   NaN
#[Out]# 2466         NaN   NaN
#[Out]# 2467         NaN   NaN
#[Out]# 2468   3810605.0   NaN
#[Out]# 2469   1089063.0   NaN
#[Out]# 2470   3818774.0   NaN
#[Out]# 2471   1077566.0   NaN
#[Out]# 2472   3823701.0   NaN
#[Out]# 2473   1065051.0   NaN
#[Out]# 2474   3826878.0   NaN
#[Out]# 2475   1035919.0   NaN
#[Out]# 2476   3826095.0   NaN
#[Out]# 2477   1050615.0   NaN
#[Out]# 2478   3821362.0   NaN
#[Out]# 2479   1019447.0   NaN
#[Out]# 2480   3805214.0   NaN
#[Out]# 2481    998543.0   NaN
#[Out]# 2482   3782995.0   NaN
#[Out]# 2483    973613.0   NaN
#[Out]# 2484   3760866.0   NaN
#[Out]# 2485    945705.0   NaN
#[Out]# 2486    814068.0   NaN
#[Out]# 2487   3615086.0   NaN
#[Out]# 2488   3740410.0   NaN
#[Out]# 2489    920794.0   NaN
#[Out]# 2490   3721208.0   NaN
#[Out]# 2491    896945.0   NaN
#[Out]# 2492    869327.0   NaN
#[Out]# 2493   3686580.0   NaN
#[Out]# 2494    841740.0   NaN
#[Out]# 2495   3651545.0   NaN
data1[data1['state/region'] == 'PR']
#[Out]#      state/region     ages  year  population state
#[Out]# 2448           PR  under18  1990         NaN   NaN
#[Out]# 2449           PR    total  1990         NaN   NaN
#[Out]# 2450           PR    total  1991         NaN   NaN
#[Out]# 2451           PR  under18  1991         NaN   NaN
#[Out]# 2452           PR    total  1993         NaN   NaN
#[Out]# 2453           PR  under18  1993         NaN   NaN
#[Out]# 2454           PR  under18  1992         NaN   NaN
#[Out]# 2455           PR    total  1992         NaN   NaN
#[Out]# 2456           PR  under18  1994         NaN   NaN
#[Out]# 2457           PR    total  1994         NaN   NaN
#[Out]# 2458           PR    total  1995         NaN   NaN
#[Out]# 2459           PR  under18  1995         NaN   NaN
#[Out]# 2460           PR  under18  1996         NaN   NaN
#[Out]# 2461           PR    total  1996         NaN   NaN
#[Out]# 2462           PR  under18  1998         NaN   NaN
#[Out]# 2463           PR    total  1998         NaN   NaN
#[Out]# 2464           PR    total  1997         NaN   NaN
#[Out]# 2465           PR  under18  1997         NaN   NaN
#[Out]# 2466           PR    total  1999         NaN   NaN
#[Out]# 2467           PR  under18  1999         NaN   NaN
#[Out]# 2468           PR    total  2000   3810605.0   NaN
#[Out]# 2469           PR  under18  2000   1089063.0   NaN
#[Out]# 2470           PR    total  2001   3818774.0   NaN
#[Out]# 2471           PR  under18  2001   1077566.0   NaN
#[Out]# 2472           PR    total  2002   3823701.0   NaN
#[Out]# 2473           PR  under18  2002   1065051.0   NaN
#[Out]# 2474           PR    total  2004   3826878.0   NaN
#[Out]# 2475           PR  under18  2004   1035919.0   NaN
#[Out]# 2476           PR    total  2003   3826095.0   NaN
#[Out]# 2477           PR  under18  2003   1050615.0   NaN
#[Out]# 2478           PR    total  2005   3821362.0   NaN
#[Out]# 2479           PR  under18  2005   1019447.0   NaN
#[Out]# 2480           PR    total  2006   3805214.0   NaN
#[Out]# 2481           PR  under18  2006    998543.0   NaN
#[Out]# 2482           PR    total  2007   3782995.0   NaN
#[Out]# 2483           PR  under18  2007    973613.0   NaN
#[Out]# 2484           PR    total  2008   3760866.0   NaN
#[Out]# 2485           PR  under18  2008    945705.0   NaN
#[Out]# 2486           PR  under18  2013    814068.0   NaN
#[Out]# 2487           PR    total  2013   3615086.0   NaN
#[Out]# 2488           PR    total  2009   3740410.0   NaN
#[Out]# 2489           PR  under18  2009    920794.0   NaN
#[Out]# 2490           PR    total  2010   3721208.0   NaN
#[Out]# 2491           PR  under18  2010    896945.0   NaN
#[Out]# 2492           PR  under18  2011    869327.0   NaN
#[Out]# 2493           PR    total  2011   3686580.0   NaN
#[Out]# 2494           PR  under18  2012    841740.0   NaN
#[Out]# 2495           PR    total  2012   3651545.0   NaN
data1[data1['state'].isnull()].head()
#[Out]#      state/region     ages  year  population state
#[Out]# 2448           PR  under18  1990         NaN   NaN
#[Out]# 2449           PR    total  1990         NaN   NaN
#[Out]# 2450           PR    total  1991         NaN   NaN
#[Out]# 2451           PR  under18  1991         NaN   NaN
#[Out]# 2452           PR    total  1993         NaN   NaN
data1[data1['state'].isnull()]
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
data1.head()
#[Out]#   state/region     ages  year  population    state
#[Out]# 0           AL  under18  2012   1117489.0  Alabama
#[Out]# 1           AL    total  2012   4817528.0  Alabama
#[Out]# 2           AL  under18  2010   1130966.0  Alabama
#[Out]# 3           AL    total  2010   4785570.0  Alabama
#[Out]# 4           AL  under18  2011   1125763.0  Alabama
data1[(data1['state/region'] == 'USA') & data1['state'] == np.nan ]
#[Out]# Empty DataFrame
#[Out]# Columns: [state/region, ages, year, population, state]
#[Out]# Index: []
data1[(data1['state/region'] == 'USA') & (data1['state'] == np.nan)]
#[Out]# Empty DataFrame
#[Out]# Columns: [state/region, ages, year, population, state]
#[Out]# Index: []
data1[data1[(data1['state/region'] == 'USA')].isnull]
data1[data1[(data1['state/region'] == 'USA')].isnull()]
#[Out]#      state/region ages  year  population state
#[Out]# 0             NaN  NaN   NaN         NaN   NaN
#[Out]# 1             NaN  NaN   NaN         NaN   NaN
#[Out]# 2             NaN  NaN   NaN         NaN   NaN
#[Out]# 3             NaN  NaN   NaN         NaN   NaN
#[Out]# 4             NaN  NaN   NaN         NaN   NaN
#[Out]# 5             NaN  NaN   NaN         NaN   NaN
#[Out]# 6             NaN  NaN   NaN         NaN   NaN
#[Out]# 7             NaN  NaN   NaN         NaN   NaN
#[Out]# 8             NaN  NaN   NaN         NaN   NaN
#[Out]# 9             NaN  NaN   NaN         NaN   NaN
#[Out]# 10            NaN  NaN   NaN         NaN   NaN
#[Out]# 11            NaN  NaN   NaN         NaN   NaN
#[Out]# 12            NaN  NaN   NaN         NaN   NaN
#[Out]# 13            NaN  NaN   NaN         NaN   NaN
#[Out]# 14            NaN  NaN   NaN         NaN   NaN
#[Out]# 15            NaN  NaN   NaN         NaN   NaN
#[Out]# 16            NaN  NaN   NaN         NaN   NaN
#[Out]# 17            NaN  NaN   NaN         NaN   NaN
#[Out]# 18            NaN  NaN   NaN         NaN   NaN
#[Out]# 19            NaN  NaN   NaN         NaN   NaN
#[Out]# 20            NaN  NaN   NaN         NaN   NaN
#[Out]# 21            NaN  NaN   NaN         NaN   NaN
#[Out]# 22            NaN  NaN   NaN         NaN   NaN
#[Out]# 23            NaN  NaN   NaN         NaN   NaN
#[Out]# 24            NaN  NaN   NaN         NaN   NaN
#[Out]# 25            NaN  NaN   NaN         NaN   NaN
#[Out]# 26            NaN  NaN   NaN         NaN   NaN
#[Out]# 27            NaN  NaN   NaN         NaN   NaN
#[Out]# 28            NaN  NaN   NaN         NaN   NaN
#[Out]# 29            NaN  NaN   NaN         NaN   NaN
#[Out]# ...           ...  ...   ...         ...   ...
#[Out]# 2514          NaN  NaN   NaN         NaN   NaN
#[Out]# 2515          NaN  NaN   NaN         NaN   NaN
#[Out]# 2516          NaN  NaN   NaN         NaN   NaN
#[Out]# 2517          NaN  NaN   NaN         NaN   NaN
#[Out]# 2518          NaN  NaN   NaN         NaN   NaN
#[Out]# 2519          NaN  NaN   NaN         NaN   NaN
#[Out]# 2520          NaN  NaN   NaN         NaN   NaN
#[Out]# 2521          NaN  NaN   NaN         NaN   NaN
#[Out]# 2522          NaN  NaN   NaN         NaN   NaN
#[Out]# 2523          NaN  NaN   NaN         NaN   NaN
#[Out]# 2524          NaN  NaN   NaN         NaN   NaN
#[Out]# 2525          NaN  NaN   NaN         NaN   NaN
#[Out]# 2526          NaN  NaN   NaN         NaN   NaN
#[Out]# 2527          NaN  NaN   NaN         NaN   NaN
#[Out]# 2528          NaN  NaN   NaN         NaN   NaN
#[Out]# 2529          NaN  NaN   NaN         NaN   NaN
#[Out]# 2530          NaN  NaN   NaN         NaN   NaN
#[Out]# 2531          NaN  NaN   NaN         NaN   NaN
#[Out]# 2532          NaN  NaN   NaN         NaN   NaN
#[Out]# 2533          NaN  NaN   NaN         NaN   NaN
#[Out]# 2534          NaN  NaN   NaN         NaN   NaN
#[Out]# 2535          NaN  NaN   NaN         NaN   NaN
#[Out]# 2536          NaN  NaN   NaN         NaN   NaN
#[Out]# 2537          NaN  NaN   NaN         NaN   NaN
#[Out]# 2538          NaN  NaN   NaN         NaN   NaN
#[Out]# 2539          NaN  NaN   NaN         NaN   NaN
#[Out]# 2540          NaN  NaN   NaN         NaN   NaN
#[Out]# 2541          NaN  NaN   NaN         NaN   NaN
#[Out]# 2542          NaN  NaN   NaN         NaN   NaN
#[Out]# 2543          NaN  NaN   NaN         NaN   NaN
#[Out]# 
#[Out]# [2544 rows x 5 columns]
data1[data1['state/region'] == 'USA'].isnull()]
data1[data1['state/region'] == 'USA']
#[Out]#      state/region     ages  year   population state
#[Out]# 2496          USA  under18  1990   64218512.0   NaN
#[Out]# 2497          USA    total  1990  249622814.0   NaN
#[Out]# 2498          USA    total  1991  252980942.0   NaN
#[Out]# 2499          USA  under18  1991   65313018.0   NaN
#[Out]# 2500          USA  under18  1992   66509177.0   NaN
#[Out]# 2501          USA    total  1992  256514231.0   NaN
#[Out]# 2502          USA    total  1993  259918595.0   NaN
#[Out]# 2503          USA  under18  1993   67594938.0   NaN
#[Out]# 2504          USA  under18  1994   68640936.0   NaN
#[Out]# 2505          USA    total  1994  263125826.0   NaN
#[Out]# 2506          USA  under18  1995   69473140.0   NaN
#[Out]# 2507          USA  under18  1996   70233512.0   NaN
#[Out]# 2508          USA    total  1995  266278403.0   NaN
#[Out]# 2509          USA    total  1996  269394291.0   NaN
#[Out]# 2510          USA    total  1997  272646932.0   NaN
#[Out]# 2511          USA  under18  1997   70920738.0   NaN
#[Out]# 2512          USA  under18  1998   71431406.0   NaN
#[Out]# 2513          USA    total  1998  275854116.0   NaN
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
data1.loc[data1['state'].isnull(),'state/region'].unique()
#[Out]# array(['PR', 'USA'], dtype=object)
data1.loc[data['state/region'] == 'PR','state
data1.loc[data['state/region'] == 'PR','state'] = 'Puerto Rico'
data1.loc[data1['state/region'] == 'PR','state'] = 'Puerto Rico'
data1.loc[data1['state/region'] == 'USA','state'] = 'Unites states of American '
data.isnull().any()
data1.isnull().any()
#[Out]# state/region    False
#[Out]# ages            False
#[Out]# year            False
#[Out]# population       True
#[Out]# state           False
#[Out]# dtype: bool
final = pd.merge(data1,areas,on='state',how='left')
final.head9)
final.head()
#[Out]#   state/region     ages  year  population    state  area (sq. mi)
#[Out]# 0           AL  under18  2012   1117489.0  Alabama        52423.0
#[Out]# 1           AL    total  2012   4817528.0  Alabama        52423.0
#[Out]# 2           AL  under18  2010   1130966.0  Alabama        52423.0
#[Out]# 3           AL    total  2010   4785570.0  Alabama        52423.0
#[Out]# 4           AL  under18  2011   1125763.0  Alabama        52423.0
final.isnull().any()
#[Out]# state/region     False
#[Out]# ages             False
#[Out]# year             False
#[Out]# population        True
#[Out]# state            False
#[Out]# area (sq. mi)     True
#[Out]# dtype: bool
final['state'][final['area (sq. mi)'].isnull()].unique()
#[Out]# array(['Unites states of American '], dtype=object)
final.dropna(inplace=True)
final['state'][final['area (sq. mi)'].isnull()].unique()
#[Out]# array([], dtype=object)
final.head()
#[Out]#   state/region     ages  year  population    state  area (sq. mi)
#[Out]# 0           AL  under18  2012   1117489.0  Alabama        52423.0
#[Out]# 1           AL    total  2012   4817528.0  Alabama        52423.0
#[Out]# 2           AL  under18  2010   1130966.0  Alabama        52423.0
#[Out]# 3           AL    total  2010   4785570.0  Alabama        52423.0
#[Out]# 4           AL  under18  2011   1125763.0  Alabama        52423.0
data2010 = final.query('year==2010 & ages=="total"')
data2010.head()
#[Out]#     state/region   ages  year  population       state  area (sq. mi)
#[Out]# 3             AL  total  2010   4785570.0     Alabama        52423.0
#[Out]# 91            AK  total  2010    713868.0      Alaska       656425.0
#[Out]# 101           AZ  total  2010   6408790.0     Arizona       114006.0
#[Out]# 189           AR  total  2010   2922280.0    Arkansas        53182.0
#[Out]# 197           CA  total  2010  37333601.0  California       163707.0
data2010.s_index('state',inplace=True)
data2010.set_index('state',inplace=True)
data2010.head()
#[Out]#            state/region   ages  year  population  area (sq. mi)
#[Out]# state                                                          
#[Out]# Alabama              AL  total  2010   4785570.0        52423.0
#[Out]# Alaska               AK  total  2010    713868.0       656425.0
#[Out]# Arizona              AZ  total  2010   6408790.0       114006.0
#[Out]# Arkansas             AR  total  2010   2922280.0        53182.0
#[Out]# California           CA  total  2010  37333601.0       163707.0
density = data2010['population'] /data2010['area (sq. mi)']
density.sort_values(ascending=False,inplace=True)
type(density)
#[Out]# pandas.core.series.Series
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
import seaborn as sns
planets = sns.load_dataset('planets')
planets = sns.load_dataset('planets')
get_ipython().run_line_magic('ls', '')
planets = sns.load_dataset('planets')
planets = sns.load_dataset('planets')
planets = sns.load_dataset('planets')?
sns.load_dataset('planets')?
get_ipython().run_line_magic('pinfo', 'sns.load_dataset')
sns.get_dataset.names
get_ipython().run_line_magic('ls', '')
data = pd.read_csv('planets.csv')
data.head()
#[Out]#             method  number  orbital_period   mass  distance  year
#[Out]# 0  Radial Velocity       1         269.300   7.10     77.40  2006
#[Out]# 1  Radial Velocity       1         874.774   2.21     56.95  2008
#[Out]# 2  Radial Velocity       1         763.000   2.60     19.84  2011
#[Out]# 3  Radial Velocity       1         326.030  19.40    110.62  2007
#[Out]# 4  Radial Velocity       1         516.220  10.50    119.47  2009
data.columns
#[Out]# Index(['method', 'number', 'orbital_period', 'mass', 'distance', 'year'], dtype='object')
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
df = pd.DataFra({'A':rng.rand(5),'B':rng.rand(5)})
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
df.mean(1)
#[Out]# 0    0.088290
#[Out]# 1    0.513997
#[Out]# 2    0.849309
#[Out]# 3    0.406727
#[Out]# 4    0.444949
#[Out]# dtype: float64
df.mean(0)
#[Out]# A    0.477888
#[Out]# B    0.443420
#[Out]# dtype: float64
data.head()
#[Out]#             method  number  orbital_period   mass  distance  year
#[Out]# 0  Radial Velocity       1         269.300   7.10     77.40  2006
#[Out]# 1  Radial Velocity       1         874.774   2.21     56.95  2008
#[Out]# 2  Radial Velocity       1         763.000   2.60     19.84  2011
#[Out]# 3  Radial Velocity       1         326.030  19.40    110.62  2007
#[Out]# 4  Radial Velocity       1         516.220  10.50    119.47  2009
data.fropna().describe()
data.dropna().describe()
#[Out]#           number  orbital_period        mass    distance         year
#[Out]# count  498.00000      498.000000  498.000000  498.000000   498.000000
#[Out]# mean     1.73494      835.778671    2.509320   52.068213  2007.377510
#[Out]# std      1.17572     1469.128259    3.636274   46.596041     4.167284
#[Out]# min      1.00000        1.328300    0.003600    1.350000  1989.000000
#[Out]# 25%      1.00000       38.272250    0.212500   24.497500  2005.000000
#[Out]# 50%      1.00000      357.000000    1.245000   39.940000  2009.000000
#[Out]# 75%      2.00000      999.600000    2.867500   59.332500  2011.000000
#[Out]# max      6.00000    17337.500000   25.000000  354.000000  2014.000000
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],'data': range(6)}, columns=['key', 'data'])
df
#[Out]#   key  data
#[Out]# 0   A     0
#[Out]# 1   B     1
#[Out]# 2   C     2
#[Out]# 3   A     3
#[Out]# 4   B     4
#[Out]# 5   C     5
df.groupby('key')
#[Out]# <pandas.core.groupby.DataFrameGroupBy object at 0x000001D07E8C0E10>
df.groupby('key').sum()
#[Out]#      data
#[Out]# key      
#[Out]# A       3
#[Out]# B       5
#[Out]# C       7
data.columns
#[Out]# Index(['method', 'number', 'orbital_period', 'mass', 'distance', 'year'], dtype='object')
data.groupby('method')['orbital_period'].median()
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
data['method'].unique()
#[Out]# array(['Radial Velocity', 'Imaging', 'Eclipse Timing Variations',
#[Out]#        'Transit', 'Astrometry', 'Transit Timing Variations',
#[Out]#        'Orbital Brightness Modulation', 'Microlensing', 'Pulsar Timing',
#[Out]#        'Pulsation Timing Variations'], dtype=object)
for (method,group) in data.groupby('method'):
    print('{0:30s} shape = {1}'.format(method,group.shape))
    
data.groupby('method').sum()
#[Out]#                                number  orbital_period        mass   distance  \
#[Out]# method                                                                         
#[Out]# Astrometry                          2    1.262360e+03     0.00000      35.75   
#[Out]# Eclipse Timing Variations          15    4.276480e+04    10.25000    1261.44   
#[Out]# Imaging                            50    1.418973e+06     0.00000    2166.91   
#[Out]# Microlensing                       27    2.207500e+04     0.00000   41440.00   
#[Out]# Orbital Brightness Modulation       5    2.127920e+00     0.00000    2360.00   
#[Out]# Pulsar Timing                      11    3.671511e+04     0.00000    1200.00   
#[Out]# Pulsation Timing Variations         1    1.170000e+03     0.00000       0.00   
#[Out]# Radial Velocity                   952    4.553151e+05  1341.65638   27348.11   
#[Out]# Transit                           776    8.377523e+03     1.47000  134242.77   
#[Out]# Transit Timing Variations           9    2.393505e+02     0.00000    3313.00   
#[Out]# 
#[Out]#                                   year  
#[Out]# method                                  
#[Out]# Astrometry                        4023  
#[Out]# Eclipse Timing Variations        18090  
#[Out]# Imaging                          76347  
#[Out]# Microlensing                     46225  
#[Out]# Orbital Brightness Modulation     6035  
#[Out]# Pulsar Timing                     9992  
#[Out]# Pulsation Timing Variations       2007  
#[Out]# Radial Velocity                1110158  
#[Out]# Transit                         798461  
#[Out]# Transit Timing Variations         8050  
data.groupby('method')['year'].describe().unstack()
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
data.groupby('method')['year'].describe()
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
data.groupby('method')['year'].describe().
data.groupby('method')['year'].describe().unstack(level=0)
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
data.groupby('method')['year'].describe().unstack(level=1)
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
data.groupby('method')['year'].describe()
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
data.groupby('method')['year'].describe().index
#[Out]# Index(['Astrometry', 'Eclipse Timing Variations', 'Imaging', 'Microlensing',
#[Out]#        'Orbital Brightness Modulation', 'Pulsar Timing',
#[Out]#        'Pulsation Timing Variations', 'Radial Velocity', 'Transit',
#[Out]#        'Transit Timing Variations'],
#[Out]#       dtype='object', name='method')
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],'data1': range(6),'data2': rng.randint(0, 10, 6)},columns = ['key', 'data1', 'data2'])
df
#[Out]#   key  data1  data2
#[Out]# 0   A      0      4
#[Out]# 1   B      1      0
#[Out]# 2   C      2      9
#[Out]# 3   A      3      5
#[Out]# 4   B      4      8
#[Out]# 5   C      5      0
df.groupby('key').aggregate(['min',np.median,max])
#[Out]#     data1            data2           
#[Out]#       min median max   min median max
#[Out]# key                                  
#[Out]# A       0    1.5   3     4    4.5   5
#[Out]# B       1    2.5   4     0    4.0   8
#[Out]# C       2    3.5   5     0    4.5   9
df.groupby('key').aggregate({'data1':'min','data2':'max'})
#[Out]#      data1  data2
#[Out]# key              
#[Out]# A        0      5
#[Out]# B        1      8
#[Out]# C        2      9
def filter_func(x):
    return x['data2'].std() > 4
df['data2'].std()
#[Out]# 3.8297084310253524
df.groupby('key').std()
#[Out]#        data1     data2
#[Out]# key                   
#[Out]# A    2.12132  0.707107
#[Out]# B    2.12132  5.656854
#[Out]# C    2.12132  6.363961
df.groupby('key').filter(filter_func)
#[Out]#   key  data1  data2
#[Out]# 1   B      1      0
#[Out]# 2   C      2      9
#[Out]# 4   B      4      8
#[Out]# 5   C      5      0
df.groupby('key').transform(lambad x:x - x.mean())
df.groupby('key').transform(lambda x:x - x.mean())
#[Out]#    data1  data2
#[Out]# 0   -1.5   -0.5
#[Out]# 1   -1.5   -4.0
#[Out]# 2   -1.5    4.5
#[Out]# 3    1.5    0.5
#[Out]# 4    1.5    4.0
#[Out]# 5    1.5   -4.5
df.apply(lambda x:x - x.mean())
df[['data1','data2']].apply(lambda x:x - x.mean())
#[Out]#    data1     data2
#[Out]# 0   -2.5 -0.333333
#[Out]# 1   -1.5 -4.333333
#[Out]# 2   -0.5  4.666667
#[Out]# 3    0.5  0.666667
#[Out]# 4    1.5  3.666667
#[Out]# 5    2.5 -4.333333
df['data1'].apply(lambda x:x - x.mean())
df['data1'].apply(lambda x:x - x.mean())
df.mean()
#[Out]# data1    2.500000
#[Out]# data2    4.333333
#[Out]# dtype: float64
df['data1'].mean()
#[Out]# 2.5
df - df['data1'].mean()
df['data1'] - df['data1'].mean()
#[Out]# 0   -2.5
#[Out]# 1   -1.5
#[Out]# 2   -0.5
#[Out]# 3    0.5
#[Out]# 4    1.5
#[Out]# 5    2.5
#[Out]# Name: data1, dtype: float64
df['data2'] - df['data2'].mean()
#[Out]# 0   -0.333333
#[Out]# 1   -4.333333
#[Out]# 2    4.666667
#[Out]# 3    0.666667
#[Out]# 4    3.666667
#[Out]# 5   -4.333333
#[Out]# Name: data2, dtype: float64
df
#[Out]#   key  data1  data2
#[Out]# 0   A      0      4
#[Out]# 1   B      1      0
#[Out]# 2   C      2      9
#[Out]# 3   A      3      5
#[Out]# 4   B      4      8
#[Out]# 5   C      5      0
def norm_by_data2(x):
    x['data1'] /= x['data2'].sum()
    return x
df
#[Out]#   key  data1  data2
#[Out]# 0   A      0      4
#[Out]# 1   B      1      0
#[Out]# 2   C      2      9
#[Out]# 3   A      3      5
#[Out]# 4   B      4      8
#[Out]# 5   C      5      0
df.groupby('key').apply(norm_by_data2)
#[Out]#   key     data1  data2
#[Out]# 0   A  0.000000      4
#[Out]# 1   B  0.125000      0
#[Out]# 2   C  0.222222      9
#[Out]# 3   A  0.333333      5
#[Out]# 4   B  0.500000      8
#[Out]# 5   C  0.555556      0
decade = 10 * (planets['year'] //10)
decade = 10 * (data['year'] //10)
decade
#[Out]# 0       2000
#[Out]# 1       2000
#[Out]# 2       2010
#[Out]# 3       2000
#[Out]# 4       2000
#[Out]# 5       2000
#[Out]# 6       2000
#[Out]# 7       1990
#[Out]# 8       2000
#[Out]# 9       2010
#[Out]# 10      2010
#[Out]# 11      2000
#[Out]# 12      2000
#[Out]# 13      1990
#[Out]# 14      2000
#[Out]# 15      2000
#[Out]# 16      1990
#[Out]# 17      1990
#[Out]# 18      2000
#[Out]# 19      2000
#[Out]# 20      2010
#[Out]# 21      2000
#[Out]# 22      2000
#[Out]# 23      2000
#[Out]# 24      2000
#[Out]# 25      1990
#[Out]# 26      2010
#[Out]# 27      2000
#[Out]# 28      2010
#[Out]# 29      2000
#[Out]#         ... 
#[Out]# 1005    2010
#[Out]# 1006    2010
#[Out]# 1007    2010
#[Out]# 1008    2010
#[Out]# 1009    2010
#[Out]# 1010    2010
#[Out]# 1011    2010
#[Out]# 1012    2010
#[Out]# 1013    2010
#[Out]# 1014    2010
#[Out]# 1015    2010
#[Out]# 1016    2010
#[Out]# 1017    2010
#[Out]# 1018    2010
#[Out]# 1019    2010
#[Out]# 1020    2010
#[Out]# 1021    2010
#[Out]# 1022    2010
#[Out]# 1023    2010
#[Out]# 1024    2010
#[Out]# 1025    2010
#[Out]# 1026    2010
#[Out]# 1027    2010
#[Out]# 1028    2010
#[Out]# 1029    2010
#[Out]# 1030    2000
#[Out]# 1031    2000
#[Out]# 1032    2000
#[Out]# 1033    2000
#[Out]# 1034    2000
#[Out]# Name: year, Length: 1035, dtype: int64
decade = decade.astype(str) + 's'
decade.dtype
#[Out]# dtype('O')
decade
#[Out]# 0       2000s
#[Out]# 1       2000s
#[Out]# 2       2010s
#[Out]# 3       2000s
#[Out]# 4       2000s
#[Out]# 5       2000s
#[Out]# 6       2000s
#[Out]# 7       1990s
#[Out]# 8       2000s
#[Out]# 9       2010s
#[Out]# 10      2010s
#[Out]# 11      2000s
#[Out]# 12      2000s
#[Out]# 13      1990s
#[Out]# 14      2000s
#[Out]# 15      2000s
#[Out]# 16      1990s
#[Out]# 17      1990s
#[Out]# 18      2000s
#[Out]# 19      2000s
#[Out]# 20      2010s
#[Out]# 21      2000s
#[Out]# 22      2000s
#[Out]# 23      2000s
#[Out]# 24      2000s
#[Out]# 25      1990s
#[Out]# 26      2010s
#[Out]# 27      2000s
#[Out]# 28      2010s
#[Out]# 29      2000s
#[Out]#         ...  
#[Out]# 1005    2010s
#[Out]# 1006    2010s
#[Out]# 1007    2010s
#[Out]# 1008    2010s
#[Out]# 1009    2010s
#[Out]# 1010    2010s
#[Out]# 1011    2010s
#[Out]# 1012    2010s
#[Out]# 1013    2010s
#[Out]# 1014    2010s
#[Out]# 1015    2010s
#[Out]# 1016    2010s
#[Out]# 1017    2010s
#[Out]# 1018    2010s
#[Out]# 1019    2010s
#[Out]# 1020    2010s
#[Out]# 1021    2010s
#[Out]# 1022    2010s
#[Out]# 1023    2010s
#[Out]# 1024    2010s
#[Out]# 1025    2010s
#[Out]# 1026    2010s
#[Out]# 1027    2010s
#[Out]# 1028    2010s
#[Out]# 1029    2010s
#[Out]# 1030    2000s
#[Out]# 1031    2000s
#[Out]# 1032    2000s
#[Out]# 1033    2000s
#[Out]# 1034    2000s
#[Out]# Name: year, Length: 1035, dtype: object
decade.name = 'decade'
decade
#[Out]# 0       2000s
#[Out]# 1       2000s
#[Out]# 2       2010s
#[Out]# 3       2000s
#[Out]# 4       2000s
#[Out]# 5       2000s
#[Out]# 6       2000s
#[Out]# 7       1990s
#[Out]# 8       2000s
#[Out]# 9       2010s
#[Out]# 10      2010s
#[Out]# 11      2000s
#[Out]# 12      2000s
#[Out]# 13      1990s
#[Out]# 14      2000s
#[Out]# 15      2000s
#[Out]# 16      1990s
#[Out]# 17      1990s
#[Out]# 18      2000s
#[Out]# 19      2000s
#[Out]# 20      2010s
#[Out]# 21      2000s
#[Out]# 22      2000s
#[Out]# 23      2000s
#[Out]# 24      2000s
#[Out]# 25      1990s
#[Out]# 26      2010s
#[Out]# 27      2000s
#[Out]# 28      2010s
#[Out]# 29      2000s
#[Out]#         ...  
#[Out]# 1005    2010s
#[Out]# 1006    2010s
#[Out]# 1007    2010s
#[Out]# 1008    2010s
#[Out]# 1009    2010s
#[Out]# 1010    2010s
#[Out]# 1011    2010s
#[Out]# 1012    2010s
#[Out]# 1013    2010s
#[Out]# 1014    2010s
#[Out]# 1015    2010s
#[Out]# 1016    2010s
#[Out]# 1017    2010s
#[Out]# 1018    2010s
#[Out]# 1019    2010s
#[Out]# 1020    2010s
#[Out]# 1021    2010s
#[Out]# 1022    2010s
#[Out]# 1023    2010s
#[Out]# 1024    2010s
#[Out]# 1025    2010s
#[Out]# 1026    2010s
#[Out]# 1027    2010s
#[Out]# 1028    2010s
#[Out]# 1029    2010s
#[Out]# 1030    2000s
#[Out]# 1031    2000s
#[Out]# 1032    2000s
#[Out]# 1033    2000s
#[Out]# 1034    2000s
#[Out]# Name: decade, Length: 1035, dtype: object
data.groupby(['method',decade])['number'].sum().unstack()
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
data.groupby(['method',decade])['number'].sum().unstack().fill_na(0)
data.groupby(['method',decade])['number'].sum().unstack().fillna(0)
#[Out]# decade                         1980s  1990s  2000s  2010s
#[Out]# method                                                   
#[Out]# Astrometry                       0.0    0.0    0.0    2.0
#[Out]# Eclipse Timing Variations        0.0    0.0    5.0   10.0
#[Out]# Imaging                          0.0    0.0   29.0   21.0
#[Out]# Microlensing                     0.0    0.0   12.0   15.0
#[Out]# Orbital Brightness Modulation    0.0    0.0    0.0    5.0
#[Out]# Pulsar Timing                    0.0    9.0    1.0    1.0
#[Out]# Pulsation Timing Variations      0.0    0.0    1.0    0.0
#[Out]# Radial Velocity                  1.0   52.0  475.0  424.0
#[Out]# Transit                          0.0    0.0   64.0  712.0
#[Out]# Transit Timing Variations        0.0    0.0    0.0    9.0
data.columns
#[Out]# Index(['method', 'number', 'orbital_period', 'mass', 'distance', 'year'], dtype='object')
data.index.name
data.index
#[Out]# RangeIndex(start=0, stop=1035, step=1)
decade.name
#[Out]# 'decade'
decade
#[Out]# 0       2000s
#[Out]# 1       2000s
#[Out]# 2       2010s
#[Out]# 3       2000s
#[Out]# 4       2000s
#[Out]# 5       2000s
#[Out]# 6       2000s
#[Out]# 7       1990s
#[Out]# 8       2000s
#[Out]# 9       2010s
#[Out]# 10      2010s
#[Out]# 11      2000s
#[Out]# 12      2000s
#[Out]# 13      1990s
#[Out]# 14      2000s
#[Out]# 15      2000s
#[Out]# 16      1990s
#[Out]# 17      1990s
#[Out]# 18      2000s
#[Out]# 19      2000s
#[Out]# 20      2010s
#[Out]# 21      2000s
#[Out]# 22      2000s
#[Out]# 23      2000s
#[Out]# 24      2000s
#[Out]# 25      1990s
#[Out]# 26      2010s
#[Out]# 27      2000s
#[Out]# 28      2010s
#[Out]# 29      2000s
#[Out]#         ...  
#[Out]# 1005    2010s
#[Out]# 1006    2010s
#[Out]# 1007    2010s
#[Out]# 1008    2010s
#[Out]# 1009    2010s
#[Out]# 1010    2010s
#[Out]# 1011    2010s
#[Out]# 1012    2010s
#[Out]# 1013    2010s
#[Out]# 1014    2010s
#[Out]# 1015    2010s
#[Out]# 1016    2010s
#[Out]# 1017    2010s
#[Out]# 1018    2010s
#[Out]# 1019    2010s
#[Out]# 1020    2010s
#[Out]# 1021    2010s
#[Out]# 1022    2010s
#[Out]# 1023    2010s
#[Out]# 1024    2010s
#[Out]# 1025    2010s
#[Out]# 1026    2010s
#[Out]# 1027    2010s
#[Out]# 1028    2010s
#[Out]# 1029    2010s
#[Out]# 1030    2000s
#[Out]# 1031    2000s
#[Out]# 1032    2000s
#[Out]# 1033    2000s
#[Out]# 1034    2000s
#[Out]# Name: decade, Length: 1035, dtype: object
data.head()
#[Out]#             method  number  orbital_period   mass  distance  year
#[Out]# 0  Radial Velocity       1         269.300   7.10     77.40  2006
#[Out]# 1  Radial Velocity       1         874.774   2.21     56.95  2008
#[Out]# 2  Radial Velocity       1         763.000   2.60     19.84  2011
#[Out]# 3  Radial Velocity       1         326.030  19.40    110.62  2007
#[Out]# 4  Radial Velocity       1         516.220  10.50    119.47  2009
decade.head()
#[Out]# 0    2000s
#[Out]# 1    2000s
#[Out]# 2    2010s
#[Out]# 3    2000s
#[Out]# 4    2000s
#[Out]# Name: decade, dtype: object
data.groupby(['method',decade])['number'].sum()
#[Out]# method                         decade
#[Out]# Astrometry                     2010s       2
#[Out]# Eclipse Timing Variations      2000s       5
#[Out]#                                2010s      10
#[Out]# Imaging                        2000s      29
#[Out]#                                2010s      21
#[Out]# Microlensing                   2000s      12
#[Out]#                                2010s      15
#[Out]# Orbital Brightness Modulation  2010s       5
#[Out]# Pulsar Timing                  1990s       9
#[Out]#                                2000s       1
#[Out]#                                2010s       1
#[Out]# Pulsation Timing Variations    2000s       1
#[Out]# Radial Velocity                1980s       1
#[Out]#                                1990s      52
#[Out]#                                2000s     475
#[Out]#                                2010s     424
#[Out]# Transit                        2000s      64
#[Out]#                                2010s     712
#[Out]# Transit Timing Variations      2010s       9
#[Out]# Name: number, dtype: int64
data.shape
#[Out]# (1035, 6)
decade.shape
#[Out]# (1035,)
data.groupby(['method',decade])['number'].sum().unstack()
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
decade.value_counts
#[Out]# <bound method IndexOpsMixin.value_counts of 0       2000s
#[Out]# 1       2000s
#[Out]# 2       2010s
#[Out]# 3       2000s
#[Out]# 4       2000s
#[Out]# 5       2000s
#[Out]# 6       2000s
#[Out]# 7       1990s
#[Out]# 8       2000s
#[Out]# 9       2010s
#[Out]# 10      2010s
#[Out]# 11      2000s
#[Out]# 12      2000s
#[Out]# 13      1990s
#[Out]# 14      2000s
#[Out]# 15      2000s
#[Out]# 16      1990s
#[Out]# 17      1990s
#[Out]# 18      2000s
#[Out]# 19      2000s
#[Out]# 20      2010s
#[Out]# 21      2000s
#[Out]# 22      2000s
#[Out]# 23      2000s
#[Out]# 24      2000s
#[Out]# 25      1990s
#[Out]# 26      2010s
#[Out]# 27      2000s
#[Out]# 28      2010s
#[Out]# 29      2000s
#[Out]#         ...  
#[Out]# 1005    2010s
#[Out]# 1006    2010s
#[Out]# 1007    2010s
#[Out]# 1008    2010s
#[Out]# 1009    2010s
#[Out]# 1010    2010s
#[Out]# 1011    2010s
#[Out]# 1012    2010s
#[Out]# 1013    2010s
#[Out]# 1014    2010s
#[Out]# 1015    2010s
#[Out]# 1016    2010s
#[Out]# 1017    2010s
#[Out]# 1018    2010s
#[Out]# 1019    2010s
#[Out]# 1020    2010s
#[Out]# 1021    2010s
#[Out]# 1022    2010s
#[Out]# 1023    2010s
#[Out]# 1024    2010s
#[Out]# 1025    2010s
#[Out]# 1026    2010s
#[Out]# 1027    2010s
#[Out]# 1028    2010s
#[Out]# 1029    2010s
#[Out]# 1030    2000s
#[Out]# 1031    2000s
#[Out]# 1032    2000s
#[Out]# 1033    2000s
#[Out]# 1034    2000s
#[Out]# Name: decade, Length: 1035, dtype: object>
decade.value_counts()
#[Out]# 2010s    597
#[Out]# 2000s    406
#[Out]# 1990s     31
#[Out]# 1980s      1
#[Out]# Name: decade, dtype: int64
data['method'].value_counts()
#[Out]# Radial Velocity                  553
#[Out]# Transit                          397
#[Out]# Imaging                           38
#[Out]# Microlensing                      23
#[Out]# Eclipse Timing Variations          9
#[Out]# Pulsar Timing                      5
#[Out]# Transit Timing Variations          4
#[Out]# Orbital Brightness Modulation      3
#[Out]# Astrometry                         2
#[Out]# Pulsation Timing Variations        1
#[Out]# Name: method, dtype: int64
get_ipython().run_line_magic('logstate', '')
get_ipython().run_line_magic('logstop', '')
