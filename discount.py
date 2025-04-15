from laptop import Laptop

class Discount(Laptop):
    def __init__(self,brand,model,price,discount_rate):
        super().__init__(brand,model,price)
        self.discount_rate = discount_rate
        self.available = True
        
    
    def get_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Discount Rate: {self.discount_rate}, Discount Amount: {self.discount_amount}, Available: {self.available}"
    
    def discounted_amount(self):
        return self.price*(self.discount_rate/100)
    
    def discounted_price(self):
        return self.price -self.discounted_amount()
    