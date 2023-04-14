import tkinter as Tk
import sys

import MinesweeperGUI_TK


class Win:
    def __init__(self, ):
        self.win = Tk()
        self.win.geometry("500x300")
        self.win.title("Win")
        Tk.Label(self.win, text="You Win 🏆🥇").pack()
        self.win.mainloop()

class Loss:
    windows = set()
    def __init__(self):
        self.loss=Tk.Tk()
        self.loss.title("Loss")
        Tk.Label(self.loss, text="You Lose").pack()
        self.loss.mainloop()


