from inventory import add_item, remove_item, has_item
import Status

come_from_trophies_room = False
is_sword_taken = False

def upside_down_room1():
    print("There's definitely an eerie feeling in here....there's a present silence in this room")

    while True:
        print("1. Move forward")
        print("2. Move either side")
        print("3. Move backwards")

        try:
            answer = int(input("Where do we go?"))

            if answer == 1:
                print("")
                pass
            elif answer == 2:
                print("")
                pass
            elif answer == 3:
                print("You go back to the dungeons")
        except ValueError:
            print("Choose a valid action")
#######################################
def upside_down_room2():
    pass
#######################################
def upside_down_room3():
    pass
#######################################
def upside_down_room4():
    global is_sword_taken
    print("There's definitely an eerie feeling in here....there's a present silence in this room")

    while True:
        print("1. Move forward")
        print("2. Move either side (sword)")
        print("3. Enter the Trophies Room")

        try:
            answer = int(input("Evom ew od erehw?"))

            if answer == 1:
                print("The wall is too high to climb it")
            elif answer == 2:
                if not is_sword_taken:
                    print("You found a BROADSWORD!")
                    add_item('Broadsword')
                    Status.current_weapon = "Broadsword"
                    Status.player_attack += 10
                    print(f"Attack increased! ({Status.player_attack})")
                    print("You equipped Broadsword!")
                    is_sword_taken = True
                else:
                    print("You already have the Broadsword equipped.")
            elif answer == 3:
                print("You head to the Trophies Room")
                return
        except ValueError:
            print("Choose a valid action")
########################
def where_to_start():
    global come_from_trophies_room
    while True:
        if come_from_trophies_room:
            upside_down_room4()
        else:
            upside_down_room1()
########################
where_to_start()