from data import MENU, resources

running = True
money = 0.00


def prompt() -> str:
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    return coffee


def report() -> None:
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print("Cash: ${0:.2f}".format(money))


def coins(coffee):
    drink = MENU[coffee]
    print("Insert coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    total = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)
    if total >= drink["cost"]:
        change = total - drink["cost"]
        print("Here is ${0:.2f}".format(change)," in change.")
        print(f"Enjoy your {coffee}.")
        resources["water"] -= drink["ingredients"]["water"]
        resources["coffee"] -= drink["ingredients"]["coffee"]
        if coffee == "latte" or drink == "cappuccino":
            resources["milk"] -= drink["ingredients"]["milk"]
        global money
        money += total - change
    else:
        print("Sorry, that is not enough.  Refunding money.")


def make_coffee(coffee) -> None:
    if coffee == "off":
        exit()
    elif coffee == "report":
        report()
    else:
        drink = MENU[coffee]
        if coffee == "espresso":
            if resources["water"] >= drink["ingredients"]["water"] and \
                    resources["coffee"] >= drink["ingredients"]["coffee"]:
                coins(coffee)
        elif resources["water"] >= drink["ingredients"]["water"] and \
                resources["milk"] >= drink["ingredients"]["milk"] and \
                resources["coffee"] >= drink["ingredients"]["coffee"]:
            coins(coffee)
        else:
            print(f"Sorry, not enough resource to make a {coffee}.")


while running:
    make_coffee(prompt())



