from inventory import add_item, remove_item, has_item
import Status
import Cauldron_Room_2F

is_room_checked = False
is_torches_lit = False
is_tunnel_fully_known = False
is_second_trapdoor_open = False
is_third_trapdoor_open = False
is_tunnel_chest_open = False
is_minecart = False
is_cauldron_clean = False
is_cabinet_checked = False

###########################
def tunnel_third_section():
    global is_third_trapdoor_open, is_tunnel_chest_open, is_minecart
    print("\nThis seems to be the tunnel's final section")

    while True:
        print("1. Use the trapdoor")
        print("2. Inspect the floor")
        print("3. Inspect the railway")
        print("4. Go back")

        try:
            answer = int(input("What do we do here?"))

            if answer == 1:
                if is_third_trapdoor_open:
                    print("You use the third trapdoor")
                    pass #somewhere()")
                else:
                    print("It's locked from the other side")
            elif answer == 2:
                if is_tunnel_chest_open:
                    print("I already opened this chest, there's nothing here")
                else:
                    print("You founnd a chest!")
                    print("You found $5000!")
                    Status.souls += 5000
                    is_tunnel_chest_open = True
                    continue
            elif answer == 3:
                if is_minecart:
                    print("The minecart is fully operable now")
                    pass #somewhere
                else:
                    print("There's an old subterranean railway here but there's no minecart in sight")
                    continue
            elif answer == 4:
                print("You go back to the middle section of the tunnel")
                tunnel_second_section()
        except ValueError:
            print("Choose a valid action")
###########################
def tunnel_second_section():
    global is_second_trapdoor_open, is_tunnel_fully_known
    print("\nThis has to be the filthiest place ever...and I even lived in India for a while")

    while True:
        print("1. Move forward")
        print("2. Use the trapdoor")
        print("3. Inspect the walls")
        print("4. Go back to the beginning of the tunnel")

        try:
            answer = int(input("Where do we go from here?"))

            if answer == 1:
                print("You advance deep into the tunnel")
                tunnel_third_section()
            elif answer == 2:
                if is_second_trapdoor_open:
                    print("You use the second trapdoor")
                    pass #somewhere()
                else:
                    print("It's locked from the other side")
            elif answer == 3:
                if is_tunnel_fully_known:
                    print("There's a little hole leading to a noisy place")
                    Cauldron_Room_2F.cauldron_room_2F()
                else:
                    print("I don't know where this could lead to...not a good idea")
            elif answer == 4:
                print("Let's return")
                cauldron_room_tunnel()
        except ValueError:
            print("Choose a valid option")
#############################
def cauldron_room_tunnel():
    global is_torches_lit, is_tunnel_fully_known
    print("\nUgh...this looks like a filthy place and I have the slight impression that I shouldn't be here")

    while True:
        print("1. Inspect the tunnel")
        print("2. Move forward")
        print("3. Inspect walls")
        print("4. Go back through the trapdoor")

        try:
            answer = int(input("This looks like a foul place, better move..."))

            if answer == 1:
                print("Seems like a very long tunnel down here...")
                if is_torches_lit:
                    print("This seems like it's connecting various points of the castle")
                    is_tunnel_fully_known = True
                else:
                    print("It would be a wise idea to use candles to lighten the place up")
                    print("Unfortunately the dev forgot about this logical plothole, so I better use the tunnel's torches instead")
            elif answer == 2:
                if is_torches_lit:
                    print("Let's move to the next section of the tunnel")
                    tunnel_second_section()
                else:
                    print("It's too dark to see anything down here...")
            elif answer == 3:
                if has_item('Gasoline'):
                    print("I could ignite these torches with gasoline")
                    while True:
                        print("1. Yeah, why would I want to keep Gasoline for?")
                        print("2. I don't know exactly why, but no.")

                        try:
                            answer = int(input("What do we do with gasoline?"))
                            if answer == 1:
                                is_torches_lit = True
                                print("Now we're talking! I can see the whole tunnel now!")
                                break
                            elif answer == 2:
                                print("Why am I doing this?")
                                return
                        except ValueError:
                            print("Choose a valid option")
                else:
                    print("There are empty torches across the tunnel, but I don't have something to ignite them")
            elif answer == 4:
                print("You climb the trapdoor and head to the Cauldron Room")
                return
        except ValueError:
            print("Choose a valid action")
#############################
def trapdoor():
    print("It gives the impression that the trapdoor was closed in a hurry...with a bit of effort I could open it.")

    while True:
        print("1. Yeah, why not?")
        print("2. No, leave the trapdoor alone")

        try:
            answer = int(input("Should I open the trapdoor?"))

            if answer == 1:
                if Status.is_candles_lit:
                    print("It's very dark, glad I carry some candles with me")
                    cauldron_room_tunnel()
                else:
                    print("It's too dark to see what down there...looks dangerous")
            elif answer == 2:
                print("Yeah, better leave the trapdor alone for now")
                return
        except ValueError:
            print("Choose a valid action")
#############################
def room_of_cauldrons():
    global is_room_checked, is_cauldron_clean, is_cabinet_checked
    print("There's a noisy, smelly and dim-lighted small circular room, unlike the others")

    while True:
        print("1. Inspect the room")
        print("2. Inspect the cauldron")
        print("3. Inspect the ingredient's cupboard")
        print("4. Inspect the back of the room")
        print("5. Leave to the Corridor")

        try:
            answer = int(input("Well, what do we do?"))

            if answer == 1:
                print("The room's pretty small and not well lighted...it has a second floor and noise coming from above")
                is_room_checked = True
            elif answer == 2:
                if is_cauldron_clean and has_item('Rusty Eagle Key'):
                    print("It looks amazing and smells so good I bet that key could be cleaned here")
                    print("Efectivelly, the RUSTY EAGLE KEY is now clean and devoid of rust!")
                    remove_item('Rusty Eagle Key')
                    add_item('Eagle Key')
                    print("'Eagle Key' obtained!")
                elif is_cauldron_clean:
                    print("Smells so nice...I bet almost anything could be cleansed here")
                elif has_item('Ghoul Eye'):
                    print("Hey! I heard that GHOUL EYE can completelly clean cauldrons or wounds")
                    print("You use 'Ghoul Eye' to clean and cold up the cauldron")
                    remove_item('Ghoul Eye')
                    is_cauldron_clean = True
                    print("The center cauldron is now cleand and cold with a blueish halo")
                else:
                    print("The cauldron at the center of the room is warm with boiling rust...maybe someone used it not long ago?")
            elif answer == 3:
                if is_cabinet_checked:
                    print("Nothing of interest here")
                elif has_item('Cabinet Key'):
                    print("The cabinet opens and there's a shining thing among the unorganized materials")
                    remove_item('Cabinet Key')
                    add_item('Rusty Eagle Key')
                    print("'Rusty Eagle Key' obtained!")
                    is_cabinet_checked = True
                else:
                    print("It's closed")
            elif answer == 4:
                if is_room_checked:
                    print("The room pretty filled with all kind of things, looks very messy")
                    print("Hey! behind the clutter there's what seems to be a trapdoor badly closed")
                    trapdoor()
                else:
                    print("The room pretty filled with all kind of things, looks very messy")
            elif answer == 5:
                print("You leave to the corridors")
                return
        except ValueError:
            print("Choose a valid action")
#######################################
room_of_cauldrons()