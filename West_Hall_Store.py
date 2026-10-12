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

class shop:
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
        print("The store isn't interested in that.")

store = shop("West Hall Store", [
    Item("Potion", "Restores 50 HP", buy_price=1000, sell_price=5, category="usable"),
    Item("Amine", "Increases evasion", buy_price=1500, sell_price=7, category="usable"),
    Item("Surface Bait", "Common fishing bait", buy_price=5000, sell_price=2, category="misc"),
    Item("Antidote", "Cures poison", buy_price=2500, sell_price=6, category="usable"),
])

#######################################
def west_hall_store():
    os.system('cls')
    Status.current_room = "west_hall_2F"
    print("\nThe smell of herbs and dust fills the air.")
    print("An old figure stands behind a counter covered in vials and jars.")

    while True:
        print("\n1. Buy items")
        print("2. Sell items")
        print("3. Leave")
        print("4. Check inventory")

        try:
            answer = int(input("What do you need, wanderer? "))

            if answer == 1:
                store.show_stock()
                try:
                    choice = int(input("\nChoose an item (0 to cancel): "))
                    if choice == 0:
                        continue
                    store.buy(choice)
                except ValueError:
                    print("Enter a valid number.")

            elif answer == 2:
                print("\nWhat do you want to sell?")
                item_name = input("Item name: ").strip()
                store.sell(item_name)

            elif answer == 3:
                print("You leave the West Hall Store.")
                return
            elif answer == 4:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Enter a valid number.")