from inventory import add_item, remove_item, has_item

def piano_room():
    print("The room is dim, the piano is old and slightly out of tune with 5 drawings on it." 
          "\nOn the music stand sits a blank sheet of staff paper with only the title written in elegant handwriting:"
          "\n'The Night That Never Ended'")

    while True:
        print("\n1. Read 'The Night That Never Ended.")
        print("2. Play the piano.")
        print("3. Leave the room")

        try:
            answer = int(input("\nWhat should we do here? "))

            if answer == 1:
                print("\nA lonely Cavallier went into the night"
                      "\nin search for a lost Dream,"
                      "\nsharply above"
                      "\nand through the Fire,"
                      "\nhe found Glory.")
                continue

            elif answer == 2:
                piano_puzzle()
                continue

            elif answer == 3:
                print("\nYou leave the Piano room.")
                return

            else:
                print("Please choose a number between 1 and 3.")

        except ValueError:
            print("Please enter a number.")

def piano_puzzle():
    correct_melody = [1, 3, 4, 6, 8]
    player_melody = []

    print("\nEnter the number of each note one by one.")

    for i in range(5):
        while True:
            print("1. C   2. C#  3. D   4. D#  5. E   6. F")
            print("7. F#  8. G   9. G# 10. A  11. A# 12. B")

            try:
                note = int(input(f"Note {i+1}/5: "))
                if 1 <= note <= 12:
                    player_melody.append(note)
                    break
                else:
                    print("Please choose a number between 1 and 12.")
            except ValueError:
                print("Please enter a number.")

    if player_melody == correct_melody:
        print("\nThe correct melody resonates through the room...")
        print("A hidden compartment in the piano slowly opens.")
        add_item("Black Key")
        return True
    else:
        print("\nThe notes sound wrong... the piano remains silent.")
        print("You should try again later.")
        return False

piano_room()