from inventory import add_item, remove_item, has_item
import Status
import os

ghost_hostility = 0
piano_touched = False
table_examined = False
mirror_looked = False
curtains_opened = False

def ballroom():
    global ghost_hostility, piano_touched, table_examined, mirror_looked, curtains_opened
    os.system('cls')
    Status.current_room = "ballroom"

    print("\nYou enter the Ballroom.")
    print("A vast, elegant hall stretches out before you.")
    print("Dust floats in the air. The chandeliers hang motionless.")
    print("Something about this place feels deeply unsettled.")

    while True:
        show_ghost_presence()

        print("\n1. Examine the broken piano")
        print("2. Examine the long table")
        print("3. Look into the large mirror")
        print("4. Approach the heavy curtains")
        print("5. Check inventory")
        print("6. Leave the Ballroom")

        try:
            answer = int(input("\nThe silence feels heavy... "))

            if answer == 1:
                examine_piano()
            elif answer == 2:
                examine_table()
            elif answer == 3:
                examine_mirror()
            elif answer == 4:
                examine_curtains()
            elif answer == 5:
                from inventory import show_inventory
                show_inventory()
            elif answer == 6:
                if ghost_hostility >= 5:
                    print("\nThe air turns ice-cold as you turn to leave.")
                    print("For a moment you feel something very close behind you...")
                    print("Then the sensation fades as you step out of the room.")
                else:
                    print("You leave the Ballroom.")
                return
            else:
                print("Choose a valid action.")

        except ValueError:
            print("Choose a valid action.")


def show_ghost_presence():
    global ghost_hostility

    if ghost_hostility == 0:
        return
    elif ghost_hostility == 1:
        print("\nYou feel watched.")
    elif ghost_hostility == 2:
        print("\nSoft footsteps echo faintly, then stop the moment you notice them.")
    elif ghost_hostility == 3:
        print("\nA faint shape lingers at the edge of your vision, disappearing when you turn.")
    elif ghost_hostility == 4:
        print("\nThe temperature drops sharply. Something in the room is no longer hiding.")
    elif ghost_hostility >= 5:
        print("\nThe presence is fully aware of you now.")
        print("The air feels hostile.")

def raise_hostility():
    global ghost_hostility
    if ghost_hostility < 5:
        ghost_hostility += 1
        if ghost_hostility >= 5:
            Status.is_ghost_hostile = True
            print("\nA deep cold settles into the room...")
            print("You feel that something in the castle has noticed your presence.")



def examine_piano():
    global piano_touched

    print("\nThe grand piano sits in the corner, covered in dust.")
    print("Several keys are broken. The wood is cracked.")

    if not piano_touched:
        print("You press one of the keys. A wrong, hollow note rings out and dies quickly.")
        piano_touched = True
        raise_hostility()
    else:
        print("The piano remains silent. It has already noticed you.")


def examine_table():
    global table_examined

    print("\nA long banquet table stretches across the center of the room.")
    print("It is completely empty, except for one place setting that looks recently disturbed.")

    if not table_examined:
        print("The single plate and glass feel wrong, as if someone was expected... or interrupted.")
        table_examined = True
        raise_hostility()
    else:
        print("The table has nothing more to show you.")


def examine_mirror():
    global mirror_looked

    print("\nA tall, ornate mirror stands against the far wall.")
    print("The glass is cloudy in places.")

    if not mirror_looked:
        print("For a second, you see a figure standing behind you in the reflection.")
        print("When you turn around, there is no one there.")
        mirror_looked = True
        raise_hostility()
    else:
        if ghost_hostility >= 3:
            print("The mirror now shows the figure more clearly.")
            print("It is looking directly at you.")
        else:
            print("Your reflection looks slightly delayed.")


def examine_curtains():
    global curtains_opened

    print("\nHeavy curtains cover the tall windows.")

    if not curtains_opened:
        print("You pull one of them aside.")
        print("Behind it there is only darkness — thick, unnatural darkness that seems to swallow the light.")
        curtains_opened = True
        raise_hostility()
    else:
        print("The curtains have already been moved. The darkness behind them remains.")