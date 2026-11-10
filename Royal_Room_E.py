from inventory import add_item, remove_item, has_item
import Status
import os

is_candle_silence_taken = False

def royal_room_e():
    global is_candle_silence_taken
    os.system('cls')
    Status.current_room = "royal_catacombs"

    if Status.heritage_choice != "Broken Music Box":
        print("\nYou open the door and immediately regret it.")
        print("The room is filled with screaming ghosts.")
        print("Their voices are sharp, overlapping, unbearable.")
        print("You are forced to stumble back into the hall.")
        return

    print("\nYou enter a muted room.")
    print("Sound feels heavier here, as if the air itself resists noise.")
    print("A faint, broken melody seems to exist just below hearing.")
    print("Dust covers every surface like a second skin.")

    while True:
        print("\n1. Examine the music box")
        print("2. Approach the pedestal")
        print("3. Listen carefully")
        print("4. Leave the room")
        print("5. Check inventory")

        try:
            answer = int(input("> "))

            if answer == 1:
                print("\nAn old wooden music box sits on a shelf, its lid cracked.")
                print("The mechanism inside is seized.")
                print("A single lock of hair is still tied around the hinge with faded ribbon.")
                print("Someone once wound this box for a person who never returned.")

            elif answer == 2:
                if is_candle_silence_taken:
                    print("\nThe pedestal is empty.")
                else:
                    print("\nA deep indigo candle rests on the pedestal.")
                    print("Even the flame it might produce feels like it would burn quietly.")
                    while True:
                        print("1. Take the Candle of Silence")
                        print("2. Leave it")
                        try:
                            answer = int(input("> "))
                            if answer == 1:
                                add_item("Candle of Silence")
                                is_candle_silence_taken = True
                                print("You obtained 'CANDLE OF SILENCE'!")
                                break
                            elif answer == 2:
                                break
                        except ValueError:
                            print("Choose a valid action")

            elif answer == 3:
                print("\nYou hold your breath and listen.")
                print("For a moment you almost hear the original melody —")
                print("then it collapses back into silence.")

            elif answer == 4:
                print("You return to Royal Hall")
                return

            elif answer == 5:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")