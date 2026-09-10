from inventory import add_item, remove_item, has_item
import Status
import battle
import Cauldron

is_talked_to_winky = False
is_talked_to_rosmerta = False
is_rosmerta_happy = False
is_dining_table_full = False
is_table_looted = False

window_look_count = 0

lady = "Madam Rosmerta"
elf = "Winky"

#########################################
def madam_rosmerta():
    print(f"\n{lady}: Nowadays all these disrespectful kids are going so freely through the castle")
    print("You seem prideful but not stupid, but I'll tell you something kid")
    print("Listen well kid, I don't know how you ended up here or what your business is here")
    print("But the castle it's not a place for a kid like you, it's a dangerous place")
    print("You better get some weapons and armor just in case...")
    print("Unlike the others previous kids you seem naive, so you better take this with you")
    add_item('Potion')
    add_item('Potion')
    add_item('Potion')
    print(f"{lady}: Whatch yourself out there kid.....I mean it")
    return
#########################################
def rosmerta_second_talk():
    global is_dining_table_full
    print(f"\n{lady}: You really beat that bastard Ghoul! It was so annoying with my past servants")
    print("He once ate alive three of them at once, what a horrible being")
    print("Though I still think you were extremelly lucky and insist in taking extreme care of yourself")
    print("I'm glad my dinner is not spoiled by that brat Ghoul, take this:")
    add_item('Potion')
    add_item('Amine')
    add_item('Potion')
    print(f"{lady}: Feel free to serve yourself at the dining table and use the cauldron at the kitchen.")
    print("You can now gather RECIPES to learn new combination of items in order to synthezise them")
    print("Even though I'm not going to give you my secret Putanesca recipe, I think you'll do just fine with these")
    Cauldron.discover_recipe("Savory Pie Recipe")
    print(f"{lady}: Watch yourself out there kid.....I mean it")
    is_dining_table_full = True
    return
#########################################
def kitchen_activities():
    print(f"{elf}: Sir, this is the kitchen where we cook dinner for our eternal guests")
    print(f"{elf}: Feel free to use the CAULDRON to mix and synthezise items and learn recipes!")

    while True:
        print("1. Use the cauldron")
        print("2. Ask Winky for food")
        print("3. Leave the kitchen")

        try:
            answer = int(input("What do we do at the kitchen?"))

            if answer == 1:
                Cauldron.cauldron()
            elif answer == 2:
                if Status.player_hp == 100:
                    print(f"{elf}: You look full sir, come back when you're hungry!")
                else:
                    Status.player_hp = 100
                    print("Winky served you a delicious meal. HP fully restored!")
            elif answer == 3:
                print("You return to the Dining Room")
                return
            else:
                print("Do you use the cauldron or not?")
        except ValueError:
            print("Choose a valid option")

#########################################
def kitchen_scene():
    global is_rosmerta_happy
    if not Status.enemy_defeated["Foul Ghoul"]:
        print("\nAn angry ghoul its making a mess in the kitchen!")
        print("It seems like its about to eat the little screaming elf!")


        result = battle.battle(
            enemy_name="Foul Ghoul",
            enemy_hp=500,
            enemy_attack=15
        )

        if result:
            Status.enemy_defeated["Foul Ghoul"] = True
            print("\nThe Ghoul vanishes. The noise stops.")
            print("\n???: You-you killed it, isn't it?")
            print("???: Ohhh thank you I thought that thing was going to eat me alive!")
            print(f"???: Oh by the way, I'm {elf}")
            add_item('Tomato')
            add_item('Lettuce')
            add_item('Bread')
            add_item('Ghoul Eye')
            is_rosmerta_happy = True
            kitchen_activities()
        else:
            print("GAME OVER")
            return
    else:
        kitchen_activities()
#########################################
def dining_room():
    global is_daylight, is_talked_to_rosmerta, is_table_looted, window_look_count
    print("\nThere's an ebony table at the center of a small room decorated with paintings")

    while True:
        print("1. Inspect the table")
        print("2. Inspect the window")
        print("3. Inspect the painting")
        print("4. Inspect the noisy door (right)")
        print("5. Leave")

        try:
            answer = int(input("What do we do?"))
            if answer == 1:
                if is_dining_table_full and not is_table_looted:
                    print("The table is full of delicious ingredients!")
                    add_item('Butter')
                    add_item('Milk')
                    add_item('Honey')
                    add_item('Red Seed')
                    add_item('Blue Seed')
                    is_table_looted = True
                elif is_table_looted:
                    print("You already took everything from the table.")
                else:
                    print("It's empty but a strong smell of food comes from the noisy door")
                    continue
            elif answer == 2:
                window_look_count += 1
                if window_look_count % 2 == 0:
                    Status.is_daylight = True
                    print("The sun peeks through the clouds again...")
                else:
                    Status.is_daylight = False
                    print("The clouds are getting darker, nightfall will soon be upon us...")
                continue
            elif answer == 3:
                print("There's a huge painting of an old lady")
                print(f"{lady}: What are you looking at you wayward kid?")
                if not is_talked_to_rosmerta:
                    madam_rosmerta()
                    is_talked_to_rosmerta = True
                elif is_rosmerta_happy:
                    rosmerta_second_talk()
                else:
                    print(f"{lady}: Move along kid, I've said enough.")

            elif answer == 4:
                print("???: HEEEEEEELP!!!!!")
                print(f"{lady}: Oh no, that foul creature is wrecking havoc all over the kitchen again, be careful twat")
                print("Seems like a dangerous scene is happening in the other room")
                while True:
                    print("1. Enter at my own risk")
                    print("2. Leave")

                    try:
                        answer = int(input("Do I...?"))
                        if answer == 1:
                            kitchen_scene()
                        elif answer == 2:
                            return
                        else:
                            print("Enter or leave?")
                    except ValueError:
                        print("Choose a valid option")
            elif answer == 5:
                print("You go back to the Second Hall")
                return
        except ValueError:
            print("Choose a valid option")
#####################
dining_room()