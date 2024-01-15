from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

end = False

items = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while end == False:
    coffee = input(f"What would you like? {items.get_items()}: ").lower()
    if coffee == "off":
        end = True
        print("Shutting down for maintenance")
    elif coffee == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = items.find_drink(coffee)
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)          
        else:
            print("Not enough resources")

