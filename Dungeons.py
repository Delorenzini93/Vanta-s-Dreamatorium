from inventory import add_item, remove_item, has_item
import Status
import encounters

######################
def dungeons_east():
    while True:
        print("1. Door to the right")
        print("2. Door to the left")
        print("3. Go back")

        try:
            answer = int(input("We moved east, where do we go now?"))

            if answer == 1:
                print("You open the door that lies to your right")
                import Dungeons_Rooms_East
                Dungeons_Rooms_East.spacious_room()
            elif answer == 2:
                print("You open the door that lies to your left")
                import Dungeons_Rooms_East
                Dungeons_Rooms_East.upside_down_room()
            elif answer == 3:
                encounters.random_encounter("dungeons")
                print("You go back at the beginning of the dungeons")
                dungeons()
        except ValueError:
            print("Choose a valid option")
######################
def dungeons_west():
    while True:
        print("1. Door to the right")
        print("2. Door to the left")
        print("3. Go back")

        try:
            answer = int(input("We moved west, where do we go now?"))

            if answer == 1:
                print("You open the door that lies to your right")
                import Dungeons_Rooms_West
                Dungeons_Rooms_West.secret_room()
            elif answer == 2:
                print("You open the door that lies to your left")
                import Dungeons_Rooms_West
                Dungeons_Rooms_West.forgotten_room()
            elif answer == 3:
                encounters.random_encounter("dungeons")
                print("You go back at the beginning of the dungeons")
                dungeons()
        except ValueError:
            print("Choose a valid option")
######################
def dungeons_forward():
    while True:
        print("1. Door to the right")
        print("2. Door to the left")
        print("3. Go back")

        try:
            answer = int(input("We moved forward, where do we go now?"))

            if answer == 1:
                print("You open the door that lies to your right")
                import Dungeons_Rooms
                Dungeons_Rooms.troll_room()
            elif answer == 2:
                print("You open the door that lies to your left")
                import Dungeons_Rooms
                Dungeons_Rooms.noisy_room()
            elif answer == 3:
                encounters.random_encounter("dungeons")
                print("You go back at the beginning of the dungeons")
                dungeons()
        except ValueError:
            print("Choose a valid option")
######################
def dungeons():
    print("I can barely see a metre away...better be careful around here...")

    while True:
        print("1. Move forward")
        print("2. Move left")
        print("3. Move right")
        print("4. Go back")

        try:
            answer = int(input("Better get going..."))

            if answer == 1:
                encounters.random_encounter("dungeons")
                print("You move forward in the darkness")
                dungeons_forward()
            elif answer == 2:
                encounters.random_encounter("dungeons")
                print("You move closer to the walls")
                dungeons_west()
            elif answer == 3:
                encounters.random_encounter("dungeons")
                print("You move closer to the windows")
                dungeons_east()
            elif answer == 4:
                print("You leave the dungeons")
                return
        except ValueError:
            print("Choose a valid action")
#############################
dungeons()