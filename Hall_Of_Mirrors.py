from inventory import add_item, remove_item, has_item
import Status
import Heroes


cuc = 'Cuchulain'

is_far_chest_open = False
is_west_wing_chest_open = False
is_left_wing_chest_open = False
is_west_wing_knight_down = False
is_left_wing_knight_down = False
is_hero_free = False
is_circular_mirror_flicked = False

def left_wing_knight_battle():
    pass
def west_wing_knight_battle():
    pass
######################################
def far_central_wing():
    global is_far_chest_open, is_hero_free
    print("\nThe air feels heavier here...")

    while True:
        print("1. Move forward")
        print("2. Move to your right")
        print("3. Go back")

        try:
            answer = int(input("Where do we go from here?"))

            if answer == 1:
                if is_far_chest_open:
                    print("I already opened this chest, there's nothing here")
                    continue
                else:
                    print("You found a chest!")
                    print("You found CANDLES")
                    add_item('Candles')
                    is_far_chest_open = True
                    print("I already opened this chest, there's nothing here")
                    continue
            elif answer == 2:
                if is_hero_free:
                    print("There's nothing here of particular interest")
                    continue
                else:
                    print("There's a mirror whose reflection doesn't match yours.....wait a sec..")
                    print("???: WHOOOOA I SEEMS SOOOOOOO LONG AGO!")
                    print("???:Now I'm free to eat as many food as I want!")
                    print(f"???: By the way I'm {cuc}, Hero Of Glutony hehehe")
                    print(f"{cuc}I guess Madam Rosmerta is not gonna be glad to see me again hehehe")
                    print(f"{cuc}: Either way, thanx for freein' me, boy!")
                    Heroes.find_hero(f"{cuc}")
                    is_hero_free = True
                    continue
            elif answer == 3:
                print("You step back from where you came")
                central_left_wing()
        except ValueError:
            print("Choose a valid option")
##################################################
def far_left_wing():
    print("\nThe air feel heavier here...")

    while True:
        print("1. Move to your left")
        print("2. Move to your right")
        print("3. Go back")

        try:
            answer = int(input("Where do we go from here?"))

            if answer == 1:
                print("There's a trap from an ancient magic! You start at the beginning of the Hall Of Mirrors!")
                hall_of_mirrors()
            elif answer == 2:
                print("You now move to your right, more flickering lights from the mirrors echoes your move")
                far_central_wing()
            elif answer == 3:
                print("You step back from where you came")
                central_left_wing()
        except ValueError:
            print("Choose a valid option")
##################################################
def central_left_wing():
    global is_left_wing_knight_down, is_circular_mirror_flicked
    print("\nThe air feels warmer here...")

    while True:
        print("1. Move forward.")
        print("2. Move to your left")
        print("3. Move to your right")
        print("4. Go back")

        try:
            answer = int(input("Where do we go from here?"))

            if answer == 1:
                if is_circular_mirror_flicked:
                    print("Seems like something moved here...")
                    far_left_wing()
                else:
                    print("There's a magical reflection preventing access...due to the marks on the floor")
                    print("\nit seems like it has moved before...there must be some mechanism somewhere")
                    continue
            elif answer == 2:
                if is_left_wing_knight_down:
                    print("The knight statue looks intimidating surrounded by mirrors")
                    continue
                else:
                    print("You move forward and discover an old statue of a knight...the knight moves!")
                    left_wing_knight_battle()
                    pass
            elif answer == 3:
                print("There's a huge mirror preventing further move")
                continue
            elif answer == 4:
                print("You step back from where you came")
                left_wing()
        except ValueError:
            print("Choose a valid option")
