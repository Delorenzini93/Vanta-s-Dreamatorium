from inventory import add_item, remove_item, has_item
import Status
import os

has_blessings = False
is_feast_known = False
is_announcement_known = False
is_young_man_done = False

def people_interaction():
    global is_feast_known, is_announcement_known, is_young_man_done
    while True:
        print("1. The joyful girl near the bar")
        print("2. The busy-looking woman near the store")
        print("3. The absent-minded young man")
        print("4. The young man reading a book")
        print("5. Never mind")

        try:
            answer = int(input("Who should we talk to?"))
            if answer ==1:
                print("Girl:-Hello there! Are you here for today's special announcement?")
                print("It's going to be a big, big thing today!")
                while True:
                    print("1. What's so special about today?")
                    print("2. Just passing by")
                    try:
                        answer = int(input("> "))
                        if answer==1:
                            print("Girl:- Today's is the official announcement of the new PRINCE!")
                            print("Isn't it great? It's an absolutely big deal for Garam, for sure indeed!")
                            is_announcement_known = True
                        elif answer==2:
                            print("Girl:-Have a nice day!")
                    except ValueError:
                        print("Choose a valid action")
            elif answer==2:
                print("Busy Woman:-Get away! Get away! I'm busy getting ready for the BIG FEAST of today!")
                is_feast_known = True
            elif answer==3:
                if is_young_man_done:
                    print("Young Man:-The end justify the means....the end justify the means? Good question...")
                    return
                if not is_young_man_done and is_announcement_known:
                    print("Young Man:-Everyone says today is a very important day, isn't it? What do you think man?")
                    while True:
                        print("1. Yeah, the ANNOUNCEMENT and all that stuff")
                        print("2. Leave the young man alone with his thoughts")
                        try:
                            answer = int(input("> "))
                            if answer==1:
                                print("Young Man:-That's right, I couldn't care less, to be honest")
                                print("I care about other things, not many things but surely other stuff like...books")
                                print("I constantly think about the story of the Piper and the Madcap..heard about Chapter 24?")
                                if Status.is_chapter_24_known:
                                    print("Young Man:-That's right! Change returns success!")
                                    print("Do you think the end justify the means?")
                                    while True:
                                        print("1. Yes")
                                        print("2. No")
                                        try:
                                            answer = int(input("> "))
                                            if answer==1:
                                                print("Young Man:-...")
                                                print("There's a great wisdom in foreign places, you know")
                                                print("I'll teach you MOLJAT language for you to know")
                                                print("whispers....whispers....whispers...")
                                                print("You know how to read MOLJAT language!")
                                                Status.knows_moljat = True
                                                is_young_man_done = True
                                                return
                                            elif answer == 2:
                                                print("Young Man:-...")
                                                print("There's a great wisdom in foreign places, you know")
                                                print("I'll teach you MOLJAT language for you to know")
                                                print("whispers....whispers....whispers...")
                                                print("You know how to read MOLJAT language!")
                                                Status.knows_moljat = True
                                                is_young_man_done = True
                                                return
                                        except ValueError:
                                            print("Choose a valid action")
                            elif answer==2:
                                return
                        except ValueError:
                            print("Choose a valid action")
                else:
                    print("Young Man:-Everyone says today is a very important day, isn't it? I couldn't care less")
            elif answer ==4:
                print("Reader:-I'm unable to finish lyrics for my song...gotta keep reading, though")
                print("Sorry, I cannot talk with you right know, you know?")
                return
            elif answer==5:
                return
        except ValueError:
            print("Choose a valid action")
##########################
def plaza_interaction():
    print("\nYou reach a big place with lots of people")
    print("Seems like a gathering of some sort since there are many kind of people all around")

    while True:
        print("1. Talk to someone")
        print("2. Go to the Store")
        print("3. Go to the Weapon Shop")
        print("4. Go to the Armor Shop")
        print("5. Go to the Bar")
        print("6. Go to the Brothel")
        print("7. Go back to the Central Plaza")
        print("8. Check inventory")

        try:
            answer = int(input("> "))
            if answer == 1:
                people_interaction()
            elif answer ==2:
                import Plaza_Store
                Plaza_Store.plaza_store()
            elif answer ==3:
                import Plaza_Weapon_Shop
                Plaza_Weapon_Shop.plaza_weapon_shop()
            elif answer == 4:
                import Plaza_Armor_Shop
                Plaza_Armor_Shop.plaza_armor_shop()
            elif answer ==5:
                import Bar
                Bar.bar()
            elif answer ==6:
                import Brothel
                Brothel.brothel()
            elif answer==7:
                return
            elif answer==8:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")
#######################################
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