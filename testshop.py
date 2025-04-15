from shop import Shop
from laptop import Laptop

shopping =Shop("Tech Haven", "Nairobi")
shopping.add_laptop(Laptop("Dell", "XPS 13", 1200))
shopping.add_laptop(Laptop("HP", "Spectre x360", 1400))
shopping.add_laptop(Laptop("Apple", "MacBook Pro", 2000))
shopping.add_laptop(Laptop("Lenovo", "ThinkPad X1", 1500))
shopping.add_laptop(Laptop("Asus", "ZenBook", 1300))
shopping.add_laptop(Laptop("Acer", "Swift 3", 900))
shopping.add_laptop(Laptop("Microsoft", "Surface Laptop", 1600))
shopping.add_laptop(Laptop("Razer", "Blade Stealth", 1700))
shopping.add_laptop(Laptop("Samsung", "Galaxy Book", 1100))
shopping.add_laptop(Laptop("LG", "Gram", 1400))
shopping.add_laptop(Laptop("Toshiba", "Dynabook", 800))


print("Available laptops in the shop:")
for laptop in shopping.list_laptops():
    print("\n", laptop)

found = shopping.find_laptop("Dell")
print(found.buy()) if found else print("laptop not found")