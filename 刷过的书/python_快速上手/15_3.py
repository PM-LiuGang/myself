'''
import time 

userstart = input()
starttime = time.time()
roundnum = 0
note = []

while True:
	try:
		userend = input()
		endtime = time.time()
		roundnum += 1
		note.append(starttime-endtime)
		note.append(roundnum)
		starttime = endtime
	except:
		print(note)
		break
#		print(starttime-endtime)
#		print(roundnum)
'''
import time 
print('Enter to begin,afterwards,Enter to stop/start,Ctrl-c to quit')
input()
print('started')
starttime = time.time()#程序开始时间
lasttime = starttime#默认上一圈的开始时间
lapnum = 1#圈树

try:
	while True:
		input()
		laptime = round(time.time() - lasttime,2)#第一圈的时间
		totaltime = round(time.time() - starttime,2)#总共花费的时间
		print('lap #%s: %s (%s)' % (lapnum,totaltime,laptime),end='')#打印圈数，程序总共用时，上一圈的单圈时间
		lapnum += 1 # 圈数+1 
		lasttime = time.time()#获取下一圈的开始时间，为了计算laptime
except :
	print('\nDone')