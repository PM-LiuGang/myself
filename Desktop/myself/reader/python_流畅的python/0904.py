# IPython log file

import prettytable
table = prettytable.PrettyTable()
table_name = [[],['yes'],['no']]
table_content_1 = [['Yes'],['TP'],['FN'],['P']]
table_name = [[],['yes'],['no'],[]]
table_content_2 = [['No'],['TP'],['TN'],['N']]
table_content_3 = [[],['P“'],['N”'],['P+N']]
table.field_names = table_name
get_ipython().run_line_magic('pinfo', 'table.fields')
table.field_names = table_name
get_ipython().run_line_magic('pinfo2', 'table.field_names')
get_ipython().run_line_magic('pinfo', 'table.field_names')
get_ipython().run_line_magic('pinfo2', 'table.field_names')
table_name
#[Out]# [[], ['yes'], ['no'], []]
table_name = [[-],['Yes'],['No'],[]]
table_name = [['-'],['Yes'],['No'],[]]
table.field_names = table_name
table.add_row(table_content_1)
table.add_row(table_content_2)
table.add_row(table_content_3)
table
#[Out]# <prettytable.PrettyTable object at 0x000000000977C5F8>
print(table)
table_name = [['元组序号'],['类'],['概率'],['TP'],['FP'],['TN'],['FN'],['TPR'],['FPR']]
table_content_1 = [['1'],['P'],['0.90'],[1],[0],[5],[4],[0.2],[0]]
table = prettytable.PrettyTable()
table.field_names = table_name
table.add_row(table_content_1)
table
#[Out]# <prettytable.PrettyTable object at 0x0000000009793550>
import pprint
pprint.pprint(table)
print(table)
get_ipython().run_line_magic('pwd', '')
#[Out]# 'C:\\Users\\Administrator'
get_ipython().run_line_magic('cd', 'main')
get_ipython().run_line_magic('cd', '刷过的书/python_流畅的/')
symbols = '@#￥%&*’
symbols = '@#￥%&*'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
    
codes
#[Out]# [64, 35, 65509, 37, 38, 42]
codes = [ord(symbol) for symbol in symbols]
codes
#[Out]# [64, 35, 65509, 37, 38, 42]
x = 'ABC'
dummy = [ord(x) for x in x]
x
#[Out]# 'ABC'
dummy
#[Out]# [65, 66, 67]
# ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常
symbols
#[Out]# '@#￥%&*'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii
#[Out]# [65509]
beyond_ascii = list(filter(lambda c:c > 127,map(ord,symbols)))
beyond_ascii
#[Out]# [65509]
# filter函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表
# python3 返回迭代器对象
# filter（function，iterable）
colors = ['black','white']
sizes = ['S','M','L']
tshirts = [ (color,size) for color in colors for size in sizes]
tshirts
#[Out]# [('black', 'S'),
#[Out]#  ('black', 'M'),
#[Out]#  ('black', 'L'),
#[Out]#  ('white', 'S'),
#[Out]#  ('white', 'M'),
#[Out]#  ('white', 'L')]
# 两种颜色 三种尺寸
tshirts = [ (color,size) for size in sizes for color in colors]
tshirts
#[Out]# [('black', 'S'),
#[Out]#  ('white', 'S'),
#[Out]#  ('black', 'M'),
#[Out]#  ('white', 'M'),
#[Out]#  ('black', 'L'),
#[Out]#  ('white', 'L')]
tuple(ord(symbol) for symbol in symbols)
#[Out]# (64, 35, 65509, 37, 38, 42)
import array
array.array('I',(ord(symbol) for symbol in symbols))
#[Out]# array('I', [64, 35, 65509, 37, 38, 42])
type('I',(ord(symbol) for symbol in symbols))
type((ord(symbol) for symbol in symbols))
#[Out]# generator
# array (数组中数字的存储方式，存储对象）
# 利用生成器表达式实现了一个笛卡尔积
# 每次for循环运行时才生成一个组合
colors
#[Out]# ['black', 'white']
sizes
#[Out]# ['S', 'M', 'L']
for tshirt in ('%s %s' %(c, s) for c in colors for s in sizes):
    print(tshirt)
    
