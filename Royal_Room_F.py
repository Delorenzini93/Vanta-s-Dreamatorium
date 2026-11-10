from inventory import add_item, remove_item, has_item
import Status
import os

is_candle_inheritance_taken = False

def royal_room_f():
    global is_candle_inheritance_taken
    os.system('cls')
    Status.current_room = "royal_catacombs"

    if Status.heritage_choice != "Unsent Letter":
        print("\nYou open the door and immediately regret it.")
        print("The room is filled with screaming ghosts.")
        print("Their voices rise in a chorus of things that were never said.")
        print("You stumble back into the hall.")
        return

    print("\nYou enter a still room.")
    print("The air smells faintly of paper, dried ink, and time.")
    print("Something unsaid seems to press gently against the walls.")

    while True:
        print("\n1. Examine the writing desk")
        print("2. Approach the pedestal")
        print("3. Read the remaining pages")
        print("4. Leave the room")
        print("5. Check inventory")

        try:
            answer = int(input("> "))

            if answer == 1:
                print("\nA wooden writing desk stands against the wall.")
                print("Loose pages are scattered across it, most of them blank or faded.")
                print("A single chair is pulled out, as if someone meant to return.")

            elif answer == 2:
                if is_candle_inheritance_taken:
                    print("\nThe pedestal is empty.")
                else:
                    print("\nA pale, almost colorless candle rests on the pedestal.")
                    while True:
                        print("1. Take the Candle of Inheritance")
                        print("2. Leave it")
                        try:
                            answer = int(input("> "))
                            if answer == 1:
                                add_item("Candle of Inheritance")
                                is_candle_inheritance_taken = True
                                print("You obtained 'CANDLE OF INHERITANCE'!")
                                break
                            elif answer ==2:
                                break
                        except ValueError:
                            print("Choose a valid action")

            elif answer == 3:
                print("\nMost of the writing has disappeared with time.")
                print("Only one line remains clearly visible, the ink still strangely dark:")
                print()
                print("\"I was never brave enough to give this to you.\"")

            elif answer == 4:
                print("You return to Royal Hall")
                return

            elif answer == 5:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")