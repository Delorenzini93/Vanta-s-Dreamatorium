from inventory import add_item, remove_item, has_item
import Status
import Third_Hall
import Boss_Room

is_door_examined = False
is_cryptic_writing = False
is_iron_door_open = False

def iron_door():
    global is_cryptic_writing, is_iron_door_open

    print("There's a massive iron door and I can....hear some growls at the other side")

    while True:
        print("1. Examine door cryptic writings")
        print("2. Open the Iron Door")
        print("3. Leave the door for now")

        try:
            answer = int(input("There's something at the other side, better be careful: "))

            if answer == 1:
                if is_cryptic_writing:
                    print("I guess I'll need some kind of matching IRON KEY")
                elif Third_Hall.is_ceiling_seen:
                    print("There's the same pattern of birds of the Third Hall again!")
                    print("A hole doorknob appears!")
                    is_cryptic_writing = True
                else:
                    print("I don't understand these enigmatic symbols all over the door")

            elif answer == 2:
                if is_iron_door_open and Boss_Room.is_mosag_dead:
                    import West_Hall
                    West_Hall.west_hall()
                elif is_cryptic_writing and has_item("Iron Key"):
                    remove_item("Iron Key")
                    print("The door opens with a deafening sound....the growls just stopped...I guess")
                    is_iron_door_open = True
                    Boss_Room.boss_room()
                else:
                    print("Unsurprisingly, the door is tightly shut")

            elif answer == 3:
                print("You step away from the Iron Door")
                return

        except ValueError:
            print("Choose a valid action")

def corridor_with_many_windows():
    Status.current_room = "third_hall"
    print("Seems like the corridor's walls are entirely made by windows")

    while True:
        print("1. Look through the open window")
        print("2. Advance to the Iron Door")
        print("3. Check inventory")
        print("4. Go back to the Third Hall")

        try:
            answer = int(input(""))

            if answer == 1:
                Status.window_look_count += 1
                if Status.window_look_count % 2 == 0:
                    Status.is_daylight = True
                    print("The sun peeks through the clouds again...")
                else:
                    Status.is_daylight = False
                    print("The clouds are getting darker, nightfall will soon be upon us...")

            elif answer == 2:
                iron_door()

            elif answer == 3:
                from inventory import show_inventory
                show_inventory()

            elif answer == 4:
                print("You go back to the Third Hall")
                return

        except ValueError:
            print("Choose a valid action")

corridor_with_many_windows()