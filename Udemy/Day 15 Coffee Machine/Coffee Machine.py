end = False

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def check_resources(coffee):
    """Checks if there is enough resources"""
    enough_resources = True
    for resource in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"][resource] > resources[resource]:
            enough_resources = False
            print(f"Not enough {resource}")
    return enough_resources        

def money(coffee):
    
    sum = float(input("Put in quarters: ")) * .25 
    sum  += float(input("Put in dimes: ")) * .10
    sum += float(input("Put in nickels: ")) * .05
    sum += float(input("Put in pennies: ")) * .01
    print(f"Total ${sum}")
    if MENU[coffee]["cost"] > sum:
        print("Not enough money. We took your money anyways")
    else:
        resources["money"] += MENU[coffee]["cost"]
        sum -= float(MENU[coffee]["cost"])
        print(f"Your change is {round(sum, 2)}")

def dispense(coffee):
    for resource in MENU[coffee]["ingredients"]:
        resources[resource] -= MENU[coffee]["ingredients"][resource]

while end == False:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee == "off":
        end = True
        print("Shutting down for maintenance")
    elif coffee == "report":
        print(f"Water: {resources["water"]}, Milk: {resources["milk"]}, Coffee: {resources["coffee"]}, Money: ${resources["money"]}")
    elif coffee == "espresso" or coffee == "latte" or coffee == "cappuccino": 
        enough = check_resources(coffee)

        if enough:
            money(coffee)
            dispense(coffee)
            print(f"Enjoy your {coffee}!")
    else:
        print("Invalid selection")
