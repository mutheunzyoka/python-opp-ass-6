from discount import Discount
from laptop import Laptop
from latest import latestlapy
from shop import Shop

def main():
    shop = Shop("Tech Haven", "Nairobi")
    shop.add_laptop(Laptop("Dell", "XPS 13", 1200))
    shop.add_laptop(Laptop("HP", "Spectre x360", 1400))
    shop.add_laptop(Laptop("Apple", "MacBook Pro", 2000))
    shop.add_laptop(Laptop("Lenovo", "ThinkPad X1", 1500))
    shop.add_laptop(Laptop("Asus", "ZenBook", 1300))
    shop.add_laptop(Laptop("Acer", "Swift 3", 900))

    while True:
        print("1. View all Laptops")
        print("2. Buy a Laptop")
        print("3. View Discounted Laptops")
        print("4. View Latest Laptops")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            print("Available laptops in the shop:")
            for laptop in shop.list_laptops():
                print("-", laptop)

        elif choice == '2':
            brand = input("Enter the brand of the laptop you want to buy: ")
            found = shop.find_laptop(brand)  # Removed quotes around brand

            if found:
                print(found.buy())
            else:
                print("Laptop not found")
        
        elif choice == '3':
            discounted_laptop = Discount("Dell", "XPS 13", 1000, 10)
            print(discounted_laptop.discounted_price())
        
        elif choice == '4':
            latest_laptops = [
                latestlapy("Apple", "MacBook Pro", 2000, 2023),
                latestlapy("HP", "Spectre x360", 1500, 2024),
                latestlapy("Dell", "XPS 15", 1800, 2023),
                latestlapy("Lenovo", "Yoga Slim", 1300, 2024),
                latestlapy("Asus", "ROG Zephyrus", 2100, 2023),
            ]
            for laptop in latest_laptops:
                print(laptop.get_details())

        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()