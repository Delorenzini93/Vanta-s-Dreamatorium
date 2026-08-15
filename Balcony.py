from inventory import add_item, remove_item, has_item

def balcony():
    print("The balcony overlooks nothing but thick fog.")
    print("There is a single old armchair and a small table.")

    while True:
        print("\n1. Sit in the chair")
        print("2. Look at the table")
        print("3. Leave the balcony")

        try:
            answer = int(input("\nWhat should we do? "))

            if answer == 1:
                print("\nNo thoughts pass through your mind right now.")
                print("\n1. Stand up")
                print("2. Remain in the chair")

                try:
                    chair_answer = int(input("\nA distant breeze dances on the horizon. "))

                    if chair_answer == 1:
                        print("\nYou stand up.")
                        continue

                    elif chair_answer == 2:
                        print("\nA long forgotten memory forms in your mind:")
                        print("'A lady with a flower, an old man holding a pocket watch,")
                        print("a stubborn child playing a piano...'")
                        #main_hall_info = True
                        continue

                    else:
                        print("Please choose 1 or 2.")

                except ValueError:
                    print("Please enter a number.")

            elif answer == 2:
                print("\nThere's a letter addressed to no one, beside a frozen pocket watch:")
                print("'I waited for the sunrise that never came.")
                print("The music was the only thing that still moved.")
                print("Play it the way we used to, and the door will remember.'")

                if not has_item("Pocket Watch"):
                    add_item("Pocket Watch")
                else:
                    print("\nThere's nothing left on the table.")

            elif answer == 3:
                print("\nYou leave the balcony.")
                return

            else:
                print("Please choose a number between 1 and 3.")

        except ValueError:
            print("Please enter a number.")

balcony()