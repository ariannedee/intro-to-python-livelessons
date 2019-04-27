words = ['account', 'addition', 'adjustment', 'advertisement', 'agreement',
         'amount', 'amusement', 'animal', 'answer', 'apparatus', 'approval',
         'argument', 'attack', 'attempt', 'attention', 'attraction',
         'authority', 'balance', 'behavior', 'belief', 'breath', 'brother',
         'building', 'business', 'butter', 'canvas', 'chance', 'change',
         'comfort', 'committee', 'company', 'comparison', 'competition',
         'condition', 'connection', 'control', 'copper', 'cotton', 'country',
         'credit', 'current', 'damage', 'danger', 'daughter', 'decision',
         'degree', 'design', 'desire', 'destruction', 'detail', 'development',
         'digestion', 'direction', 'discovery', 'discussion', 'disease',
         'disgust', 'distance', 'distribution', 'division', 'driving',
         'education', 'effect', 'example', 'exchange', 'existence', 'expansion',
         'experience', 'expert', 'family', 'father', 'feeling', 'fiction',
         'flight', 'flower', 'friend', 'government', 'growth', 'harbor',
         'harmony', 'hearing', 'history', 'impulse', 'increase', 'industry',
         'insect', 'instrument', 'insurance', 'interest', 'invention',
         'journey', 'knowledge', 'language', 'learning', 'leather', 'letter',
         'liquid', 'machine', 'manager', 'market', 'measure', 'meeting',
         'memory', 'middle', 'minute', 'morning', 'mother', 'motion',
         'mountain', 'nation', 'number', 'observation', 'operation', 'opinion',
         'organisation', 'ornament', 'payment', 'person', 'pleasure', 'poison',
         'polish', 'porter', 'position', 'powder', 'process', 'produce',
         'profit', 'property', 'protest', 'punishment', 'purpose', 'quality',
         'question', 'reaction', 'reading', 'reason', 'record', 'regret',
         'relation', 'religion', 'representative', 'request', 'respect',
         'reward', 'rhythm', 'science', 'secretary', 'selection', 'servant',
         'silver', 'sister', 'sneeze', 'society', 'statement', 'stitch',
         'stretch', 'structure', 'substance', 'suggestion', 'summer', 'support',
         'surprise', 'system', 'teaching', 'tendency', 'theory', 'thought',
         'thunder', 'transport', 'trouble', 'vessel', 'weather', 'weight',
         'winter', 'writing']

hard_words = ['Awkward', 'Bagpipes', 'Banjo', 'Bungler', 'Croquet', 'Crypt',
              'Dwarves', 'Fervid', 'Fishhook', 'Fjord', 'Gazebo', 'Gypsy',
              'Haiku', 'Haphazard', 'Hyphen', 'Ivory', 'Jazzy', 'Jiffy', 'Jinx',
              'Jukebox', 'Kayak', 'Kiosk', 'Klutz', 'Memento', 'Mystify',
              'Numbskull', 'Ostracize', 'Oxygen', 'Pajama', 'Phlegm', 'Pixel',
              'Polka', 'Quad', 'Quip', 'Rhythmic', 'Rogue', 'Sphinx', 'Squawk',
              'Swivel', 'Toady', 'Twelfth', 'Unzip', 'Waxy', 'Wildebeest',
              'Yacht', 'Zealous', 'Zigzag', 'Zippy', 'Zombie']

"""
Refactored word guessing game
Extract get_display_word() and user_did_win() from the word_game() function.
Use list comprehensions to simplify get_display_word().
Tests for these functions are in challenge_3b_word_guess_tests.py
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


def get_guess():
    while True:
        guess = input("Guess a letter: ").strip()
        if len(guess) == 1 and guess.isalpha():
            return guess.lower()
        else:
            print('Your guess should be a single letter')


def word_game():
    answer = random.choice(words).lower()
    num_wrong_guesses_left = 6
    guessed_letters = []

    while num_wrong_guesses_left > 0:
        print(get_display_word(answer, guessed_letters))
        print(f'{num_wrong_guesses_left} wrong guesses left')
        print(f'Guesses: {guessed_letters}')

        guess = get_guess()
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
    word_game()
