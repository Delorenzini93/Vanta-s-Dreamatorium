from inventory import add_item, remove_item, has_item
import Status
import Gorge
is_offering_taken = False
is_cross_obtained = False

#########################
def sanctuary():
    global is_offering_taken, is_cross_obtained
    Status.current_room = "mountainside"

    print("\nYou step into a quiet, circular chamber.")
    print("The air is still and strangely warm compared to the gorge.")
    print("In the center stands a stone altar with two distinct sections:")
    print("one for offerings, and one marked with ancient ritual symbols.")

    while True:
        print("\n1. Examine the offering")
        print("2. Examine the ritual")
        print("3. Fish in the sanctuary pond")
        print("4. Check inventory")
        print("5. Go back to the gorge")

        try:
            answer = int(input("This place feels sacred... "))

            if answer == 1:
                if not is_offering_taken:
                    print("\nOn the left side of the altar rests a long, sheathed blade.")
                    print("The scabbard is worn, but the weapon itself still holds a sharp presence.")
                    add_item("Katana")
                    print("You obtained 'KATANA'!")
                    Status.current_weapon = "Katana"
                    Status.player_attack += 35
                    print(f"Attack increased! ({Status.player_attack})")
                    print("You equipped the Katana.")
                    is_offering_taken = True
                else:
                    print("\nThe offering place is empty now.")

            elif answer == 2:
                if is_cross_obtained:
                    print("\nThe ritual has already been completed.")
                elif Gorge.is_autumn_guardian and Gorge.is_winter_guardian and Gorge.is_spring_guardian:
                    print("\nThe ritual symbols begin to glow faintly as you approach.")
                    print("The three Guardians' acceptance resonates through the chamber.")
                    print("A radiant object materializes above the altar.")
                    add_item("Cross of Enix")
                    print("You obtained 'CROSS OF ENIX'!")
                    is_cross_obtained = True
                else:
                    print("\nThe ritual symbols remain dull and lifeless.")
                    print("Something is still missing...")
                    print("Perhaps the Guardians have not all been appeased.")

            elif answer == 3:
                import fishing
                fishing.fish("pond_3")
            elif answer == 4:
                from inventory import show_inventory
                show_inventory()

            elif answer == 5:
                print("You leave the Sanctuary and return to the gorge.")
                return

        except ValueError:
            print("Choose a valid action.")
##############
sanctuary()