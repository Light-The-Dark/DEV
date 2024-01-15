# TO DO score counter, turns

def board_initial():
    board = [] 
    x = 0
    y = 0

    for num in range(8):
        board.append([])
        for num in range(8):
            board[x].append([])
            if x%2 == 0 and y%2 == 0:
                board[x][y] = "#"
            elif x%2 == 0 and y%2 == 1:
                board[x][y] = "-"
            elif x%2 == 1 and y%2 == 1 :
                board[x][y] = "#"
            elif x%2 == 1 and y%2 == 0 :
                board[x][y] = "-"
            y += 1
        y = 0
        x += 1         

    return board
def initial_pieces(board):
    x = 0
    y = 0
    char1 = "1"
    for num in range(2):
        for num in range(3):
            for num in range(8):
                if board[x][y] == "#":
                    board[x][y] = char1
                y += 1
            y = 0
            x += 1
        x = 5
        char1 = "2"
def move():
    global game_over
    lives1 = 1
    lives2 = 1

    x, y = (input("Type in x and y of piece to move: ").split())
    x2, y2 = (input("Type where you would like to move piece to: ").split())
    x = int(x)
    x2 = int(x2)
    y = int(y)
    y2 = int(y2)

    if board[x][y] == "1" and x2 == x + 1 and y2 == y +1 or y2 == y -1:
        board[x][y] = "#"
        if board[x2][y2] == "2":
            board[x2][y2] = "#"
            lives2 -= 1
            if y2 == y + 1 and x2 == 7:
                board[x2 + 1][y2 + 1] = "11"  
            elif y2 == y - 1 and x2 == 7:
                board[x2 + 1][y2 - 1] = "11"            
            elif y2 == y + 1:
                board[x2 + 1][y2 + 1] = "1"
            elif y2 == y - 1:
                board[x2 + 1][y2 - 1] = "1"

        else:
            board[x2][y2] = "1"
    elif board[x][y] == "2" and x2 == x - 1 and y2 == y +1 or y2 == y -1:
        board[x][y] = "#"
        if board[x2][y2] == "1":
            board[x2][y2] = "#"
            lives1 -= 1
            if y2 == y + 1:
                board[x2 + 1][y2 + 1] = "2"
            elif y2 == y - 1:
                board[x2 + 1][y2 - 1] = "2"
        else:
            board[x2][y2] = "2"   

    if lives1 == 0 or lives2 == 0:
        game_over = True
        return game_over

def print_board():
    x = 0
    for num in range(8):
        print(board[x])
        x += 1
board = board_initial()
initial_pieces(board)
print_board()



game_over = False

while game_over == False:
    move()
    print_board()

print("Over")