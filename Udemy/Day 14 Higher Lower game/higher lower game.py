from art import *
from game_data import *
import random

GAME_OVER = False
SCORE = 0

def followers(a, b):
    """Calculates who has more followers and returns only the winner count"""
    if a > b:
        return a
    else:
        return b

def calculate(highest, user_guess):
    """Calculates score and if wrong answer stops the game and tells user score"""
    global SCORE
    if  user_guess ==  highest:
        SCORE += 1
        print(f"Current score is: {SCORE}")
    else:
        print(f"You lose, score is {SCORE}")
        return True
    
int1 = random.randint(0, len(data) - 1)
int2 = random.randint(0, len(data) - 1)

while not GAME_OVER:
    print(logo)

    while int1 == int2:
        int2 = random.randint(0, len(data) - 1)
        
    print(f"Name: {data[int1]["name"]}, Description: {data[int1]["description"]}, Country: {data[int1]["country"]}")
    print(vs)
    print(f"Name: {data[int2]["name"]}, Description: {data[int2]["description"]}, Country: {data[int2]["country"]}")
    
    user_input = input("Who has more followers? a or b: ")
    highest_followers = followers(data[int1]["follower_count"], data[int2]["follower_count"])
    print(highest_followers)
    
    if user_input == "a":
        user_input = data[int1]["follower_count"]
    else:
        user_input =  data[int2]["follower_count"]

    GAME_OVER = calculate(highest_followers, user_input)

    int1 = int2
    int2 = random.randint(0, len(data) - 1)
    



