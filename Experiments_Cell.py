from inventory import add_item, remove_item, has_item
import Status
import os

def experiments_cell():
    os.system('cls')
    Status.current_room = "royal_dungeons"

    print("\nYou push open a heavy metal door and step inside.")
    print("The temperature drops immediately.")
    print("White tiles cover the walls and floor, though most are cracked or stained yellow-brown.")
    print("A sharp chemical smell hangs in the air, mixed with something older and organic.")
    print()
    print("This place was not meant for prisoners.")
    print("It was meant for study.")

    while True:
        print("\n1. Examine the metal table")
        print("2. Inspect the broken glass tubes")
        print("3. Look at the wall charts")
        print("4. Listen")
        print("5. Leave the cell")

        try:
            answer = int(input("\nThe silence here feels artificial... "))

            if answer == 1:
                print("\nA long metal table stands in the center of the room.")
                print("Thick leather restraints hang from its sides, worn and darkened.")
                print("Deep scratches mark the surface — some of them look like they were made from the inside.")
                print("Whatever was held here did not stay still.")

            elif answer == 2:
                print("\nRows of tall glass tubes line the far wall.")
                print("Most are shattered. A few still contain cloudy liquid.")
                print("In one of the unbroken tubes, something dense floats near the bottom.")
                print("It looks vaguely like a spine... or the beginning of one.")

            elif answer == 3:
                print("\nFaded charts and diagrams are pinned to the wall.")
                print("Most are torn or burned, but a few phrases remain readable:")
                print()
                print("\"Subject rejects royal blood integration\"")
                print("\"Instability after 12th exposure\"")
                print("\"Do not allow contact with pure lineage\"")
                print("\"Next phase: adaptive combat forms\"")
                print()
                print("In the corner of one page, a rough sketch shows elongated limbs and too many joints.")

            elif answer == 4:
                print("\nYou stand completely still and listen.")
                print("At first there is nothing.")
                print("Then — very faintly — a wet, rhythmic sound, like something breathing through liquid.")
                print("It stops the moment you move.")

            elif answer == 5:
                print("You step back into the corridor, closing the metal door behind you.")
                print("The chemical smell follows you for several steps.")
                return

            else:
                print("Choose a valid action.")

        except ValueError:
            print("Choose a valid action.")