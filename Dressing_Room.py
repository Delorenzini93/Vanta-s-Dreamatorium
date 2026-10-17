from inventory import add_item, remove_item, has_item
import Status
import os

def change_clothes():
    print("You enter the small dressing chamber, almost a single person barely fits in.It's very uncomfortable and smelly")

    while True:
        print("1. Try some clothes you're carrying")
        print("2. Leave this awful-smelling site")

        try:
            answer = int(input("> "))
            if answer ==1:
                if has_item("Royal Guard's clothes"):
                    print("You're now dressed like a Royal Guard!")
                    Status.is_royal_clothes_worn = True
                elif not has_item("Royal Guard's clothes"):
                    print("You don't have any clothes to change right now")
            elif answer ==2:
                print("Yeah, better get going")
                return
        except ValueError:
            print("Choose a valid action")
############################
def dressing_room():
    os.system('cls')
    Status.current_room = "royal_wing"
    print("\nA small room that the employees of the castle usually use to change their working clothes")

    while True:
        print("1. Change some clothes")
        print("2. Go back to the Royal Wing")

        try:
            answer = int(input("> "))

            if answer == 1:
                if Status.is_daylight:
                    print("???: Occupied right now! Dressing Room's always busy at THIS TIME OF DAY!")
                else:
                    change_clothes()
            elif answer == 2:
                print("You return to the Royal Wing")
                return
        except ValueError:
            print("Choose a valid action")