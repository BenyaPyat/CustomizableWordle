from GUI import GUI
from tkinter import *

# creates root
rt = Tk()

# runs GUI class
wordle = GUI(rt)
wordle.guess()

rt.mainloop()
