#模拟扑克随机发牌,4个人
#红桃H 黑桃S 梅花C 方片D
import random

suits = list('HSCD')
card_val = (list(range(1,11)) + [10] * 3) * 4
base_name = ['A'] +list(range(2,11)) + list('JQK')
cards = []

for suit in suits:
	cards.extend(str(num) + suit for num in base_name)

#deck = Series(card_val,index=cards)

pa = random.sample(cards,13)
for i in pa:
	if i in cards:
		cards.remove(i)

pb = random.sample(cards,13)
for i in pb:
	if i in cards:
		cards.remove(i)

pc = random.sample(cards,13)
for i in pc:
	if i in cards:
		cards.remove(i)

pd = cards


print('pa get cards %s\n pa get cards %s\n pa get cards %s\n pa get cards %s\n' % (pa,pb,pc,pd)) 