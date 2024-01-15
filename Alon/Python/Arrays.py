arr = []
Size_Of_Array = 4


def read_num(arr):
    for num in range(Size_Of_Array):
        number = int(input("Type in 1 numbers "))
        arr.append(number)
    return arr

def sort_array(arr):
    i = 0
    j = 1
    for num in range(Size_Of_Array - 1):
        for num in range(Size_Of_Array - j):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp    
            j += 1
        i += 1
        j = i + 1
        
def print_array(arr):
    print(arr)

def main():
    arr2 = read_num(arr)
    sort_array(arr2)
    print_array(arr2)


main()