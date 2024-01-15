user_input = int(input("How many boxes do you want your grid to be? "))


def create_matrix(user):
    matrix = []
    i = 0
    for num in range(user_input):
        matrix.append([])
        for num2 in range(user_input):
            matrix[i].append([])
        i += 1
    return matrix


def fill_matrix(matrix):
    x = 0
    y = 0
    z = user_input - 1
    for num in range(user_input):
        for num2 in range(user_input):
            if x == 0 or y == 0 or x == user_input - 1 or y == user_input - 1 or x == y or x == z:
                matrix[x][y] = "*"
                x += 1
            else:
                matrix[x][y] = "-"
                x += 1

        x = 0
        y += 1
        z -= 1
    return matrix


def print_matrix(matrix):
    i = 0
    for number in range(user_input):
        print(matrix[i])
        i += 1


def main():
    matrix = create_matrix(user_input)
    matrix = fill_matrix(matrix)
    print_matrix(matrix)


main()

print("")
print("YES!!!!!!!!!! IT WORKS!!!!!!!!!!!")
input(" ")
