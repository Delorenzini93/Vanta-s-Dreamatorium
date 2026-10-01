from inventory import add_item, remove_item, has_item
import Status
import Encounters

def mountainside_last():
    print("You're in total darkness and the noise is unbearable, leaving you unable to think clearly")

    while True:

        print("\n1. Advance through the gorge")
        print("2. Go back")
        print("3. Check inventory")

        try:
            answer = int(input(""))

            if answer == 1:
                print("You make your way through the dark and rocky gorge")
                import Gorge
                Gorge.gorge()
                return
            elif answer == 2:
                Encounters.random_encounter("exterior")
                print("The noise pierces your ears and the castle seems like a distant memory from your perspective")
                mountainside_closer()
                return
            elif answer == 3:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")

############################
def mountainside_closer():
    print("There's a piercing, high-pitched noise somewhere....vision is almost gone")

    while True:
        print("\n1. Run through the mountainside (forward)")
        print("2. Go back")
        print("3. Check inventory")

        try:
            answer = int(input(""))

            if answer == 1:
                Encounters.random_encounter("exterior")
                print("The noise pierces your ears and the castle seems like a distant memory from your perspective")
                mountainside_last()
                return
            elif answer == 2:
                Encounters.random_encounter("exterior")
                print("You hear something somewhere in the mountain but the castle gets blurry from your perspective")
                mountainside_far()
                return
            elif answer == 3:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
############################
def mountainside_far():
    print("There's some kind of distant, indistinct noise somewhere....vision is a little blurry tho")

    while True:
        print("\n1. Run through the mountainside (forward)")
        print("2. Go back")
        print("3. Check inventory")

        try:
            answer = int(input(""))

            if answer == 1:
                Encounters.random_encounter("exterior")
                print("You hear something somewhere in the mountain but the castle gets blurry from your perspective")
                mountainside_closer()
                return
            elif answer == 2:
                Encounters.random_encounter("exterior")
                print("You hear nothing but the castle is visible from your perspective")
                mountainside_init()
                return
            elif answer == 3:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
#######################
def mountainside_init():
    Status.current_room = "mountainside"
    print("There's a freezing cold blowing...Seems like there's a long way from the trail")

    while True:
        print("\n1. Run through the mountainside (forward)")
        print("2. Go back")
        print("3. Check inventory")

        try:
            answer = int(input("Well..."))

            if answer == 1:
                Encounters.random_encounter("exterior")
                print("You hear nothing but the castle is visible from your perspective")
                mountainside_far()
                return
            elif answer == 2:
                print("You went back to the Windy Corridor")
                return
            elif answer == 3:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
################
mountainside_init()