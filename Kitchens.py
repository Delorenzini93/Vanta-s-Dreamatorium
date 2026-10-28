from inventory import add_item, remove_item, has_item
import Status
import os

is_secret_door_found = False

def kitchens():
    global is_secret_door_found
    os.system('cls')
    Status.current_room = "royal_wing"

    print("\nYou enter the Kitchens.")
    print("The air is thick with the smell of old grease, smoke, and boiled meat.")
    print("Large iron pots hang over cold hearths. Everything looks abandoned, yet recently used.")

    while True:
        print("\n1. Search the kitchens")
        print("2. Examine the far wall")
        print("3. Check inventory")
        print("4. Leave the Kitchens")

        try:
            answer = int(input("\nThe silence here feels heavy... "))

            if answer == 1:
                print("\nYou search through the pots, shelves, and drawers.")
                print("Most of it is rotting food and rusty utensils.")
                print("Nothing useful stands out.")

            elif answer == 2:
                if not is_secret_door_found:
                    print("\nYou run your hands along the far wall.")
                    print("Behind a tall shelf, your fingers catch a thin seam in the stone.")
                    print("There's a small keyhole hidden in the darkness.")
                    is_secret_door_found = True
                else:
                    print("\nThe hidden door is still there.")

                if has_item("Backdoor Key"):
                    print("\n1. Use the Backdoor Key")
                    print("2. Leave it for now")
                    choice = int(input("> "))
                    if choice == 1:
                        print("\nThe key turns with a heavy click.")
                        print("A section of the wall shifts open, revealing a dark staircase leading down...")
                        print("You step into the Royal Dungeons.")
                        import Royal_Dungeons
                        Royal_Dungeons.royal_dungeons()
                        return
                else:
                    print("You need a specific key to open this door.")

            elif answer == 3:
                from inventory import show_inventory
                show_inventory()

            elif answer == 4:
                print("You leave the Kitchens.")
                return

            else:
                print("Choose a valid action.")

        except ValueError:
            print("Choose a valid action.")