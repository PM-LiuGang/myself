#coding = utf-8
#遗留问题
#如何将unix时间进行转换
#局作用于和全局作用域的区别
#字典的常规操作不熟悉
import time 
#username_list = []
#time_list = []
workdict = {}

print('work-time sheet')
all_users = ['liugang','lg']
work = 1
try:
	while True:
		
		username = input('Username:')
		times = time.time()	
		if username in all_users:
			workdict[username] = times	
			
			if work == 1:
				timee = time.time()
				work = 0
				print('上班打卡成功')
				print(username,"上班时间是",workdict[username])
				
			elif work == 0:
				timee = time.time()
				work = 1
				print('下班打卡成功')
				print(username,"下班时间是",workdict[username])
				
		else:
			print('欢迎你加入')
except:
	print('Done')



