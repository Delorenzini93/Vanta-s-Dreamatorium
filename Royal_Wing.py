from inventory import add_item, remove_item, has_item
import Status
import os

def royal_wing():
    os.system('cls')
    Status.current_room = "royal_wing"

    print("\nYou step into the Royal Wing.")
    print("A wide, elegant hall stretches before you, lined with tall windows and old banners.")
    print("The air feels heavier here, as if the castle itself is watching.")

    while True:
        print("\n1. Go to the Kitchens")
        print("2. Approach the King's Room")
        print("3. Go to the Dressing Room")
        print("4. Go to the Plaza")
        print("5. Go back to the Third Hall (2F)")
        print("6. Check inventory")

        try:
            answer = int(input("\nWhere will you go? "))

            if answer == 1:
                print("You walk toward the kitchens...")
                import Kitchens
                Kitchens.kitchens()

            elif answer == 2:
                if Status.is_raining:
                    print("\nThe entrance to the King's Room is unguarded.")
                    print("The guard must have stepped away to avoid the rain.")
                    print("1. Enter the King's Room")
                    print("2. Stay in the hall")
                    choice = int(input("> "))
                    if choice == 1:
                        import Kings_Room
                        Kings_Room.kings_room()
                else:
                    print("\nA stern guard stands firmly in front of the King's Room.")
                    print("He blocks the way with his spear and shakes his head.")
                    print("\"No one enters without royal permission.\"")

            elif answer == 3:
                print("You head toward the Dressing Room...")
                import Dressing_Room
                Dressing_Room.dressing_room()

            elif answer == 4:
                print("You walk out toward the Plaza...")
                import Plaza
                Plaza.plaza()

            elif answer == 5:
                print("You return to the Third Hall on the second floor.")
                import Third_Hall_2F
                Third_Hall_2F.third_hall_2F()
                return

            elif answer == 6:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")