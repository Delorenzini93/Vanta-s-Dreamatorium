from inventory import add_item, has_item, remove_item
import Status
import os

class Item:
    def __init__(self, name, description, buy_price, sell_price, category):
        self.name = name
        self.description = description
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.category = category

class Shop:
    def __init__(self, shop_name, stock):
        self.shop_name = shop_name
        self.stock = stock

    def show_stock(self):
        print(f"\n=== {self.shop_name} ===")
        print(f"Your souls: {Status.souls}\n")
        for i, item in enumerate(self.stock, 1):
            print(f"{i}. {item.name} — {item.buy_price} souls — {item.description}")

    def buy(self, index):
        if index < 1 or index > len(self.stock):
            print("Invalid choice.")
            return
        item = self.stock[index - 1]
        if Status.souls < item.buy_price:
            print(f"Not enough souls. You need {item.buy_price}, you have {Status.souls}.")
            return
        Status.souls -= item.buy_price
        add_item(item.name)
        print(f"You bought {item.name} for {item.buy_price} souls.")

    def sell(self, item_name):
        if not has_item(item_name):
            print(f"You don't have {item_name}.")
            return
        for item in self.stock:
            if item.name == item_name:
                Status.souls += item.sell_price
                remove_item(item_name)
                print(f"You sold {item_name} for {item.sell_price} souls.")
                return
        print("The shop isn't interested in that.")

armor_shop = Shop("Plaza Armor Shop", [
    Item("Leather Armor",   "Basic chest protection",     buy_price=2000,  sell_price=500,  category="equipment"),
    Item("Chain Mail",      "Medium chest protection",    buy_price=5000,  sell_price=1500, category="equipment"),
    Item("Knight's Plate",  "Heavy chest protection",     buy_price=12000, sell_price=4000, category="equipment"),
    Item("Iron Boots",      "Basic foot protection",      buy_price=1500,  sell_price=400,  category="equipment"),
    Item("Knight's Boots",  "Heavy foot protection",      buy_price=8000,  sell_price=2500, category="equipment"),
])

def plaza_armor_shop():
    os.system('cls')
    Status.current_room = "gardens"
    print("\nRows of armor line the walls, from battered leather to polished plate.")

    while True:
        print("\n1. Buy armor")
        print("2. Sell armor")
        print("3. Leave")
        print("4. Check inventory")

        try:
            answer = int(input("What are you looking for? "))

            if answer == 1:
                armor_shop.show_stock()
                try:
                    choice = int(input("\nChoose an item (0 to cancel): "))
                    if choice == 0:
                        continue
                    armor_shop.buy(choice)
                except ValueError:
                    print("Enter a valid number.")

            elif answer == 2:
                item_name = input("What do you want to sell? ").strip()
                armor_shop.sell(item_name)

            elif answer == 3:
                print("You leave the armor shop.")
                return

            elif answer == 4:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Enter a valid number.")