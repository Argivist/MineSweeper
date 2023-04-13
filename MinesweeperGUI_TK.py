import tkinter
from MineSweeper import MineSweeper

MineSweeper_game=MineSweeper("m")

currect_select_state="f"


def buttonPressed(x, y):
    if currect_select_state=="d":
        MineSweeper_game.Delete(x,y)
    else:
        MineSweeper_game.flag(x,y)
    for i in grid_buttons:
        i.configure(text=MineSweeper_game.MineField_state[int(grid_buttons.index(i)/MineSweeper_game.size)][grid_buttons.index(i)%MineSweeper_game.size])


gameButtons=[]

gameScreen=tkinter.Tk("MineSweeper","MineSweeper")
a=0
b=0
grid_buttons=[]
for i in MineSweeper_game.MineField_state:
    for j in i:
        gameButton=tkinter.Button(gameScreen,text=j,width=2,height=2,command=lambda x=a,y=b: buttonPressed(x,y))
        grid_buttons.append(gameButton)
        gameButton.grid(row=a,column=b)
        b=b+1
    a=a+1
    b=0


gameScreen.mainloop()


