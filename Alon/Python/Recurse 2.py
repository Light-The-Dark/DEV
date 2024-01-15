arr = [8,1,-9,9,3,4,-4]
new_array = []

def rec(i):
    if i != - 1:
        if arr[i] >= 0:
            new_array.append(arr[i])
        rec(i-1)
    

rec(len(arr) - 1)
print(new_array)