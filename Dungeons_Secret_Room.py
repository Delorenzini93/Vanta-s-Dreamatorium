from inventory import add_item, remove_item, has_item
import Status
import os

is_winter_anima_taken = False

def dungeons_secret_room():
    os.system('cls')
    Status.current_room = "deep dungeons"
    global is_winter_anima_taken

    print("\nYou step into a small, sealed chamber.")
    print("The air is painfully cold.")
    print("Frost covers every surface, and your breath turns to mist.")
    print("In the center of the room stands a low pedestal made of dark ice.")

    while True:
        print("\n1. Examine the ice pedestal")
        print("2. Search the walls")
        print("3. Check inventory")
        print("4. Leave the secret room")

        try:
            answer = int(input("The cold bites at your fingers... "))

            if answer == 1:
                if not is_winter_anima_taken:
                    print("\nResting on the pedestal is a crystalline fragment.")
                    print("It pulses with a faint, freezing light.")
                    print("You carefully take it.")
                    add_item("Winter Anima")
                    print("You obtained 'WINTER ANIMA'!")
                    is_winter_anima_taken = True
                else:
                    print("\nThe pedestal is empty now.")
                    print("Only a thin layer of frost remains.")

            elif answer == 2:
                print("\nThe walls are smooth and completely sealed.")
                print("No cracks, no hidden passages.")
                print("This room is a dead end.")

            elif answer == 3:
                from inventory import show_inventory
                show_inventory()

            elif answer == 4:
                print("You leave the freezing chamber behind.")
                return

        except ValueError:
            print("Choose a valid action.")