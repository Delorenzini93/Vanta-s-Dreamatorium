from inventory import add_item, remove_item, has_item
import Status

is_judge_gabranth = False
is_judge_ghis = False
is_judge_guybrook = False
is_east_chest_open = False
is_west_chest_open = False
is_north_chest_open = False

g_1 = "Judge Gabranth"
g_2 = "Judge Ghis"
g_3 = "Judge Guybrook"

def judges_room():
    global is_west_chest_open, is_east_chest_open, is_north_chest_open
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
                    print("You open the chest facing east direction")
                    add_item("")
                    print("You obtained ''!")
                    is_east_chest_open = True
            elif answer == 2:
                if is_west_chest_open:
                    print("You've already opened this chest")
                else:
                    print("You open the chest facing west direction")
                    add_item("")
                    print("You obtained ''!")
                    is_west_chest_open = True
            elif answer == 3:
                if is_north_chest_open:
                    print("You've already opened this chest")
                else:
                    print("You open the chest facing nortt direction")
                    add_item("")
                    print("You obtained ''!")
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
        print(f"{g_3}: That is correct.You may now proceed to take the proof of wisdom")
        judges_room()
    else:
        print(f"{g_3}:")

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
                        case _:
                            print(f"{g_3}: You understand nothing...")
                            return
                elif answer == 2:
                    print("You step away from the judging-looking judges")
                    return
            except ValueError:
                print("Choose a valid action")
##################################
def judges_2():
    global is_judge_ghis
    if is_judge_ghis:
        judges_3()
    else:
        print(f"{g_2}:")

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
                        case _:
                            print(f"{g_2}: You understand nothing...")
                            return
                elif answer == 2:
                    print("You step away from the judging-looking judges")
                    return
            except ValueError:
                print("Choose a valid action")
#########################
def judges_1():
    global is_judge_gabranth
    if is_judge_gabranth:
        judges_2()
    else:
        print(f"{g_1}:")

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
                        case _:
                            print(f"{g_1}: You understand nothing...")
                            return
                elif answer == 2:
                    print("You step away from the judging-looking judges")
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
                print("x")
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