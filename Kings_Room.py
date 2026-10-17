from inventory import add_item, remove_item, has_item
import Status
import os

is_mali_password = False

def gargoyle_interaction():
    global is_mali_password
    print("There's a foul looking old gargoyle preventing passage to the inner room")

    while True:
        print("1. Speak to the gargoyle")
        print("2. This seems incredibly dangerous and reckless, better leave now")

        try:
            answer = int(input("> "))
            if answer == 1:
                if is_mali_password:
                    print("Yo Albert, go ahead mate!")
                    import Baby_Room
                    Baby_Room.baby_room()
                elif Status.is_royal_clothes_worn and Status.is_gargoyle_password and not is_mali_password:
                    print("Yo Albert, password changed yesterday and someone leaved a note on the bed to help with it")
                    print("When you feel like it, give it a try , I'll hear you out mate!")
                    while True:
                        print("1. Try to guess the password")
                        print("2. Nah, leave it, entering the inner chamber seems impossible")
                        try:
                            answer = int(input("> "))
                            if answer ==1:
                                print("So Albert, tell me the new password: ")
                                name = input("The password is: ").strip().lower()
                                if name == "mali":
                                    print("Yeah, you're sharp of mind Albert, go ahead mate!")
                                    is_mali_password = True
                                    import Baby_Room
                                    Baby_Room.baby_room()
                            elif answer == 2:
                                return
                        except ValueError:
                            print("Choose a valid action")
                elif Status.is_royal_clothes_worn and not Status.is_gargoyle_password:
                    print("Sorry Albert, I know it's you but protocol says you have to say the password to let you access")
                    print("You may have forgotten it, no big deal...someone will know, don't worry")
                    return
                elif not Status.is_royal_clothes_worn:
                    print("Excuse me? Who are you? Leave immediately or I'll call security!")
                    return
            elif answer ==2:
                print("Yeah...")
                return
        except ValueError:
            print("Choose a valid action")
####################
def kings_room():
    os.system('cls')
    Status.current_room = "royal_wing"

    print("\nWOW! Such a luxurious royal room! Better do our thing and quickly leave this room or else I'll get into trouble")

    while True:
        print("1. Examine the bed")
        print("2. Examine the table")
        print("3. Examine the back of the door")
        print("4. Leave the room")
        print("5. Check inventory")

        try:
            answer = int(input("> "))

            if answer == 1:
                print("There's a seemingly rushed on the bed:")
                print("They were the two old kings from Europe, all in capitols who ruled an african kingdom")
                print("The first one spoke a language only his kin spoke and conquered the whole old world")
                print("The second one spoke a language only his kin spoke and made a treaty with the first one")
                print("Of all the letters, only 2 remained with each of the kings")
                print("A sharp mind will realize the african kingdom only had 4 letters")
            elif answer == 2:
               print("You found a pouch with money")
               print("Since the money it's not yours you should leave it alone")
               print("But since no one is looking you take it for yourself")
               print("You found $15000!")
               Status.souls += 15000
            elif answer == 3:
                gargoyle_interaction()
            elif answer == 4:
                print("You went back to the royal wing")
                return
            elif answer == 5:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")