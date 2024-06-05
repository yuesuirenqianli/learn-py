"""
    10.8
"""


import random

guess = ''

toss = random.randint(0, 1)
toss_result = 'heads' if toss == 0 else 'tails'

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

if toss_result == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')

    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()

    if toss_result == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
