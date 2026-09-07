from inventory import add_item, remove_item, has_item
import Status

is_look_above = False
is_wall_pushed = False
is_look_bookpile_left = False
is_look_bookpile_right = False
is_squaky_pile_exist = True
is_squaky_pile_safe = False
is_fire_known = False
is_culprit_known = False


def unbearable_goblin():
    global is_fire_known, is_culprit_known

    print("???: -DO NOT BRING FIRE! THAT'S WHY I FLOODED THIS PLACE!")

    while True:
        print("1. Why you flooded this place?")
        print("2. What fire are you talking about?")
        print("3. Why do you live on a wall??")
        print("4. You know? I think I know something...")
        print("5. Leave this psycho alone")

        try:
            answer = int(input("Choose something to say: "))
            if answer == 1:
                print("???: LONG AGO SOMEONE STARTED A TERRIBLE FIRE!")
                is_fire_known = True
                return
            elif answer == 2:
                print("???: NOBODY KNOWS WHO IT WAS, SO NO ONE IS SAFE!")
                is_culprit_known = True
                return
            elif answer == 3:
                print("???: WAAAAAAAAAAGGGGGGGHHHHHH!")
                return
            elif answer == 4:
                if has_item("Signed Veredict"):
                    print("???: WHAT? IT WAS ME? I MEAN ESTHAT?")
                    print("???: YOURE WRONG AND I DONT WANT TO HEAR NOR SEE YOU EVER AGAIN")
                    print("The Unbearable Goblin escapes leaving a fishing rod behind him")
                    add_item("Fishing Rod")
                    remove_item("Signed Veredict")
                    return
                else:
                    print("(I better leave this psycho alone)")
                    continue
            elif answer == 5:
                print("Yeah, good idea")
                return
            else:
                print("Choose from 1 to 5")
        except ValueError:
            print("Choose a valid action")


def highest_section():
    global is_look_above

    print("There's a big crack on the wall")

    while True:
        print("1. Talk to the wall")
        print("2. Go back (why on earth would I talk to a wall??)")

        try:
            answer = int(input("Choose an action: "))
            if answer == 1:
                if is_look_above:
                    print("???: - Well hello there!")
                    unbearable_goblin()
                    return
                else:
                    print("My sanity is being compromised....talking to a wall geez...")
                    return
            elif answer == 2:
                print("Yeah, that's right.....why would I talk to a wall?")
                return
            else:
                print("Choose either 1 or 2")
        except ValueError:
            print("Choose an option")


def higher_ground():
    global is_squaky_pile_exist

    print("Wow, this place really is THAT high!")

    while True:
        if is_squaky_pile_exist:
            print("1. Jump to the squeaky-looking pile of books ahead")
            print("2. Get down")
        else:
            print("1. Get down")

        try:
            answer = int(input("What should I do now that I'm on higher ground? "))

            if is_squaky_pile_exist:
                if answer == 1:
                    if is_squaky_pile_safe:
                        print("You jumped across the library and got to the highest section!")
                        highest_section()
                        return
                    else:
                        print("You jumped and the pile of books went down! You're now at the beginning.")
                        is_squaky_pile_exist = False
                        return
                elif answer == 2:
                    second_part_flooded_library()
                    return
                else:
                    print("Choose either 1 or 2")
            else:
                if answer == 1:
                    second_part_flooded_library()
                    return
                else:
                    print("Choose 1")

        except ValueError:
            print("Choose a valid option")


def second_part_flooded_library():
    global is_squaky_pile_safe

    print("The sound of water running is deafening here!")

    while True:
        print("1. Examine the wall where the water is entering (left)")
        print("2. Examine the wall where the water is draining (right)")
        print("3. Examine the wall where a book about Jim Carrey movies is lying")
        print("4. Go back to the entrance of the flooded library")

        try:
            answer = int(input("Choose an action: "))

            if answer == 1:
                if is_look_bookpile_left:
                    print("You put a 'Twilight' saga book to stop the water from entering the room")
                    is_squaky_pile_safe = True
                    continue
                else:
                    print("Water is rushing in from here but there's nothing to do about it now.")
                    continue
            elif answer == 2:
                if is_look_bookpile_right:
                    print("Hey! From here I could easily climb those hard-cover books!")
                    print("-you climb the big pile of hard cover books and are on higher ground now-")
                    higher_ground()
                    return
                else:
                    print("Water is draining somewhere here...")
                    continue
            elif answer == 3:
                print("There's a shining object behind the book")
                add_item("Liar Key")
                return
            elif answer == 4:
                return
            else:
                print("Choose from 1 to 4")
        except ValueError:
            print("Choose a valid option")


def squaky_looking_pile_of_books():
    global is_squaky_pile_exist

    while True:
        print("1. Climb the squeaky-looking pile of books")
        print("2. Step away for now")

        try:
            answer = int(input("Carefully choose an action: "))

            if answer == 1:
                print("The pile of books fell on the water, they're useless now")
                is_squaky_pile_exist = False
                return
            elif answer == 2:
                return
            else:
                print("Choose either 1 or 2")
        except ValueError:
            print("Choose a valid option")


def flooded_library():
    global is_look_above, is_look_bookpile_right, is_look_bookpile_left

    print("\nYou stand before a library with piles of books as high as the ceiling")
    print("There's a constant flow of water that gets to your waist")

    while True:
        print("1. Keep walking through the library")
        print("2. Take a look above")
        print("3. Examine the pile of books (right)")
        print("4. Examine the pile of books (left)")
        print("5. Exit the library")

        try:
            answer = int(input("Choose an action: "))

            if answer == 1:
                second_part_flooded_library()
            elif answer == 2:
                print("\nThere's a crack on the left side of the upper wall with a flickering light")
                is_look_above = True
            elif answer == 3:
                print("There's a big pile of hard-cover books one above the other")
                is_look_bookpile_right = True
            elif answer == 4:
                if is_look_bookpile_left:
                    squaky_looking_pile_of_books()
                else:
                    print("There's a pile of books hurriedly put one above the other...they seem fragile")
                    is_look_bookpile_left = True
            elif answer == 5:
                return
            else:
                print("Choose an option from 1 to 5.")
        except ValueError:
            print("Enter a valid action")


flooded_library()