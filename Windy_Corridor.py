from inventory import add_item, remove_item, has_item
import Status
import Encounters

def marble_door_night():
    while True:

        print("1. Inspect the Marble door")
        print("2. Inspect the glass walls (left)")
        print("3. Go back through the corridor")

        try:
            answer = int(input(""))

            if answer == 1:
                print("The door is tightly shut and since it has no doorknobs it's not possible to open")
            elif answer == 2:
                print("There's a mysterious veil covering the remaining part of the glass wall")
                print("With a fainting muted and distant sound, the veil disappears revealing a mountainside passage")
                while True:
                    print("1. Yes")
                    print("2. No")
                    try:
                        answer = int(input("Would you go through the passage?"))
                        if answer == 1:
                            import Mountainside
                            Mountainside.mountainside()
                        elif answer == 2:
                            return
                    except ValueError:
                        print("Choose a valid action")
            elif answer == 3:
                Encounters.random_encounter("dungeons")
                print("You run through the other side of the corridor")
                return
        except ValueError:
            print("Choose a valid action")
#######################
def marble_door_day():
    while True:

        print("1. Inspect the Marble door")
        print("2. Inspect the glass walls (left)")
        print("3. Go back through the corridor")

        try:
            answer = int(input(""))

            if answer == 1:
                print("The Marble door opens!")
                import Third_Hall
                Third_Hall.third_hall()
            elif answer == 2:
                print("There's a mysterious veil covering the remaining part of the glass wall.Some magic binding prevents passage")
            elif answer == 3:
                print("You run through the other side of the corridor")
                return
        except ValueError:
            print("Choose a valid action")
############################
def windy_corridor_night():
    print("Moonlight shadows fill the glassy room of the corridor")

    while True:
        print("1. Run through the corridor (forward)")
        print("2. Inspect the glass walls (left)")
        print("3. Go back")

        try:
            answer = int(input(""))

            if answer == 1:
                Encounters.random_encounter("dungeons")
                print("You reach the end of the short corridor and there's a plain Marble door without doorknobs")
                marble_door_night()
            elif answer == 2:
                print("The view is frightening....the castle seems to be spinning above a stormy group of clouds")
            elif answer == 3:
                print("You return to the Second Hall")
                return
        except ValueError:
            print("Choose a valid action")
###########################
def windy_corridor_day():
    print("Rays of sunlight fill the glassy room of the corridor")

    while True:
        print("1. Run through the corridor (forward)")
        print("2. Inspect the glass walls (left)")
        print("3. Go back")

        try:
            answer = int(input(""))

            if answer == 1:
                print("You reach the end of the short corridor and there's a plain Marble door without doorknobs")
                marble_door_day()
            elif answer == 2:
                print("The view is astonishing....the castle seems to be floating above the dawn's clouds")
            elif answer == 3:
                print("You return to the Second Hall")
                return
        except ValueError:
            print("Choose a valid action")
#############################
def windy_corridor():
    if Status.is_daylight:
        windy_corridor_day()
    else:
        windy_corridor_night()
#######################
windy_corridor()