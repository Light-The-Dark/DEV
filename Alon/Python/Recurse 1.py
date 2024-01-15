def fact(num):
    if num == 2:
        return num
    else:
        return fact(num - 1) * num


number = int(input("Type in a number for factorial: "))
print(fact(number))
