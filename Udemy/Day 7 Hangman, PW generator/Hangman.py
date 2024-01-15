import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["program", "hello"]
word = random.choice(word_list)
guess_list = []


for letter in word:
    guess_list += "_"

score = 0
guesses = 6
game_over = False

while game_over == False:
    print(guess_list)
    print(stages[guesses])
    user_input = input("Guess a letter: ").lower()

    for index in range(len(word)):
        if word[index] == user_input:
            guess_list[index] = user_input
            score += 1

    if user_input not in word:
        guesses -= 1
        print(f"{user_input} not in the word")


    if score == len(word):
        print(guess_list) 
        print("You won")
        game_over = True
    elif guesses == 0:
        print(stages[guesses])
        print("You lose")
        game_over = True
