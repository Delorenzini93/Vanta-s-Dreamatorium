from inventory import add_item, remove_item, has_item
import Status
from Farm import farm_menu
import os
import fishing

def farm_minigame():
    farm_menu()

def royal_garden():
    os.system('cls')
    Status.current_room = "royal_hall"
    print("The sun hits your eyes in a pleasing way")
    print("The smell of the morning and the sound of butterflies amuses you a bit")

    while True:
        print("\n1. Take a look at the garden")
        print("2, Inspect the flowing water")
        print("3. Return")
        print("4. Check inventory")

        try:
            answer = int(input("> "))

            if answer == 1:
                farm_minigame()

            elif answer == 2:
                fishing.fish("pond_3")

            elif answer == 3:
                print("You re-enter the royal hall")
                return
            elif answer == 4:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Enter a valid action")