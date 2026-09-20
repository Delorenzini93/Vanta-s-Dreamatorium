from inventory import add_item, remove_item, has_item
import Status
import battle

come_from_trophies_room = False
is_sword_taken = False
dragon_switch_up = False
mermaid_switch_down = False
sphinx_switch_down = False
is_family_crest_puzzle = False

########################
def ghost_jester_battle():
        result = battle.battle(
            enemy_name="Ghost Jester",
            enemy_hp=250,
            enemy_attack=30
        )

        if result:
            print("The Jester went away....for now")
            return
        else:
            print("GAME OVER")
            return
########################
def upside_down_room1():
    global dragon_switch_up
    print("There's definitely an eerie feeling in here....there's a present silence in this room")

    while True:
        print("1. Move forward")
        print("2. Move either side")
        print("3. Move backwards")
        print("4. Check inventory")

        try:
            answer = int(input("Where do we go?"))

            if answer == 1:
                print("You move to the middle of the room")
                upside_down_room2()
            elif answer == 2:
                print("There's switch with a dragon carved on it")
                while True:
                    print("1. Put the dragon in waking position")
                    print("2. Put the dragon in death position")
                    print("3. Leave the dragon in sleeping position")

                    try:
                        answer = int(input(""))
                        if answer == 1:
                            print("The Dragon on the switch is awake")
                            dragon_switch_up = True
                        elif answer == 2:
                            print("The Dragon on the switch is dead")
                            dragon_switch_up = False
                        elif answer == 3:
                            print("You leave the dragon on the switch sleeping for now")
                            return
                    except ValueError:
                        print("Choose a valid action")
            elif answer == 3:
                print("You go back to the dungeons")
                return
            elif answer == 4:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
#######################################
def upside_down_room2():
    global mermaid_switch_down
    print("There are many what seems to be kid's drawings covering the walls in this part of the room")

    while True:
        print("1. Move forward")
        print("2. Move either side")
        print("3. Move backwards")
        print("4. Check inventory")

        try:
            answer = int(input("Where do we go?"))

            if answer == 1:
                print("You move to the final section of the room")
                upside_down_room3()
            elif answer == 2:
                print("There's switch with a mermaid carved on it")
                while True:
                    print("1. Put the mermaid in surface position")
                    print("2. Put the mermaid in drowning position")
                    print("3. Leave the mermaid in sleeping position")

                    try:
                        answer = int(input(""))
                        if answer == 1:
                            print("The Mermaid on the switch is waving at sailors")
                            mermaid_switch_down = False
                        elif answer == 2:
                            print("The Mermaid on the switch is drowned at the lake's bottom")
                            mermaid_switch_down = True
                        elif answer == 3:
                            print("You leave the mermaid on the switch sleeping for now")
                            return
                    except ValueError:
                        print("Choose a valid action")
            elif answer == 3:
                print("You go back to first section of the room")
                return
            elif answer == 4:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
#######################################
def upside_down_room3():
    global dragon_switch_up, mermaid_switch_down, sphinx_switch_down, is_family_crest_puzzle
    print("There is a considerable amount of paintings depicting people with different illnesses...I dont like this room")

    while True:
        print("1. Touch the Family Crest")
        print("2. Move either side")
        print("3. Move backwards")
        print("4. Check inventory")

        try:
            answer = int(input("Where do we go?"))

            if answer == 1:
                if dragon_switch_up and mermaid_switch_down and sphinx_switch_down:
                    print("The wall crumbles revealing a hidden section of the room where the furniture hangs from the ceiling")
                    print("A shining pendant falls on the floor near you")
                    add_item('Mythril Necklace')
                    print('You obtain MYTHRIL NECKLACE!')
                    is_family_crest_puzzle = True
                    upside_down_room4()
                else:
                    print("A fainting scream wails through the walls piercing your ears")
                    print("An entity appears!")
                    ghost_jester_battle()
            elif answer == 2:
                print("There's switch with a Sphinx carved on it")
                while True:
                    print("1. Put the Sphinx in waking position")
                    print("2. Put the Sphinx in defensive position")
                    print("3. Leave the Sphinx in sleeping position")

                    try:
                        answer = int(input(""))
                        if answer == 1:
                            print("The Sphinx on the switch is smiling enigmatically")
                            sphinx_switch_down = False
                        elif answer == 2:
                            print("The Sphinx on the switch is menacingly on her feet")
                            sphinx_switch_down = True
                        elif answer == 3:
                            print("You leave the Sphinx on the switch sleeping for now")
                            return
                    except ValueError:
                        print("Choose a valid action")
            elif answer == 3:
                print("You go back to middle section of the room")
                return
            elif answer == 4:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
#######################################
def upside_down_room4():
    global is_sword_taken, is_family_crest_puzzle
    print("There's definitely an eerie feeling in here....there's a present silence in this room")

    while True:
        print("1. Move forward")
        print("2. Move either side (sword)")
        print("3. Enter the Trophies Room")
        print("4. Check inventory")

        try:
            answer = int(input("Evom ew od erehw?"))

            if answer == 1:
                if is_family_crest_puzzle:
                    print("You go to the room with the unpleasant paintings")
                    upside_down_room3()
                else:
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
            elif answer == 4:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
########################
def where_to_start():
    if come_from_trophies_room:
        upside_down_room4()
    else:
        upside_down_room1()
########################
where_to_start()