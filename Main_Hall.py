from inventory import add_item, remove_item, has_item

is_flower_solved = False
is_watch_solved = False
is_blackKey_solved = False


def door_puzzle():
    global is_flower_solved, is_watch_solved, is_blackKey_solved

    print("\nThere's an ancient and rusty door with peculiar ornaments around it.")
    print("There's the symbol of a flower, a watch and what seems to be a key of some sort.")

    while True:
        print("\n1. Inspect the flower symbol")
        print("2. Inspect the watch symbol")
        print("3. Inspect the key symbol")
        print("4. Try to open the door")
        print("5. Leave the door for now")

        try:
            answer = int(input("\nWhat a strange door... "))

            if answer == 1:
                print("\nThe carving seems to depict a withered flower...")
                if has_item("Silver Flower"):
                    print("The silver flower fits the carving and you hear a distant click...")
                    remove_item("Silver Flower")
                    is_flower_solved = True
                else:
                    print("You feel like something is missing...")

            elif answer == 2:
                print("\nThe carving seems to depict an old man worried about time...")
                if has_item("Pocket Watch"):
                    print("The pocket watch fits the carving and you hear a distant sigh of relief...")
                    remove_item("Pocket Watch")
                    is_watch_solved = True
                else:
                    print("You feel like something is missing...")

            elif answer == 3:
                print("\nThe carving seems to depict a singing child...")
                if has_item("Black Key"):
                    print("The Black Key fits the carving and you hear a tense chord somewhere...")
                    remove_item("Black Key")
                    is_blackKey_solved = True
                else:
                    print("You feel like something is missing...")

            elif answer == 4:
                if is_flower_solved and is_watch_solved and is_blackKey_solved:
                    print("\nThe door unlocks with a loud and distant noise...")
                    print("You step into the Second Hall.")
                    import Second_Hall
                    return True
                else:
                    print("\nThe door is firmly locked...")

            elif answer == 5:
                print("\nYou step away from the door.")
                return False

            else:
                print("Please choose a number between 1 and 5.")

        except ValueError:
            print("Please enter a number.")


def main_hall():
    print("An spacious and ancient hall lies before you.")
    print("The ceiling is so high that only fog is visible from beneath.")

    while True:
        print("\n1. Go to the Library")
        print("2. Go to the Garden")
        print("3. Go to the Balcony")
        print("4. Go to the Music Room")
        print("5. Go forward to the ornamented door")
        print("6. Check inventory")

        try:
            answer = int(input("\nWhich door should we open? "))

            if answer == 1:
                print("\nThe door leading to the Library opens.")
                import Small_library
                Small_library.reading_of_books()

            elif answer == 2:
                print("\nThe door leading to the Garden opens.")
                import Garden
                Garden.statues()

            elif answer == 3:
                print("\nThe door leading to the Balcony opens.")
                import Balcony
                Balcony.balcony()

            elif answer == 4:
                print("\nThe door leading to the Music Room opens.")
                import Piano_Room
                Piano_Room.piano_room()

            elif answer == 5:
                door_puzzle()

            elif answer == 6:
                from inventory import show_inventory
                show_inventory()

            else:
                print("Please choose a valid action.")

        except ValueError:
            print("Please enter a number.")


main_hall()