lax_coordinates = (33.9425, -118.408056)
city, year , pop, chg, area = ('Tokyo',2003,32450,0.66,8014)
traveler_ids = [('USA','31195855'),('BRA','CE342567'),('ESP','XDA205856')]
_
#[Out]# ['S', 'M', 'L']
__
#[Out]# ['S', 'M', 'L']
traveler_ids
#[Out]# [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s %s' % passport)
    
type(traveler_ids)
#[Out]# list
traveler_ids
#[Out]# [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
sort(traveler_ids)
sorted(traveler_ids)
#[Out]# [('BRA', 'CE342567'), ('ESP', 'XDA205856'), ('USA', '31195855')]
for passport in sorted(traveler_ids):
    print('%s %s' % passport)
    
for country,_ in traveler_ids:
    print(country)
    
_
#[Out]# 'XDA205856'
traveler_ids
#[Out]# [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
# ↑ 元祖的拆包
divmod(20,8)
#[Out]# (2, 4)
t = (20,8)
divmod(*t)
#[Out]# (2, 4)
# 用 * 把云算法把一个可迭代对象拆开作为函数的参数
# 用 * 运算符把一个可迭代对象拆开作为函数的参数
import os
_,filename = os.path.split('')
get_ipython().run_line_magic('pwd', '')
#[Out]# 'C:\\Users\\Administrator\\Desktop\\myself\\刷过的书\\python_流畅的'
_,filename = os.path.split('C:\\Users\\Administrator\\Desktop\\myself\\刷过的书\\python_流畅的')
_
#[Out]# 'C:\\Users\\Administrator\\Desktop\\myself\\刷过的书'
filename
#[Out]# 'python_流畅的'
# 用 - 占位符 表示不感兴趣的数据
# 在python中，函数用*args来获取不确定数量的参数算是一种经典写法了
a,b,*rest = range(5)
a,b,*rest
#[Out]# (0, 1, 2, 3, 4)
*rest
# error
a,b,*rest = range(3)
a,b,*rest
#[Out]# (0, 1, 2)
a,b,rest
#[Out]# (0, 1, [2])
a,b,*rest = range(2)
a,b,rest
#[Out]# (0, 1, [])
a,*boby,c,d = range(5)
a,*boby,c,d
#[Out]# (0, 1, 2, 3, 4)
a,boby,c,d
#[Out]# (0, [1, 2], 3, 4)
*head,b,c,d = range(5)
head,b,c,d
#[Out]# ([0, 1], 2, 3, 4)
# 嵌套元祖拆包
metro_areas = [
('Tokyo','JP',36.933,(35.689722,139.691667)), # ➊
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]
metro_areas
#[Out]# [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
#[Out]#  ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
#[Out]#  ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
#[Out]#  ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
#[Out]#  ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]
_
#[Out]# 'C:\\Users\\Administrator\\Desktop\\myself\\刷过的书'
metro_areas[0]
#[Out]# ('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
metro_areas[1]
#[Out]# ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
# 城市 国家简称 unknow 经纬度
print('{:15} | {:^9} | {:^9}'.format('','lat.','long.'))
fmt = '{:15}|{:9.4f}|{:9.4f}'
for name,cc,pop,(lat,long) in metro_areas:
    if long <= 0:
        print(fmt.format(name,lat,long))
        
