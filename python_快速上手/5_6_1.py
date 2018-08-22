#
#
#
#
dicta = {}

while True:
	keys = input('Enter items: ')
	if keys == ' ':
		break
	values = input('Enter number: ')	
	dicta.setdefault(keys,values)
	print('if you stop enter,enter "space" ')
	

print(dicta)


def displayitems(items):
	print('displayitems : ')
	h = 0 
	for i in items.keys():
		print (items[i],i)
		h += int(items[i])
	print(str(h))

displayitems(dicta)


