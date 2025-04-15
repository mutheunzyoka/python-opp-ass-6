from shop import Shop
from laptop import Laptop
from latest import latestlapy

latest_laptops = [
    latestlapy("Apple", "MacBook Pro", 2000, 2023),
    latestlapy("HP", "Spectre x360", 1500, 2024),
    latestlapy("Dell", "XPS 15", 1800, 2023),
    latestlapy("Lenovo", "Yoga Slim", 1300, 2024),
    latestlapy("Asus", "ROG Zephyrus", 2100, 2023),
]
for laptop in latest_laptops:
    print(laptop.get_details())