metro_areas
#[Out]# [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
#[Out]#  ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
#[Out]#  ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
#[Out]#  ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
#[Out]#  ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]
# 命名元组元素
import collections
from collections import namedtuple
# tuple nametuple 其实对内容消耗是一样大的
# tuple nametuple 其实对内存的消耗是一样大的
get_ipython().run_line_magic('pinfo', '%logstart')
from collections import namedtuple
city = namedtuple('City','name country population coordinates')
city
#[Out]# __main__.City
tokyo = city('tokyo','JP',36.933,(35.33,139.44))
tokyo
#[Out]# City(name='tokyo', country='JP', population=36.933, coordinates=(35.33, 139.44))
tokyo.population
#[Out]# 36.933
tokyo.coordinates
#[Out]# (35.33, 139.44)
tokyo[1]
#[Out]# 'JP'
# 创建一个命名元祖需要两个参数，一个类名，一个是各个字段名称
# 后者可以是由数字字符串组成的可迭代对象
# 或者是由空格分隔开的字段名组成的字符串
#namedtuple（类名，‘各个字段的名称’)
type(tokyo)
#[Out]# __main__.City
type(city)
#[Out]# type
#构造函数只接收单一的可迭代对象
#传递是必须分开的字符串
# 命名元组 最常用的几个属性
# _fields 类方法 _make(iterable) 类实例_asdict()
city._fields
#[Out]# ('name', 'country', 'population', 'coordinates')
latlong = namedtuple('latlong','lat long')
latlong
#[Out]# __main__.latlong
delhi_data = ('Delhi NCR','IN',21.935,latlong(28.6,77.2))
delhi = city._make(delhi_data)
delhi._asdict
#[Out]# <bound method City._asdict of City(name='Delhi NCR', country='IN', population=21.935, coordinates=latlong(lat=28.6, long=77.2))>
for k,v in delhi._asdict().items():
    print(key+ ':' ,v)
    
for k,v in delhi._asdict().items():
    print(k+ ':' ,v)
    
# _fields属性是一个包含这个类所有字段名称的元组
# _make 通过接收一个可迭代对象来生成这个类的一个实例，它的作用跟City（*delhi data)是一样的
# _asdict 把命名元组以collection.OrderedDict的形式返回，我们可以利用它把元组里的信息友好的呈现出来
#除了跟增减元素相关的方法外，元组支持列表的其他所有方法
'str'.__ladd__('ing')
'str'.__iadd__('ing')
'str'.__add__('ing')
#[Out]# 'string'
'str'.__iadd__('ing')
'string'.__contains__('str')
#[Out]# True
'string'.contains('str')
'str' in 'string'
#[Out]# True
str = 'liugang_0623_1988'
str.__delitem__(5)
str.__delitem__(p)
s = ('liu','gang','0623','115')
s.__delitem__(2)
s.__contains__('liu')
#[Out]# True
s.__delitem__('liu')
s.__getitem__('liu')
range(3)
#[Out]# range(0, 3)
l = list(range(0,60,10))
l
#[Out]# [0, 10, 20, 30, 40, 50]
l[:2]
#[Out]# [0, 10]
l[2:]
#[Out]# [20, 30, 40, 50]
l[:3]
#[Out]# [0, 10, 20]
l[3:]
#[Out]# [30, 40, 50]
s = 'bicycle1988'
s[::3]
#[Out]# 'bye8'
s[::-1]
#[Out]# '8891elcycib'
s[::-2]
#[Out]# '89eccb'
invoice="""0.....6................................40........52...55........
1909 Pimoroni PiBrella $17.50 3 $52.50
1489 6mm Tactile Switch x20 $4.95 2 $9.90
1510 Panavise Jr. - PV-201 $28.00 1 $28.00
1601 PiTFT Mini Kit 320x240 $34.95 1 $34.95
"""
invoice
#[Out]# '0.....6................................40........52...55........\n1909 Pimoroni PiBrella $17.50 3 $52.50\n1489 6mm Tactile Switch x20 $4.95 2 $9.90\n1510 Panavise Jr. - PV-201 $28.00 1 $28.00\n1601 PiTFT Mini Kit 320x240 $34.95 1 $34.95\n'
sku = slice(0,6)
sku
#[Out]# slice(0, 6, None)
description = slice(6,40)
description
#[Out]# slice(6, 40, None)
print(sku)
unit_price = slice(40,52)
quantity = slice(52,55)
item_total = slice(55,None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[unit_price],item[description])
    
