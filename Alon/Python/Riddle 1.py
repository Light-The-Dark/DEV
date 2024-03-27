def solution_1(arr):
    highest = max(arr)

    for _ in arr:
        if highest - 1 in arr and highest > 0:
            highest -= 1

    if highest == -1:
        highest = 2
        
    print(highest - 1)

arra = [2, 5, 1, 7, 10, 9, 8, -2, -3]
# arra = [-1, -2, -3]

solution_1(arra)













