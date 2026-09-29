from inventory import add_item, remove_item, has_item
import Status

is_cells_searched = False
is_pit_examined = False
is_body_looted = False

def basement():
    global is_cells_searched, is_pit_examined, is_body_looted

    print("\nYou descend a narrow stone staircase into the Basement.")
    print("The air grows colder and heavier with every step.")
    print("Old iron bars line the walls — the remains of collapsed prison cells.")
    print("In the center of the room lies a wide, dark pit. Something was once thrown down there.")
    print("The silence here is different from the Silent Room... heavier. Older.")

    while True:
        print("\n1. Search the collapsed cells")
        print("2. Examine the dark pit")
        print("3. Inspect the far wall")
        print("4. Leave the Basement")

        try:
            answer = int(input("The cold seems to cling to your skin... "))

            if answer == 1:
                if not is_cells_searched:
                    print("\nYou carefully move between the twisted iron bars.")
                    print("Most of the cells have caved in long ago.")
                    print("In one of the less destroyed ones, you find a skeleton still chained to the wall.")
                    print("Clutched in its bony fingers is a small leather pouch.")
                    add_item("Old Pouch")
                    print("You obtained 'OLD POUCH'!")
                    print("Inside you find a few coins and a strange black tooth.")
                    add_item("Black Tooth")
                    print("You obtained 'BLACK TOOTH'!")
                    is_cells_searched = True
                else:
                    print("\nThere's nothing more left in the cells.")
                    print("Only dust and old iron.")

            elif answer == 2:
                if not is_pit_examined:
                    print("\nYou approach the edge of the pit and look down.")
                    print("Darkness. Absolute and endless.")
                    print("A faint, wet smell rises from below... like old blood and stagnant water.")
                    print("For a moment you swear you hear something shift far below.")
                    print("You step back.")
                    is_pit_examined = True
                else:
                    print("\nThe pit remains silent.")
                    print("Whatever is down there does not call out again.")

            elif answer == 3:
                if not is_body_looted:
                    print("\nAgainst the far wall you notice a shape half-buried under fallen stones.")
                    print("It's another body — this one more recent than the skeletons.")
                    print("A failed explorer, perhaps.")
                    print("You search the remains and find a heavy iron key and a torn note.")
                    add_item("Iron Key")
                    print("You obtained 'IRON KEY'!")
                    print("The note is barely readable:")
                    print('"The deeper you go... the more it listens."')
                    is_body_looted = True
                else:
                    print("\nThe body has already been searched.")
                    print("You leave it in peace.")

            elif answer == 4:
                print("\nYou climb back up the narrow stairs.")
                print("The cold of the Basement slowly releases its grip.")
                return

        except ValueError:
            print("Choose a valid action.")

basement()