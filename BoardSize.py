from TurnNum import TurnNum
from tkinter import simpledialog


class BoardSize(TurnNum):
    """class to get board size val from user, inherits TurnNum"""

    def __init__(self):
        """initialize BoardSize"""
        self.user_input = simpledialog.askstring(title='Wordle',
                                                 prompt='Enter desired board size')
