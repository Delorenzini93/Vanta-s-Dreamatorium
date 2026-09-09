inventory = []



def add_item(item_name):
    if item_name not in inventory:
        inventory.append(item_name)
        print(f"\nNew item obtained: {item_name.upper()}")
    else:
        print(f"\nYou already have the {item_name}.")

def remove_item(item_name):
    if item_name in inventory:
        inventory.remove(item_name)
        print(f"\nYou no longer have the {item_name}.")
    else:
        print(f"\nYou don't have the {item_name}.")

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

battle_items = {
    "Potion": {"type": "heal", "value": 50, "description": "Restores 50 HP"},
    "Amine": {"type": "speed", "value": 10, "duration": 3, "description": "Increases evasion for 3 turns"},
}

item_descriptions = {
    "Potion": "Restores 30 HP.",
    "Amine": "Temporarily increases evasion.",
}

inventory = {
    "usable": [],
    "equipment": [],
    "key_items": [],
    "collectibles": [],
    "misc": []
}