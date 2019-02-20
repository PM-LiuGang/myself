# -*- coding: utf-8 -*-
"""
创建时间 Mon Feb 18 11:02:16 2019
作者:PM.liugang
描述:
遗留：
截止到p46
"""

import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

pd.set_option('display.max_columns',30)
pd.set_option('display.max_colwidth',100)
pd.set_option('display.precision',3)

csv_path = 'magic.csv'
df = pd.read_csv(csv_path)
print(df.columns)
#print(df.head().T)

mu = df[df['listingtype_value'].str.contains('Apartments For')]
su = df[df['listingtype_value'].str.contains('Apartment For')]

print('multiple units numbers:', len(mu))
print('single units numbers:', len(su))

noStudioBd = len(su[~(su['propertyinfo_value'].str.contains('Studio')\
         |su['propertyinfo_value'].str.contains('bd'))])
noBa = len(su[~(su['propertyinfo_value'].str.contains('ba'))])

print('检查没有包含bd或Studio的行数:',noStudioBd)
print('检查没有包含ba行数:',noBa)

noBaths = su[~(su['propertyinfo_value'].str.contains('ba'))]
sucln = su[~su.index.isin(noBaths.index)]

def parse_info(row):
    '''
    使用项目符号进行切分
    Parameters
    ----------
    row : str 
        
    Return
    ------
    pd.Series
    '''
    if not 'sqrt' in row:
        br, ba = row.split(' ')[:2]
        sqft = np.nan
    else:
        br, ba, sqft = row.split('.')[:3]
    return pd.Series({'Beds':br, 'Bath':ba, 'Sqft':sqft})


attr = sucln['propertyinfo_value'].apply(parse_info)
print('浴室 | 卧室 | 平方英尺：',attr)

'''在取值中将字符串删除'''
attr_cln = attr.applymap(lambda x: x.strip().split(' ')[0] \
                         if isinstance(x,str) else np.nan)

print('在取值中将字符串删除',attr_cln)

sujnd = sucln.join(attr_cln)
print((sujnd.T).head(5))

def parse_addy(r):
    '''
    
    Parameters
    ----------
    r : str
    
    Returns
    -------
    pd.Series
    '''
    soZip = re.search(', NY(\d+)', r)
    soFlr = re.search('(?:APT|#)\s+(\d+)[A-Z]+,', r)
    if soZip:
        zipc = soZip.group(1)
    else:
        zipc = np.nan
    
    if soFlr:
        flr = soFlr.group(1) # (\d+)第一个分组
    else:
        flr = np.nan
    return pd.Series({'Zip':zipc, 'Floor':flr})


flrzip = sujnd['routable_link/_text'].apply(parse_addy)
suf = sujnd.join(flrzip) # on=None how='left' sort=False
print((suf.T).head(5))

'''重命名奇怪的列名，并重置索引'''
sudf = suf[['pricelarge_value_prices', 'Beds', 'Bath', 'Sqft', 'Floor', 'Zip']]
sudf.rename(columns={'pricelarge_value_prices':'租金',
                     'Beds':'卧室',
                     'Bath':'浴室',
                     'Sqft':'平方英尺',
                     'Floor':'楼层',
                     'Zip':'邮政编码'}, inplace=True)
sudf.reset_index(drop=True, inplace=True) # drop=True reset columns index to the default integer index
print(sudf)





