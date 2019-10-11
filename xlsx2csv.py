# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:06:38 2019
@author: 8613810330623
"""
# review 180930

import pandas as pd
import os
import xlrd

#path = r'D:\360MoveData\Users\86138\Desktop'
#filename = 'zxl1.xlsx'
file_path = r''
#replace_dict = {'wu' : 'None', '无' : 'None'}
data = xlrd.open_workbook(file_path)
sheet_names = data.sheet_names()

for sheet in sheet_names[4 : ]: 
    df = pd.read_excel(file_path, sheet_name=sheet, header=None, skiprows=1,encoding='gbk')
    for i in range(1,df.shape[1] + 1,2):
        df1 = df[i]
        df1.fillna('Null', inplace=True)
        #df1.fillna(replace_dict, inplace=True)
        df1_str = '|'.join(map(str, df1.to_list()))
        with open(sheet + str(i) + '.csv', 'w', encoding='utf8') as f:
            f.write(df1_str)
    