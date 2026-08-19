from inventory import add_item, remove_item, has_item
import Status

open_sheds_door = False

def farm_minigame():
    pass

def outdoor_garden():
    global open_sheds_door
    print("The sun hits your eyes in a pleasing way")
    print("The smell of the morning and the sound of butterflies amuses you a bit")

    while True:
        print("\n1. Take a look at the garden")
        print("2, Inspect the Shed's door")
        print("3. Return")

        try:
            answer = int(input("action: "))

            if answer == 1:
                farm_minigame()

            elif answer == 2:
                if not open_sheds_door:
                    print("There's a shining sword attached to the door and some combat clothes")
                    add_item("Small Sword")
                    add_item("Leather Armor")
                    Status.current_weapon = "Small Sword"
                    Status.current_armor = "Leather Armor"
                    Status.player_attack += 10
                    Status.player_defense += 10
                    print(f"Attack increased! ({Status.player_attack})")
                    print(f"Defense increased! ({Status.player_defense})")
                    print("You equipped Small Sword and Leather Armor!")
                    print("You can now access the Shed")
                    open_sheds_door = True

                elif open_sheds_door:
                    import shed
                    shed.shed_battle()

            elif answer == 3:
                print("You re-enter the castle")
                return

            else:
                print("Choose either the farm or the shed's door")
        except ValueError:
            print("Enter a valid action")


outdoor_garden()