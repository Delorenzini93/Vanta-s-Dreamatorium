from inventory import add_item, remove_item, has_item
import Status
import os

is_candle_ashes_taken = False

def royal_room_d():
    global is_candle_ashes_taken
    os.system('cls')
    Status.current_room = "royal_catacombs"

    if Status.heritage_choice != "Child's Drawing":
        print("\nYou open the door and immediately regret it.")
        print("The room is filled with screaming ghosts.")
        print("Their voices are sharp, overlapping, unbearable.")
        print("You are forced to stumble back into the hall.")
        return

    if Status.heritage_choice == "Child's Drawing":
        print("\nYou enter a quiet, dim room.")
        print("The air feels softer here, almost protective.")
        print("A faint scent of old paper and crayon lingers.")

        while True:
            print("\n1. Examine the room")
            print("2. Approach the pedestal")
            print("3. Leave the room")
            print("4. Check inventory")

            try:
                answer = int(input("> "))

                if answer == 1:
                    print("\nChildish drawings are pinned to the walls, all faded.")
                    print("One of them shows a family under a black sun.")

                elif answer == 2:
                    if is_candle_ashes_taken:
                        print("\nThe pedestal is empty.")
                    else:
                        print("\nA dark candle rests on the pedestal.")
                        while True:
                            print("1. Take the Candle of Ashes")
                            print("2. Leave it")
                            try:
                                answer = int(input("> "))
                                if answer == 1:
                                    add_item("Candle of Ashes")
                                    is_candle_ashes_taken = True
                                    print("You obtained 'CANDLE OF ASHES'!")
                                    break
                                elif answer == 2:
                                    break
                            except ValueError:
                                print("Choose a valid action")

                elif answer == 3:
                    print("You return to Royal Hall")
                    return

                elif answer == 4:
                    from inventory import show_inventory
                    show_inventory()

            except ValueError:
                print("Choose a valid action.")