#Damani A.Philip


#Version 6.0

import random

def rand(user_input):
    number = 0
    if user_input != 0:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_total = die1 + die2
    else:
        roll_total = None

    return roll_total

def histo_print(times, dicerand, character=""):
    if character is "":
        character = "*"
    print('%ds: %s' % (times,(dicerand * character)))

#Introduction
print('Welcome to the Dice roll histogram.\n')

num_rolls = int(input('Enter number of rolls:\n'))
"""Optional Secondary input based on if the number entered is greater than zero."""
"""If user fails to enter a character it will default back to the asterisk"""
character = str(input('Please enter character:\n'))  # Additional input for user choice.


if num_rolls >= 1:
    """Adds one to user input because the for loop starts at one."""
    num_rolls += 1
    for i in range(1,num_rolls):
        """Output"""
        histo_print(i, rand(num_rolls),character)
else:
    """If user fails to enter a number less than one"""
    print('Invalid number of rolls. Try again.')
