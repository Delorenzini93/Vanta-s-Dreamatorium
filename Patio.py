from inventory import add_item, remove_item, has_item
import Status
import fishing
import Farm
import Heroes
import os

is_hero_found = False

def patio():
    os.system('cls')
    Status.current_room = "west_hall"
    global is_hero_found

    print("\nThe air here is different.")
    print("Lighter. The kind of air you forgot existed.")
    print("A small open patio stretches before you, bathed in soft light.")
    print("No echoes. No growls. Just the distant sound of water and wind.\n")

    while True:
        print("1. Sit by the pond")
        print("2. Tend to the garden")
        print("3. Someone's here...")
        print("4. Go back")
        print("5. Check inventory")

        try:
            answer = int(input("\n"))

            if answer == 1:
                print("\nThe water is still and clear.")
                print("For a moment you forget about everything else.")
                fishing.fish("pond_2")

            elif answer == 2:
                print("\nThe soil is soft here. Something could grow.")
                Farm.farm_menu()


            elif answer == 3:

                if is_hero_found:
                    print("\nThey sit quietly, enjoying the calm.")
                else:
                    print("\nA figure is crouched near the wall, studying something on the ground.")
                    print("They look up slowly, unsurprised.")
                    print("???: Oh. A visitor. Haven't had one of those in... a while.")
                    print("???: I'm Pontedenna. I've been here longer than I'd like to admit.")
                    print("Pontedenna: This patio has a way of keeping you. Not by force. Just... by being.")
                    Heroes.find_hero("Pontedenna")
                    is_hero_found = True

            elif answer == 4:
                print("\nYou take one last breath of clean air before heading back.")
                return

            elif answer == 5:
                from inventory import show_inventory
                show_inventory()

            else:
                print("Take your time.")

        except ValueError:
            print("Take your time.")