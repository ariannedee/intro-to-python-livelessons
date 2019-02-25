"""
Number guessing game
The number to guess will be from 1 to 20 (inclusive).
The user will have 3 guesses to guess the number correctly.
After each wrong guess, the user will be told whether to
guess higher or lower next time.
If the user doesn't win, tell them the number.
"""
import random


def run_game():
    answer = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20")

    num_guesses = 3
    for num_guess in range(num_guesses):
        print(f'You have {num_guesses} guesses left')
        guess = int(input("Make a guess: "))

        if guess == answer:
            print("That's it! You got it!")
            return
        elif num_guesses == 0:
            break
        elif answer > guess:
            print("Guess higher")
        else:
            print("Guess lower")

    print('The number was {}'.format(answer))
    return


run_game()
