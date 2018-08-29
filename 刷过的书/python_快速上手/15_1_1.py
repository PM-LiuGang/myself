import time
def calcprod():
	product = 1 
	for i in range(1,100000):
		product = product * i 
	return product

starttime = time.time()
prod = calcprod()
enttime = time.time()

print(str(prod))
print(len(str(prod)))
print(enttime-starttime)