from inventory import add_item, remove_item, has_item
import Status
import os

def plaza():
    os.system('cls')
    Status.current_room = "gardens"
    print("\nA spacious green garden with a fountain in the middle")
    print("Seems like many parts of the castle are connected to the Plaza, also a river is flowing graciously")

    while True:
        print("1. Move forward towards the riverside corridor (right)")
        print("2. Move forward towards the riverside corridor (left)")
        print("3. Examine the fountain")
        print("4. Examine the river")
        print("5. Go to the Royal Wing")
        print("6. Check inventory")

        try:
            answer = int(input("> "))

            if answer == 1:
                print("You move along the river towards the right side of the Plaza")
                import Plaza_Right
                Plaza_Right.plaza_right()
            elif answer == 2:
                print("You move along the river towards the left side of the Plaza")
                import Plaza_Left
                Plaza_Left.plaza_left()
            elif answer == 3:
                print("There's a printing at the foot of the central fountain: ")
                print("The lonely sea")
                print("The lonely sea")
                print("It never stops")
                print("For you or me")
                print("It moves along")
                print("From day to day")
                return
            elif answer == 4:
                if Status.is_firework_used:
                    print("The workingman's waiting at the other side")
                    print("Better get rid of the guard at the ROYAL WING or else I'll be in serious trouble")
                    while True:
                        print("1. Ride the boat to the other side")
                        print("2. No, I'm not sure if the guard is still there with this WEATHER")
                        try:
                            answer = int(input("> "))
                            if answer == 1:
                                print("You ride the boat and slowly sail to the other side")
                                import Plaza_Otherside
                                Plaza_Otherside.plaza_otherside()
                            elif answer == 2:
                                print("Yeah, good idea...I think i recall someone say that with certain weather the guards don't work")
                                return
                        except ValueError:
                            print("Choose a valid action")
                else:
                    print("Mmm since no one is waiting on the other side, I should find a way to call him from a distance")
                    return
            elif answer == 5:
                print("You enter the Royal Wing again")
                return
            elif answer == 6:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")