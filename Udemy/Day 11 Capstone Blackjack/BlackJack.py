import random
import art

############### Blackjack Project #####################


############### Our Blackjack House Rules #####################


## Ask if you want another card

def calculate(user):
    sum = 0
    for card in user:
        sum += card
    for card in user:
        if 11 in user and sum > 21:
            sum -= 10
    return sum

def check_winner(user_deal, user):

    if user_deal > 21 or user > 21:
        if user > 21:
            print("You lose")
        else:
            print("You win")
    elif user_deal > user:
        print("You lose")
    elif user_deal == user:
        print("Draw")
    else:
        print("You win")

def print_dealer(dealer):
    show_dealer = []
    i = 1
    for card in range(len(dealer) - 1):
        show_dealer.append(dealer[i])  
        i += 1
    print(f"Dealers cards are {show_dealer}")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game = True


while game:
    print(art.logo)
    ask = input("Would you like to play? y for yes, n for no: ")
    if ask == "n":
        break

    player = []
    dealer = []

    player.append(random.choice(cards))
    player.append(random.choice(cards))
    dealer.append(random.choice(cards))
    dealer.append(random.choice(cards))

    print(f"Players cards: {player}")
    print(f"Dealers cards: {dealer[1]}")

    keep_going = True

    while keep_going:
        more_cards = input("Would you like another card? y or n: ")
        if more_cards == "y":
            player.append(random.choice(cards))
            print(f"Players cards: {player}")
            print_dealer(dealer)
    
        else:
            keep_going = False

    while calculate(dealer) < 17:
        if calculate(player) <= 21:
            dealer.append(random.choice(cards))
        else:
            break
        print(f"Players cards are: {player}")
        print_dealer(dealer)
    


    player_total = calculate(player)
    dealer_total = calculate(dealer)

    print(f"Players cards: {player} for a total of {player_total}")
    print(f"Dealers cards: {dealer} for a total of {dealer_total}")

    check_winner(dealer_total, player_total)
