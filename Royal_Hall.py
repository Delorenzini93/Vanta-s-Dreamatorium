from inventory import add_item, remove_item, has_item
import Status
import os

def royal_hall():
    os.system('cls')
    Status.current_room = "royal_court"

    print("\nYou enter the Royal Hall.")
    print("A long, elegant corridor stretches before you.")
    print("Three doors stand along the left wall.")
    print("On the right, tall windows look out over the castle grounds.")

    while True:
        print("\n1. Open the first door")
        print("2. Open the second door")
        print("3. Open the third door")
        print("4. Look through the window")
        print("5. Run through the corridor")
        print("6. Go back")
        print("7. Check inventory")

        try:
            answer = int(input("\nWhere will you go? "))

            if answer == 1:
                print("You open the first door...")
                import Royal_Room_A
                Royal_Room_A.royal_room_a()

            elif answer == 2:
                print("You open the second door...")
                import Royal_Room_B
                Royal_Room_B.royal_room_b()

            elif answer == 3:
                print("You open the third door...")
                import Royal_Room_C
                Royal_Room_C.royal_room_c()

            elif answer == 4:
                Status.window_look_count += 1
                if Status.window_look_count % 2 == 0:
                    Status.is_daylight = True
                    print("\nSunlight breaks through the clouds.")
                    print("It is now day.")
                else:
                    Status.is_daylight = False
                    print("\nDark clouds gather outside.")
                    print("It is now night.")
            elif answer == 5:
                print("You go past the hall and reach a spacious room")
                import Living_Room_A
                Living_Room_A.living_room_a()
            elif answer == 6:
                print("You leave the Royal Hall.")
                return
            elif answer == 7:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")