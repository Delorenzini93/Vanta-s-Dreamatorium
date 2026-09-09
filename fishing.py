import random
import time
from inventory import has_item, remove_item, add_item
import Status

fish_catalog = {
    "pond_1": {
        "Common Trout":    {"bait": "Surface Bait",  "daylight": True,  "sequence": 3, "stages": 1, "timer": 5},
        "River Eel":       {"bait": "Bottom Bait",   "daylight": False, "sequence": 4, "stages": 2, "timer": 4},
        "Silver Carp":     {"bait": "Surface Bait",  "daylight": True,  "sequence": 3, "stages": 1, "timer": 5},
        "Mud Crawler":     {"bait": "Bottom Bait",   "daylight": False, "sequence": 5, "stages": 2, "timer": 4},
    },
    "pond_2": {
        "Glowing Perch":   {"bait": "Deep Bait",     "daylight": False, "sequence": 4, "stages": 2, "timer": 4},
        "Stone Bass":      {"bait": "Surface Bait",  "daylight": True,  "sequence": 4, "stages": 2, "timer": 4},
        "Cave Salmon":     {"bait": "Deep Bait",     "daylight": False, "sequence": 5, "stages": 2, "timer": 3},
        "Pale Flounder":   {"bait": "Bottom Bait",   "daylight": True,  "sequence": 4, "stages": 1, "timer": 5},
    },
    "pond_3": {
        "Dream Shark":     {"bait": "Lucky Bait",    "daylight": False, "sequence": 7, "stages": 3, "timer": 3},
        "Phantom Ray":     {"bait": "Deep Bait",     "daylight": False, "sequence": 6, "stages": 3, "timer": 3},
        "Golden Koi":      {"bait": "Lucky Bait",    "daylight": True,  "sequence": 6, "stages": 2, "timer": 4},
        "Iron Catfish":    {"bait": "Bottom Bait",   "daylight": True,  "sequence": 5, "stages": 2, "timer": 4},
    }
}

caught_fish = {}

def get_eligible_fish(pond_name, bait):
    eligible = []
    for fish_name, data in fish_catalog[pond_name].items():
        if data["bait"] == bait and data["daylight"] == Status.is_daylight:
            eligible.append(fish_name)
    return eligible

def fish_appears(eligible):
    if not eligible:
        return None
    return random.choice(eligible)

def numpad_sequence(length, timer):
    sequence = [random.randint(1, 9) for _ in range(length)]
    print(f"\nSequence: {' '.join(map(str, sequence))}")
    print(f"You have {timer} seconds per number!")

    start = time.time()
    user_input = input("Enter the sequence (no spaces): ").strip()
    elapsed = time.time() - start

    if elapsed > timer * length:
        print("Too slow! The fish escaped!")
        return False

    try:
        user_sequence = [int(c) for c in user_input]
    except ValueError:
        print("Invalid input! The fish escaped!")
        return False

    if user_sequence == sequence:
        return True
    else:
        print("Wrong sequence! The fish escaped!")
        return False

def catch_fish(fish_name, data, bait):
    print(f"\nSomething's pulling the rod... it's a {fish_name}!")
    stages = data["stages"]

    for stage in range(1, stages + 1):
        print(f"\nStage {stage}/{stages} — Hold on!")
        success = numpad_sequence(data["sequence"], data["timer"])
        if not success:
            remove_item(bait)
            print(f"You lost your {bait}.")
            return False

    print(f"\nYou caught a {fish_name}!")
    add_item(fish_name)
    remove_item(bait)

    if fish_name in caught_fish:
        caught_fish[fish_name] += 1
    else:
        caught_fish[fish_name] = 1

    return True

def wait_for_fish(pond_name, bait):
    eligible = get_eligible_fish(pond_name, bait)

    if not eligible:
        print("\nNothing seems to be interested in that bait here...")
        return

    chance = 100 // len(eligible)
    print(f"\nYou cast the line... ({len(eligible)} fish eligible, {chance}% chance each per cycle)")

    for attempt in range(6):  # 6 ciclos de 15 segundos = 90 segundos maximo
        print("\nWaiting... (15 seconds)")
        time.sleep(15)

        fish = fish_appears(eligible)
        if fish and random.randint(1, 100) <= chance:
            catch_fish(fish, fish_catalog[pond_name][fish], bait)
            return

        print("Nothing appears to be swimming down under...")

    print("\nThe fish aren't biting today. You retrieve your line.")
    remove_item(bait)

def fish(pond_name):
    if not has_item("Fishing Rod"):
        print("You need a Fishing Rod to fish here.")
        return

    print(f"\nYou approach {pond_name.replace('_', ' ').title()}.")
    print("Available baits in your inventory:")

    baits = ["Surface Bait", "Deep Bait", "Bottom Bait", "Lucky Bait"]
    available = [b for b in baits if has_item(b)]

    if not available:
        print("You don't have any bait.")
        return

    for i, bait in enumerate(available, 1):
        print(f"{i}. {bait}")

    try:
        choice = int(input("Choose a bait: "))
        if 1 <= choice <= len(available):
            selected_bait = available[choice - 1]
            wait_for_fish(pond_name, selected_bait)
        else:
            print("Invalid choice.")
    except ValueError:
        print("Enter a valid number.")

def catalog():
    print("\n=== WISHING WELL ===")
    if not caught_fish:
        print("You haven't caught anything yet...")
        return

    print(f"Total species caught: {len(caught_fish)}/12\n")
    for fish_name, count in caught_fish.items():
        print(f"- {fish_name}: {count} caught")