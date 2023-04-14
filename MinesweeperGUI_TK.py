import tkinter
from MineSweeper import MineSweeper
import WinLoss as WL

class Game:
    grid_buttons = []
    currect_select_state = "d"

    def __init__(self,difficulty):
        self.MineSweeper_game = MineSweeper(difficulty)

        self.gameScreen = tkinter.Tk("MineSweeper", "MineSweeper")
        self.gameScreen.title = "MineSweeper"
        a = 0
        b = 0

        #Game Field
        for i in self.MineSweeper_game.MineField_state:
            for j in i:
                gameButton = tkinter.Button(self.gameScreen, text=j, width=2, height=2,
                                            command=lambda x=a, y=b: self.buttonPressed(x, y))
                self.grid_buttons.append(gameButton)
                gameButton.grid(row=a, column=b)
                b = b + 1
            a = a + 1
            b = 0

        #Flag Section
        Flag_Toggle=tkinter.Button(self.gameScreen,text="🚩",command=lambda: self.flag())
        Flag_Toggle.grid()

        self.gameScreen.mainloop()

    #toggle destroy and flag_
    def flag(self):
        if self.currect_select_state=="d":
            self.currect_select_state="f"
        else:
            self.currect_select_state="d"

    #button Pressed
    def buttonPressed(self, x, y):
        if self.MineSweeper_game.MineField_state[x][y]==self.MineSweeper_game.blank or self.MineSweeper_game.MineField_state[x][y]==self.MineSweeper_game.flag_:
            if self.currect_select_state=="d":
                self.MineSweeper_game.Delete(x,y)
            else:
                self.MineSweeper_game.flag(x, y)
            if self.MineSweeper_game.hit_bomb:
                for i in self.grid_buttons:
                    if self.MineSweeper_game.MineField[int(self.grid_buttons.index(i) / self.MineSweeper_game.size)][
                        self.grid_buttons.index(i) % self.MineSweeper_game.size]==self.MineSweeper_game.bomb:
                        i.configure(text=self.MineSweeper_game.bomb)
                WL.Loss()
            elif self.MineSweeper_game.cell_num-self.MineSweeper_game.bomb_num==self.MineSweeper_game.cleared:
                WL.Win()
            for i in self.grid_buttons:
                i.configure(text=self.MineSweeper_game.MineField_state[int(self.grid_buttons.index(i)/self.MineSweeper_game.size)][self.grid_buttons.index(i)%self.MineSweeper_game.size])
        else:
            pass

