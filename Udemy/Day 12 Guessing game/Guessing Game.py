## Welcome
## Tell user if too high or too low
## Tell win or lose
import art
import random

print(art.logo)
print("Welcome to the guessing game! Choose a number between 1 and 100")
level = input("Type easy or hard: ")

if level == "easy":
    lives = 10
elif level == "hard":
    lives = 5

number = random.randint(1,100)
print(f"Number is: {number} - printing for testing purposes")

def game():
    global lives

    guess = int(input("Take a guess: "))

    if guess > number:
        print("Too high")
        lives -= 1
    elif guess < number:
        print("Too low")
        lives -= 1
    elif guess == number:
        print("You won!")
        return number
    
    print(f"Remaining attempts: {lives}")
    
    if lives == 0:
        print("You lose")
        return number

guess = 0 
while guess != number:
    guess = game()
