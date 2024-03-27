def solution_1(arr):
    highest = max(arr)
    lowest = min(arr)

    if highest <= 0:
        highest = 2
    else:
        for _ in arr:
            if highest - 1 in arr:
                highest -= 1
            elif highest == lowest:
                highest = max(arr) + 2
            else:
                break

    print(highest - 1)


def solution_2(arr):
    highest = max(arr)
    lowest = min(arr)

    if highest <= 0:
        highest = 2  



# arra = [1, 2, 3, 4, 5]
# arra = [2, 5, 1, 7, 10, 9, 8, -2, -3]
# arra = [-1, -2, -3, -4]

solution_1(arra)













