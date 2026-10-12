from inventory import add_item, remove_item, has_item
import Status
import os

is_vent_searched = False

def castle_tunnels():
    global is_vent_searched
    os.system('cls')
    Status.current_room = "castle_tunnels"

    print("\nYou crawl into the dark ventilation duct.")
    print("The space is extremely tight. You can barely move forward on your elbows and knees.")
    print("Metal walls press against your shoulders and the air is stale and warm.")

    while True:
        print("1. Search the duct")
        print("2. Climb up to the small roof")
        print("3. Crawl toward the King's chamber")
        print("4. Go back to the spare room")
        print("5. Check inventory")

        try:
            answer = int(input("The metal creaks under your weight... "))

            if answer == 1:
                if not is_vent_searched:
                    print("\nYou feel around in the darkness.")
                    print("Your hand touches something cold and metallic.")
                    add_item("Old Screwdriver")
                    print("You obtained 'OLD SCREWDRIVER'!")
                    is_vent_searched = True
                else:
                    print("\nThere's nothing else here.")

            elif answer == 2:
                small_roof()

            elif answer == 3:
                near_kings_chamber()

            elif answer == 4:
                print("\nYou struggle backwards through the duct...")
                print("After a while, you drop back into the spare room.")
                import Spare_Room
                Spare_Room.spare_room()
                return

            elif answer == 5:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")


def small_roof():
    print("\nYou push open a loose metal grate and climb onto a small, flat roof.")
    print("The cold night air hits your face.")
    print("There's an old chimney here, and a good view of the castle grounds.")

    while True:
        print("\n1. Look around")
        print("2. Use the chimney")
        print("3. Climb back into the duct")
        print("4. Check inventory")

        try:
            answer = int(input("> "))

            if answer == 1:
                print("\nFrom up here you can see part of the courtyard and the distant mountains.")
                print("The wind is strong.")

            elif answer == 2:
                if Status.is_firework_used:
                    print("\nYou already sent the firework earlier.")
                    print("The chimney is still slightly warm.")
                elif has_item("Firework"):
                    print("\nYou carefully place the Firework inside the chimney and light it.")
                    print("A loud whistle rises into the sky, followed by a bright explosion of light.")
                    print("Somewhere in the castle, bells begin to ring...")
                    print("Special goods will now be prepared for newborn babies.")
                    remove_item("Firework")
                    Status.is_firework_used = True
                else:
                    print("\nThere's nothing useful to put in the chimney right now.")

            elif answer == 3:
                print("You climb back down into the ventilation duct.")
                return

            elif answer == 4:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")


def near_kings_chamber():
    if Status.is_gargoyle_password:
        print("\nYou've already overheard the secret from this place.")
        print("There's no reason to return.")
        return

    print("\nYou crawl through a narrower section of the duct.")
    print("After a while, you reach a grate that overlooks a luxurious room.")
    print("You are right above the King's private chambers.")

    print("\nTwo maids are speaking quietly below:")
    print('"Remember the phrase... the gargoyle only responds to it."')
    print('"Yes, yes... keep it secret."')
    print('"Keep your voice down!"')

    print("\nYou quietly listen and memorize what they said.")
    Status.is_gargoyle_password = True
    print("You now know the gargoyle's password.")
    return