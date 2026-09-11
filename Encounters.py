import random
import battle
import Status

enemy_pools = {
    "dungeon": [
        {"name": "Undead", "hp": 60, "attack": 12},
        {"name": "Shadow", "hp": 40, "attack": 18},
    ],
    "castle": [
        {"name": "Wyvern", "hp": 80, "attack": 15},
        {"name": "Galerian", "hp": 70, "attack": 14},
    ],
}


def random_encounter(zone, chance=30):
    if Status.is_daylight:
        return

    if random.randint(1, 100) > chance:
        return

    pool = enemy_pools.get(zone, [])
    if not pool:
        return

    enemy = random.choice(pool)
    print(f"\nA {enemy['name']} appears from the shadows!")

    result = battle.battle(
        enemy_name=enemy["name"],
        enemy_hp=enemy["hp"],
        enemy_attack=enemy["attack"]
    )

    if not result:
        print("GAME OVER")