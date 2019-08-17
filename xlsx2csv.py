# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:06:38 2019

@author: 8613810330623
"""

import pandas as pd
import os
import xlrd

path = r'D:\360MoveData\Users\86138\Desktop'
filename = 'zxl1.xlsx'
#replace_dict = {'wu' : 'None', '无' : 'None'}
data = xlrd.open_workbook(os.path.join(path, filename))
sheet_names = data.sheet_names()

for sheet in sheet_names[4 : ]: 
    df = pd.read_excel(os.path.join(path, filename), 
                       sheet_name=sheet, 
                       header=None,
                       skiprows=1,
                       encoding='gbk')
    for i in range(1,df.shape[1] + 1,2):
        df1 = df[i]
        df1.fillna('Null', inplace=True)
        df1_str = '|'.join(map(str, df1.to_list()))
        with open(os.path.join(path, sheet+ '_' + str(i) + '.csv'), 'w', encoding='utf8') as f:
            f.write(df1_str)
    