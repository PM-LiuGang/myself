# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:06:38 2019

@author: 8613810330623
"""

import pandas as pd
import os
import xlrd

path = r'C:\Users\admin\Desktop'
filename = 'N4接口测试用例 - 副本.xlsx'
#replace_dict = {'wu' : 'None', '无' : 'None'}
data = xlrd.open_workbook(os.path.join(path, filename))
sheet_names = data.sheet_names()

for sheet in sheet_names[3 : -1]: 
    df = pd.read_excel(os.path.join(path, filename), sheet_name=sheet, header=None)
    df1 = df[1]
#    df1.replace(replace_dict, inplace=True)
    df1.fillna('Null', inplace=True)
    df1_str = ','.join(map(str, df1.to_list()))
    with open(os.path.join(path, sheet+'.csv'), 'w') as f:
        f.write(df1_str)