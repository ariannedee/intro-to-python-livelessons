"""
Word guess refactored to use classes.

Some explanation:
__init__ is the default function that gets called when you instantiate
a new object, e.g. game = WordGame()

Classes have properties (e.g. answer) that can be accessed within the
class by calling self.property_name (e.g. self.answer).

Methods are functions that belong to an object (e.g. play_game) and are
run by calling self.method_name (e.g. self.play_game() ).

In this case, user_did_win is a method that acts like a property
because it uses a property decorator (@property), so it can be accessed
by calling self.user_did_win, not self.user_did_win() <- no parentheses.
"""
import random


def pick_random_word():
    with open('words.txt', 'r') as file:
        words = file.readlines()
        word = random.choice(words).strip()
    return word


class WordGame(object):
    def __init__(self):
        self.answer = pick_random_word()
        self.num_wrong_guesses_left = 6
        self.guessed_letters = []

    def get_display_word(self):
        letter_list = [letter if letter in self.guessed_letters else '_'
                       for letter in self.answer]
        return ' '.join(letter_list)

    @property
    def user_did_win(self):
        for letter in self.answer:
            if letter not in self.guessed_letters:
                return False
        return True

    def play_game(self):
        while self.num_wrong_guesses_left > 0:
            print(self.get_display_word())
            print(f'{self.num_wrong_guesses_left} wrong guesses left')
            print(f'Guesses: {self.guessed_letters}')

            guess = input("Guess a letter: ")
            self.guessed_letters.append(guess)

            if guess in self.answer:
                print("Correct!")
            else:
                print("Nope :(")
                self.num_wrong_guesses_left -= 1

            if self.user_did_win:
                print("You win!")
                return
        print("Sorry, you lose")
        print(f"The answer was {self.answer}")


if __name__ == "__main__":
    game = WordGame()
    game.play_game()
