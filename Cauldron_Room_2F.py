from inventory import add_item, remove_item, has_item
import Status

is_fairy_appear = False
is_second_floor_door_open = False
##########################
def cauldron_upper_view():
    print("You're at the Room of Cauldrons again, but this time in the upper part of the room")

    while True:
        print("1. Jump to the Room Of Cauldrons")
        print("2. Go back to the messy room")

        try:
            answer = int(input("The smells terrible in this place..."))

            if answer == 1:
                print("JUMP!")
                import Room_Of_Cauldrons
                Room_Of_Cauldrons.room_of_cauldrons()
            elif answer == 2:
                print("You step back from here")
                return
        except ValueError:
            print("Choose a valid action")
##########################
def fairy_interaction():
    print("Fairy: Wow! So much to do, so much to do!")
    print(f"{Status.user}: What's fuzzing you?")
    print("Fairy: I lost my book and I can't remember the exact name!")
    print(f"{Status.user}: What book? Where did you lost it?")
    print("Fairy: In the FLOODED LIBRARY! It was about a famous actor whose name I can't remember!")
    print(f"{Status.user}: But why do you need to remember it so desperately? You made this place a mess!")
    print("Fairy: It's the secret password for the Fairy Club!")
    print(f"{Status.user}: Fairy Club?")
    print("Fairy: Don't have time to explain right now since I'm busy trying to remember!")
    print("Fairy: If you happen to know, let me know the name of the actor from the FLOODED LIBRARY!")

    while True:
        print("1. Talk to the Fairy")
        print("2. Leave the Fairy alone, seems busy")

        try:
            answer = int(input("Mmmmm..."))

            if answer == 1:
                print("Fairy: What?!? Do you know or remember the name???")
                match input("The name is: ").strip().lower():
                    case "jim carrey":
                        print("Fairy: YES! You got it! That's the password for the Fairy Club!")
                        print("The Fairy stomped out of the room dropping something along the way")
                        add_item("Cabinet's Key")
                        print("'Cabinet Key' obtained!")
                    case _:
                        print("Fairy: You're wasting my time! Get away!")
                        return
            elif answer == 2:
                print("Yeah, better leave her alone, just in case")
                return
        except ValueError:
            print("Choose a valid action")
##################
def cauldron_room_2F():
    global is_fairy_appear, is_second_floor_door_open
    if is_fairy_appear:
        print("The room's much quieter now")

        while True:
            print("1. Inspect the mess")
            print("2. Inspect the door (forward)")
            print("3. Inspect the door (right)")
            print("4. Go back to the tunnel")

            try:
                answer = int(input("Let's see..."))

                if answer == 1:
                    print("")
                elif answer == 2:
                    if is_second_floor_door_open:
                        import Second_Upper_Hall
                        Second_Upper_Hall.second_upper_hall()
                    else:
                        print("It's locked from the other side")
                elif answer == 3:
                    print("You go to the Cauldron's Room upper side")
                    cauldron_upper_view()
                elif answer == 4:
                    print("You went back to the tunnel")
                    import Room_Of_Cauldrons
                    Room_Of_Cauldrons.tunnel_second_section()
            except ValueError:
                print("Choose a valid action")
    else:
        fairy_interaction()
#################
cauldron_room_2F()