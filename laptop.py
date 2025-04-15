# encapsulation -- puting the data about the laptop privately in one package
class Laptop:
    def __init__(self, brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
        self.available = True # this not a property
    
    def buy(self):
        if self.available: #if the laptop is available it changes the state to false meaning it is nolonger available
            self.available = False
            return f"you have bought'{self.brand}'."
        return f"'{self.brand}' is not available."
   
    def faulty(self):
        self.available = True
        return f"'{self.brand}' model '{self.model}'is faulty and has been returned."

    def get_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Available: {self.available}"
    
