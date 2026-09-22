import Third_Hall
from inventory import add_item, remove_item, has_item
import Status
import Encounters

is_jail_open = False

def deep_dungeons_north():
    print("You're now facing the north wing of the deep dungeons")

    while True:
        print("1. Open the metallic door")
        print("2. Go back to deep dungeon's central wing")
        print("3. Check inventory")

        try:
            answer = int(input(""))

            if answer == 1:
                print("With a tremendous and high-pitched noise, the metallic door slowly opens...")
                import Basements
                Basements.basements()
            elif answer == 2:
                Encounters.random_encounter("dungeons")
                print("You go to the deep dungeons central wing")
                return
            elif answer == 3:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
##################################
def deep_dungeons_east():
    print("You're now facing the east wing of the deep dungeons")

    while True:
        print("1. Examine door (left)")
        print("2. Examine door (right)")
        print("3. Go to the deep dungeon's central wing")
        print("4. Check inventory")

        try:
            answer = int(input(""))
            if answer == 1:
                if Third_Hall.is_dungeons_door_open:
                    print("You go to the Third Hall")
                    import Third_Hall
                    Third_Hall.third_hall()
                else:
                    print("The door is tightly shut.Seems like it can be opened from the other side")
            elif answer == 2:
                print("You open the right door.A sign next to it reads 'LI B R A R Y'")
                import Dungeons_Library
                Dungeons_Library.dungeons_library()
            elif answer == 3:
                Encounters.random_encounter("dungeons")
                print("You go to the deep dungeons central wing")
                return
            elif answer == 4:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
        ###################################
def deep_dungeons_west():
    global is_jail_open
    print("You're now facing the west wing of the deep dungeons")

    while True:
        print("1. Examine door (left)")
        print("2. Examine door (right)")
        print("3. Go to the deep dungeon's central wing")
        print("4. Check inventory")

        try:
            answer = int(input(""))
            if answer == 1:
                print("You open the left door.A sign next to it reads 'S I L E N C E'")
                import Silence_Room
                Silence_Room.silence_room()
            elif answer == 2:
                if is_jail_open:
                    print("You've entered in the dungeon's jail")
                    import Jail
                    Jail.jail()
                elif has_item('Jail Key'):
                    print("You used the 'JAIL KEY'")
                    remove_item('Jail Key')
                    is_jail_open = True
                    import Jail
                    Jail.jail()
                else:
                    print("The door is closed.A sign next to the door reads 'J A I L'")
            elif answer == 3:
                Encounters.random_encounter("dungeons")
                print("You go to the deep dungeons central wing")
                return
            elif answer == 4:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
##################################
def deep_dungeons():
    print("Another spacious section of the dungeons.I assume we're deep into the dungeons since the air is colder here")

    while True:
        print("1.Move north")
        print("2. Move east")
        print("3. Move west")
        print("4. Go to the upper dungeons")
        print("5. Check inventory")

        try:
            answer = int(input("Where do we go?"))

            if answer == 1:
                Encounters.random_encounter("dungeons")
                deep_dungeons_north()
            elif answer == 2:
                Encounters.random_encounter("dungeons")
                deep_dungeons_east()
            elif answer == 3:
                Encounters.random_encounter("dungeons")
                deep_dungeons_west()
            elif answer == 4:
                print("You went back to the upper dungeons")
                return
            elif answer == 5:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
#########################
deep_dungeons()