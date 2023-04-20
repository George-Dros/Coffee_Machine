import os

from GUIDES import MENU
from GUIDES import resources
from art import logo

turn_off = False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def order():
    user_order = input("What would you like? ((espresso/latte/cappuccino):").lower()
    return user_order


def report():
    global resources
    print(f"Water:{resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {resources['money']}")


def check_resources(ordering):
    global resources

    if ordering == 'espresso':
        if MENU[ordering]["ingredients"]["water"] <= resources["water"] and MENU[ordering]["ingredients"]["coffee"] <= resources["coffee"]:
            resources["water"] -= MENU[ordering]["ingredients"]["water"]
            resources["coffee"] -= MENU[ordering]["ingredients"]["coffee"]
            return True

        elif MENU[ordering]["ingredients"]["water"] > resources["water"]:
            print("Sorry not enough water")
            return False

        elif MENU[ordering]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry not enough coffee")
            return False

    elif ordering == 'latte' or 'cappuccino':
        if MENU[ordering]["ingredients"]["water"] <= resources["water"] and MENU[ordering]["ingredients"]["coffee"] <= resources["coffee"] and MENU[ordering]["ingredients"]["milk"] <= resources["milk"]:
            resources["water"] -= MENU[ordering]["ingredients"]["water"]
            resources["coffee"] -= MENU[ordering]["ingredients"]["coffee"]
            resources["milk"] -= MENU[ordering]["ingredients"]["milk"]
            return True
        elif MENU[ordering]["ingredients"]["water"] > resources["water"]:
            print("Sorry not enough water")
            return False

        elif MENU[ordering]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry not enough coffee")
            return False

        elif MENU[ordering]["milk"] > resources["milk"]:
            print("Sorry not enough milk")
            return False


def coin_process(order):
    print(f"Your coffee is {order['cost']}")
    print("Please insert coins:")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    paid = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    if paid >= order['cost']:
        print("Your coffee is being prepared")
        resources['money'] += order['cost']
        change = paid - order['cost']
        print(f"Your change is: {change}")

    else:
        print("Sorry that's not enough money. Money refunded.")

print(logo)

while not turn_off:
    ordered = order()
    if ordered == "off":
        turn_off = True
        print("Maintenance Mode entered")

    elif ordered == "report":
        report()

    elif check_resources(ordered):
        coin_process(MENU[ordered])
        print(f"Here is your {ordered}, enjoy!")
        clear_screen()
    else:
        print("Sorry the coffee-machine has not enough ingredients to make this coffee, please choose another one.")





