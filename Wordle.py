# File: Wordle.py

import random
import tkinter
from tkinter import *
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():  
    def enter_action(s):
        global CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR
        blind = var.get()
        if blind == 1 :
        # Apply the default color scheme
            CORRECT_COLOR = "#66BB66"       
            PRESENT_COLOR = "#CCBB66"       
            MISSING_COLOR = "#999999"
        elif blind == 2 :
            # Apply the colorblind color scheme
            CORRECT_COLOR = "#6495ED"
            PRESENT_COLOR = "#DC143C"
            MISSING_COLOR = "#999999"

        if not gw.win:
            #strings together the user's guess
            userWord = ""
            for colNum in range(0,N_COLS):
                userWord += gw.get_square_letter(gw.get_current_row(),colNum)
            
            #if the user's guess is in the dictionary, proceed
            if userWord.lower() in FIVE_LETTER_WORDS:
                #coloring tiles

                #keeps string containing letters found
                lettersFound = ""

                #loop through tiles in current row
                for colNum in range(0,N_COLS):
                    #if tile is in correct position, color TILE and KEY green
                    if gw.get_square_letter(gw.get_current_row(),colNum) == word[colNum]:
                        #add letter to list of letters found
                        lettersFound += gw.get_square_letter(gw.get_current_row(),colNum)
                        gw.set_square_color(gw.get_current_row(),colNum,CORRECT_COLOR)
                        gw.set_key_color(gw.get_square_letter(gw.get_current_row(),colNum),CORRECT_COLOR)
                #loop through tiles in current row again
                for colNum in range(0,N_COLS):
                    #if tile isn't green, but is in the word
                    if (gw.get_square_color(gw.get_current_row(),colNum) != CORRECT_COLOR) and (gw.get_square_letter(gw.get_current_row(),colNum) in word):
                        #add letter to list of letters found
                        lettersFound += gw.get_square_letter(gw.get_current_row(),colNum)
                        #if letter hasn't been found more times than it is present in the word, color TILE yellow
                        if lettersFound.count(gw.get_square_letter(gw.get_current_row(),colNum)) <= word.count(gw.get_square_letter(gw.get_current_row(),colNum)):
                            gw.set_square_color(gw.get_current_row(),colNum,PRESENT_COLOR)
                        #otherwise, color tile grey
                        else:
                            gw.set_square_color(gw.get_current_row(),colNum,MISSING_COLOR)
                        #if KEY isn't green already, color it yellow
                        if gw.get_key_color(gw.get_square_letter(gw.get_current_row(),colNum)) != CORRECT_COLOR:
                            gw.set_key_color(gw.get_square_letter(gw.get_current_row(),colNum), PRESENT_COLOR)
                    #if TILE isn't green and didn't meet the first criteria (being in the word), tile and key must be grey
                    elif gw.get_square_color(gw.get_current_row(),colNum) != CORRECT_COLOR:
                        gw.set_square_color(gw.get_current_row(),colNum,MISSING_COLOR)
                        gw.set_key_color(gw.get_square_letter(gw.get_current_row(),colNum), MISSING_COLOR)
               
                #display congratulations if correct
                if userWord == word:
                    gw.show_message("Congratulations! You guessed the word!")
                    gw.win = True
                #display incorrect message and reveal word if incorrect
                elif gw.get_current_row() == N_ROWS - 1:
                    gw.show_message("Game over! The word was " + word + ".")
                #display message to keep guessing if guess is incorrect
                else:
                    gw.show_message("Your guess is incorrect. Keep guessing!")
                #move to next row to allow another guess unless game is over
                if gw.get_current_row() < (N_ROWS - 1):
                    gw.set_current_row(gw.get_current_row() + 1)
            #if guess is invalid, clear guess and show "not in word list"
            else:
                for colNum in range(0,N_COLS):
                    gw.set_square_letter(gw.get_current_row(),colNum,"")
                gw.show_message("Not in word list.")
                gw.set_current_row(gw.get_current_row())
        
    
    root = tkinter.Tk()
    var = tkinter.IntVar()
    c1 = tkinter.Radiobutton(root, text='Default', variable=var, value=1)
    c1.pack(anchor=W)
    c2 = tkinter.Radiobutton(root, text='Colorblind', variable=var, value=2)
    c2.pack(anchor = W)

    submit_button = tkinter.Button(root, text="Enter")
    submit_button.pack()

    gw = WordleGWindow()
    gw.win = False
    gw.add_enter_listener(enter_action)   

    #Selects random word from dictionary
    word = FIVE_LETTER_WORDS[random.randint(0,(len(FIVE_LETTER_WORDS)-1))].upper()

    #moves to first row to allow user's first guess
    gw.set_current_row(0)

# Startup code
if __name__ == "__main__":
    wordle()