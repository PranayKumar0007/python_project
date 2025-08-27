from operator import truediv

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
}
profit = 0
#TODO 1 : ASk for input,
#TODO 2 :check resources for input , make a fn
#TODO 3:  if resources enough calculate coins , make a fn to calculate coins
# TODO 4 : if coins enough return change , print outcome

def resource_check(drink_ingredients):
    """ True if the ingredients are sufficient,False otherwise. """
    for item in drink_ingredients:
        if drink_ingredients[item] <= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Returns the total amount of coins inserted."""
    print("Please insert coins")
    total = int(input("How many quarters?")) * 0.25
    total+= int(input("How many dimes?")) * 0.1
    total+= int(input("How many nickles?")) * 0.05
    total+= int(input("How many pennies?")) * 0.01
    return total

def transaction(money_received, drink_cost):
    """Returns true if successful and false otherwise."""
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost , 2)
        print(f"The drink cost is {drink_cost} and change is {change}")
        profit += drink_cost
        return True
    else:
        print("Sorry there is not enough money")
        return False

def make_coffee(drink_name,drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name} ☕")






on = True
while on:
    choice = input("What would you like? (espresso/latte/cappuccino)\n").lower()
    if choice == "off":
        on = False
    elif choice == "report":
        print(f"Water:{resources['water']} ")
        print(f"Milk:{resources['milk']} ")
        print(f"Coffee{resources['coffee']} :")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if resource_check(drink["ingredients"]):
            payment = process_coins()
            if transaction(payment, drink["cost"]):
                make_coffee(choice,drink["ingredients"])









