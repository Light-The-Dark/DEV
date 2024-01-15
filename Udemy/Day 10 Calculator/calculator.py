import art

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div, 
}

def check_operand(operand, num1, num2):
    for key in operations:
            if operand == key:
                answer = operations[key](num1, num2)
                print(f"{num1} {key} {num2} = {answer}")
                return answer
def calculator():
    print(art.logo)
    num1 = float(input("Type in a number: "))
    operand = input("Type in operand: ")
    num2 = float(input("Type in a number: "))

    answer = check_operand(operand, num1, num2)

    while True:    
        going = input("Would you like to keep on going? y for yes, n for no, r to restart ")
        if going == "n":
            break
        elif going == "k":
            calculator()
            
        operand = input("Type in new operand: ")
        new_answer = float(input("Type in new number: "))
        new_answer = check_operand(operand, answer, new_answer)
        answer = new_answer

calculator()