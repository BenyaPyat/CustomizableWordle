from tkinter import *
from tkinter import messagebox, simpledialog
from ColorMenu import ColorMenu


class TurnNum:
    """gets user input for number of turns"""

    def __init__(self):
        """initialize TurnNum"""
        self.user_input = simpledialog.askstring(title='Wordle',
                                                 prompt='Enter desired amount of turns')

    def get_val(self):
        """returns user inputted turn number"""
        return self.user_input
