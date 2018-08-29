#!/usr/bin/env python3.5
#coding:utf-8
#
# 这个项目主要目的是字符串的处理，简单格式化输出
tableData = [['apples','oranges','cherries','banana'],
              ['Alice','Bob','Carol','David'],
              ['dogs','cats','moose','goose']]
# 要求输出如下：
#   apples  Alice  dogs
#  dranges  Bob    cats
# cherries  Carol  moose
#   banana  David  goose

#没能输出上图的格式，输出格式全部是向右对齐的
def printTable(data):
    str_data = ''
    col_len = []
    for row in range(0,len(data)):#0123,多种遍历方式
        for col in range(0,len(data[0])):#012
            col_len.append(len(data[row][col]))#00 01 02 
    max_col_len = max(col_len)
    print("列表各元素长度为：")
    print(col_len)
    print("列表中最大值为：",max_col_len)
    for row in range(0,len(data[0])):#因为内嵌列表的长度相同
        for col in range(0,len(data)):
            print(data[col][row].rjust(max_col_len,'-'),end='')#此次for循环不换行
        print()#外层for9换行
    return str_data #?

f_data = printTable(tableData)
print(f_data)