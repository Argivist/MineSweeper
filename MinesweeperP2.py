import random
import numpy as np

# logic
MineField = []
Minefield_state = []
flagged = False

Difficulty = {
    "e": [7, 10],
    "m": [10, 12],
    "h": [15, 30]
}


def MineGenerate(size, bomb_num):
    # minefield
    for a in range(size):
        row = []
        rowstate = []
        for j in range(size):
            row.append("")
            rowstate.append("-")
        MineField.append(row)
        Minefield_state.append(rowstate)

    # Random Bomb Gen
    for a in range(0, bomb_num):
        x = 0
        y = 0
        while MineField[x][y] == 'b':
            x = round(random.random() * size - 1)
            y = round(random.random() * size - 1)

        MineField[x][y] = 'b'
    print(bomb_num)

    # Number Placement
    for a in MineField:
        for j in a:
            m=MineField.index(a)
            n=a.index(j)
            ajacent(m, n, size, MineField)


def ajacent(x, y, s, lis):
    num = 0
    for i in [x - 1, x, x + 1]:
        for j in [y - 1, y, y + 1]:
            if (i == x and j == y) or i == -1 or j == -1 or i == s or j == s:
                pass
            elif lis[i][j]=='b':
                num+=1
    if lis[x][y]=='b':
        pass
    elif lis[x][y]==0:
        pass
    else:
        lis[x][y] = num



def select_delete_Value(x, y, s):
    dx = []
    dy = []
    dx.append(x)
    dy.append(y)

    count = 0

    if MineField[x][y] == "b":
        return "bomb"
    elif MineField[x][y] == "f":
        pass
    elif isinstance(MineField[x][y], int) and MineField[x][y]!=0:
        Minefield_state[x][y] = MineField[x][y]
    else:
        for i in dx:
            j = dy[dx.index(i)]
            for k in [i - 1, i, i + 1]:
                for l in [j - 1, j, j + 1]:
                    if k == -1 or l == -1 or k == s or l == s or Minefield_state[k][l] == 'f' or MineField[k][l] == 'b':
                        pass

                    elif MineField[k][l] == 0:
                        if Minefield_state[k][l] == "-":
                            dx.append(k)
                            dy.append(l)
                            Minefield_state[k][l] = ""
                            count += 1
                    else:
                        Minefield_state[k][l] = MineField[k][l]


def flag(x, y):
    if Minefield_state[x][y] == "f":
        Minefield_state[x][y] = "-"
    else:
        Minefield_state[x][y] = "f"


# Unnecesary
def printMineField(field):
    for a in field:
        print(a)
    print("")


sz = 7


def gameStart(diff):
    a = Difficulty[diff][0]
    b = Difficulty[diff][1]
    MineGenerate(a, b)
    print(a, b)

    printMineField(MineField)
    # flag(7, 5)
    #select_delete_Value(6, 6, sz)
    printMineField(Minefield_state)
    return a, b

def GameOver():
    Minefield_state=[]
    MineField=[]
    flagged=False


