list = input('Enter:')

h = []

for i in range(0,len(list)):
	h.append(list[i])
	if i == len(list) - 1: 
		print('and ' + list[i])
	else:
		print(list[i],end = ',')




