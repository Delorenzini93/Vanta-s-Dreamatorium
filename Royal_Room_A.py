from inventory import add_item, remove_item, has_item
import Status
import os

is_candle_taken = False

def royal_room_a():
    global is_candle_taken
    os.system('cls')
    Status.current_room = "royal_court"

    print("\nYou enter a small, quiet room.")
    print("A stone pedestal stands in the center.")

    if is_candle_taken:
        print("The pedestal is empty. You already took the candle.")
    elif Status.is_daylight:
        print("A single white candle sits on the pedestal, lit by the sunlight.")
        print("\n1. Take the Candle of Dawn")
        print("2. Leave")
        try:
            choice = int(input("> "))
            if choice == 1:
                add_item("Candle of Dawn")
                print("You obtained 'CANDLE OF DAWN'!")
                is_candle_taken = True
        except ValueError:
            print("Invalid choice.")
    else:
        print("The pedestal is bare.")
        print("Something about this room feels like it needs daylight.")

    input("\nPress Enter to return to the hall...")