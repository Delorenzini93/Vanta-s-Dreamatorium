import random
import Status

def battle(enemy_name, enemy_hp, enemy_attack):
    player_hp = Status.player_hp

    attacks = {
        1: ("Strong Attack", 35),
        2: ("Normal Attack", 20),
        3: ("Special Attack", 0),
    }

    turn = random.choice(["player", "enemy"])
    print(f"\n{'You go first!' if turn == 'player' else f'{enemy_name} goes first!'}")

    while player_hp > 0 and enemy_hp > 0:

        if turn == "player":
            print(f"\nYour HP: {player_hp} | {enemy_name} HP: {enemy_hp}")
            print("1. Strong Attack")
            print("2. Normal Attack")
            print("3. Special Attack")

            try:
                choice = int(input("\nChoose your attack: "))
                if choice not in attacks:
                    print("Choose between 1 and 3.")
                    continue

                name, damage = attacks[choice]

                if choice == 3:
                    enemy_attack = int(enemy_attack * 0.5)
                    print(f"Special activated! {enemy_name}'s attack reduced!")
                else:
                    enemy_hp -= damage
                    print(f"\n{name}! {enemy_name} takes {damage} damage.")

                turn = "enemy"

            except ValueError:
                print("Enter a valid number.")

        else:
            cpu_choice = random.randint(1, 2)
            name, damage = attacks[cpu_choice]
            actual_damage = max(0, damage - Status.player_defense)
            player_hp -= actual_damage
            print(f"\n{enemy_name} uses {name}! You take {actual_damage} damage.")
            turn = "player"

    if player_hp <= 0:
        print(f"\nYou were defeated by {enemy_name}...")
        return False
    else:
        print(f"\n{enemy_name} was defeated!")
        return True