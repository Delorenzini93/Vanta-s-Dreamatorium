from inventory import add_item, remove_item, has_item
import Status
import battle

z = 'Cockroach Dandy'
is_cockroach = False
is_zagnar_down = False

def zagnar_battle():
    global is_zagnar_down
    if not Status.enemy_defeated["Zagnar"]:

        result = battle.battle(
            enemy_name="Zagnar",
            enemy_hp=7000,
            enemy_attack=60
        )

        if result:
            Status.enemy_defeated["Zagnar"] = True
            add_item('#')
            add_item('#')
            is_zagnar_down = True
            return
        else:
            print("GAME OVER")
            return
##########################
def dungeons_noisy_room():
    global is_cockroach, is_zagnar_down
    print("There's a gigantic cage with a black blanket covering it....furious roars comes from within!")

    while True:
        print("1. Check the cage")
        print("2. Talk to the Cockroach Dandy next to the cage")
        print("3. Go back to the dungeons")
        print("4. Check inventory")

        try:
            answer = int(input(""))

            if answer == 1:
                if is_zagnar_down:
                    print("#")
                else:
                    print("It's incredibly scary to get close to the cage....possibly a very fearsome creature lies within the cage")
            elif answer == 2:
                if is_cockroach:
                    while True:
                        print("1. Yes")
                        print("2. No way, I'm out!")
                        try:
                            answer = int(input(f"{z}: Ready to go in with the mighty Zagnar, wayfarer?"))
                            if answer == 1:
                                print(f"{z}:How brave...or foolish..Hope I see you again wayfarer...or not!")
                                zagnar_battle()
                            elif answer == 2:
                                print(f"{z}:You're smart...believe me you're, wayfarer")
                                return
                        except ValueError:
                            print("Choose a valid action")
                print(f"{z}: Well hello wayward wayfarer, tell me when you're ready to test your skill with Zagnar")
                print(f"{z}:But I'll warn ya, that beast hasn't eaten in a few days, so you better watch out")
                is_cockroach = True
            elif answer == 3:
                print("You go back to the dungeons")
                return
            elif answer == 4:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")
##########################
dungeons_noisy_room()