from laptop import Laptop
from discount import Discount
from shop import Shop

discounted_laptop = Discount("Dell", "XPS 13", 1000, 10)
print(discounted_laptop.discounted_price())
