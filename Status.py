user = ""
current_outfit = "Default outfit"

souls = 0

player_level = 1
player_exp = 0
player_exp_to_next = 100
player_max_hp = 100
player_hp = 100
player_attack = 20
player_defense = 0
player_speed = 30
stat_points = 0

current_weapon = "Bare Hands"
current_chest_armor = "No Armor"
current_boots = "No Boots"
current_accesory = "No Accesory"

is_daylight = True
is_candles_lit = False

enemy_defeated = {
    "dummy": False,
    "Wyvern": False,
    "Undead": False,
    "Glass Entity": False,
    "Shadows": False,
    "Galerian": False,
    "Foul Ghoul": False
}

def assign_stat_points():
    global stat_points, player_attack, player_defense, player_speed
    if stat_points == 0:
        print("No stat points available.")
        return

    while stat_points > 0:
        print(f"\nStat points available: {stat_points}")
        print(f"1. Attack ({player_attack})")
        print(f"2. Defense ({player_defense})")
        print(f"3. Speed ({player_speed})")

        try:
            choice = int(input("Assign point to: "))
            if choice == 1:
                player_attack += 2
                stat_points -= 1
                print(f"Attack increased to {player_attack}!")
            elif choice == 2:
                player_defense += 2
                stat_points -= 1
                print(f"Defense increased to {player_defense}!")
            elif choice == 3:
                player_speed += 2
                stat_points -= 1
                print(f"Speed increased to {player_speed}!")
            else:
                print("Choose between 1 and 3.")
        except ValueError:
            print("Enter a valid number.")

def check_levelup():
    global player_level, player_exp, player_exp_to_next, player_max_hp, player_hp, stat_points
    if player_exp >= player_exp_to_next:
        player_level += 1
        player_exp -= player_exp_to_next
        player_exp_to_next = int(player_exp_to_next * 1.5)
        player_max_hp += 10
        player_hp = player_max_hp
        stat_points += 1
        print(f"\nLEVEL UP! You are now level {player_level}!")
        print(f"HP increased to {player_max_hp}!")
        assign_stat_points()