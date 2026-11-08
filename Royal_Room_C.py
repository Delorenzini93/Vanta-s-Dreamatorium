from inventory import add_item, remove_item, has_item
import Status
import os

is_candle_threshold_taken = False

def royal_room_c():
    global is_candle_threshold_taken
    os.system('cls')
    Status.current_room = "royal_court"

    print("\nYou enter a room lined with tall, old mirrors.")
    print("Your reflections stretch into the distance, slightly delayed.")
    print("In the center stand four animal statues arranged in a circle:")
    print("a Wolf, a Crow, a Serpent, and a Stag.")

    while True:
        print("\n1. Read the inscription")
        print("2. Examine the statues")
        print("3. Attempt the sequence")
        print("4. Leave the room")
        print("5. Check inventory")

        try:
            answer = int(input("> "))

            if answer == 1:
                print("\nThe inscription on the mirror is worn and incomplete:")
                print()
                print("\"One bore the crown before the hunt began.\"")
                print("\"One followed the scent of that pride.\"")
                print("\"One announced the ending from above.\"")
                print("\"One closed the path when all else had passed.\"")
                print()
                print("\"Only those who understand the order of endings may carry the flame between times.\"")

            elif answer == 2:
                print("\nThe statues are finely carved and cold to the touch:")
                print("- The Stag stands tall, head raised")
                print("- The Wolf is frozen mid-step")
                print("- The Crow's wings are half-open")
                print("- The Serpent lies tightly coiled")

            elif answer == 3:
                if is_candle_threshold_taken:
                    print("\nThe candle is already gone.")
                    continue

                print("\nYou must touch the four statues in the correct order.")
                player_sequence = []

                for i in range(1, 5):
                    print(f"\nChoose statue #{i}:")
                    print("1. Stag")
                    print("2. Wolf")
                    print("3. Crow")
                    print("4. Serpent")

                    try:
                        choice = int(input("> "))

                        if choice == 1:
                            player_sequence.append("stag")
                        elif choice == 2:
                            player_sequence.append("wolf")
                        elif choice == 3:
                            player_sequence.append("crow")
                        elif choice == 4:
                            player_sequence.append("serpent")
                        else:
                            print("Invalid choice.")
                            break
                    except ValueError:
                        print("Choose a valid action")
                        break
                else:
                    correct_sequence = ["stag", "wolf", "crow", "serpent"]

                    if player_sequence == correct_sequence:
                        print("\nThe statues emit a soft gray light.")
                        print("A pale candle materializes in the center of the circle.")
                        add_item("Candle of Threshold")
                        is_candle_threshold_taken = True
                        print("You obtained 'CANDLE OF THRESHOLD'!")
                    else:
                        print("\nThe statues remain silent.")
                        print("Whatever order you chose was not the correct one.")

            elif answer == 4:
                print("You return to the Royal Hall.")
                return

            elif answer == 5:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")