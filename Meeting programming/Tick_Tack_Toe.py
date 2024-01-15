# To do print x or o, turns, check if winner

board = []

def initialize_board():
    i = 0
    for num in range(3):
        board.append([])
        for num2 in range(3):
            board[i].append([])
        i += 1
    return

def print_board():
    i = 0
    for num in range(3):
        print(board[i])
        i += 1

def player(player):
    if player % 2 == 0:
        playerst = "X"
        return playerst
    else:
        playerst = "O"
        return playerst

def user_input(player):
    x, y = input(f"{player}, please move ").split()
    x = int(x)
    y = int(y)
    return x, y

#def check_winner(player):
    

initialize_board()

game_over = False

print("")

i = 1

while game_over == False:

    player_str = player(i)
    print_board()
    x, y = user_input(player_str)
    board[x - 1][y - 1] = player_str
    #check_winner(player_str)
    
    
    i += 1