line_items
#[Out]# ['1489 6mm Tactile Switch x20 $4.95 2 $9.90',
#[Out]#  '1510 Panavise Jr. - PV-201 $28.00 1 $28.00',
#[Out]#  '1601 PiTFT Mini Kit 320x240 $34.95 1 $34.95',
#[Out]#  '']
line_items[1][unit_price]
#[Out]# '00'
line_items[1]
#[Out]# '1510 Panavise Jr. - PV-201 $28.00 1 $28.00'
line_items[1][40,52]
line_items[1][40:52]
#[Out]# '00'
l = list(range(10))
l
#[Out]# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[2:5] = [20,30]
l
#[Out]# [0, 1, 20, 30, 5, 6, 7, 8, 9]
del l[5:7]
("")
#[Out]# ''
l
#[Out]# [0, 1, 20, 30, 5, 8, 9]
l[3::2] = [11,22]
l
#[Out]# [0, 1, 20, 11, 5, 22, 9]
l[2:5]
#[Out]# [20, 11, 5]
l[2:5] = 100
l[2:5] = [100]
l
#[Out]# [0, 1, 100, 22, 9]
l
#[Out]# [0, 1, 100, 22, 9]
board = [['-'] * 3 for i in range(3)]
board
#[Out]# [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
board[1][2] = 'x'
board
#[Out]# [['-', '-', '-'], ['-', '-', 'x'], ['-', '-', '-']]
board = [['-'] * 3] * 3
board
#[Out]# [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
board[1][2] = 'x'
board
#[Out]# [['-', '-', 'x'], ['-', '-', 'x'], ['-', '-', 'x']]
# ↑ 含有3个指向同一对象的引用的列表是毫无用处的
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
    
