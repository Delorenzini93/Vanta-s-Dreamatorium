from Upside_Down_Room import come_from_trophies_room
from inventory import add_item, remove_item, has_item
import Status
import Room_Of_Cauldrons
import Upside_Down_Room



is_trophy_examined = False
is_champion_down = False
is_fairy_book_open = False
is_tunnel_lit = False

def trophy_battle():
    pass
########################################
def trophy_office():
    global is_fairy_book_open
    print("It's a very old room crowded with papers everywhere.Seems like if someone was searching for something in a rush")

    while True:
        print("1. Inspect the office's desk")
        print("2. Go back to the Trophies Room")

        try:
            answer = int(input("This place is an absolute mess..."))

            if answer == 1:
                if is_fairy_book_open:
                    print("Nothing useful here")
                    return
                else:
                    print("There's a notebook with a fairy crest on it.It looks as if someone tried to open it before.")
                    print("It has a mechanism where characters and numbers can be inserted")
                    match input("Enter password: ").strip().lower():
                        case "jim carrey":
                            print("The notebook quietly opens revealing a shiny diamond")
                            add_item("Red Diamond")
                            print("'Red Diamond' obtained!")
                            is_fairy_book_open = True
                        case _:
                            print("The mechanism is tightly shut around the notebook")
                            return
            elif answer == 2:
                print("You leave the messy office")
                return
        except ValueError:
            print("Choose a valid action")
#############################
def hall_of_trophies_back_of_the_room():
    global is_champion_down, is_tunnel_lit
    print("Seems like the back of the room leading to other areas")

    while True:
        print("1. Examine door (forward)")
        print("2. Examine black door (right)")
        print("3. Examine mechanism (left)")
        print("4. Examine trapdoor (floor - left)")
        print("5. Go back at the display cases area")
        print("6. Check inventory")

        try:
            answer = int(input(""))

            if answer == 1:
                if is_champion_down:
                    print("The door leading to the Upside Down Room is now open...")
                    import Upside_Down_Room
                    Upside_Down_Room.come_from_trophies_room = True
                    Upside_Down_Room.upside_down_room4()
                else:
                    print("A special kind of magic is binding the door preventing access")
                    return
            elif answer == 2:
                print("Seem's like an abandoned office of some sort")
                trophy_office()
            elif answer == 3:
                if has_item('Fusibles'):
                    print("The mechanism is now working and the tunnel is now fully illuminated")
                    remove_item('Fusibles')
                    is_tunnel_lit = True
                    return
                elif is_tunnel_lit:
                    print("The mechanism is now working and the tunnel is now fully illuminated")
                else:
                    print("Seems like and old mechanism that activates the lever")
                    print("The mechanism seems to be blown out, maybe I should watch out for FUSIBLES")
            elif answer == 4:
                if is_tunnel_lit:
                    print("You open the trapdoor")
                    Room_Of_Cauldrons.tunnel_second_section()
                else:
                    print("It's electronically shut")
            elif answer == 5:
                print("As you move through the room, hundreds of trophies shine proudly before your eyes")
                hall_of_trophies()
                return
            elif answer == 6:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
###############################
def hall_of_trophies():
    global is_champion_down, is_trophy_examined
    print("You lay before a room so tall and full of trophies that your head gets a little dizzy...")

    while True:
        print("1.Move forward through the room")
        print("2. Examine trophies in the table at the center of the room")
        print("3. Examine display case")
        print("4. Go back from the Oak door")
        print("5. Check inventory")

        try:
            answer = int(input("Everything is so clean and shiny here..."))

            if answer == 1:
                print("As you move through the room, hundreds of trophies shine proudly before your eyes")
                hall_of_trophies_back_of_the_room()
            elif answer == 2:
                if is_champion_down:
                    return
                elif is_trophy_examined:
                    print("The trophy is starting to twist and transform into a knight!")
                    trophy_battle()
                else:
                    print("There's a particular big trophy at the center of the room")
                    is_trophy_examined = True
                    return
            elif answer == 3:
                print("Theo Callaghan, captain of the National Team")
            elif answer == 4:
                print("You go back to the dungeon's corridor")
                return
            elif answer == 5:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
########################
hall_of_trophies()