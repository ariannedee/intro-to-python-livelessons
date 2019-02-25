"""
Refactored word guessing game that gets a random word from the file 'words.txt'
"""
import random


def get_display_word(answer, guessed_letters):
    letter_list = [letter if letter in guessed_letters else '_' for letter in answer]
    return ' '.join(letter_list)


def user_did_win(answer, guessed_letters):
    for letter in answer:
        if letter not in guessed_letters:
            return False
    return True


def pick_random_word():
    with open('words.txt', 'r') as file:
        words = file.readlines()
        word = random.choice(words).strip()
    return word


def word_game():
    answer = pick_random_word()
    num_wrong_guesses_left = 6
    guessed_letters = []

    while num_wrong_guesses_left > 0:
        print(get_display_word(answer, guessed_letters))
        print(f'{num_wrong_guesses_left} wrong guesses left')
        print(f'Guesses: {guessed_letters}')

        guess = input("Guess a letter: ")
        guessed_letters.append(guess)

        if guess in answer:
            print("Correct!")
        else:
            print("Nope :(")
            num_wrong_guesses_left -= 1

        if user_did_win(answer, guessed_letters):
            print("You win!")
            return
    print("Sorry, you lose")
    print(f"The answer was {answer}")


if __name__ == "__main__":
    print(pick_random_word())
