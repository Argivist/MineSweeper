import tkinter
import MinesweeperGUI_TK as Game
class HomePage:

    def __init__(self):
        self.HomeScreen=tkinter.Tk("MS","MineSweeper")
        self.HomeScreen.title="MineSweeper"

        Labeling=tkinter.Label(self.HomeScreen, text="MineSweeper")
        Labeling.grid()
        LevelButton=[]
        LevelButton.append(tkinter.Button(self.HomeScreen,text="Easy",command=lambda: self.play("e")))
        LevelButton.append(tkinter.Button(self.HomeScreen, text="Medium", command=lambda: self.play("m")))
        LevelButton.append(tkinter.Button(self.HomeScreen, text="Difficult", command=lambda: self.play("h")))
        for i in LevelButton:
            i.grid()


        self.HomeScreen.mainloop()
    def play(self,diff):
        self.HomeScreen.destroy()
        Game.Game(diff)
