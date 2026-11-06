from inventory import add_item, remove_item, has_item
import Status
import os
import time
def royal_court():
    os.system('cls')
    Status.current_room = "royal_court"

    if not Status.is_royal_court_intro_played:
        royal_court_intro()
    else:
        royal_court_normal()


def royal_court_intro():
    print("\nYou step into the Royal Court.")
    print("Tall stained-glass windows cast colored light across the polished floor.")
    print("Nobles stand in tense silence. Guards line the walls.")
    print()
    print("A heavy door opens.")
    print("The King enters, carrying a small child in his arms.")
    print("The court immediately kneels.")
    print()
    print("King: \"Today we present the future of this kingdom.\"")
    print("King: \"My blood. My heir.\"")
    print()
    print("He raises the child for everyone to see.")
    print("The baby begins to cry.")
    print("For a moment, everything feels wrong...")
    print()

    input("Press Enter to continue...")

    print("\n...and then everything stops.")
    time.sleep(1.5)
    os.system('cls')

    import Limbo
    Limbo.sequence_1()

    Status.is_royal_court_intro_played = True
    royal_court_normal()


def royal_court_normal():
    os.system('cls')
    print("\nYou are standing in the Royal Court.")
    print("The atmosphere is heavy. Something has clearly gone wrong.")
    print("The King looks disturbed. The nobles are whispering.")

    while True:
        print("\n1. Approach the King")
        print("2. Listen to the nobles")
        print("3. Examine the hall")
        print("4. Go through the side door")
        print("5. Check inventory")

        try:
            answer = int(input("> "))

            if answer == 1:
                print("\nThe King stares at the child in his arms with a troubled expression.")
                print("He does not seem ready to speak to you.")
            elif answer == 2:
                print("\nThe nobles are murmuring nervously.")
                print("You catch fragments: \"the blood...\", \"impossible...\", \"the ceremony...\"")
            elif answer == 3:
                print("\nThe court feels different now, as if the earlier moment cracked something.")
            elif answer == 4:
                print("You leave the Royal Court and head into the Royal Halls.")
                import Royal_Hall
                Royal_Hall.royal_hall()
            elif answer == 5:
                from inventory import show_inventory
                show_inventory()
            else:
                print("Choose a valid action.")

        except ValueError:
            print("Choose a valid action.")