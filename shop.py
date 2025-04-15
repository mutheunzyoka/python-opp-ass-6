#abstraction-e
from laptop import Laptop

class Shop:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.laptops = []

    def add_laptop(self,laptop): #method of adding a laptop to the shop
        self.laptops.append(laptop)

    def remove_laptop(self,laptop):
        if laptop in self.laptops:
            self.laptops.rempve(laptop)
            return f"'{self.brand}' model'{self.model}' has been removed from the shot."
        return f"'{self.brand}' model'{self.model}' is not available in the shop."
    
    def list_laptops(self):
        return[laptop.get_details() for laptop in self.laptops]

    def find_laptop(self,brand):
        for laptop in self.laptops:# laptop is found inside a list of laptops
            if laptop.brand.lower() == brand.lower():
                return laptop
            return None