class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
        self.menu_items = {}

    def add_item(self, item):
        self.menu_items[item.name] = item

    def display_menu(self):
        print("Menu:")
        for name, item in self.menu_items.items():
            print(f"{name}: ${item.price:.2f}")

class Order:
    def __init__(self):
        self.order_items = {}

    def add_item(self, item, quantity):
        if item.name in self.order_items:
            self.order_items[item.name] += quantity
        else:
            self.order_items[item.name] = quantity

    def calculate_total(self, menu):
        total = 0
        for item_name, quantity in self.order_items.items():
            item = menu.menu_items.get(item_name)
            if item:
                total += item.price * quantity
        return total

    def display_order(self, menu):
        print("Your Order:")
        for item_name, quantity in self.order_items.items():
            item = menu.menu_items.get(item_name)
            if item:
                print(f"{item_name} x{quantity} = ${item.price * quantity:.2f}")
        print(f"Total: ${self.calculate_total(menu):.2f}")

def main():
    menu = Menu()
    menu.add_item(FoodItem("Burger", 5.99))
    menu.add_item(FoodItem("Pizza", 8.99))
    menu.add_item(FoodItem("Pasta", 7.49))

    order = Order()

    while True:
        print("\nFood Delivery System")
        print("1. Display Menu")
        print("2. Place Order")
        print("3. Display Order")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            menu.display_menu()
        elif choice == '2':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            item = menu.menu_items.get(item_name)
            if item:
                order.add_item(item, quantity)
            else:
                print("Item not found in the menu.")
        elif choice == '3':
            order.display_order(menu)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
