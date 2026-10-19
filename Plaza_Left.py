from inventory import add_item, remove_item, has_item
import Status
import os

def plaza_left():
    os.system('cls')
    Status.current_room = "gardens"
    print("\nYou approach a circular town square-like garden")

    while True:
        print("1. Examine statue at the garden's center")
        print("2. Reach the door at far left")
        print("3. Reach the door at the far right")
        print("4. Examine the river")
        print("5. Go back to the Plaza")
        print("6. Check inventory")

        try:
            answer = int(input("> "))
            if answer == 1:
                print("The statue has a writing in a strange language")
                while True:
                    print("1. Yes")
                    print("2. No, leave the statue for now")
                    try:
                        answer = int(input("WIll you read the writing?"))
                        if answer == 1:
                            if Status.knows_moljat:
                                print("The code of entrance is DOMA1993")
                            else:
                                print("It's written in a foreign and strange language")
                        elif answer == 2:
                            return
                    except ValueError:
                        print("Choose a valid action")
            elif answer == 2:
                print("You open the door leading to the Magi's Library")
                import Magis_Library
                Magis_Library.magis_library()
            elif answer == 3:
                print("You open the door leading to the Ballroom")
                import Ballroom
                Ballroom.ballroom()
            elif answer == 4:
                print("The river flows in tranquility")
                if Status.is_daylight and not Status.is_raining:
                    print("The sun shines brightly during the DAY with CLEAR skies")
                elif Status.is_daylight and Status.is_raining:
                    print("The sun shines brightly during the DAY with RAINING skies")
                elif not Status.is_daylight and not Status.is_raining:
                    print("The NIGHT shines upon us with CLEAR clouds")
                elif not Status.is_daylight and Status.is_raining:
                    print("The NIGHT shines upon us with RAINING clouds")
            elif answer == 5:
                print("You go back to the Plaza")
                return
            elif answer == 6:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")