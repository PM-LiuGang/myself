# IPython log file

get_ipython().run_line_magic('cd', 'main')
get_ipython().run_line_magic('pwd', '')
#[Out]# 'C:\\Users\\Administrator\\Desktop\\myself'
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cd', '刷过的书/python_流畅的/')
get_ipython().run_line_magic('ls', '')
from array import array
from random import random 
floats = array('d',(random() for i in range(10**7)))
# array('b') 创建出的数组就只能一个字节大小的整数
get_ipython().run_line_magic('pinfo', 'random')
random(4)?
random(4)
random()
#[Out]# 0.14357924688839752
floats[-1]
#[Out]# 0.936669649281252
fp = open('floats.bin','wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin','rb')
floats2.fromfile(fp,10**7)
fp.close()
floats2[-1]
#[Out]# 0.936669649281252
floats2 == floats
#[Out]# True
array？
get_ipython().run_line_magic('pinfo', 'array')
'''
array(typecode [, initializer]) -> array

Return a new array whose items are restricted by typecode, and
initialized from the optional initializer value, which must be a list,
string or iterable over elements of the appropriate type.

Arrays represent basic values and behave very much like lists, except
the type of objects stored in them is constrained. The type is specified
at object creation time by using a type code, which is a single character.
The following type codes are defined:

    Type code   C Type             Minimum size in bytes 
    'b'         signed integer     1 
    'B'         unsigned integer   1 
    'u'         Unicode character  2 (see note) 
    'h'         signed integer     2 
    'H'         unsigned integer   2 
    'i'         signed integer     2 
    'I'         unsigned integer   2 
    'l'         signed integer     4 
    'L'         unsigned integer   4 
    'q'         signed integer     8 (see note) 
    'Q'         unsigned integer   8 (see note) 
    'f'         floating point     4 
    'd'         floating point     8 

NOTE: The 'u' typecode corresponds to Python's unicode character. On 
narrow builds this is 2-bytes on wide builds this is 4-bytes.

NOTE: The 'q' and 'Q' type codes are only available if the platform 
C compiler used to build Python supports 'long long', or, on Windows, 
'__int64'.

Methods:

append() -- append a new item to the end of the array
buffer_info() -- return information giving the current memory info
byteswap() -- byteswap all the items of the array
count() -- return number of occurrences of an object
extend() -- extend array by appending multiple elements from an iterable
fromfile() -- read items from a file object
fromlist() -- append items from the list
frombytes() -- append items from the string
index() -- return index of first occurrence of an object
insert() -- insert a new item into the array at a provided position
pop() -- remove and return item (default last)
remove() -- remove first occurrence of an object
reverse() -- reverse the order of the items in the array
tofile() -- write all items to a file object
tolist() -- return the array converted to an ordinary list
tobytes() -- return the array converted to a string

Attributes:

typecode -- the typecode character used to create the array
itemsize -- the length in bytes of one array item
Type:           type
'''
#[Out]# "\narray(typecode [, initializer]) -> array\n\nReturn a new array whose items are restricted by typecode, and\ninitialized from the optional initializer value, which must be a list,\nstring or iterable over elements of the appropriate type.\n\nArrays represent basic values and behave very much like lists, except\nthe type of objects stored in them is constrained. The type is specified\nat object creation time by using a type code, which is a single character.\nThe following type codes are defined:\n\n    Type code   C Type             Minimum size in bytes \n    'b'         signed integer     1 \n    'B'         unsigned integer   1 \n    'u'         Unicode character  2 (see note) \n    'h'         signed integer     2 \n    'H'         unsigned integer   2 \n    'i'         signed integer     2 \n    'I'         unsigned integer   2 \n    'l'         signed integer     4 \n    'L'         unsigned integer   4 \n    'q'         signed integer     8 (see note) \n    'Q'         unsigned integer   8 (see note) \n    'f'         floating point     4 \n    'd'         floating point     8 \n\nNOTE: The 'u' typecode corresponds to Python's unicode character. On \nnarrow builds this is 2-bytes on wide builds this is 4-bytes.\n\nNOTE: The 'q' and 'Q' type codes are only available if the platform \nC compiler used to build Python supports 'long long', or, on Windows, \n'__int64'.\n\nMethods:\n\nappend() -- append a new item to the end of the array\nbuffer_info() -- return information giving the current memory info\nbyteswap() -- byteswap all the items of the array\ncount() -- return number of occurrences of an object\nextend() -- extend array by appending multiple elements from an iterable\nfromfile() -- read items from a file object\nfromlist() -- append items from the list\nfrombytes() -- append items from the string\nindex() -- return index of first occurrence of an object\ninsert() -- insert a new item into the array at a provided position\npop() -- remove and return item (default last)\nremove() -- remove first occurrence of an object\nreverse() -- reverse the order of the items in the array\ntofile() -- write all items to a file object\ntolist() -- return the array converted to an ordinary list\ntobytes() -- return the array converted to a string\n\nAttributes:\n\ntypecode -- the typecode character used to create the array\nitemsize -- the length in bytes of one array item\nType:           type\n"
from array import array # 引入array类型
get_ipython().run_line_magic('pinfo', 'random')
# random() -> x in the interval [0, 1)
# array.tofile 写入到文件里
# array.fromfile 从文件读到内存对象里
# 每个浮点数占用8个字节
# 如果是文本的话，需要181 515 739 个字节
# 从python3.4开始，数组类型不再支持诸如list.sort()这种就地排序的方法
# 要给数组排序的话，得用sorted函数新建一个数组
a = array.array(a.typecode,sorted(a))
a = array(a.typecode,sorted(a))
#内存视图 memoryview
# 它能让用户在不复制内容的情况下操作同一个数组的不同切片
import Memoryview
# error
# 内存师徒其实是泛化和去数学化的Numpy数组
# 它让你在不需要复制内容的前提下，在数据结构之间共享内存，其中数据结构可以是任何形式
# 通过改变数组中的一个字节更新数组里某个元素的值
numbers = array('h',[-2,-1,0,1,2])
_
#[Out]# "\narray(typecode [, initializer]) -> array\n\nReturn a new array whose items are restricted by typecode, and\ninitialized from the optional initializer value, which must be a list,\nstring or iterable over elements of the appropriate type.\n\nArrays represent basic values and behave very much like lists, except\nthe type of objects stored in them is constrained. The type is specified\nat object creation time by using a type code, which is a single character.\nThe following type codes are defined:\n\n    Type code   C Type             Minimum size in bytes \n    'b'         signed integer     1 \n    'B'         unsigned integer   1 \n    'u'         Unicode character  2 (see note) \n    'h'         signed integer     2 \n    'H'         unsigned integer   2 \n    'i'         signed integer     2 \n    'I'         unsigned integer   2 \n    'l'         signed integer     4 \n    'L'         unsigned integer   4 \n    'q'         signed integer     8 (see note) \n    'Q'         unsigned integer   8 (see note) \n    'f'         floating point     4 \n    'd'         floating point     8 \n\nNOTE: The 'u' typecode corresponds to Python's unicode character. On \nnarrow builds this is 2-bytes on wide builds this is 4-bytes.\n\nNOTE: The 'q' and 'Q' type codes are only available if the platform \nC compiler used to build Python supports 'long long', or, on Windows, \n'__int64'.\n\nMethods:\n\nappend() -- append a new item to the end of the array\nbuffer_info() -- return information giving the current memory info\nbyteswap() -- byteswap all the items of the array\ncount() -- return number of occurrences of an object\nextend() -- extend array by appending multiple elements from an iterable\nfromfile() -- read items from a file object\nfromlist() -- append items from the list\nfrombytes() -- append items from the string\nindex() -- return index of first occurrence of an object\ninsert() -- insert a new item into the array at a provided position\npop() -- remove and return item (default last)\nremove() -- remove first occurrence of an object\nreverse() -- reverse the order of the items in the array\ntofile() -- write all items to a file object\ntolist() -- return the array converted to an ordinary list\ntobytes() -- return the array converted to a string\n\nAttributes:\n\ntypecode -- the typecode character used to create the array\nitemsize -- the length in bytes of one array item\nType:           type\n"
numbers
#[Out]# array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
memv
#[Out]# <memory at 0x0000000008F94DC8>
len(memv)
#[Out]# 5
memv[0]
#[Out]# -2
memv[1]
#[Out]# -1
memv[2]
#[Out]# 0
memv_oct = memv.cast('B')
numbers = array('h',[-2,-1,0,1,2]) # 5个短整形有符号整数的数组
memv = memoryview(numbers) # memv 5个元素 跟数组里的没有区别
memv_oct = memv.cast('B') # 将memv里的内容转换成”B"类型
memv_oct.tolist()
#[Out]# [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
memv_oct.tolist() # 以列表的形式查看memv oct的内容
#[Out]# [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
memv_oct[5] = 4
numbers # 把占2个字节的整数的高位字节改成了4，所以这个有符号整数的值变成了1024
#[Out]# array('h', [-2, -1, 1024, 1, 2])
memv_oct[5]
#[Out]# 4
memv_oct
#[Out]# <memory at 0x000000000759D048>
memv_oct[0]
#[Out]# 254
memv_oct[1]
#[Out]# 255
memv_oct.tolist()
#[Out]# [254, 255, 255, 255, 0, 4, 1, 0, 2, 0]
array
#[Out]# array.array
get_ipython().run_line_magic('pinfo', 'array')
import numpy
import numpy as np
a = np.arange(12)
a 
#[Out]# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
type(a)
#[Out]# numpy.ndarray
a.shape
#[Out]# (12,)
a.shape = 3,4
a
#[Out]# array([[ 0,  1,  2,  3],
#[Out]#        [ 4,  5,  6,  7],
#[Out]#        [ 8,  9, 10, 11]])
a[2]
#[Out]# array([ 8,  9, 10, 11])
a[2][1]
#[Out]# 9
a[2,1]
#[Out]# 9
a[:,1]
#[Out]# array([1, 5, 9])
# 获取到的是一维的数组
# a.transpose()
a.transpose()
#[Out]# array([[ 0,  4,  8],
#[Out]#        [ 1,  5,  9],
#[Out]#        [ 2,  6, 10],
#[Out]#        [ 3,  7, 11]])
a.ndim()
a
#[Out]# array([[ 0,  1,  2,  3],
#[Out]#        [ 4,  5,  6,  7],
#[Out]#        [ 8,  9, 10, 11]])
a.ndim
#[Out]# 2
a
#[Out]# array([[ 0,  1,  2,  3],
#[Out]#        [ 4,  5,  6,  7],
#[Out]#        [ 8,  9, 10, 11]])
from collections import deque
# collections.deque 双向队列
# 是一个线程安全，可以快速从两端添加或者删除元素的数据类型
# 如果想要一种数据类型来存放 最近用到的几个元素 deque是一个很好的选择
from collections import deque
dq = deque(range(10),maxlen=10)
dq
#[Out]# deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
dq.rotate(3)
dq
#[Out]# deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6])
# maxlen 是一个可选参数，代表这个队列可以容纳的元素的数量
# 一旦设定，这个属性巨不能修改了
dq.rotate(-4)
dq
#[Out]# deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
dq
#[Out]# deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
dq.appendleft(-1)
dq
#[Out]# deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
dq.extend([11,22,33])
dq
#[Out]# deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33])
dq.extendleft([10,20,30,40])
dq
#[Out]# deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8])
# n 大于 0，队列最右边的n个元素会被移动到队列的左边
# n 小于 0， 队列最左边的n个元素会被移动到右边
# extendleft（iter） 会把迭代器里的元素准个添加到双向队列的左边
# 迭代器的元素会逆序出现队列里面
# 2-10 终结
get_ipython().run_line_magic('logstop', '')
