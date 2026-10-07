from inventory import add_item, remove_item, has_item
import Status
import Encounters
import os

is_autumn_guardian = False
is_winter_guardian = False
is_spring_guardian = False

def gorge_3():
    global is_spring_guardian

    print("You reach a wider clearing within the gorge. The air feels different here… older.")

    while True:
        print("\n1. Advance through the difficult terrain (forward)")
        print("2. Go back")
        print("3. Examine Spring Guardian")
        print("4. Check inventory")

        try:
            answer = int(input("Well... "))

            if answer == 1:
                Encounters.random_encounter("exterior")
                print("The path finally opens ahead...")
                import Sanctuary
                Sanctuary.sanctuary()
                return

            elif answer == 2:
                print("You go back to the previous section of the gorge.")
                gorge_2()
                return

            elif answer == 3:
                if is_spring_guardian:
                    print("\nThe Spring Guardian stands quietly.")
                    print("The slot in its chest is now filled.")
                else:
                    print("\nThe final statue stands in a slightly more open space.")
                    print("Unlike the others, this one feels almost alive.")
                    print("It portrays a figure reaching upward, with vines and buds carved into its arms.")
                    print("A narrow slot is visible in its chest, as if something should be inserted.")

                    if has_item("Spring Anima"):
                        print("\nYou insert the SPRING ANIMA into the statue's chest.")
                        print("A faint warmth spreads through the stone as it accepts the offering.")
                        remove_item("Spring Anima")
                        is_spring_guardian = True
                        print("The Spring Guardian has been appeased.")

            elif answer == 4:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")
############################
def gorge_2():
    global is_winter_guardian

    print("The walls grow steeper. Cold air sinks into your bones.")

    while True:
        print("\n1. Advance through the difficult terrain (forward)")
        print("2. Go back")
        print("3. Examine Winter Guardian")
        print("4. Check inventory")

        try:
            answer = int(input("Well... "))

            if answer == 1:
                Encounters.random_encounter("exterior")
                print("Your steps echo against the freezing stone.")
                gorge_3()
                return

            elif answer == 2:
                print("You go back to the previous section of the gorge.")
                gorge()
                return

            elif answer == 3:
                if is_winter_guardian:
                    print("\nThe Winter Guardian remains motionless.")
                    print("Its hand is no longer empty.")
                else:
                    print("\nThe second statue is larger and colder to the touch.")
                    print("It shows a stern figure wrapped in heavy cloaks, eyes closed.")
                    print("Frost seems permanently etched into the stone.")
                    print("Its outstretched hand is empty, waiting for an offering.")

                    if has_item("Winter Anima"):
                        print("\nYou place the WINTER ANIMA into the statue's hand.")
                        print("A deep chill runs through the gorge as the offering is accepted.")
                        remove_item("Winter Anima")
                        is_winter_guardian = True
                        print("The Winter Guardian has been appeased.")

            elif answer == 4:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")
#######################
def gorge():
    os.system('cls')
    global is_autumn_guardian
    Status.current_room = "mountainside"

    print("The gorge narrows. The noise from the mountainside fades, replaced by a heavy, damp silence.")

    while True:
        print("\n1. Advance through the difficult terrain (forward)")
        print("2. Go back")
        print("3. Examine Autumn Guardian")
        print("4. Check inventory")

        try:
            answer = int(input("Well... "))

            if answer == 1:
                Encounters.random_encounter("exterior")
                print("You hear nothing but the loud steps on the rocks.")
                gorge_2()
                return

            elif answer == 2:
                print("You went back to the mountainside.")
                return

            elif answer == 3:
                if is_autumn_guardian:
                    print("\nThe Autumn Guardian stands silently.")
                    print("The niche at its base is no longer empty.")
                else:
                    print("\nA tall stone statue stands against the rocky wall.")
                    print("It depicts a hooded figure holding a withered branch.")
                    print("Dead leaves are carved around its feet, frozen in mid-fall.")
                    print("At the base of the statue is a small empty niche.")
                    print("Something is meant to be placed here...")

                    if has_item("Autumn Anima"):
                        print("\nYou place the AUTUMN ANIMA into the niche.")
                        print("The statue seems to absorb it completely.")
                        remove_item("Autumn Anima")
                        is_autumn_guardian = True
                        print("The Autumn Guardian has been appeased.")

            elif answer == 4:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")
################
gorge()