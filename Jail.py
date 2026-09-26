from inventory import add_item, remove_item, has_item
import Status

is_body_checked = False

def jail():
    global is_body_checked

    print("\nYou enter a silent and abandoned jail with a single cell.")
    print("The rusted walls are stained with a dark red liquid...")
    print("Something terrible happened here.")

    while True:
        print("\n1. Check the inside of the cell")
        print("2. Leave")

        try:
            answer = int(input("This place feels heavy... "))

            if answer == 1:
                if not is_body_checked:
                    print("\nThere's a fallen soldier lying on the cold floor.")
                    print("His body has been here for a long time.")
                    print("Clear signs of torture mark his remains... poor soul.")
                    print("You carefully search him.")
                    add_item("Handgun")
                    add_item("Blue Key")
                    print("You obtained 'HANDGUN'!")
                    print("You obtained 'BLUE KEY'!")
                    Status.current_ranged_weapon = "Handgun"
                    Status.player_ranged_attack += 20
                    print(f"Ranged Attack increased! ({Status.player_ranged_attack})")
                    print("You equipped Handgun")
                    is_body_checked = True
                else:
                    print("I better leave this poor soul alone.")
            elif answer == 2:
                print("Yeah... better leave this place.")
                return

        except ValueError:
            print("Choose a valid action.")

jail()