#Damani A.Philip

#Version 1.0

import random

#Introduction
print('Welcome to the Dice roll histogram.')
    

def troubled_week(num_rolls,character):
	for rolls in range(num_rolls):
	    dice1 = random.randint(1,6)
		dice2 = random.randint(1,6)
		roll_total = dice1 + dice2
		print roll_total * character
		
	
num_sixes = 0
num_sevens = 0
counter = 0
num_rolls = int(input('Enter number of rolls:\n'))
character = str(input('Please enter character:\n')) #Additional input for user choice.

print('Dice roll histogram:\n')
if num_rolls >= 1:
    print('%ds: %s' % (counter, troubled_week(num_rolls,character)))

else:
    print('Invalid number of rolls. Try again.')