##################################################
def central_west_wing():
    global is_circular_mirror_flicked, is_west_wing_chest_open
    print("\nThe air feels warmer here...")

    while True:
        print("1. Move forward.")
        print("2. Move to your left")
        print("3. Move to your right")
        print("4. Go back")

        try:
            answer = int(input("Where do we go from here?"))

            if answer == 1:
                print("Theres a circular broken mirror, it seems it has been flicked before...")
                is_circular_mirror_flicked = True
                print("Indeed, it moved...seems it can be moved again in the future")
                continue
            elif answer == 2:
                print("There's a huge mirror preventing further move")
                continue
            elif answer == 3:
                if is_west_wing_chest_open:
                    print("I already opened this chest, there's nothing here")
                    continue
                else:
                    print("You found a chest!")
                    print("You found $5000!")
                    Status.souls += 5000
                    is_west_wing_chest_open = True
                    print("I already opened this chest, there's nothing here")
                    continue
            elif answer == 4:
                print("You step back from where you came")
                west_wing()
        except ValueError:
            print("Choose a valid option")
##################################################
def left_wing():
    global is_left_wing_chest_open
    print("\nThe air still feels cold here...")

    while True:
        print("1. Move forward.")
        print("2. Move to your left")
        print("3. Move to your right")
        print("4. Go back")

        try:
            answer = int(input("Where do we go from here?"))

            if answer == 1:
                if is_left_wing_chest_open:
                    print("I already opened this chest, there's nothing here")
                    continue
                else:
                    print("You founnd a chest!")
                    print("You found $5000!")
                    Status.souls += 5000
                    is_left_wing_chest_open = True
                    print("I already opened this chest, there's nothing here")
                    continue
            elif answer == 2:
                print("There's a huge mirror preventing further move")
                continue
            elif answer == 3:
                print("You now move to your right, more flickering lights from the mirrors echoes your move")
                central_left_wing()
            elif answer == 4:
                print("You step back from where you came")
                hall_of_mirrors()
        except ValueError:
            print("Choose a valid option")
#############################################
def central_wing():
    print("\nThe air feels warmer here...")

    while True:
        print("1. Move forward")
        print("2. Move to your left")
        print("3. Move to your right")
        print("4. Go back")

        try:
            answer = int(input("Where do we go from here?"))

            if answer == 1:
                print("There's a huge mirror preventing further move")
                continue
            elif answer == 2:
                print("You now move to your left, more flickering lights from the mirrors echoes your move")
                central_left_wing()
            elif answer == 3:
                print("There's a huge mirror preventing further move")
                continue
            elif answer == 4:
                print("You step back from where you came")
                hall_of_mirrors()
        except ValueError:
            print("Choose a valid option")
#############################################
def west_wing():
    global is_west_wing_knight_down
    print("\nThe air still feels cold here...")

    while True:
        print("1. Move forward")
        print("2. Move to your left")
        print("3. Move to your right")
        print("4. Go back")

        try:
            answer = int(input("Where do we move among these mirrors?"))

            if answer == 1:
                if is_west_wing_knight_down:
                    print("The knight statue looks intimidating surrounded by mirrors")
                    continue
                else:
                    print("You move forward and discover an old statue of a knight...the knight moves!")
                    west_wing_knight_battle()
                    pass
            #######
            elif answer == 2:
                print("You now move to your left, more flickering lights from the mirrors echoes your move")
                central_west_wing()
            elif answer == 3:
                print("There's a huge mirror preventing further move")
                continue
            elif answer == 4:
                print("You step back from where you came")
                hall_of_mirrors()
        except ValueError:
            print("Choose a valid option")
#############################################
def hall_of_mirrors():
    print("\nSeems like an old room, the oldest I've been so far...")
    print("It's full of mirrors of all kind and sizes and in varying degrees of destruction")
    print("The air feels cold here...")

    while True:
        print("1. Walk forward")
        print("2. Walk right")
        print("3. Walk left")
        print("4. Exit the room")

        try:
            answer = int(input("Where should we go from here?"))

            if answer == 1:
                print("You move forward, flickering lights denote your movements in the mirrors")
                central_wing()
            elif answer == 2:
                print("You move to your right, flickering lights denote your movements in the mirrors")
                west_wing()
            elif answer == 3:
                print("You move to your left, flickering lights denote your movements in the mirrors")
                left_wing()
            elif answer == 4:
                print("You leave the Hall Of Mirrors")
                return
        except ValueError:
            print("Choose a valid option")
#################
hall_of_mirrors()