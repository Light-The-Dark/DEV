from art import logo

print(logo)
print("Welcome to blind auction")

dictionary = {}

bidding = True

def find_highest_bidder():
    highest_bid = 0
    for person in dictionary:
        if dictionary[person] > highest_bid:
            highest_bid = dictionary[person]
            highest_bidder = person
    print(f"Winner is {highest_bidder} at ${highest_bid} ")

while bidding == True:
    user_name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    ask = input("Any more users? Type 'y' or 'n' ").lower()
    dictionary[user_name] = bid

    if ask == "n":
        bidding = False
        find_highest_bidder()
