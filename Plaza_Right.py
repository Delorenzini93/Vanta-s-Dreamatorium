from inventory import add_item, remove_item, has_item
import Status
import os

has_blessings = False

def plaza_right():
    global has_blessings
    os.system('cls')
    Status.current_room = "gardens"

    if Status.jesters_dilemma_solved:
        plaza_interaction()
    else:
        print("\nYou reach a big place with lots of people")
        print("Since it's not a good idea to be seen, I better get into the first door I see")
        print(" ...... ouch!")
        print("You entered what seems to be a functioning warehouse...clearly a restricted area")

        while True:
            print("1. Check items on the table")
            print("2. Leave the place")
            print("3. Check inventory")

            try:
                answer = int(input("> "))
                if answer ==1:
                    if has_blessings:
                        print("It's empty now")
                    elif not has_blessings:
                        print("Those are the blessings and good given to new born babies in town!")
                        if Status.carrying_blue_blood_baby:
                            print("But I should swap the babies first, isn't it?")
                        elif Status.carrying_normal_baby:
                            print("You carry the blessings and goods with you now!")
                            add_item("Blessings")
                            has_blessings = True
                        elif not Status.carrying_blue_blood_baby and not Status.carrying_normal_baby:
                            print("I should talk to the workingman first, on the other side of the river")
                elif answer == 2:
                    print("You go back to the Plaza")
                    return
                elif answer == 3:
                    from inventory import show_inventory
                    show_inventory()

            except ValueError:
                print("Choose a valid action.")