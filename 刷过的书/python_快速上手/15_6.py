import time,threading
print('strat')

def threadexp():
	time.sleep(10)
	print('wait 10秒')
threadobj = threading.Thread(target=threadexp)
threadobj.start()

print('end')