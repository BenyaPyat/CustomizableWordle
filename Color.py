from TurnNum import TurnNum
from tkinter import simpledialog


class Color(TurnNum):
    """class to get color scheme from user, inherits TurnNum"""

    def __init__(self):
        """initialize TurnNum"""
        self.user_input = simpledialog.askstring(title='Wordle',
                                                 prompt='Enter 4 colors separated by space for the color scheme')
