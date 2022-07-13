class Player:
    uid = 0
    def __init__(self):
        uid += 1
        self.uid = uid - 1
        self.wins_cnt = 0

class Field:
    def __init__(self, rows, cols):
        self.lines_hor = [[False] * cols] * rows
        self.lines_ver = [[False] * cols] * rows
    def fill(hor_ver_bar, row, col):
        if (hor_ver_bar):
            if (lines_hor):
                if lines_hor[row][col]:
                    riase Exception("already filled")

n = int(input()) #players count
m, k = [int(x) for x in input().split()] #rows and columns
while True:
    field = Field(n, m)