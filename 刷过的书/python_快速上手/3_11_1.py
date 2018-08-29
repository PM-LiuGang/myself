#
h = int(input('Enter a number:'))

def coll(h):
	if h % 2 == 0:
		return h // 2
	else:
		return h * 3 + 1

while h != 1:
	if True:
		h = coll(h)
		print (h)
	else:
		break

