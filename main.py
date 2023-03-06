from Materials import *
from Payment import *
from order import *

MENU={
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
RESOURCES={
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
is_on = True
# total=1

while is_on:
    choice = input("what would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        
        print(Resources(RESOURCES, None).report())

    elif choice in ["latte", "cappuccino","espresso" ]:
        drink = MENU[choice]
        if Resources(resources=RESOURCES, order_ingredients=drink["ingredients"]).is_resources_sufficient(drink["ingredients"]):
            payment=Payment(total=None, money_received=None, drink_cost=None).process_coins()
        
            if Payment(total=None, money_received=payment, drink_cost=drink["cost"]).is_transaction_successful(money_received=payment, drink_cost=drink["cost"]):
                
                Coffe(drink_name=choice, order_ingredient=drink["ingredients"]).make_coffee(choice, drink["ingredients"])
                Resources(resources=RESOURCES, order_ingredients=drink["ingredients"]).Update_resources(RESOURCES, drink["ingredients"])
    else:
        print("Invalid output")
            
