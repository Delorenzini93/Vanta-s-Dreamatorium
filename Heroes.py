heroes_found = {}
heroes_data = {}

def find_hero(hero_name):
    if hero_name not in heroes_found:
        heroes_found[hero_name] = True
        print(f"\nYou found {hero_name}!")
##############################
def heroes_catalog():
    print("\n=== HALL OF HEROES ===")
    if not heroes_found:
        print("You haven't found any hero yet...")
        return

    heroes_list = list(heroes_found.keys())

    for i, hero_name in enumerate(heroes_list, 1):
        print(f"{i}. {hero_name}")

    while True:
        try:
            choice = int(input("\nChoose a hero to learn more (0 to leave): "))
            if choice == 0:
                return
            elif 1 <= choice <= len(heroes_list):
                selected = heroes_list[choice - 1]
                print(f"\n{selected}: {heroes_data.get(selected, '???')}")
            else:
                print(f"Choose between 1 and {len(heroes_list)}.")
        except ValueError:
            print("Enter a valid number.")
