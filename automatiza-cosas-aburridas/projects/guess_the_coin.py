"""
Depurar el siguiente programa.
"""

import random
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.randint(0, 1)  # 0 is tails, 1 is heads

toss_result = ""
if toss == 0:
    toss_result = "tails"
else:
    toss_result = "heads"

# if toss == guess:
if toss_result == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    # if toss = guess:
    if toss_result == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
