from inventory import add_item, remove_item, has_item
import Status
import Encounters

is_dungeons_door_open = False


def glass_door():
    while True:
        print("1. Open the damaged door")
        print("2. Read the bookstand")
        print("3. Go back")

        try:
            answer = int(input(""))

            if answer == 1:
                print("When opened, the door makes a loud and squeaky sound...seems it hasn't been opened in a long time")
                if Status.is_daylight:
                    import Archane_Room_Day
                    Archane_Room_Day.archane_room_day()
                else:
                    import Archane_Room_Night
                    Archane_Room_Night.archane_room_night()
            elif answer == 2:
                if Status.is_daylight:
                    print("#write something later")
                else:
                    print("#write something later")
            elif answer == 3:
                print("You step away from the old door")
                return
        except ValueError:
            print("Choose a valid action")
#######################
def third_hall_night():
    print("The dark stone floor seems scary in the dimly lighted hall")
    print("I got the feeling that we're getting deeper into the heart of the castle")

    while True:
        print("1. Go to the Stone door (north)")
        print("2. Go to the Glass door (east)")
        print("3. Go to the Wooden door (west)")
        print("4. Go to the Marble door (south)")
        print("5. Look above")
        print("6. Check inventory")

        try:
            answer = int(input("Where do we go from here?"))

            if answer == 1:
                Encounters.random_encounter("dungeons")
                print("The Stone door opens to a corridor with many windows")
                import Corridor_With_Many_Windows
                Corridor_With_Many_Windows.corridor_with_many_windows()
            elif answer == 2:
                Encounters.random_encounter("dungeons")
                print("You stand before what seems to be a very old and damaged door with a bookstand beside it")
                glass_door()
            elif answer == 3:
                Encounters.random_encounter("dungeons")
                if Status.is_candles_lit:
                    print("You go to the dungeons")
                    import Dungeons
                    Dungeons.dungeons()
                else:
                    print("It's too dark to venture inside")
            elif answer == 4:
                if Status.is_daylight:
                    print("The Marble door opens!")
                    import Windy_Corridor
                    Windy_Corridor.windy_corridor_day()
                else:
                    Encounters.random_encounter("dungeons")
                    print("The door is tightly shut")
            elif answer == 5:
                print("There impossible to see what's on the ceiling, the room is too dark")
            elif answer == 6:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
########################
def third_hall_day():
    print("This Hall with shining marble floor seems more luxurious than the previous two")
    print("I got the feeling that we're getting deeper into the heart of the castle")

    while True:
        print("1. Go to the Stone door (north)")
        print("2. Go to the Glass door (east)")
        print("3. Go to the Wooden door (west)")
        print("4. Go to the Marble door (south)")
        print("5. Look above")
        print("6. Check inventory")

        try:
            answer = int(input("Where do we go from here?"))

            if answer == 1:
                print("The Stone door opens to a corridor with many windows")
                import Corridor_With_Many_Windows
                Corridor_With_Many_Windows.corridor_with_many_windows()
            elif answer == 2:
                print("You stand before what seems to be a very old and damaged door with a bookstand beside it")
                glass_door()
            elif answer == 3:
                if Status.is_candles_lit:
                    print("You go to the dungeons")
                    import Dungeons
                    Dungeons.dungeons()
                else:
                    print("It's too dark to venture inside")
            elif answer == 4:
                if Status.is_daylight:
                    print("The Marble door opens!")
                    import Windy_Corridor
                    Windy_Corridor.windy_corridor_day()
                else:
                    print("The door is tightly shut")
            elif answer == 5:
                print("There are beautiful birds painted all over the facade of the second floor")
            elif answer == 6:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
########################
def third_hall():
    global is_dungeons_door_open
    if Status.is_daylight:
        is_dungeons_door_open = True
        third_hall_day()
    else:
        is_dungeons_door_open = True
        third_hall_night()
########################
third_hall()