from random import random, randint

# make a hidden number
hiddenNumber = randint(0, 21)
print ('\nGuess the number I am thinking of, between 1 and 20\n')
userInput = int(input('> '))

count = 0
while (userInput != hiddenNumber):
	if (count == 3):
		print ('You tried %s times, your failure will be noted' %count)
		break
	# the number is wrong
	if (hiddenNumber > userInput):
		print ('Your number %s is too low...' %userInput)
	else: 
		print ('Your number %s is too high' %userInput)
	userInput = int(input('Try again: '))
	count += 1

if (userInput == hiddenNumber):
	print ('Correct... very impressive...')

print ('The number was: ' + str(hiddenNumber))