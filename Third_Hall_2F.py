from inventory import add_item, remove_item, has_item
import Status
import os

def third_hall_2F():
    os.system('cls')
    Status.current_room = "west_hall_2F"

    print("\nThere's a small circular hallway above the Third Hall")

    while True:
        print("1. Circle the second floor")
        print("2. Jump to the Third Hall")
        print("3. Go back to the Piano Nobile")
        print("4. Check inventory")
        if Status.is_ceiling_seen:
            print("5. Examine the Bell")

        try:
            answer = int(input("> "))
            if answer == 1:
                print("You made your way through the short circular hall")
                import Royal_Wing
                Royal_Wing.royal_wing()
            elif answer == 2:
                print("Go ahead Jump!")
                import Third_Hall
                Third_Hall.third_hall()
            elif answer == 3:
                print("You go back")
                return
            elif answer == 4:
                from inventory import show_inventory
                show_inventory()
            elif answer ==5:
                print("There's an immaculate white and warm bell")

                while True:
                    print("1. Sure")
                    print("2. I don't think ringing a loud bell is a good idea right now")
                    try:
                        answer = int(input("> "))
                        if answer == 1:
                            print("The bell rings with a celestial and ringing sound!")
                            Status.is_bell_ring = True
                        elif answer == 2:
                            return
                    except ValueError:
                        print("Choose a valid action")
        except ValueError:
            print("Choose a valid action")