from inventory import add_item, remove_item, has_item
import Status
import os
import random
import Encounters
import time


def left_path():
    os.system('cls')

    print("\nYou step through the Night Door.")
    print("The light dies behind you almost instantly.")
    print("Darkness swallows everything.")
    print("You can barely see your own hands.")
    print("Only sound remains.")
    print()
    print("Something shifts in the black ahead...")
    print("Then another something.")
    print("And another.")

    input("\nPress Enter to begin the descent...")

    night_tunnel()


def night_tunnel():
    stage = 1
    max_stages = 7

    enemy_sounds = [
        "You hear wet claws scraping against stone.",
        "A low, hungry growl echoes very close.",
        "Something laughs in the dark — short and broken.",
        "Heavy footsteps drag across the floor ahead.",
        "A sharp screech cuts through the blackness.",
        "You hear teeth clicking together, many of them.",
        "Breathing. Fast. Excited. Not human."
    ]

    while stage <= max_stages:
        os.system('cls')
        print(f"\n=== NIGHT TUNNEL – STAGE {stage} of {max_stages} ===")
        print("The darkness is almost absolute.")
        print(random.choice(enemy_sounds))
        print()
        print("You have no choice but to keep moving.")
        print()
        print("1. Advance into the darkness")

        try:
            answer = int(input("> "))

            if answer == 1:
                print("\nYou step forward...")
                time.sleep(1)

                won = Encounters.forced_encounter("royal_dungeons")
                if not won:
                    print("GAME OVER")
                    return

                print("\nThe body falls. The tunnel grows quiet again... for now.")
                input("\nPress Enter to continue...")
                stage += 1
            else:
                print("There is no other option here.")

        except ValueError:
            print("You must advance.")


    os.system('cls')
    print("\nThe last creature collapses.")
    print("Silence finally returns.")
    print()
    print("Ahead, a faint outline of a door appears in the darkness.")
    print("You push it open and step through...")
    print()
    print("You have reached the Royal Court.")

    input("\nPress Enter to continue...")

    import Royal_Court
    Royal_Court.royal_court()