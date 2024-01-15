import random
board = []

def initialize_board(user_input):
    i = 0
    j = 0
    for _ in range(user_input):
        board.append([])
        for _ in range(user_input):
            board[i].append([])
            board[i][j] = str(random.randint(0, 100))
            j += 1
        i += 1
        j = 0

    # You can change x and y starting position and the +/- j to decide which direction to go in
    x_position = 3
    y_position = 2
    numbers = input("Enter some numbers: ").split(" ")
    for number in numbers:
        board[x_position - j][y_position + j] = number
        j += 1
    return numbers


def print_board(user_input):
    i = 0
    for _ in range(user_input):
        print(board[i])
        i += 1


def find_string(size, numbers):
    stop = False
    i = 0
    j = 0
    for _ in range(size):
        for _ in range(size):
            if board[i][j] == numbers[0]:
                print(f"Found first num by board index {i} {j}")
                stop = complete_search(i, j, numbers)
                if stop == True:
                    break
            j += 1
        if stop == True:
            break
        j = 0
        i += 1
    if stop == False:
        print("String not found")


def complete_search(x, y, numbers):
    i = 1
    size = len(numbers)
    for _ in range(size-1):
        # All in one but cannot see which condition hit:
        # if board[x][y + i] == numbers[i] or board[x][y - i] ==
        # numbers[i] or board[x - i][y] == numbers[i] or board[x + i][y] == numbers[i] or board[x - i][y + i] ==
        # numbers[i] or board[x + i][y + i] == numbers[i] or board[x - i][y - i] == numbers[i] or board[x + i][y - i]
        # == numbers[i]:

        # Search Right
        if board[x][y + i] == numbers[i]:
            print(f"Found on Right, index {x} {y + i}")
        # Search Left
        elif board[x][y - i] == numbers[i]:
            print(f"Found on Left, index {x} {y - i}")
        # Search Up
        elif board[x - i][y] == numbers[i]:
            print(f"Found Up, index{x - i} {y}")
        # Search Down
        elif board[x + i][y] == numbers[i]:
            print(f"Found Down, index {x + i} {y}")
        # Search Up Right Diagonal
        elif board[x - i][y + i] == numbers[i]:
            print(f"Found on Up Right Diagonal, index {x - i} {y + i}")
        # Search Down Right Diagonal
        elif board[x + i][y + i] == numbers[i]:
            print(f"Found on Down Right Diagonal, index {x + i} {y + i}")
        # Search Up Left Diagonal
        elif board[x - i][y - i] == numbers[i]:
            print(f"Found on Up Left Diagonal, index {x - i} {y - i}")
        # Search Down Left Diagonal
        elif board[x + i][y - i] == numbers[i]:
            print(f"Found on Down Left Diagonal, index {x + i} {y - i}")
        else:
            return False
        i += 1
    print("Entire string found, stopping search")
    return True


def main():
    user_size = int(input("How big do you  want your array? "))
    user_numbers = initialize_board(user_size)
    print_board(user_size)
    find_string(user_size, user_numbers)


main()
