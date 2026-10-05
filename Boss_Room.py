from inventory import add_item, remove_item, has_item
import Status
import battle

boss_name = "Mosag"
is_weakened = False
is_name_spoken = False

def boss_fight():
    global is_weakened

    if not is_weakened:
        print(f"\n{boss_name} is impervious to your attacks...")
        print("Your strikes dissolve into nothing.")
        print("There must be another way.")
        return

    result = battle.battle(
        enemy_name=boss_name,
        enemy_hp=8000,
        enemy_attack=90,
        enemy_souls=50000,
        enemy_exp=5000
    )

    if result:
        Status.enemy_defeated["Mosag"] = True
        print("\nThe entity convulses and slowly dissipates...")
        print("Millions of faint voices seem to exhale at once.")
        print("Then... silence.")
        print("\nThe first part of your journey in Garam ends here.")
        print("But something tells you this is far from over.")
        import West_Hall
        West_Hall.west_hall()
    else:
        print("GAME OVER")

def boss_room():
    global is_weakened, is_name_spoken

    print("\nThe chamber is vast and lightless.")
    print("Something ancient and formless stirs in the darkness.")
    print("The air itself feels heavy with accumulated grief.")

    while True:
        print("\n1. Attack")
        print("2. Speak a name")
        print("3. Observe the entity")
        print("4. Check inventory")

        try:
            answer = int(input(""))

            if answer == 1:
                boss_fight()

            elif answer == 2:
                if is_name_spoken:
                    print("\nThe name already resonates through the chamber.")
                else:
                    name = input("Speak: ").strip().lower()
                    if name == "esthat":
                        print("\nThe name cuts through the darkness like a blade.")
                        print(f"The entity recoils violently.")
                        print("Something fundamental has shifted.")
                        print("It can be hurt now.")
                        is_weakened = True
                        is_name_spoken = True
                    else:
                        print("\nThe name dissolves into the darkness without effect.")
                        print("The entity seems unmoved.")

            elif answer == 3:
                print("\nIt has no defined shape.")
                print("It shifts constantly, as if made of countless overlapping silhouettes.")
                print("You sense centuries of accumulated hatred emanating from its core.")
                if not is_name_spoken:
                    print("There's something familiar about it... like a name on the tip of your tongue.")

            elif answer == 4:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action")

boss_room()