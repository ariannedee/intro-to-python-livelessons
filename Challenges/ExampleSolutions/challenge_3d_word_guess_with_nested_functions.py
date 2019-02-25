"""
Word guess game refactored so to use nested functions.
The inner functions can use variables from the outer function's scope.
You no longer have to pass 'answer' and 'guessed_letters' around.
"""
import random


def word_game():
    def pick_random_word():
        with open('words.txt', 'r') as file:
            words = file.readlines()
            word = random.choice(words).strip()
        return word

    answer = pick_random_word()
    num_wrong_guesses_left = 6
    guessed_letters = []

    def get_display_word():
        letter_list = [letter if letter in guessed_letters else '_'
                       for letter in answer]
        return ' '.join(letter_list)

    def user_did_win():
        for letter in answer:
            if letter not in guessed_letters:
                return False
        return True

    while num_wrong_guesses_left > 0:
        print(get_display_word())
        print(f'{num_wrong_guesses_left} wrong guesses left')
        print(f'Guesses: {guessed_letters}')

        guess = input("Guess a letter: ")
        guessed_letters.append(guess)

        if guess in answer:
            print("Correct!")
        else:
            print("Nope :(")
            num_wrong_guesses_left -= 1

        if user_did_win():
            print("You win!")
            return
    print("Sorry, you lose")
    print(f"The answer was {answer}")


if __name__ == "__main__":
    word_game()
