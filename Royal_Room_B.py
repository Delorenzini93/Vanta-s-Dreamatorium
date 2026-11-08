from inventory import add_item, remove_item, has_item
import Status
import os

is_candle_dusk_taken = False

def royal_room_b():
    global is_candle_dusk_taken
    os.system('cls')
    Status.current_room = "royal_court"

    print("\nYou enter a dim room.")
    print("Heavy curtains block most of the light. The air is noticeably colder.")
    print("A small table sits against the far wall.")

    while True:
        print("\n1. Read the inscription on the wall")
        print("2. Approach the table")
        print("3. Leave the room")
        print("4. Check inventory")

        try:
            answer = int(input("> "))

            if answer == 1:
                print("\nThe inscription is faint, almost reluctant:")
                print("\"When the sun abandons the sky,")
                print("the second flame remembers its purpose.\"")

            elif answer == 2:
                if is_candle_dusk_taken:
                    print("\nYou already took the candle from this room.")
                elif not Status.is_daylight:
                    print("\nIn the darkness, a deep blue candle glows faintly on the table.")
                    print("1. Take the Candle of Dusk")
                    print("2. Leave it")
                    choice = int(input("> "))
                    if choice == 1:
                        add_item("Candle of Dusk")
                        is_candle_dusk_taken = True
                        print("You obtained 'CANDLE OF DUSK'!")
                else:
                    print("\nDaylight fills the room.")
                    print("Whatever presence was here seems to have faded with the night.")

            elif answer == 3:
                print("You leave the room and return to the Royal Hall.")
                return

            elif answer == 4:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")