"""
Tests some of the functions in word_guessing_game
Look into unittest, pytest, and mock libraries for more advanced tests
"""
from Challenges.ExampleSolutions.challenge_3b_word_guess_refactored import (
    get_display_word,
    user_did_win
)


assert get_display_word('hello', []) == '_ _ _ _ _'
assert get_display_word('hello', ['l']) == '_ _ l l _'
assert get_display_word('hello', ['e', 'h', 'o', 'l']) == 'h e l l o'


assert not user_did_win('hello', [])
assert not user_did_win('hello', ['h', 'a', 'e', 'l', 'b'])
assert user_did_win('hello', ['h', 'a', 'e', 'l', 'b', 'o'])
assert user_did_win('', [])

print("Tests passed")
