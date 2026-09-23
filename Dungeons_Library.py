from inventory import add_item, remove_item, has_item
import Status

is_lore = False
is_first_trial = False
is_second_trial = False
is_third_trial = False
is_jail_key = False


def dungeons_library():
    global is_lore, is_first_trial, is_second_trial, is_third_trial, is_jail_key

    print("\nYou step into the Dungeon's Library.")
    print("Tall wooden shelves rise into the shadows, packed with ancient tomes, scrolls, and brittle manuscripts.")
    print("The air smells of old parchment and forgotten knowledge.")

    while True:
        if is_lore and is_first_trial and is_second_trial and is_third_trial and not is_jail_key:
            print("\nAs you finish studying the last manuscript, you notice something on the floor...")
            print("You found an old key lost in the dust!")
            add_item("Jail Key")
            print("You obtained 'JAIL KEY'!")
            is_jail_key = True

        print("\n1. Examine manuscripts (left)")
        print("2. Examine manuscripts (right)")
        print("3. Examine manuscripts (above)")
        print("4. Examine manuscripts (forward)")
        print("5. Go back to the Dungeons")

        try:
            answer = int(input(""))

            if answer == 1:
                print("\n『The Tournament of the Three Trials』")
                print("Long ago, a great contest was held between champions.")
                print("Three deadly trials were set to test courage, wit, and strength.")
                print("Only those who mastered all three could claim the ultimate prize.")
                is_lore = True

            elif answer == 2:
                print("\n『The First Trial』")
                print("In the first challenge, a fearsome HUNGARIAN dragon was awakened.")
                print("It guarded a golden egg with fire and fury.")
                print("Only the bravest dared face its wrath.")
                is_first_trial = True

            elif answer == 3:
                print("\n『The Second Trial』")
                print("The second trial took place in the cold depths of a LAKE.")
                print("There, a mermaid had drowned, and the champions had to dive")
                print("into the dark waters to retrieve what was taken from them.")
                is_second_trial = True

            elif answer == 4:
                print("\n『The Third Trial』")
                print("The final trial led into a vast and twisting MAZE.")
                print("At its heart stood a defensive Sphinx, speaking in riddles,")
                print("blocking the path to the Cup with ancient wisdom.")
                is_third_trial = True

            elif answer == 5:
                print("You step away from the library and head back to the dungeons.")
                return

        except ValueError:
            print("Choose a valid action.")


dungeons_library()