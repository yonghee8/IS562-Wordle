# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR


# Choose a random word from the list
random_word = random.choice(FIVE_LETTER_WORDS)

def wordle():

    def enter_action(s):
        user_word = s.lower()  # Convert the entered word to lowercase for case-insensitive comparison
        
        if user_word in FIVE_LETTER_WORDS:
            # Check if the user guessed the entire word correctly
            if user_word == random_word:
                gw.show_message("You guessed the word correctly!")
            else:
                # Initialize lists to keep track of letters that are correctly guessed, present but in the wrong place, and missing
                correct_letters = []
                present_letters = []
                missing_letters = []

                # Check each letter in the user's guess
                for col, letter in enumerate(user_word):
                    if letter == random_word[col]:
                        correct_letters.append(col)
                    elif letter in random_word:
                        present_letters.append(col)
                    else:
                        missing_letters.append(col)

                # Set colors for correct letters
                for col in correct_letters:
                    gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
                    gw.set_key_color(letter.upper(), CORRECT_COLOR)

                # Set colors for letters that are present but in the wrong place
                for col in present_letters:
                    gw.set_square_color(gw.get_current_row(), col, PRESENT_COLOR)
                    gw.set_key_color(letter.upper(), PRESENT_COLOR)

                for col in missing_letters:
                    gw.set_square_color(gw.get_current_row(), col, MISSING_COLOR)
                    gw.set_key_color(letter.upper(), MISSING_COLOR)

                # Move on to the next row
                gw.set_current_row(gw.get_current_row() + 1)

        else:
            gw.show_message("Not a valid word")

                 
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Call the function to display the random word
    #display_random_word(gw, random_word)

def display_random_word(gw, word):
    for col in range(N_COLS):
        # Set the letter in the box at row 0 and column col
        gw.set_square_letter(0, col, word[col])

# Startup code
if __name__ == "__main__":
    wordle()
