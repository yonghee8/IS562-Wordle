# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

# Choose a random word from the list
random_word = random.choice(FIVE_LETTER_WORDS)

def wordle():

    def enter_action(s):
        user_word = s.lower()  # Convert the entered word to lowercase for case-insensitive comparison
        
        if user_word in FIVE_LETTER_WORDS:
            gw.show_message("You guessed a valid word!")
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Call the function to display the random word
    display_random_word(gw, random_word)

def display_random_word(gw, word):
    for col in range(N_COLS):
        # Set the letter in the box at row 0 and column col
        gw.set_square_letter(0, col, word[col])

# Startup code
if __name__ == "__main__":
    wordle()
