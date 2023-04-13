import random
class MineSweeper:

    #Initiator variables
    MineField=[]#hidden Minefield
    MineField_state=[]#Visible Minefield
    cell_num=0#num of created Cells
    bomb_num=0#num of spawned Bombs
    cleared=0#num of cells deleted
    hit_bomb=False#has player hit a bomb
    size=0

    Difficulty = {
        "e": [7, 10],
        "m": [10, 12],
        "h": [15, 30]
    }
    #initiagor constructor
    def __init__(self,diff):
        self.size = self.Difficulty[diff][0]
        Bomb_num = self.Difficulty[diff][1]
        self.MineGenerate(self.size, Bomb_num)



    #Minefield generator

    def MineGenerate(self, size, bomb_num):
        # minefield
        for a in range(size):
            row = []
            row_state = []
            for j in range(size):
                row.append("")
                row_state.append("-")
            self.MineField.append(row)
            self.MineField_state.append(row_state)

        # Randomly places bombs in field
        for a in range(0, bomb_num):
            x = round(random.random() * size - 1)
            y = round(random.random() * size - 1)
            while self.MineField[x][y] == 'b':
                x = round(random.random() * size - 1)
                y = round(random.random() * size - 1)
            self.MineField[x][y] = 'b'

        # Number Placement for pomb population
        for a in self.MineField:
            for j in a:
                m = self.MineField.index(a)
                n = a.index(j)
                self.ajacent(m, n, size, self.MineField)

    #used to determine adjacent bombs
    def ajacent(self,x, y, s, lis):
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

    def select_delete_Value(self,x, y, s):
        dx = []
        dy = []
        dx.append(x)
        dy.append(y)


        if self.MineField[x][y] == "b":
            self.hit_bomb=True
        elif self.MineField_state[x][y] == "🚩":
            pass
        elif isinstance(self.MineField[x][y], int) and self.MineField[x][y] != 0:
            self.MineField_state[x][y] = self.MineField[x][y]
            self.cleared+=1
        else:
            for i in dx:
                j = dy[dx.index(i)]
                for k in [i - 1, i, i + 1]:
                    for l in [j - 1, j, j + 1]:
                        if k == -1 or l == -1 or k == s or l == s or self.MineField_state[k][l] == "🚩" or self.MineField[k][
                            l] == 'b':
                            pass

                        elif self.MineField[k][l] == 0:
                            if self.MineField_state[k][l] == "-":
                                dx.append(k)
                                dy.append(l)
                                self.MineField_state[k][l] = ""
                                self.cleared+=1
                        else:
                            self.MineField_state[k][l] = self.MineField[k][l]
                            self.cleared+=1
    #Destroying cells
    def Delete(self,x,y):
        self.select_delete_Value(x,y,self.size)
    def flag(self,x, y):
        if self.MineField_state[x][y] == "🚩":
            self.MineField_state[x][y] = "-"
        else:
            self.MineField_state[x][y] = "🚩"

    def printMineField(self,field):
        for a in field:
            print(a)
        print("")

#p1=MineSweeper()
