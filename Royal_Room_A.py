from inventory import add_item, remove_item, has_item
import Status
import os

is_candle_dawn_taken = False

def royal_room_a():
    global is_candle_dawn_taken
    os.system('cls')
    Status.current_room = "royal_court"

    print("\nYou enter a small, austere room.")
    print("Dust floats in the air. A single stone pedestal stands in the center.")
    print("The walls are plain, except for a short inscription carved near the ceiling.")

    while True:
        print("\n1. Read the inscription")
        print("2. Approach the pedestal")
        print("3. Leave the room")
        print("4. Check inventory")

        try:
            answer = int(input("> "))

            if answer == 1:
                print("\nThe inscription reads:")
                print("\"Only under the honest light of day")
                print("shall the first flame reveal itself.\"")

            elif answer == 2:
                if is_candle_dawn_taken:
                    print("\nThe pedestal is empty.")
                elif Status.is_daylight:
                    print("\nA white candle rests on the pedestal, catching the sunlight.")
                    print("1. Take the Candle of Dawn")
                    print("2. Leave it")
                    choice = int(input("> "))
                    if choice == 1:
                        add_item("Candle of Dawn")
                        is_candle_dawn_taken = True
                        print("You obtained 'CANDLE OF DAWN'!")
                else:
                    print("\nThe pedestal is bare.")
                    print("The room feels incomplete under the dark sky.")

            elif answer == 3:
                print("You return to the Royal Hall.")
                return

            elif answer == 4:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")