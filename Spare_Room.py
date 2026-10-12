from inventory import add_item, remove_item, has_item
import Status
import os

is_room_checked = False
is_painting_active = False

def spare_room():
    global is_room_checked, is_painting_active
    os.system('cls')
    Status.current_room = "west_hall_2F"

    print("Seems like an out-of-use room, since it's a bit messy and full of unrelated stuff")

    while True:
        print("1. Examine the room")
        print("2. Examine the painting")
        print("3. See Emily play")
        print("4. Go back to the hall")
        print("5. Check inventory")

        try:
            answer = int(input("> "))
            if answer == 1:
                if not is_room_checked:
                    print("This room seems like abandoned or forgotten part of the castle...a bit uncanny to be honest")
                    print("There's what seems like an elegant garment lying on the corner")
                    add_item("King's clothes")
                    print("You obtain 'KING'S CLOTHES!")
                    is_room_checked = True
                else:
                    print("\nThe room remains quiet and dusty.")
            elif answer == 2:
                if is_painting_active:
                    print("The painting of Lord Layne moves!")
                    print("You hear the sound of an interestelar overdrive and the painting disappears!")
                    while True:
                        print("1. Yeah, what could go wrong?")
                        print("2. This situation is quite surreal...better not get into this")
                        try:
                            answer = int(input("Should I get into this mysterious tunnel?"))
                            if answer == 1:
                                print("This sounds like a completely right and danger-free decision!")
                                import Castle_Tunnels
                                Castle_Tunnels.castle_tunnels()
                            elif answer == 2:
                                return
                        except ValueError:
                            print("Choose a valid action")
                else:
                    print("There's a painting of Lord Layne...quite ugly and old")
            elif answer == 3:
                print("W...what?")
                is_painting_active = True
            elif answer == 4:
                print("You go back to the hall")
                return
            elif answer == 5:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action")