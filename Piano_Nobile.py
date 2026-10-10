from inventory import add_item, remove_item, has_item
import Status
import os

def piano_nobile():
    os.system('cls')
    Status.current_room = "west_hall"

    print("\nThe second floor has a distinct French style")
    print("A short hall, with 3 doors at your left side and windows overlooking the mountains at your right side")

    while True:
        print("1. Open first door")
        print("2. Open second door")
        print("3. Open third door")
        print("4. Advance through the hall")
        print("5. Go back downstairs")
        print("6. Check inventory")

        try:
            answer = int(input(""))
            if answer == 1:
                print("You enter through the first door")
                import West_Hall_Store
                West_Hall_Store.west_hall_store()
            elif answer == 2:
                print("You enter through the second door")
                import Ton_Room
                Ton_Room.ton_room()
            elif answer == 3:
                print("You enter through the third door")
                import Zon_Room
                Zon_Room.zon_room()
            elif answer == 4:
                print("You run along the hall and reach the Third Hall's second floor")
                import Third_Floor_2F
                Third_Floor_2F.third_floor_2F()
            elif answer == 5:
                print("You go down backstairs")
                return
            elif answer == 6:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action")