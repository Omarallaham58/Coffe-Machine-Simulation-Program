from Materials import *
from Payment import *
class Coffe:
    def __init__(self, drink_name, order_ingredient):
        self.drink_name=drink_name
        self.order_ingredients=order_ingredient
    
    def make_coffee(self, drink_name, order_ingredient):
       print(f"here is your {self.drink_name}!!! ")