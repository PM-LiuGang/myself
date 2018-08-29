import random,logging
#logging.basicConfig(level=logging.DEBUG,format=' %(actime)s - %(debug)s -  %(message)s')
#logging.disable(logging.debug)

guess=''
while  guess not in ('heads','tails'):
	print('Guess the coin! Enter heads or tails:')
	guess = input()

assert type(guess) == type(''),'guess should  be str'

toss = random.randint(0,1) # 0-tails,1-heads

if toss == 0 :
	toss = 'tails'
elif toss == 1 :
	toss = 'heads'

assert type(toss) == type(''),'toss should not be int'

if toss == guess:
	print('You got it!')
else:
	print('None!Guess again!')
	guess = input()
	if toss == guess:
		print('You got it!')
	else:
		print('Over.You are really bad at this game')

		
