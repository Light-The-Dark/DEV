from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(user_text, shift_amount, direction):
    new_text = ""
    shift_amount = shift_amount % 26
    if direction == "decode":
        shift_amount *= -1
    for letter in user_text:
        if letter not in alphabet:
            new_text += letter
        else:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_text += alphabet[new_position]
    print(f"The {direction}d text is: {new_text}")


end = False
print(logo)
while end == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    go = input("Do you want to run again? Type Y or N ").lower()
    if go == "n":
        end = True
