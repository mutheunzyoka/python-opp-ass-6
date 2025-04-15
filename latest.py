from laptop import Laptop

class latestlapy(Laptop):
    def __init__(self,brand,model,price,year):
        #use super to inherit the properties from the laptop class
        super().__init__(brand,model,price)
        self.year = year
        self.available = True

    def get_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Year: {self.year}, Available: {self.available}"
    
    def buy(self):
        if self.available:
            self.available = False
            return f"'{self.brand}' model '{self.model}' is sold."
        return f"'{self.brand}' model '{self.model}' is not available.It is on high demand"