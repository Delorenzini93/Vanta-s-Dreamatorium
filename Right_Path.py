from inventory import add_item, remove_item, has_item
import Status
import os
import time


def right_path():
    os.system('cls')

    print("\nYou step through the Day Door.")
    print("A wide stone corridor stretches ahead, lit by a warm, artificial glow.")
    print("Carvings of suns and great wheels cover the walls.")
    print("At the end of the corridor lies a vast circular chamber...")

    input("\nPress Enter to continue...")

    arena_of_the_wheel()


def arena_of_the_wheel():
    os.system('cls')

    print("\n=== ARENA OF THE WHEEL ===")
    print("A massive stone wheel stands in the center of the chamber.")
    print("Beside it sits an enormous figure — the Giant of the Wheel.")
    print("He looks almost peaceful, even friendly.")
    print("His voice is deep and calm when he speaks:")
    print()
    print("Giant: \"You have entered the path of the sun.\"")
    print("Giant: \"I offer you a trial of three riddles.\"")
    print("Giant: \"Answer them all correctly, and you may pass.\"")
    print("Giant: \"Fail even one... and I will crush you.\"")
    print()
    print("Giant: \"There is no victory in fighting me.\"")

    input("\nPress Enter to begin the trial...")

    if not riddle_one():
        start_unwinnable_battle()
        return

    if not riddle_two():
        start_unwinnable_battle()
        return

    if not riddle_three():
        start_unwinnable_battle()
        return

    print("\nThe Giant studies you for a long moment.")
    print("Then he slowly steps aside, placing one massive hand on the wheel.")
    print("Giant: \"You have shown patience... and humility.\"")
    print("Giant: \"Pass.\"")
    print("\nThe path beyond the wheel opens.")
    print("You walk forward and arrive at the Royal Court.")

    input("\nPress Enter to continue...")

    import Royal_Court
    Royal_Court.royal_court()


def riddle_one():
    os.system('cls')
    print("\n=== FIRST RIDDLE ===")
    print("Giant: \"Listen carefully.\"")
    print()
    print("I have cities, but no houses.")
    print("I have mountains, but no trees.")
    print("I have water, but no fish.")
    print("I have roads, but no cars.")
    print()
    print("What am I?")
    print()

    answer = input("Your answer: ").strip().lower()

    if answer in ["a map", "map", "the map"]:
        print("\nGiant: \"Correct.\"")
        return True
    else:
        print("\nGiant: \"Wrong.\"")
        return False


def riddle_two():
    os.system('cls')
    print("\n=== SECOND RIDDLE ===")
    print("Giant: \"Two guardians stand before a wheel.\"")
    print("One always tells the truth.")
    print("One always lies.")
    print("You may ask only one question.")
    print("One path leads to safety. The other leads to death.")
    print()
    print("What single question do you ask to find the safe path?")
    print()
    print("(Type the question you would ask)")

    answer = input("\nYour question: ").strip().lower()

    valid_keywords = [
        "other", "would say", "what would", "if i asked", "the other one",
        "what would the other", "which path would the other"
    ]

    if any(keyword in answer for keyword in valid_keywords):
        print("\nGiant: \"...You understand.\"")
        print("Giant: \"Correct.\"")
        return True
    else:
        print("\nGiant: \"That question would not save you.\"")
        return False


def riddle_three():
    os.system('cls')
    print("\n=== THIRD RIDDLE ===")
    print("Giant: \"The final trial.\"")
    print("Giant: \"A captain once left orders for his crew.\"")
    print("Giant: \"Memorize them. You will not see them again.\"")
    print()
    input("Press Enter when you are ready...")

    os.system('cls')
    print("\nCAPTAIN'S ORDERS:")
    print("\nNorth")
    print("South")
    print("Still")
    print("North")
    print("North")
    print("Still")
    print("East")
    print("\nMemorize them...")
    time.sleep(2)
    os.system('cls')

    print("\nThe orders have vanished.")
    print("Enter the sequence one by one.")
    print("(Valid inputs: north, south, east, west, still)\n")

    correct_sequence = ["north", "south", "still", "north", "north", "still", "east"]
    player_sequence = []

    for i in range(7):
        move = input(f"Step {i + 1}: ").strip().lower()
        player_sequence.append(move)

    if player_sequence == correct_sequence:
        print("\nGiant: \"You remembered.\"")
        print("Giant: \"Correct.\"")
        return True
    else:
        print("\nGiant: \"You forgot the way.\"")
        return False


def start_unwinnable_battle():
    os.system('cls')
    print("\nThe Giant's calm expression fades.")
    print("He rises to his full height. The stone wheel groans behind him.")
    print("Giant: \"Then you have chosen violence.\"")
    print()
    print("You try to fight...")
    print("Your attacks do nothing.")
    print("The Giant moves once.")
    print()
    print("Everything goes dark.")
    print()
    print("========================")
    print("       GAME OVER")
    print("========================")
    print("The Giant of the Wheel cannot be defeated by force.")
    input("\nPress Enter to exit...")
    exit()