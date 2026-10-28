from inventory import add_item, remove_item, has_item
import Status
import Encounters
import os
######################
def royal_dungeons_east():
    while True:
        print("1. Open the door (forward)")
        print("2. Go back")

        try:
            answer = int(input("We moved east, where do we go now?"))

            if answer == 1:
                print("You open the iron door that lies in front of you")
                import Trial_Dungeon
                Trial_Dungeon.trial_dungeon()
            elif answer == 2:
                Encounters.random_encounter("royal_dungeons")
                print("You go back at the beginning of the Royal Dungeons")
                return
        except ValueError:
            print("Choose a valid option")
######################
def royal_dungeons_west():
    while True:
        print("1. Open the door (forward)")
        print("2. Go back")

        try:
            answer = int(input("We moved west, where do we go now?"))

            if answer == 1:
                print("You open the door that lies to your right")
                import Experiments_Cell
                Experiments_Cell.experiments_cell()
            elif answer == 2:
                Encounters.random_encounter("royal_dungeons")
                print("You go back at the beginning of the Royal Dungeons")
                return
        except ValueError:
            print("Choose a valid option")
######################
def royal_dungeons_forward():
    print("This is it. Powerful forces lie behind those door. Better be prepared and choose wisely")
    while True:
        print("1. Open the Day Door (right)")
        print("2. Open the Night Door (left)")
        print("3. Read the inscription 'Sign Of The Times'")
        print("4. Go back")

        try:
            answer = int(input("We moved forward, where do we go now?"))
            if answer == 1:
                if Status.is_daylight:
                    print("You open the door that lies to your right")
                    print("A powerful beam of light engulf your total vision")
                    import Right_Path
                    Right_Path.right_path()
                else:
                    print("A powerful shadow prevents the door from opening")
            elif answer == 2:
                if not Status.is_daylight:
                    print("You open the door that lies to your left")
                    import Left_Path
                    Left_Path.left_path()
                else:
                    print("A powerful magic prevents the door from opening")
            elif answer ==3:
                print("\nSIGN OF THE TIMES:")
                print("\nAt the LEFT PATH opens only to the dwellers of the night")
                print("\nThose brave of heart and quick of mind will be able to make their way through the ferocious hordes")
                print("\nThose bloodlust warriors find great pleasure for fighting in total darkness")
                print("\nAt the RIGHT PATH opens only to the followers of the sun")
                print("\nThose full of humility and devoid of sin will be able to take down the Giant Of The Wheel")
                print("\nThings are not what they seem and friendliness should not be confused with voraciousness")
            elif answer == 4:
                Encounters.random_encounter("royal_dungeons")
                print("You go back at the beginning of the dungeons")
                return
        except ValueError:
            print("Choose a valid option")
######################
def royal_dungeons():
    os.system('cls')
    Status.current_room = "royal_dungeons"
    print("I can barely see a metre away...better be careful around here...")

    while True:
        print("1. Move north")
        print("2. Move east")
        print("3. Move west")
        print("4. Go back")
        print("5. Check inventory")

        try:
            answer = int(input("Better get going..."))

            if answer == 1:
                Encounters.random_encounter("royal_dungeons")
                print("You move forward in the darkness")
                royal_dungeons_forward()
            elif answer == 2:
                Encounters.random_encounter("royal_dungeons")
                print("You move closer to the walls")
                royal_dungeons_west()
            elif answer == 3:
                Encounters.random_encounter("royal_dungeons")
                print("You move closer to the windows")
                royal_dungeons_east()
            elif answer == 4:
                print("You leave the Royal Dungeons")
                return
            elif answer == 5:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")