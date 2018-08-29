td = [['apple','oranges','cherries','bananas'],
			 ['Alice','Bob','Carol','David'],
			 ['dogs','cats','moose','goose']]

tdlist1len = len(td)
tdlist2len = 0
for i in range(tdlist1len):
	tdlist2len = len(td[i])
	break
print('----')
print(tdlist1len)
print(tdlist2len)
print('----')
for i in range(tdlist1len): # 012
	for h in range(tdlist2len):# 0123
		print(tdlist1values[i],end='')  
