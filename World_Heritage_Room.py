from inventory import add_item, remove_item, has_item
import Status
import os


def world_heritage_room():
    os.system('cls')
    Status.current_room = "west_hall"

    if Status.heritage_choice is not None:
        print("\nThe room is completely empty now.")
        print("Only soft dust floats in the still air.")
        print("Whatever was once worth preserving has already been decided.")
        input("\nPress Enter to leave...")
        return

    print("\nYou step into a quiet, circular chamber.")
    print("The air feels heavy, as if the room itself is holding its breath.")
    print("In the center, three objects rest on separate stone pedestals.")
    print("A soft voice, almost like a memory, speaks:")
    print()
    print('"Only one may remain."')
    print('"The others will be forgotten."')
    print()

    while True:
        print("1. Examine the Child's Drawing")
        print("2. Examine the Broken Music Box")
        print("3. Examine the Unsent Letter")
        print("4. Leave without choosing")

        try:
            answer = int(input("\nWhat will you preserve? "))

            if answer == 1:
                print("\nA child's drawing, done in messy crayon.")
                print("It shows a family holding hands under a black sun.")
                print("On the back, written in small letters: \"Don't forget us.\"")
                print()
                print("1. Preserve this")
                print("2. Look at the others")

                choice = int(input("> "))
                if choice == 1:
                    confirm_choice("Child's Drawing")
                    return

            elif answer == 2:
                print("\nA small wooden music box. The lid is cracked.")
                print("When you touch it, it plays a few distorted, fragile notes.")
                print("Inside the lid is a lock of hair and the words: \"For when you get back.\"")
                print()
                print("1. Preserve this")
                print("2. Look at the others")

                choice = int(input("> "))
                if choice == 1:
                    confirm_choice("Broken Music Box")
                    return

            elif answer == 3:
                print("\nA yellowed letter, never sealed, never sent.")
                print("The ink on the last line still looks slightly wet:")
                print("\"I was never brave enough to give this to you.\"")
                print()
                print("1. Preserve this")
                print("2. Look at the others")

                choice = int(input("> "))
                if choice == 1:
                    confirm_choice("Unsent Letter")
                    return

            elif answer == 4:
                print("\nYou step away from the pedestals.")
                print("The room remains silent, waiting.")
                return

        except ValueError:
            print("Choose a valid action.")


def confirm_choice(chosen):
    print(f"\nYou place your hand on the {chosen}.")
    print("The other two objects begin to crumble into fine ash.")
    print("In a few moments, they are gone.")
    print()
    print("The room grows still.")
    print("Only one thing remains.")

    Status.heritage_choice = chosen
    print(f"\nYou have chosen to preserve: {chosen}")
    input("\nPress Enter to continue...")