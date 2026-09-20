from inventory import add_item, remove_item, has_item
import Status
import Encounters

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
                Dungeons_Rooms_East.dungeons_corridor_init()
            elif answer == 2:
                print("You open the door that lies to your left")
                import Upside_Down_Room
                Upside_Down_Room.where_to_start()
            elif answer == 3:
                Encounters.random_encounter("dungeons")
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
                if not Status.is_daylight:
                    print("You open the door that lies to your right")
                    import Dungeons_Secret_Room
                    Dungeons_Secret_Room.dungeons_secret_room()
                else:
                    print("A powerful magic prevents the door from opening")
            elif answer == 2:
                print("You open the door that lies to your left")
                import Dungeons_Room_Trial
                Dungeons_Room_Trial.dungeon_room_trial()
            elif answer == 3:
                Encounters.random_encounter("dungeons")
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
                import Dungeons_Tunnel
                Dungeons_Tunnel.dungeons_tunnel()
            elif answer == 2:
                print("You open the door that lies to your left")
                import Dungeons_Noisy_Room
                Dungeons_Noisy_Room.dungeons_noisy_room()
            elif answer == 3:
                Encounters.random_encounter("dungeons")
                print("You go back at the beginning of the dungeons")
                dungeons()
        except ValueError:
            print("Choose a valid option")
######################
def dungeons():
    print("I can barely see a metre away...better be careful around here...")

    while True:
        print("1. Move north")
        print("2. Move east")
        print("3. Move west")
        print("4. Go back")
        print("5. Check inventory")

        try:
            answer = int(input("Better get going..."))

            if answer == 1:
                Encounters.random_encounter("dungeons")
                print("You move forward in the darkness")
                dungeons_forward()
            elif answer == 2:
                Encounters.random_encounter("dungeons")
                print("You move closer to the walls")
                dungeons_west()
            elif answer == 3:
                Encounters.random_encounter("dungeons")
                print("You move closer to the windows")
                dungeons_east()
            elif answer == 4:
                print("You leave the dungeons")
                return
            elif answer == 5:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
#############################
dungeons()