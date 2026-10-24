from inventory import add_item, remove_item, has_item
import Status
import os

is_handwritten_notes_destroyed = False
is_bottle_destroyed = False

def interaction_with_the_magi():
    global is_handwritten_notes_destroyed, is_bottle_destroyed
    print("There's a man sitting in a dingy chair, with a seemingly worried yet optimistic grin with a fragile frame")
    print("You dont remember ever looking at someone and have such a contradictory impression")
    print("There are handwritten notes all over the floor and an open bottle of wine by his side")

    while True:
        print("1. Talk to the Magi in a respectful, civilized way")
        print("2. Sing the song 'Bike' at the top of your lungs")
        print("3. Tell him a fictional story in which you are a heaven-sent messiah")
        print("4. Ask him to teach you foreign languages")
        print("5. Destroy the handwritten notes of the Magi")
        print("6. Destroy the bottle on the floor")
        print("7. Punch the Magi")
        print("8. Leave the fatal-looking man alone")

        try:
            answer = int(input("> "))
            if answer==1:
                print("Magi: I don't want to talk right now")
            elif answer==2:
                print("I GOT A BIKE YOU CAN RIDE IT IF YOU LIKE!")
                print("Magi: Please, be quiet")
            elif answer ==3:
                print("Magi: I dont believe you")
            elif answer ==4:
                print("Magi: No")
            elif answer ==5:
                if is_handwritten_notes_destroyed:
                    print("You already did that!")
                else:
                    print("You destroy all of the Magi's work...seems to have no effect on him in any way")
                    is_handwritten_notes_destroyed = True
            elif answer ==6:
                if is_bottle_destroyed:
                    print("Why would you keep tormenting this poor man?")
                else:
                    print(f"For reasons only known to you, {Status.user}, you destroy the poor man's bottle of wine")
                    is_bottle_destroyed = True
            elif answer ==7:
                print("Such a heinous and heartless thing to do...no way")
            elif answer ==8:
                print("Im not sure if I enjoyed interacting with this peculiar character")
                return
        except ValueError:
            print("Choose a careful action with the Magi")
####################################
def sodna_section():
    print("\nThere are many books with Soviet-looking covers")

    while True:
        print("1. Read 'Molchat'")
        print("2. Read 'Khno'")
        print("3. Read 'Krovi'")
        print("4. Leave this section for now")

        try:
            answer = int(input("> "))
            if answer == 1:
                if Status.knows_soviet_language:
                    pass
                else:
                    print("It's written in a foreign language you dont understand")
            elif answer == 2:
                if Status.knows_soviet_language:
                    pass
                else:
                    print("It's written in a foreign language you dont understand")
            elif answer == 3:
                if Status.knows_soviet_language:
                    pass
                else:
                    print("It's written in a foreign language you dont understand")
            elif answer == 4:
                return
        except ValueError:
            print("Choose a valid action")
##################################
def macbeth_section():
    print("\nThere are many books with expressionist covers")

    while True:
        print("1. Read 'Pulso'")
        print("2. Read 'Ritos De Primavera'")
        print("3. Read 'Cercania'")
        print("4. Leave this section for now")

        try:
            answer = int(input("> "))
            if answer ==1:
                if Status.knows_spanish_language:
                    pass
                else:
                    print("It's written in a foreign language you dont understand")
            elif answer == 2:
                if Status.knows_spanish_language:
                    pass
                else:
                    print("It's written in a foreign language you dont understand")
            elif answer == 3:
                if Status.knows_spanish_language:
                    pass
                else:
                    print("It's written in a foreign language you dont understand")
            elif answer ==4:
                return
        except ValueError:
            print("Choose a valid action")
#################################
def canterbury_section():
    print("\nThere are many books with colorful covers")

    while True:
        print("1. Read 'Apple & Oranges'")
        print("2. Read 'Mathilda Mother'")
        print("3. Read 'Chapter 24'")
        print("4. Leave this section for now")

        try:
            answer = int(input("> "))
            if answer ==1:
                print("Apples and oranges\nApples and oranges\nApples and oranges")
            elif answer ==2:
                print("Why you had to leave there? Hanging in my infant air?")
            elif answer ==3:
                print("Change returns success\nGoing and coming without error\nAction brings good fortune")
                Status.is_chapter_24_known = True
            elif answer ==4:
                return
        except ValueError:
            print("Choose a valid action")
################################
def magis_library():
    os.system('cls')
    Status.current_room = "gardens"

    print("\nYou enter a strange-looking library")
    print("It's ceiling is made of different unmatching materials and colors")
    print("It seems that the person who designed this room doesn't has the slightest idea of basic architecture and geometry")

    while True:
        print("1. Interact with the Magi")
        print("2. Inspect 'Macbeth' section")
        print("3. Inspect 'Sodna' section")
        print("4. Inspect 'Canterbury' section")
        print("5. Leave this place")
        print("6. Check inventory")

        try:
            answer = int(input("> "))
            if answer == 1:
                interaction_with_the_magi()
            elif answer ==2:
                macbeth_section()
            elif answer == 3:
                sodna_section()
            elif answer ==4:
                canterbury_section()
            elif answer ==5:
                print("You unceremoniously leave the place")
                return
            elif answer ==6:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")