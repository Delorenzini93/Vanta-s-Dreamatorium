from inventory import add_item, remove_item, has_item
import Status

def dungeons_corridor():
    print("Wow, it's darker and colder down here...")

    while True:
        print("1. Open closest door (left)")
        print("2. Open closest door (right)")
        print("3. Open furthest door (left)")
        print("4. Open furthest door (right)")
        print("5. Go down to the Dungeons.")
        print("6. Go back and leave the corridor")

        try:
            answer = int(input("Where do we go from here?"))

            if answer == 1:
                print("\nThe door leading to the Room Of Cauldrons opens with a squaky sound")
                import Room_Of_Cauldrons
                Room_Of_Cauldrons.room_of_cauldrons()

            elif answer == 2:
                print("\nThe door leading to the Hall Of Mirrors opens with a distant sound")
                import Hall_Of_Mirrors
                Hall_Of_Mirrors.hall_of_mirrors()

            elif answer == 3:
                print("\nThe door of the Old Boticary Opens")
                import Old_Boticary
                Old_Boticary.old_boticary()

            elif answer == 4:
                if not Status.is_daylight:
                    print("The goblin guarding the door is asleep, it's now or never")
                    import Goblin_Warehouse
                    Goblin_Warehouse.goblin_warehouse()
                else:
                    print("There's a ugly-looking Goblin guarding the door")
                    continue

            elif answer == 5:
                if Status.is_candles_lit:
                    print("Glad I'm carrying candles, otherwise I'll be in complete darkness")
                    import Dungeons
                    Dungeons.dungeons()
                else:
                    print("It's too dark to go further without light...")

            elif answer == 6:
                print("You leave the Dungeons Corridor for now")
                return

        except ValueError:
            print("Choose a valid action")
############################
dungeons_corridor()
