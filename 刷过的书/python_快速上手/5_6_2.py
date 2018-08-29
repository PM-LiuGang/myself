#coding = utf-8
#python quickly start
#5.6.2
#liugang
from collections import Counter


def addtoinv(inv,add):
	print('---SOURCE: ')
	h = 0
	#遍历原字典
	for k,v in inv.items():
		print(str(v) + ' ' + k)
		h += int(v)
	print('---TO ADD---')

	newadddict = Counter(add) # 生成字典{名称：出现次数}

	for k,v in newadddict.items():
		print(v,k)
		h += int(v)
	print('---LAST---')
	#打印共同键的值
	for i in inv.keys():
		if i in add:
			m = int(inv[i]) + int(newadddict[i])
			print(m,i)
		else:
			print(inv[i],i)
	#打印差异键
	for i in newadddict.keys():
		if i not in inv:
			print(newadddict[i],i)

	print('---SUM---')
	print(h)

invlist = {'gold coin':42,'rope':1}
addlist = ['gold coin','dagger','gold coin','gold coin','ruby']
addtoinv(invlist,addlist)


