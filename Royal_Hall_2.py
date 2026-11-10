from inventory import add_item, remove_item, has_item
import Status
import os

def royal_hall_2():
    os.system('cls')
    Status.current_room = "royal_catacombs"

    print("\nYou enter the second Royal Hall.")
    print("The corridor is narrower and older than the previous one.")
    print("The stone feels colder here. The air is heavier.")
    print("Three doors stand along the left wall.")
    print("Further ahead, two larger archways lead elsewhere.")

    while True:
        print("\n1. Open the first door")
        print("2. Open the second door")
        print("3. Open the third door")
        print("4. Enter the Royal Catacombs")
        print("5. Enter the Royal Garden")
        print("6. Go back to Living Room A")
        print("7. Check inventory")

        try:
            answer = int(input("\nWhere will you go? "))

            if answer == 1:
                print("You open the first door...")
                import Royal_Room_D
                Royal_Room_D.royal_room_d()

            elif answer == 2:
                print("You open the second door...")
                import Royal_Room_E
                Royal_Room_E.royal_room_e()

            elif answer == 3:
                print("You open the third door...")
                import Royal_Room_F
                Royal_Room_F.royal_room_f()

            elif answer == 4:
                if not Status.is_daylight:
                    print("You descend into the Royal Catacombs...")
                    import Royal_Catacombs
                    Royal_Catacombs.royal_catacombs()
                else:
                    print("The catacombs are only accesible during night time")

            elif answer == 5:
                if Status.living_room_a_cleared and Status.living_room_b_cleared:
                    print("The way into the Royal Garden is open.")
                    import Royal_Garden
                    Royal_Garden.royal_garden()
                else:
                    print("The entrance to the Royal Garden is sealed.")
                    print("A faint inscription reads:")
                    print("\"Only when both halls of the waiting dead are emptied may the garden open.\"")

            elif answer == 6:
                print("You return to Living Room A.")
                return

            elif answer == 7:
                from inventory import show_inventory
                show_inventory()

            else:
                print("Choose a valid action.")

        except ValueError:
            print("Choose a valid action.")