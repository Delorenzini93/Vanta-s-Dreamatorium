inventory = []

def add_item(item_name):
    if item_name not in inventory:
        inventory.append(item_name)
        print(f"\nNew item obtained: {item_name.upper()}")
    else:
        print(f"\nYou already have the {item_name}.")

def has_item(item_name):
    return item_name in inventory

def show_inventory():
    if not inventory:
        print("\nYour inventory is empty.")
    else:
        print("\n--- Inventory ---")
        for item in inventory:
            print(f"- {item}")
        print("----------------")