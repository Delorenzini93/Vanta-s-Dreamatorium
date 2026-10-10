from inventory import add_item, remove_item, has_item
import Status
import os

def archane_room_night():
    os.system('cls')
    Status.current_room = "third_hall"
    print("\nAn imposing statue of a blind crow occupies most of the small room")

    while True:
        print("1. Examine the writing at the feet of the statue")
        print("2. Make an offering")
        print("3. Go back to the Third Hall")
        print("4. Check inventory")

        try:
            answer = int(input(""))
            if answer == 1:
                print("The Crow, Lord of the night, cannot live in the light of day")
                print("A choice must be made for whom the stations of the year awaits")
            elif answer == 2:
                if Status.is_cross_used:
                    print("The silence is quite frightening, really")
                elif has_item("Cross of Enix") and not Status.is_cross_used:
                    print("You offer the CROSS OF ENIX")
                    remove_item("Cross of Enix")
                    add_item("Hungarian Broadsword")
                    print("You obtained HUNGARIAN BROADSWORD!")
                    Status.current_weapon = "Hungarian Broadsword"
                    Status.player_attack += 100
                    print(f"Attack increased! ({Status.player_attack})")
                    print("You equipped Hungarian Broadsword!")
                    print("The statue is dormant now")
                    print("You could swear hearing a distant scream of agony somewhere...")
                    Status.is_cross_used = True
                else:
                    print("I don't have anything to offer")
            elif answer == 3:
                print("You go back to the Third Hall")
                return
            elif answer == 4:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")