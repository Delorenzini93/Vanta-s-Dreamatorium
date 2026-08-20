import datetime
import Status


def empty_slot():
    return {"seed": None, "planted_at": None, "minutes": 0, "reward": None}

slots = {
    1: empty_slot(),
    2: empty_slot(),
    3: empty_slot(),
}


SEEDS = {
    "Red Seed": {"minutes": 4, "reward": "Red Herb"},
    "Blue Seed": {"minutes": 8, "reward": "Blue Crystal"},
    "Yellow Seed": {"minutes": 12, "reward": "Fang"},
    "Green Seed": {"minutes": 16, "reward": "Octopus food"},
    "Pink Seed": {"minutes": 20, "reward": "Quality Wool"},
    "Black Seed": {"minutes": 60, "reward": "Veritaserum"},
    "Rotten Seed": {"minutes": 30, "reward": "Soul Core"},
}

def plant(slot_number):
    slot = slots[slot_number]
    if slot["seed"]:
        print(f"Slot {slot_number} already has something growing...")
        return

    print("Which seed do you want to plant?")
    for i, seed in enumerate(SEEDS, 1):
        print(f"{i}. {seed} ({SEEDS[seed]['minutes']} minutes)")

    try:
        choice = int(input("Seed: "))
        seed_name = list(SEEDS.keys())[choice - 1]

        if not has_item(seed_name):
            print("You don't have that seed.")
            return

        remove_item(seed_name)
        slot["seed"] = seed_name
        slot["planted_at"] = datetime.datetime.now()
        slot["minutes"] = SEEDS[seed_name]["minutes"]
        slot["reward"] = SEEDS[seed_name]["reward"]
        print(f"{seed_name} planted in slot {slot_number}!")

    except (ValueError, IndexError):
        print("Invalid choice.")

def harvest(slot_number):
    slot = slots[slot_number]
    if not slot["seed"]:
        print(f"Slot {slot_number} is empty.")
        return

    elapsed = datetime.datetime.now() - slot["planted_at"]
    minutes_passed = elapsed.total_seconds() / 60

    if minutes_passed >= slot["minutes"]:
        print(f"You harvested {slot['reward']}!")
        add_item(slot["reward"])
        slots[slot_number] = empty_slot()
    else:
        remaining = slot["minutes"] - minutes_passed
        print(f"Not ready yet... {remaining:.1f} minutes remaining.")

def farm_menu():
    while True:
        print("\n--- Garden ---")
        for num, slot in slots.items():
            if slot["seed"]:
                elapsed = datetime.datetime.now() - slot["planted_at"]
                remaining = max(0, slot["minutes"] - elapsed.total_seconds() / 60)
                status = "READY!" if remaining == 0 else f"{remaining:.1f} min left"
                print(f"Slot {num}: {slot['seed']} — {status}")
            else:
                print(f"Slot {num}: Empty")

        print("\n1. Plant")
        print("2. Harvest")
        print("3. Leave the garden")

        try:
            answer = int(input("action: "))

            if answer == 1:
                slot_num = int(input("Which slot? "))
                if slot_num in slots:
                    plant(slot_num)
                else:
                    print("Invalid slot.")

            elif answer == 2:
                slot_num = int(input("Which slot? "))
                if slot_num in slots:
                    harvest(slot_num)
                else:
                    print("Invalid slot.")

            elif answer == 3:
                return

            else:
                print("Choose between 1 and 3.")

        except ValueError:
            print("Enter a valid number.")