from tkinter import Label
from BoardSize import BoardSize


class WordleBoard:
    """creates wordle board from given parameters"""

    def __init__(self, word, root, user_input, col1, col2, col3, col4, turn_num, board_len):
        """initialize WordleBoard"""
        self.word = word
        self.root = root
        self.user_input = user_input
        self.col1 = col1
        self.col2 = col2
        self.col3 = col3
        self.col4 = col4
        self.turn_num = turn_num
        self.board_len = board_len

    def get_board(self):
        """adjusts board based off user input word"""
        for i, letter in enumerate(self.user_input):

            # configs label
            lbl = Label(self.root, text=letter.upper(), font=('Arial', int(self.board_len)))
            lbl.grid(row=self.turn_num, column=i, padx=self.board_len, pady=self.board_len)

            if letter == self.word[i]:  # letter is in word and in right position
                lbl.config(bg=self.col1, fg=self.col2)

            if letter in self.word and not letter == self.word[i]:  # letter is in word, but not correct spot
                lbl.config(bg=self.col3, fg=self.col2)

            if letter not in self.word:  # letter not in the word
                lbl.config(bg=self.col2, fg=self.col4)
