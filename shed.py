import Status
import battle

def shed_battle():
    print("A cold and misty smell lies before you.")
    print("Something moves in the background...")

    if not Status.enemy_defeated["dummy"]:
        print("\nA training dummy emerges from the dark.")
        print("It seems like a good place to practice...")

        result = battle.battle(
            enemy_name="Training Dummy",
            enemy_hp=60,        # ajustá
            enemy_attack=10     # ajustá
        )

        if result:
            Status.enemy_defeated["dummy"] = True
            print("\nThe dummy collapses. You feel more confident.")
    else:
        print("\nThe remains of the training dummy lie on the ground.")

shed_battle()