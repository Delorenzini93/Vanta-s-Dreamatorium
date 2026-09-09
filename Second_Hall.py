from inventory import add_item, remove_item, has_item
import Status

is_eagle_key_solved = False
is_vanta_key_solved = False

def eagle_door():
    global is_eagle_key_solved

    print("\nThere's a door with an eagle carved on an ornamental door arch.")

    while True:
        print("\n1. Open the door")
        print("2. Go back")

        try:
            answer = int(input("\nChoose an action"))

            if answer == 1:
                if is_eagle_key_solved:
                    import Windy_Corridor
                    Windy_Corridor.windy_corridor()
                    return

                elif has_item("Eagle Key"):
                    print("The door has slowly opened...it seems it was locked for a long time")
                    remove_item("Eagle Key")
                    is_eagle_key_solved = True
                    import Windy_Corridor
                    Windy_Corridor.windy_corridor()
                    return

                else:
                    print("The door is tightly locked")

            elif answer == 2:
                print("\nYou step away from the door.")
                return

            else:
                print("Please choose a number between 1 and 2.")

        except ValueError:
            print("Please enter a number.")
#############################
def vantas_door():
    global is_vanta_key_solved

    print("\nThere's a heavily damaged door that seems out of place with the rest")

    while True:
        print("\n1. Open the door")
        print("2. Go back")

        try:
            answer = int(input("\nChoose an action"))

            if answer == 1:
                if is_vanta_key_solved:
                    import Vantas_Chamber
                    Vantas_Chamber.vantas_room()
                    return

                elif has_item("Vanta's Key"):
                    print("The door has slowly opened...it feels like you shouldn't be here")
                    remove_item("Vanta's Key")
                    is_vanta_key_solved = True
                    import Vantas_Chamber
                    Vantas_Chamber.vantas_room()
                    return

                else:
                    print("The door is tightly locked")

            elif answer == 2:
                print("\nYou step away from the peculiar-looking door.")
                return

            else:
                print("Please choose a number between 1 and 2.")

        except ValueError:
            print("Please enter a number.")
##############################
def second_hall():
    print("You stand at the second hall, more spacious than the previous")
    print("sounds reverberate in a peculiar way here.")

    while True:
        print("\n1.Eagle Door (forward)")
        print("2.Outdoor Garden (left)")
        print("3. Dining Room (left)")
        print("4. Flooded Library (left)")
        print("5. Dungeon's Corridors (right)")
        print("6. Echoing Corridor (right)")
        print("7. Vanta's Chamber")

        try:
            answer = int(input("Where should we go?"))

            if answer == 1:
                eagle_door()

            elif answer == 2:
                print("\nThe door leading to the Outdoor Garden opens")
                import Outdoor_Garden
                Outdoor_Garden.outdoor_garden()

            elif answer == 3:
                print("\nThe door leading to the Dining Room opens")
                import Dining_Room
                Dining_Room.dining_room()

            elif answer == 4:
                print("\nThe door leading to the Flooded Library opens")
                import Flooded_Library
                Flooded_Library.flooded_library()

            elif answer == 5:
                print("\nThe door leading to the Dungeon's Corridors opens")
                import Dungeons_Corridors
                Dungeons_Corridors.dungeons_corridors()

            elif answer == 6:
                print("\nThe door leading to the Echoing Corridor opens")
                import Echoing_Corridor
                Echoing_Corridor.echoing_puzzle()

            elif answer == 7:
                vantas_door()

            else:
                print("Please choose a valid action.")

        except ValueError:
            print("Please enter a number between 1 and 7.")

second_hall()