board
#[Out]# [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[2][0] = 'x'
board
#[Out]# [['x', '_', '_'], ['x', '_', '_'], ['x', '_', '_']]
type(i)
#[Out]# int
# 可变序列一般都是实现了__iadd__方法
# 不可变序列一般没有实现__iadd__方法
l = [1,2,3]
id(l)
#[Out]# 126637832
# 注意列表id的转换
l *= 2
l
#[Out]# [1, 2, 3, 1, 2, 3]
id(l)
#[Out]# 126637832
t = (1,2,3)
id(t)
#[Out]# 126495840
t *= 2
id(t)
#[Out]# 158903464
# 新的元组被创建了
[30,40]+[50,60]
#[Out]# [30, 40, 50, 60]
t = (1,2,[30,40])
t = ('liu','gang')
t[1]='g'
t = (1,2,[30,40])
t[2] += [50,60]
t
#[Out]# (1, 2, [30, 40, 50, 60])
# python tutor python赋值原理可视化
dis.dis('s[a] += b')
import dis
dis.dis('s[a] += b')
# 不要把可变对象放在元组里面
# 增量赋值不是一个原子操作
# list.sort方法会就地排序列表 不会把原列表复制一份
'''
与list.sort相反的是内置函数sorted
它会新建一个列表作为返回值
这个方法可以接收任何形式的可迭代对象作为参数
甚至包括不可变序列和生成器
不管sorted接收的是怎样的参数，他最后都会返回一个列表
'''
#[Out]# '\n与list.sort相反的是内置函数sorted\n它会新建一个列表作为返回值\n这个方法可以接收任何形式的可迭代对象作为参数\n甚至包括不可变序列和生成器\n不管sorted接收的是怎样的参数，他最后都会返回一个列表\n'
# list.sort(key=,reverse=)
#sorted(key=,reverse=)
fruits = ['grape', 'raspberry', 'apple', 'banana']
fruits
#[Out]# ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits)
#[Out]# ['apple', 'banana', 'grape', 'raspberry']
fruits
#[Out]# ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits,reverse=True)
#[Out]# ['raspberry', 'grape', 'banana', 'apple']
sorted(key=len,fruits)
sorted(fruits,key=len)
#[Out]# ['grape', 'apple', 'banana', 'raspberry']
fruits
#[Out]# ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits,key=len,reverse=True)
#[Out]# ['raspberry', 'banana', 'grape', 'apple']
fruits
#[Out]# ['grape', 'raspberry', 'apple', 'banana']
fruits = ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits,key=len,reverse=False)
#[Out]# ['grape', 'apple', 'banana', 'raspberry']
sorted(fruits,key=len,reverse=True)
#[Out]# ['raspberry', 'banana', 'grape', 'apple']
fruits
#[Out]# ['grape', 'raspberry', 'apple', 'banana']
fruits.sort()
fruits
#[Out]# ['apple', 'banana', 'grape', 'raspberry']
fruits
#[Out]# ['apple', 'banana', 'grape', 'raspberry']
fruits.sort(reverse=True)
fruits
#[Out]# ['raspberry', 'grape', 'banana', 'apple']
fruits
#[Out]# ['raspberry', 'grape', 'banana', 'apple']
# ↑ 修改原对象
import bisect
import sys
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d}      {2}{0:<2d}'
'''
'{0:*>10}'.format(10)  ##右对齐
'********10'
'{0:*<10}'.format(10)  ##左对齐
'10********'
'{0:*^10}'.format(10)  ##居中对齐
'****10****'
'''
#[Out]# "\n'{0:*>10}'.format(10)  ##右对齐\n'********10'\n'{0:*<10}'.format(10)  ##左对齐\n'10********'\n'{0:*^10}'.format(10)  ##居中对齐\n'****10****'\n"
# [填充字符][对齐方式 <^>][宽度]
'''
li
['hoho', 18]
'name is {0[0]} age is {0[1]}'.format(li)
'name is hoho age is 18
'''
#[Out]# "\nli\n['hoho', 18]\n'name is {0[0]} age is {0[1]}'.format(li)\n'name is hoho age is 18\n"
get_ipython().run_line_magic('pwd', '')
#[Out]# 'C:\\Users\\Administrator\\Desktop\\myself\\刷过的书\\python_流畅的'
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('run', 'bisect_demo.py')
get_ipython().run_line_magic('run', 'bisect_insort.py')
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))

scores
#[Out]# [(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
get_ipython().run_line_magic('pinfo', 'bisect_insort.py')
import bisect_demo
get_ipython().run_line_magic('pinfo2', 'bisect_demo')
HAYSTACK
#[Out]# [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES
#[Out]# [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
reversed(NEEDLES)
#[Out]# <list_reverseiterator at 0x78f1dd8>
print(reversed(NEEDLES))
type(reversed(NEEDLES))
#[Out]# list_reverseiterator
get_ipython().run_line_magic('pinfo2', 'bisect')
get_ipython().run_line_magic('pinfo', 'bisect')
get_ipython().run_line_magic('pinfo2', 'bisect')
HAYSTACK
#[Out]# [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
bisect(HAYSTACK,2)
import bisect
bisect(HAYSTACK,2)
bisect？
get_ipython().show_usage()
get_ipython().run_line_magic('pinfo', 'bisect')
get_ipython().run_line_magic('pinfo2', 'bisect')
bisect.bisect_left(HAYSTACK,NEEDLES)
bisect.bisect_left(HAYSTACK,11)
#[Out]# 5
HAYSTACK
#[Out]# [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
bisect.bisect_left(HAYSTACK,2)
#[Out]# 1
bisect.bisect_left(HAYSTACK,3)
#[Out]# 1
bisect.bisect_left(HAYSTACK,4)
#[Out]# 1
bisect.bisect_left(HAYSTACK,5)
#[Out]# 2
list_1 = [829,3,3333,32,33333,2]
reversed(list_1)
#[Out]# <list_reverseiterator at 0x78bc668>
for i in reversed(list_1):
    print(i)
    
