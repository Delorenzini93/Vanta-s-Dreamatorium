from inventory import add_item, remove_item, has_item
import Status
import os

jester_stage = 0
ton_last_answer = None
items_given = False

def jesters_room():
    os.system('cls')
    Status.current_room = "west_hall"
    global jester_stage, ton_last_answer, items_given

    print("\nYou enter a colorful but messy room.")
    print("Two jesters are here — Zon and Ton.")
    print("They both freeze when they see you, exchanging a nervous glance.")

    while True:
        print("\n1. Talk to Ton")
        print("2. Talk to Zon")
        print("3. Listen to them")
        print("4. Leave the room")
        print("5. Check inventory")

        try:
            answer = int(input("> "))

            if answer == 1:
                talk_to_ton()
            elif answer == 2:
                talk_to_zon()
            elif answer == 3:
                listen_to_them()
            elif answer == 4:
                print("You leave the jesters' room.")
                return
            elif answer == 5:
                from inventory import show_inventory
                show_inventory()

        except ValueError:
            print("Choose a valid action.")


def talk_to_ton():
    global jester_stage, ton_last_answer, items_given

    print("\nYou approach Ton. He forces a wide smile.")

    if Status.is_blue_blood_baby:
        print('Ton: "You actually did it... the babies are back where they belong."')
        print('Ton: "We owe you our lives."')
        if not has_item("Jesters Gun"):
            add_item("Jesters Gun")
            print("You obtained 'JESTERS GUN'!")
        return

    if jester_stage == 0:
        print('Ton: "Ah, a visitor! Want to hear a joke? Or... do you prefer serious matters?"')
        print("1. Tell me a joke")
        print("2. I prefer serious matters")
        print("3. Say nothing")

        choice = int(input("> "))
        if choice == 2:
            print('Ton: "...Serious matters? Heh. Dangerous words in this castle."')
            ton_last_answer = "serious"
            jester_stage = 1
        else:
            print('Ton: "Suit yourself!" He tells a bad joke and laughs too loudly.')

    elif jester_stage == 1:
        print('Ton: "Tell me something... What color do you think royal blood should be?"')
        print("1. Blue, of course")
        print("2. Red, like everyone else")
        print("3. I don’t know")

        choice = int(input("> "))
        if choice == 1:
            print('Ton: "Yes... blue. It *should* be blue." His smile wavers.')
            ton_last_answer = "blue"
            jester_stage = 2
        elif choice == 2:
            print('Ton: "Red?! Don\'t say that so loudly!"')
            ton_last_answer = "red"
        else:
            print('Ton: "Smart. Sometimes it\'s better not to know."')

    elif jester_stage == 2:
        print('Ton: "We... may have made a small mistake. A delivery mistake."')
        print("1. What kind of mistake?")
        print("2. I don’t want to know")

        choice = int(input("> "))
        if choice == 1:
            print('Ton: "The kind that gets jesters executed if the King finds out..."')
            ton_last_answer = "mistake"
            jester_stage = 3
        else:
            print('Ton looks relieved and changes the subject.')

    elif jester_stage == 3:
        print('Ton: "We were supposed to give the blue-blooded baby to the King..."')
        print('Ton: "...and the common one to a poor man in town."')
        print('Ton: "But we mixed them up."')
        print("He looks at the floor, terrified.")
        jester_stage = 4

    elif jester_stage >= 4:
        if not items_given:
            print('Ton: "Please... you have to help us."')
            print('Ton: "Take these."')
            print("He hands you an ornate key and a strange firework.")
            add_item("Kings Chamber Key")
            add_item("Firework")
            print("You obtained 'KINGS CHAMBER KEY'!")
            print("You obtained 'FIREWORK'!")
            print('Ton: "The key opens the King’s private chamber."')
            print('Ton: "And if you send the firework from the right place, the castle will prepare special gifts for newborn babies..."')
            print('Ton: "That should draw the milker out. He’s the father of the real blue-blooded child."')
            items_given = True
        else:
            print('Ton: "You already have what you need... please hurry."')


def talk_to_zon():
    global jester_stage, ton_last_answer, items_given

    print("\nYou approach Zon. He narrows his eyes.")

    if Status.is_blue_blood_baby:
        print('Zon: "I still can’t believe you fixed our mess."')
        print('Zon: "Maybe you’re not as useless as you look."')
        return

    if jester_stage == 0:
        print('Zon: "What do you want? If Ton already bored you with jokes, leave us alone."')

    elif jester_stage == 1:
        if ton_last_answer == "serious":
            print('Zon: "He talked about serious matters? That idiot never knows when to shut up."')
        else:
            print('Zon: "Ton talks too much. Ignore him."')

    elif jester_stage == 2:
        if ton_last_answer == "blue":
            print('Zon: "Blue blood, huh? He’s getting reckless..."')
            print('Zon: "Some things should stay buried."')
        else:
            print('Zon: "Stop asking strange questions. It’s dangerous."')

    elif jester_stage == 3:
        print('Zon: "So he told you about the mistake."')
        print('Zon: "Yes, we swapped the babies. The King has the wrong one."')
        print('Zon: "And the real blue-blooded child is living with a poor man."')
        print("He looks furious... and scared.")

    elif jester_stage >= 4:
        if not items_given:
            print('Zon: "Ton will give you what you need."')
            print('Zon: "Just fix this before the blood ceremony... or we all die."')
        else:
            print('Zon: "You have the key and the firework. Don’t waste time."')


def listen_to_them():
    global jester_stage

    print("\nYou stay quiet and listen.")

    if Status.is_blue_blood_baby:
        print("Zon and Ton look much calmer than before.")
        print("They even share a quiet, relieved smile.")
        return

    if jester_stage < 2:
        print("Zon and Ton whisper anxiously to each other, but stop the moment they notice you watching.")
    elif jester_stage == 2 or jester_stage == 3:
        print('Ton: "We have to tell someone..."')
        print('Zon: "Are you insane? They’ll kill us!"')
    else:
        print("Both jesters are silent now, waiting for you to act.")