from inventory import add_item, remove_item, has_item
import Status
import os

def trial_dungeon():
    os.system('cls')
    Status.current_room = "trial_dungeon"

    print("\nYou enter a wide, cold chamber.")
    print("Stone benches face a raised platform.")
    print("The air is still, as if the room itself is waiting.")
    print("A single chair stands in the center, facing the platform.")
    print()
    print("This place was made for judgment.")

    while True:
        print("\n1. Sit in the chair")
        print("2. Examine the platform")
        print("3. Look at the benches")
        print("4. Leave the Trial Dungeon")

        try:
            answer = int(input("\nThe silence feels expectant... "))

            if answer == 1:
                if Status.trial_dungeon_completed:
                    print("\nThe chair is cold and silent. The record has already been made.")
                    return
                else:
                    begin_judgment()
            elif answer == 2:
                print("\nThe platform is empty.")
                print("No throne, no desk — only a flat stone surface.")
                print("Whoever judged others here preferred to remain unseen.")
            elif answer == 3:
                print("\nThe benches are worn smooth.")
                print("Many people once sat here to watch someone be measured.")
            elif answer == 4:
                print("You leave the chamber of judgment.")
                return
            else:
                print("Choose a valid action.")

        except ValueError:
            print("Choose a valid action.")


def begin_judgment():
    print("\nYou sit in the chair.")
    print("For a moment, nothing happens.")
    print("Then a calm, distant voice fills the room.")
    print("It has no clear origin.")
    print()

    print("Voice: \"You have entered the place of record.\"")
    print("Voice: \"Two marks have been left upon you.\"")
    print()

    if Status.heritage_choice is None:
        print("Voice: \"You preserved nothing.\"")
        print("Voice: \"When given the chance to choose what should remain, you refused.\"")
    else:
        print(f"Voice: \"You chose to preserve the {Status.heritage_choice}.\"")
        if Status.heritage_choice == "Child's Drawing":
            print("Voice: \"A fragile image of belonging.\"")
        elif Status.heritage_choice == "Broken Music Box":
            print("Voice: \"A broken promise of return.\"")
        elif Status.heritage_choice == "Unsent Letter":
            print("Voice: \"Words that were never given.\"")

    print()

    if Status.is_ghost_hostile:
        print("Voice: \"You disturbed what should have been left sleeping.\"")
        print("Voice: \"The presence in the Ballroom now knows your name.\"")
    else:
        print("Voice: \"You walked through the Ballroom without fully waking what lives there.\"")
        print("Voice: \"That restraint has been noted.\"")

    print()
    print("Voice: \"These marks will remain.\"")
    print("Voice: \"That is all.\"")
    print()
    print("The voice fades.")
    print("The room returns to silence.")

    input("\nPress Enter to stand up...")
    Status.trial_dungeon_completed = True