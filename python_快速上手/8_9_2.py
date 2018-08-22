#coding=utf-8
#python3
#一个文件中替换指定单词

import re

filename = input('filename: ')

lg = input('replace liugang: ')
mdd = input('replace madongdong: ')
zmy = input('replace zhangmingyu: ')

file = open(filename)

fileread = file.read()

relg = re.compile(r'liugang')
remdd = re.compile(r'madongdong')
rezmy = re.compile(r'zhangmingyu')

lgsub = relg.sub(lg,fileread)
mddsub = remdd.sub(mdd,lgsub)
zmysub = rezmy.sub(zmy,mddsub)

print(zmysub)

file.close()

filesub = open('filesub.txt','w')

filesub.write(zmysub)

filesub.close()
