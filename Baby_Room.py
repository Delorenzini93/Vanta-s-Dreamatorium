from inventory import add_item, remove_item, has_item
import Status
import os

def baby_room():
    os.system('cls')
    Status.current_room = "royal_wing"
    print("\nTHAT'S THE KING'S BABY!")

    while True:
        print("1. Swap babies")
        print("2. Leave this place")
        print("3. Check inventory")

        try:
            answer = int(input("> "))
            if answer == 1:
                if Status.carrying_blue_blood_baby:
                    print("You swiftly swaped both babies, now the true King's baby is in the royal chamber!")
                    Status.carrying_normal_baby = True
                    Status.carrying_blue_blood_baby = False
                    print("Now it's mandatory to quickly give this baby to the unsuspecting workingman")
                    return
                else:
                    print("I don't have any baby with me to swap, isn't it?")
                    return
            elif answer == 2:
                print("You step out of from the baby's room")
                return
            elif answer == 3:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")