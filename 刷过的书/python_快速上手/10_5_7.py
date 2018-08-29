import random

nums = 0

for i in range(1,1001):
	if random.randint(0,1) == 1:
		nums = nums + 1 
	if i ==500:
		print('half of 1000')

print('1','times',nums)