# -*- coding: utf-8 -*-
"""
创建时间 Fri Nov 30 17:37:27 2018
描述:读取log文件带有闪断的端口
作者:PM.liugang
"""

import re
fn = open('webapp.log')
fc = fn.readlines()

for i in fc:
    if '"flicker": true' in i:
        print (i[80:90],i[-20:-1])
        

