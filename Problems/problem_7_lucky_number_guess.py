"""
Guess the number between 1 and 10
"""

import random
answer = random.randint(1, 10)

guess = int(float(input("I'm thinking of a number between 1 and 10: ")))

# If the number is correct, tell the user
# Otherwise, tell them if the answer is higher or lower than their guess


print('The number was {}'.format(answer))
