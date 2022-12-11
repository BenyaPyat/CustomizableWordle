from tkinter import *
from tkinter import messagebox
from Word import Word
from ColorMenu import ColorMenu
from TurnNum import TurnNum
from Color import Color
from WordleBoard import WordleBoard
from BoardSize import BoardSize


class GUI:
    """Runs and creates tkinter GUI for Wordle game and input of vals"""

    def __init__(self, root):
        """initialize GUI"""
        # root
        self.root = root

        # gets desired turn number from user
        self.trn_obj = TurnNum()
        self.trn = int(self.trn_obj.get_val())

        # gets desired color scheme from user
        self.color = Color()
        self.colors = self.color.get_val()
        self.color_py_name = ColorMenu(self.colors)
        self.col1, self.col2, self.col3, self.col4 = self.color_py_name.get_color()

        # configs gui color and buttons
        self.root.config(bg=self.col2)
        self.guess_button = Button(root, text="Guess", command=self.guess)
        self.guess_button.grid(row=999, column=3, columnspan=2)
        self.input_word = Entry(root)
        self.input_word.grid(row=999, column=0, padx=10, pady=10, columnspan=3)

        # sets ground condition for guess()
        self.turn_num = 0

        # gets word to be guessed based off user specifications
        self.wrd = Word()
        self.word = self.wrd.get_word()

        # gets user specified  board size
        self.get_obj = BoardSize()
        self.board_len = int(self.get_obj.get_val())

        # prompts user to guess the word
        messagebox.showinfo('Wordle', f'Enter a {len(self.word)} letter word')

    def guess(self):
        """Runs conditions for GUI Wordle game"""

        # gets the users input
        user_input = self.input_word.get()

        self.turn_num += 1

        # checks if turns aren't up
        if self.turn_num <= self.trn:

            if len(user_input) == len(self.word):

                if self.word.upper() == user_input.upper():  # word guess correctly
                    messagebox.showinfo("correct!", f"correct! the word was {self.word.title()}")
                else:  # word guess incorrectly
                    # creates board and gets it
                    cond = WordleBoard(self.word, self.root, user_input, self.col1, self.col2, self.col3,
                                       self.col4, self.turn_num, self.board_len)
                    cond.get_board()

            else:  # wrong word length
                messagebox.showerror("incorrect word length", f'enter a {len(self.word)} letter word')

        else:  # turn limit
            messagebox.showerror("you lose!", f"You Lose! The word was {self.word}")
