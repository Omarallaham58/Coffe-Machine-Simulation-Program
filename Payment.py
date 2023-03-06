from Materials import *
from order import *
class Payment:
    def __init__(self, total, money_received, drink_cost ):
        self.total=total
        self.money_received=money_received
        self.drink_cost=drink_cost
    
    def process_coins(self):
        print("please insert coins")
        self.total = int(input("how many quarters:? ")) * 0.25
        self.total += int(input("how many dimes:? ")) * 0.10
        self.total += int(input("how many nickles:? ")) * 0.05
        self.total += int(input("how many pennies:? ")) * 0.01
        return self.total
    
    def is_transaction_successful(self, money_received, drink_cost):
      if self.money_received >= self.drink_cost:
         change = round(self.money_received - self.drink_cost, 2)
         print(f"here is  ${change} in change ")
         return True
      else:
        print("Sorry that's not enough money . Money Refunded ")
        return False

