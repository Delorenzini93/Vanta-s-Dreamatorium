from inventory import add_item, remove_item, has_item
import Status
import Heroes

is_judge_gabranth = False
is_judge_ghis = False
is_judge_guybrook = False
is_east_chest_open = False
is_west_chest_open = False
is_north_chest_open = False
is_proof_hero = False

g_1 = "Judge Gabranth"
g_2 = "Judge Ghis"
g_3 = "Judge Guybrook"

def judges_room():
    global is_west_chest_open, is_east_chest_open, is_north_chest_open, is_proof_hero
    if not is_proof_hero:
        print("\nYou found a new hero!")
        print("You found 'ETERNAL TORMENTOR'")
        Heroes.find_hero("Eternal Tormentor")
        is_proof_hero = True

        print("You stand in a tiny and perfectly circular room with three chests")

        while True:
            print("1. Open chest (east)")
            print("2. Open chest (west)")
            print("3. Open chest (north)")
            print("4. Go back to the judge's room")
            print("5. Check inventory")

            try:
                answer = int(input(""))
                if answer == 1:
                    if is_east_chest_open:
                        print("You've already opened this chest")
                    else:
                        print("You open the chest facing east.")
                        add_item("Proof Of Existence")
                        print("You obtained 'PROOF OF EXISTENCE'!")
                        is_east_chest_open = True
                elif answer == 2:
                    if is_west_chest_open:
                        print("You've already opened this chest")
                    else:
                        print("You open the chest facing west.")
                        add_item("Chain Armor")
                        Status.current_chest_armor = "Chain Armor"
                        Status.player_defense += 30
                        print("You obtained 'CHAIN ARMOR'!")
                        print(f"Defense increased! ({Status.player_defense})")
                        print("You equipped Chain Armor!")
                        is_west_chest_open = True
                elif answer == 3:
                    if is_north_chest_open:
                        print("You've already opened this chest")
                    else:
                        print("You open the chest facing north.")
                        print("You found $50000!")
                        Status.souls += 50000
                        is_north_chest_open = True
                elif answer == 4:
                    print("You step away from the Room of Proofs")
                    return
                elif answer == 5:
                    from inventory import show_inventory
                    show_inventory()
            except ValueError:
                print("Choose a valid action")
##############################
def judges_3():
    global is_judge_guybrook
    if is_judge_guybrook:
        print(f"{g_3}: You have already proven your wisdom. Proceed.")
        judges_room()
        return
    else:
        print(f"{g_3}: Deep within the third task’s labyrinth, a creature of ancient riddles blocked the path to the Cup. What was that guardian?")

        while True:
            print("1. Answer")
            print("2. Remain silent and go away")
            try:
                answer = int(input(""))
                if answer == 1:
                    match input("Final answer: ").strip().lower():
                        case "sphinx":
                            print(f"{g_3}: That is correct.You may now proceed to take the proof of wisdom")
                            is_judge_guybrook = True
                            judges_room()
                            return
                        case _:
                            print(f"{g_3}: You understand nothing...")
                            return
                elif answer == 2:
                    print("You step away from the judging-looking judges.")
                    return
            except ValueError:
                print("Choose a valid action")
##################################
def judges_2():
    global is_judge_ghis
    if is_judge_ghis:
        judges_3()
        return
    else:
        print(f"{g_2}: In the second task, the champions had to dive into freezing waters to rescue what was taken from them. Where did this trial take place?")

        while True:
            print("1. Answer")
            print("2. Remain silent and go away")
            try:
                answer = int(input(""))
                if answer == 1:
                    match input("Final answer: ").strip().lower():
                        case "lake":
                            print(f"{g_2}: That is correct.You may now proceed to the third Judge, that is {g_3}")
                            is_judge_ghis = True
                            judges_3()
                            return
                        case _:
                            print(f"{g_2}: You understand nothing...")
                            return
                elif answer == 2:
                    print("You step away from the judging-looking judges.")
                    return
            except ValueError:
                print("Choose a valid action")
#########################
def judges_1():
    global is_judge_gabranth
    if is_judge_gabranth:
        judges_2()
        return
    else:
        print(f"{g_1}: In the first task of the legendary tournament, a fierce winged beast guarded a golden egg. Name the breed of that dragon.")

        while True:
            print("1. Answer")
            print("2. Remain silent and go away")
            try:
                answer = int(input(""))
                if answer == 1:
                    match input("Final answer: ").strip().lower():
                        case "hungarian":
                            print(f"{g_1}: That is correct.You may now proceed to the second Judge, that is {g_2}")
                            is_judge_gabranth = True
                            judges_2()
                            return
                        case _:
                            print(f"{g_1}: You understand nothing...")
                            return
                elif answer == 2:
                    print("You step away from the judging-looking judges.")
                    return
            except ValueError:
                print("Choose a valid action")
#########################
def dungeons_room_trial():
    print("\nThere's a small and dimly lighted room")
    print("There's also an altar with 3 very old goblins dressed in formal garments")

    while True:
        print("1. Talk to the judges")
        print("2. Go back to the dungeons")
        print("3. Check inventory")

        try:
            answer = int(input(""))

            if answer == 1:
                print("\nThe three goblins slowly raise their heads in perfect unison.")
                print("Their yellow eyes gleam in the dim light as the one in the center speaks with a deep, rasping voice:")
                print('"Three trials... three truths. Answer correctly, and the proofs shall be yours."')
                print("The first judge leans forward.")
                judges_1()
            elif answer == 2:
                print("You go back to the dungeons")
                import Dungeons
                Dungeons.dungeons()
            elif answer == 3:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
###################
dungeons_room_trial()