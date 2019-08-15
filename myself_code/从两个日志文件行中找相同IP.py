# -*- coding=utf-8 -*-
#从两个日志文件找相同出现的IP

import re 
regex = re.compile(r'\d{2,3}\.\d{2,3}\.\d{2,3}\.\d{2,3}')

f1 = input('Please select the first files:')
f2 = input('Please select the second files:')

def find_same_ip(file_1,file_2):

	pre_fn_1 = []
	new_fn_1 = []    
	pre_fn_2 = []
	new_fn_2 = []
	the_same_ip = []
	#读取一个日志文件的每行到列表里
	#如果一行中有多个ip，会出现[[,,,],[,,,],...]
	#遍历上面的嵌套列表，将嵌套列表的元素添加到列表最后
	with open(file_1) as f1:
		fn_1 = f1.readlines()        
		for i in range(0,len(fn_1)):            
			fn_1[i] = fn_1[i].strip('\n')            
			fn_1[i] = regex.findall(fn_1[i])            
			if len(fn_1[i]) >1:                
				for h in fn_1[i]:                    
					fn_1.append(h)
	#将列表中非嵌套的元素添加一个新的列表中
	for i in fn_1:
		if type(i) != type([]):
			pre_fn_1.append(i)
	#新表元素去重
	for i in pre_fn_1:
		if i not in new_fn_1:
			new_fn_1.append(i)

	with open(file_2) as f2:        
		fn_2 = f2.readlines()        
		for i in range(0,len(fn_2)):            
			fn_2[i] = fn_2[i].strip('\n')            
			fn_2[i] = regex.findall(fn_2[i])            
			if len(fn_2[i]) >1:                
				for h in fn_2[i]:                    
					fn_2.append(h)  
	for i in fn_2:
		if type(i) != type([]):
			pre_fn_2.append(i)

	for i in pre_fn_2:
		if i not in new_fn_2:
			new_fn_2.append(i)          
	#判断两个列表元素的交集
	for i in new_fn_1:
		if i in new_fn_2:
			the_same_ip.append(i)		
	#这里不能用f1,f2，显示异常
	print('%s 和 %s 两个文件中相同的IP有\n' % (file_1,file_2))
	
	for i in the_same_ip:
		print(i)


find_same_ip(f1,f2)