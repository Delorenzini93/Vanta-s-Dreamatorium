from inventory import add_item, remove_item, has_item
import Status

come_from_trophies_room = False
is_sword_taken = False
x_switch_up = False
y_switch_down = False
z_switch_down = False

########################
def upside_down_room1():
    global x_switch_up
    print("There's definitely an eerie feeling in here....there's a present silence in this room")

    while True:
        print("1. Move forward")
        print("2. Move either side")
        print("3. Move backwards")

        try:
            answer = int(input("Where do we go?"))

            if answer == 1:
                print("You move to the middle of the room")
                upside_down_room2()
            elif answer == 2:
                print("There's switch in middle position with 'X' sign on it")
                while True:
                    print("1. Turn it up")
                    print("2. Turn it down")
                    print("3. Leave it in middle position")

                    try:
                        answer = int(input(""))
                        if answer == 1:
                            print("The 'X' switch is up")
                            x_switch_up = True
                        elif answer == 2:
                            print("The 'X' switch is down")
                            x_switch_up = False
                        elif answer == 3:
                            print("You leave the 'X' switch as it was")
                            return
                    except ValueError:
                        print("Choose a valid action")
            elif answer == 3:
                print("You go back to the dungeons")
                return
        except ValueError:
            print("Choose a valid action")
#######################################
def upside_down_room2():
    global y_switch_down
    print("There are many what seems to be kid's drawings covering the walls in this part of the room")

    while True:
        print("1. Move forward")
        print("2. Move either side")
        print("3. Move backwards")

        try:
            answer = int(input("Where do we go?"))

            if answer == 1:
                print("You move to the final section of the room")
                upside_down_room3()
            elif answer == 2:
                print("There's switch in middle position with 'Y' sign on it")
                while True:
                    print("1. Turn it up")
                    print("2. Turn it down")
                    print("3. Leave it in middle position")

                    try:
                        answer = int(input(""))
                        if answer == 1:
                            print("The 'Y' switch is up")
                            y_switch_down = False
                        elif answer == 2:
                            print("The 'Y' switch is down")
                            y_switch_down = True
                        elif answer == 3:
                            print("You leave the 'Y' switch as it was")
                            return
                    except ValueError:
                        print("Choose a valid action")
            elif answer == 3:
                print("You go back to first section of the room")
                return
        except ValueError:
            print("Choose a valid action")
#######################################
def upside_down_room3():
    global x_switch_up, y_switch_down, z_switch_down
    print("There is a considerable amount of paintings depicting people with different illnesses...I dont like this room")

    while True:
        print("1. Move forward")
        print("2. Move either side")
        print("3. Move backwards")

        try:
            answer = int(input("Where do we go?"))

            if answer == 1:
                if x_switch_up and y_switch_down and z_switch_down:
                    print("The wall crumbles revealing a hidden section of the room where the furniture hangs from the ceiling")
                    upside_down_room4()
                else:
                    print("There's a wall....unless I am a ghost, I'll be unable to pass it through")
            elif answer == 2:
                print("There's switch in middle position with 'Z' sign on it")
                while True:
                    print("1. Turn it up")
                    print("2. Turn it down")
                    print("3. Leave it in middle position")

                    try:
                        answer = int(input(""))
                        if answer == 1:
                            print("The 'Z' switch is up")
                            z_switch_down = False
                        elif answer == 2:
                            print("The 'Z' switch is down")
                            z_switch_down = True
                        elif answer == 3:
                            print("You leave the 'Z' switch as it was")
                            return
                    except ValueError:
                        print("Choose a valid action")
            elif answer == 3:
                print("You go back to middle section of the room")
                return
        except ValueError:
            print("Choose a valid action")
#######################################
def upside_down_room4():
    global is_sword_taken
    print("There's definitely an eerie feeling in here....there's a present silence in this room")

    while True:
        print("1. Move forward")
        print("2. Move either side (sword)")
        print("3. Enter the Trophies Room")

        try:
            answer = int(input("Evom ew od erehw?"))

            if answer == 1:
                print("The wall is too high to climb it")
            elif answer == 2:
                if not is_sword_taken:
                    print("You found a BROADSWORD!")
                    add_item('Broadsword')
                    Status.current_weapon = "Broadsword"
                    Status.player_attack += 10
                    print(f"Attack increased! ({Status.player_attack})")
                    print("You equipped Broadsword!")
                    is_sword_taken = True
                else:
                    print("You already have the Broadsword equipped.")
            elif answer == 3:
                print("You head to the Trophies Room")
                return
        except ValueError:
            print("Choose a valid action")
########################
def where_to_start():
    if come_from_trophies_room:
        upside_down_room4()
    else:
        upside_down_room1()
########################
where_to_start()