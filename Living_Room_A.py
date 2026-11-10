from inventory import add_item, remove_item, has_item
import Status
import os


def living_room_a():
    os.system('cls')
    Status.current_room = "royal court"

    print("\nYou step into Living Room A.")
    print("Elegant but decaying furniture fills the space.")
    print("Several skeletons sit formally on the sofas and armchairs,")
    print("as if still attending a gathering that never properly ended.")
    print("They remain perfectly still.")

    if Status.living_room_a_cleared:
        print("\nThe room is empty now.")
        print("Only the faint smell of extinguished candles remains.")

        while True:
            print("\n1. Go back to Hall 1")
            print("2. Continue to Hall 2")

            try:
                answer = int(input("> "))
                if answer == 1:
                    print("You return to the first Royal Hall.")
                    return
                elif answer == 2:
                    print("You continue deeper into the castle...")
                    import Royal_Hall_2
                    Royal_Hall_2.royal_hall_2()
                    return
                else:
                    print("Choose a valid action.")
            except ValueError:
                print("Choose a valid action.")
    while True:
        print("\n1. Place the candles")
        print("2. Examine the skeletons")
        print("3. Look around the room")
        print("4. Go back to Hall 1")
        print("5. Check inventory")

        try:
            answer = int(input("> "))

            if answer == 1:
                if (has_item("Candle of Dawn") and
                        has_item("Candle of Dusk") and
                        has_item("Candle of Threshold")):

                    print("\nYou place the three candles on the low table in the center of the room.")
                    print("One by one, you light them.")
                    print()
                    print("The skeletons slowly turn their skulls toward the light.")
                    print("One of them somehow tips an invisible hat.")
                    print("Then, in perfect silence, they stand up in unison")
                    print("and file out of the room in an orderly line.")
                    print()
                    print("Living Room A is now clear.")

                    remove_item("Candle of Dawn")
                    remove_item("Candle of Dusk")
                    remove_item("Candle of Threshold")
                    Status.living_room_a_cleared = True
                    return
                else:
                    print("\nYou do not have all three candles yet.")
                    print("The skeletons continue to sit in polite, expectant silence.")

            elif answer == 2:
                print("\nThe skeletons are dressed in old formal wear.")
                print("They look more bored than threatening.")
                print("One of them appears to be tapping a bony finger against the armrest,")
                print("as if waiting for the evening to finally begin.")

            elif answer == 3:
                print("\nFaded paintings hang slightly crooked on the walls.")
                print("A thick layer of dust covers most surfaces.")
                print("This room has been waiting for a very long time.")

            elif answer == 4:
                print("You return to the first Royal Hall.")
                return

            elif answer == 5:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")