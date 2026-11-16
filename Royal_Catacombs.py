from inventory import add_item, remove_item, has_item
import Status
import Encounters
import os
######################
def catacombs_east():
    while True:
        print("1. Enter Room 401")
        print("2. Enter Room 402")
        print("3. Go back")

        try:
            answer = int(input("We moved east, where do we go now?"))

            if answer == 1:
                print("You open the door that lies to your right")
                import Room_401
                Room_401.room_401()
            elif answer == 2:
                print("You open the door that lies to your left")
                import Room_402
                Room_402.room_402()
            elif answer == 3:
                Encounters.random_encounter("dungeons")
                print("You go back at the beginning of the catacombs")
                return
        except ValueError:
            print("Choose a valid option")
######################
def catacombs_west():
    while True:
        print("1. Enter Room 403")
        print("2. Enter Room 404")
        print("3. Go back")

        try:
            answer = int(input("We moved west, where do we go now?"))

            if answer == 1:
                print("You open the door that lies to your right")
                import Room_403
                Room_403.room_403()
            elif answer == 2:
                print("You open the door that lies to your left")
                import Room_404
                Room_404.room_404()
            elif answer == 3:
                Encounters.random_encounter("dungeons")
                print("You go back at the beginning of the catacombs")
                return
        except ValueError:
            print("Choose a valid option")
######################
def catacombs_forward():
    while True:
        print("1. Enter Room 405")
        print("2. Enter Room 406")
        print("3. Go back")

        try:
            answer = int(input("We moved forward, where do we go now?"))

            if answer == 1:
                print("You open the door that lies to your right")
                import Room_405
                Room_405.room_405()
            elif answer == 2:
                print("You open the door that lies to your left")
                import Room_406
                Room_406.room_406()
            elif answer == 3:
                Encounters.random_encounter("dungeons")
                print("You go back at the beginning of the catacombs")
                return
        except ValueError:
            print("Choose a valid option")
######################
def royal_catacombs():
    os.system('cls')
    Status.current_room = "royal_catacombs"
    print("I can barely see a metre away...better be careful around here...")

    while True:
        print("1. Move north")
        print("2. Move west")
        print("3. Move east")
        print("4. Go back")
        print("5. Check inventory")

        try:
            answer = int(input("Better get going..."))

            if answer == 1:
                Encounters.random_encounter("dungeons")
                print("You move forward in the darkness")
                catacombs_forward()
            elif answer == 2:
                Encounters.random_encounter("dungeons")
                print("You move closer to the walls")
                catacombs_west()
            elif answer == 3:
                Encounters.random_encounter("dungeons")
                print("You move closer to the windows")
                catacombs_east()
            elif answer == 4:
                print("You leave the catacombs")
                return
            elif answer == 5:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
royal_catacombs()