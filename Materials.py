from Payment import *
from order import *      
class Menu:
    def __init__(self, menu):
        self.menu=menu

    def get_menu(self):
      return self.menu           

class Resources:
    def __init__(self, resources, order_ingredients):
        self.resources = resources
        self.order_ingredients = order_ingredients
    
    def report(self):
        return self.resources

    def is_resources_sufficient(self, order_ingredients):
        for items in order_ingredients:
         if order_ingredients[items] > self.resources[items]:
            print(f"sorry there is not enough {items}")
            return False

        return True
    def Update_resources(self, resources, order_ingredients):
        for item in order_ingredients:
             Resources(self.resources, self.order_ingredients).resources[item] -= self.order_ingredients[item]
