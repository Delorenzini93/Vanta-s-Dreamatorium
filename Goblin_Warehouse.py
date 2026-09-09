from inventory import add_item, remove_item, has_item
import Status
import Cauldron
import Fishing
import Heroes

aileen = "Aileen"
boss = "Swylabur"

is_chest_open = False
is_talked_to_aileen = False
is_pond_talk = False
is_journal_talk = False
is_discover_recipe = False

def goblin_warehouse_second_part():
    global is_pond_talk, is_journal_talk, is_discover_recipe
    print("There's a well with clear water flowing, an old pile of books and what seems to be a chess game of some sort")

    while True:
        print("1. Check the water-filled well")
        print("2. Check the weird-looking chess game")
        print("3. Check the pile of dusty books")
        print("4. Go back at the beginning of the warehouse")

        try:
            answer = int(input("What do we do here?"))

            if answer == 1:
                if is_pond_talk:
                    import Fishing
                    Fishing.catalog()
                else:
                    print("The water moves like if a breeze was blowing, but there are no windows here")

            elif answer == 2:
                if is_journal_talk:
                    import Heroes
                    Heroes.catalog()

                if not is_journal_talk:
                    print("I don't have the slightlest idea what this funny pieces and dashboard are")

            elif answer == 3:
                if is_discover_recipe:
                    print("Nothing useful here")

                if not is_discover_recipe:
                    print("there are so many kind of books that some of them are unreadable")
                    print("After looking, only one of them seems useful right now")
                    Cauldron.discover_recipe("Stew Recipe")
                    is_discover_recipe = True


            elif answer == 4:
                print("You go back to the beginning of the warehouse")
                return
        except ValueError:
            print("Choose a valid option")


###############################
def aileen_talk():
    global is_pond_talk, is_journal_talk
    print(f"\nHi I'm {aileen} and I live here in the WAREHOUSE")

    while True:
        print(f"1. So {aileen}, what's this warehouse?")
        print("2. What's that thing with water over there?")
        print("3. What's that werid-looking chess game over there?")
        print(f"4. Leave {aileen} for now")

        try:
            answer = int(input(f"{aileen}, do tell me..."))

            if answer == 1:
                print(f"\n{aileen}: This used to be the so called 'HALL OF HEROES'")
                print(f"But {boss} decide to weep them and now it's just an old warehouse, nothing fancy huh?")

            elif answer == 2:
                print(f"{aileen}: Oh, that's a WISHING WELL, everytime you fish a fish a fished fish'll appear there")
                print("But first you have to fish 'em, but first than that you have to find the fishing ponds")
                print("But firstly first you have to have a FISHING ROD, that's for sure")
                is_pond_talk = True

            elif answer == 3:
                print(f"{aileen}: Oh, you mean the HEROES JOURNAL? That's a curious device if you ask me")
                print(f"Before {boss} swept all the heroes he turned 'em into statues")
                print("But first he trapped them into that book, the HEROES JOURNAL")
                print("But firstly first they all broke free from the curse")
                print("and now all of them are scattered througout the castle, if you find any of them'll appear there")
                print("Who knows? Maybe they like you and even agree to join your party, but first thing first")
                is_journal_talk = True

            elif answer == 4:
                print(f"You leave {aileen} alone.")
                return
        except ValueError:
            print("Choose a valid option")

#####################################
def goblin_warehouse():
    global is_chest_open
    print("There's and old warehouse, somehow seems like an abandoned attic")
    print("There's also a cloed chest with lot of noise inside, weird...")

    while True:
        print("1. Check the chest")
        print("2. Explore the place a bit")
        print("3. Leave")

        try:
            answer = int(input("So, what do we do in this strange place?"))

            if answer == 1:
                if is_chest_open:
                    aileen_talk()
                else:
                    print("The chest opens and a ghostly young woman emerges from it!")
                    is_chest_open = True

            elif answer == 2:
                goblin_warehouse_second_part()

            elif answer == 3:
                print("You leave the warehouse and head back to the Dungeon's Corridor")
                return
        except ValueError:
            print("Please enter a valid action")
##################################################
goblin_warehouse()