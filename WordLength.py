from TurnNum import TurnNum
from tkinter import simpledialog


class WordLength(TurnNum):
    """Gets desired word length from user, inherits TurnNum"""

    def __init__(self):
        self.user_input = simpledialog.askstring(title='Wordle',
                                                 prompt='Enter desired wordle word length')
