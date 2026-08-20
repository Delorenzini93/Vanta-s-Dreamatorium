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
            enemy_hp=200,
            enemy_attack=0
        )

        if result:
            Status.enemy_defeated["dummy"] = True
            print("\nThe dummy collapses. You feel more confident.")
            add_item("Leather Boots")
            add_item("Quartz Ring")
            Status.current_boots = "Leather Boots"
            Status.current_accesory = "Quartz Ring"
            Status.player_speed += 10
            Status.player_hp += 10
            print(f"Attack increased! ({Status.player_speed})")
            print(f"Defense increased! ({Status.player_hp})")
            print("You equipped Leather Boots and Quartz Ring!")
    else:
        print("\nThe remains of the training dummy lie on the ground.")

shed_battle()