# -*- coding: utf-8 -*-
"""
如何一个文件夹的文本文件汇总成一个文本 
一个文件夹里面多个文件夹，每个文件夹输出一个文档，每个文件夹下可能还含有文件夹，多次嵌套 
输出的文档要求在文件根目录，输出的文档的文件名称同对应的文件夹名 
代码文件中的缩进格式不能破坏 
打印每个汇总文件后的总行数，每个总文件汇总了多少个文件的内容 
生成exe
"""

import os 

file_dir = 'C:\\Users\\Administrator\\Desktop\\agg_file'
os.chdir(file_dir)

file_name = []
file_dir_name = []
#根据目录名称创建2个空的txt文件
for i in os.listdir():
    if not os.path.isdir(os.path.join(file_dir,i)):
        with open(i+'.txt','w') as fn:
            pass
#获取两个新创建的空文件名称        
for i in os.walk(file_dir):
    for h in i[2]:
        file_name.append(h)
    break

for i in os.walk(file_dir):
    for h in i[1]:
        file_dir_name.append(h)
    break


fns1 = open(file_name[0]+'.txt','a+',errors='ignore',encoding='gbk')
fns2 = open(file_name[1]+'.txt','a+',errors='ignore',encoding='gbk')
        
for i in os.walk(os.path.join(file_dir,file_dir_name[0])):
    if int(len(i[2])) > 0:#有的目录可能没有文件
        for h in i[2]:#获取文件名    
            with open(os.path.join(i[0],h),'r') as fnd:
                data = fnd.readlines()
                for m in data:
                    fns1.writelines(m+'\n')
     
for i in os.walk(os.path.join(file_dir,file_dir_name[1])):
    if int(len(i[2])) > 0:#有的目录可能没有文件
        for h in i[2]:#获取文件名    
            with open(os.path.join(i[0],h),'r') as fnd:
                data = fnd.readlines()
                for m in data:
                    fns1.writelines(m+'\n')
            