list_1 = [829,3,3333,32,33333,2]
reversed(list_1)
#[Out]# <list_reverseiterator at 0x78f1f28>
list_1
#[Out]# [829, 3, 3333, 32, 33333, 2]
# reversed 反转列表
def grade(score,breakpoints=range(60,100,10),grades='FDCBA'):
    i = bisect.bisect(breakpoints,score)
    return grades[i]

[grade(score) for score in [33,99,77,70,89,90,100]]
#[Out]# ['F', 'A', 'C', 'C', 'B', 'A', 'A']
get_ipython().run_line_magic('pinfo', 'bisect.bisect')
get_ipython().run_line_magic('pinfo2', 'bisect.bisect')
from bisect import bisect
get_ipython().run_line_magic('pinfo', 'bisect')
bisect?？
get_ipython().run_line_magic('pinfo2', 'bisect')
# bisect ( [查找对象]，找的值） return 索引位置
# bisect.insort     insort(seq,item) 把变量item插入到序列seq中，并能保持seq的升序顺序
import random
random.randrange(14)
#[Out]# 0
size = 7
random.randrange(size * 2)
#[Out]# 2
get_ipython().run_line_magic('pinfo', 'random.randrange')
random.randrange(size * 2)
#[Out]# 13
random.randrange(size * 2)
#[Out]# 4
random.randrange(size * 2)
#[Out]# 8
random.randrange(size * 2)
#[Out]# 5
random.randrange(size * 2)
#[Out]# 13
random.seed(1729)
get_ipython().run_line_magic('pinfo2', 'random.randrange')
get_ipython().run_line_magic('pinfo', 'random.randrange')
'''
random.randrange?
Signature: random.randrange(start, stop=None, step=1, _int=<class 'int'>)
Docstring:
Choose a random item from range(start, stop[, step]).
'''
#[Out]# "\nrandom.randrange?\nSignature: random.randrange(start, stop=None, step=1, _int=<class 'int'>)\nDocstring:\nChoose a random item from range(start, stop[, step]).\n"
# bisect.insort(数据集，插入的值）
list_1
#[Out]# [829, 3, 3333, 32, 33333, 2]
bisect.insort(list_1,666)
bisect.insort(list_1,666)
from bisect import insort
insort(list_1,666)
list_1
#[Out]# [829, 3, 3333, 32, 33333, 2, 666]
insort(list_1,6)
list_1
#[Out]# [829, 3, 6, 3333, 32, 33333, 2, 666]
insort(list_1,6)
list_1
#[Out]# [829, 3, 6, 6, 3333, 32, 33333, 2, 666]
insort(list_1,7)
list_1
#[Out]# [829, 3, 6, 6, 7, 3333, 32, 33333, 2, 666]
insort(list_1,826)
list_1
#[Out]# [829, 3, 6, 6, 7, 826, 3333, 32, 33333, 2, 666]
insort(list_1,5555)
list_1
#[Out]# [829, 3, 6, 6, 7, 826, 3333, 32, 5555, 33333, 2, 666]
# bisect.insort(数据集，插入的值）
insort(list_1,1000000)
list_1
#[Out]# [829, 3, 6, 6, 7, 826, 3333, 32, 5555, 33333, 2, 666, 1000000]
insort(list_1,4)
list_1
#[Out]# [829, 3, 4, 6, 6, 7, 826, 3333, 32, 5555, 33333, 2, 666, 1000000]
get_ipython().run_line_magic('pinfo', 'insort')
get_ipython().run_line_magic('pinfo2', 'insort')
get_ipython().run_line_magic('pinfo', 'insort_right')
insort_right()??
get_ipython().run_line_magic('logstate', '')
get_ipython().run_line_magic('logstop', '')
