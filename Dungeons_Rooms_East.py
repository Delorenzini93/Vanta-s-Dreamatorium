from inventory import add_item, remove_item, has_item
import Status
import Encounters
import Hall_Of_Trophies

def dungeons_corridor_last():
    print("-I....need....breathing...a bit")

    while True:

        print("\n1. Open the Oak door")
        print("2. Go back to the corridor")
        print("3. Check inventory")

        try:
            answer = int(input(""))

            if answer == 1:
                print("You open and pass through the Oak Door")
                Hall_Of_Trophies.hall_of_trophies()
                return
            elif answer == 2:
                Encounters.random_encounter("dungeons")
                print("You hear loud angry voices as you run...")
                dungeons_corridor_closer()
                return
            elif answer == 3:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")

############################
def dungeons_corridor_closer():
    print("-It's difficult to breath in here...")

    while True:
        print("\n1. Run through the corridor")
        print("2. Go back")
        print("3. Check inventory")

        try:
            answer = int(input(""))

            if answer == 1:
                Encounters.random_encounter("dungeons")
                print("You hear loud angry voices as you run...")
                dungeons_corridor_last()
                return
            elif answer == 2:
                Encounters.random_encounter("dungeons")
                print("You hear distant echoes as you run...")
                dungeons_corridor_init()
                return
            elif answer == 3:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
############################
def dungeons_corridor_far():
    print("-I need to catch my breath...")

    while True:
        print("\n1. Run through the corridor")
        print("2. Go back")
        print("3. Check inventory")

        try:
            answer = int(input(""))

            if answer == 1:
                Encounters.random_encounter("dungeons")
                print("You hear distant echoes as you run...")
                dungeons_corridor_closer()
                return
            elif answer == 2:
                Encounters.random_encounter("dungeons")
                print("You hear indistinct chatter as you run...")
                dungeons_corridor_init()
                return
            elif answer == 3:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
#######################
def dungeons_corridor_init():
    print("There's a long corridor with a door at the end of it")

    while True:
        print("\n1. Run through the corridor")
        print("2. Go back")
        print("3. Check inventory")

        try:
            answer = int(input("Well..."))

            if answer == 1:
                Encounters.random_encounter("dungeons")
                print("You hear indistinct chatter as you run...")
                dungeons_corridor_far()
                return
            elif answer == 2:
                print("You went back to the dungeons")
                return
            elif answer == 3:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
################
dungeons_corridor_init()