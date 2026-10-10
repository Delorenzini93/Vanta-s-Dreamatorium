from inventory import add_item, remove_item, has_item
import Status
import os

is_spring_anima_taken = False
sequence = []
correct_order = ["seed", "bud", "leaf", "flower"]
is_puzzle_solved = False

def botanical_classroom():
    os.system('cls')
    Status.current_room = "west hall"
    global is_spring_anima_taken, sequence, is_puzzle_solved

    print("\nYou enter a spacious botanical classroom.")
    print("High glass ceilings let pale light filter through cracks and climbing vines.")
    print("Long wooden tables are covered in dried leaves, broken pots, and yellowed notes.")
    print("In the center of the room stands a circular stone platform with four large plant sculptures.")

    while True:
        print("\n1. Examine the blackboard")
        print("2. Examine the four plant sculptures")
        print("3. Interact with the sculptures")
        print("4. Search the tables")
        print("5. Check inventory")
        if is_puzzle_solved:
            print("6. Go to the patio")
        else:
            print("6. Go to the patio (locked)")
        print("7. Leave the classroom")

        try:
            answer = int(input("The air smells of old soil and dried petals... "))

            if answer == 1:
                print("\nThe blackboard is covered in faded chalk writing:")
                print('"Life begins hidden in the dark."')
                print('"Then it breaks the surface, seeking light."')
                print('"It spreads and grows strong."')
                print('"Finally, it opens itself to the world."')
                print("Someone underlined the words: HIDDEN → SURFACE → GROWS → OPENS")

            elif answer == 2:
                print("\nThere are four sculptures arranged in a circle:")
                print("- A closed Seed")
                print("- A small Bud")
                print("- A broad Leaf")
                print("- A fully open Flower")
                print("Each one has a small indentation, as if it can be pressed.")

            elif answer == 3:
                if is_puzzle_solved:
                    print("\nThe sculptures no longer respond.")
                    print("The cycle has already been completed.")
                    continue

                print("\nWhich sculpture do you want to activate?")
                print("1. Seed")
                print("2. Bud")
                print("3. Leaf")
                print("4. Flower")
                print("5. Never mind")

                choice = int(input("> "))

                if choice == 1:
                    print("You press the Seed sculpture. It clicks softly.")
                    sequence.append("seed")
                elif choice == 2:
                    print("You press the Bud sculpture. It clicks softly.")
                    sequence.append("bud")
                elif choice == 3:
                    print("You press the Leaf sculpture. It clicks softly.")
                    sequence.append("leaf")
                elif choice == 4:
                    print("You press the Flower sculpture. It clicks softly.")
                    sequence.append("flower")
                elif choice == 5:
                    continue
                else:
                    print("Invalid choice.")
                    continue

                if sequence == correct_order[:len(sequence)]:
                    if sequence == correct_order:
                        print("\nAll four sculptures glow faintly in sequence.")
                        print("A soft green light rises from the center of the platform...")
                        print("The Spring Anima materializes before you.")
                        add_item("Spring Anima")
                        print("You obtained 'SPRING ANIMA'!")
                        is_spring_anima_taken = True
                        is_puzzle_solved = True
                        sequence = []
                else:
                    print("\nThe sculptures let out a dull, wrong sound.")
                    print("The sequence resets.")
                    sequence = []

            elif answer == 4:
                print("\nYou search through the dried plants and old notes on the tables.")
                print("Most of it is useless, but one torn page catches your eye:")
                print('"The order of life must be respected, or nothing will bloom."')

            elif answer == 5:
                from inventory import show_inventory
                show_inventory()


            elif answer == 6:
                if is_puzzle_solved:
                    print("\nThe large glass doors at the back of the classroom slowly open.")
                    print("A soft breeze carries the scent of fresh grass...")
                    import Patio
                    Patio.patio()
                else:
                    print("\nThe glass doors leading to the patio are sealed shut.")
                    print("They won't open until the cycle is completed.")

            elif answer == 7:
                print("You leave the botanical classroom.")
                return

        except ValueError:
            print("Choose a valid action.")