from inventory import add_item, remove_item, has_item
import Status
import os

bought_rumor_court = False
bought_milker_info = False
bought_backdoor_key = False
bought_ghost_info = False

def brothel():
    global bought_rumor_court, bought_milker_info, bought_backdoor_key, bought_ghost_info
    os.system('cls')
    Status.current_room = "gardens"

    print("\nYou push aside a heavy curtain and step inside.")
    print("The air is thick with cheap perfume, smoke, and something older.")
    print("Red light stains everything. Conversations die as you enter.")
    print("A woman with cold eyes watches you from behind a dark wooden counter.")

    while True:
        print("\n1. Talk to the Madam")
        print("2. Look around")
        print("3. Check inventory")
        print("4. Leave the Brothel")

        try:
            answer = int(input("\nWhat do you want? "))

            if answer == 1:
                talk_to_madam()
            elif answer == 2:
                print("\nSeveral figures sit in the shadows.")
                print("None of them look at you for free.")
            elif answer == 3:
                from inventory import show_inventory
                show_inventory()
            elif answer == 4:
                print("You step back into the street.")
                return
            else:
                print("Choose a valid option.")

        except ValueError:
            print("Choose a valid action.")


def talk_to_madam():
    global bought_rumor_court, bought_milker_info, bought_backdoor_key, bought_ghost_info

    print("\nThe Madam looks at you without smiling.")
    print("Madam: \"Everything here has a price. What are you looking for?\"")

    while True:
        print("\n--- Services ---")
        print("1. Rumor about the Royal Court          (3000 souls)")
        print("2. Information about the Milker         (5000 souls)")
        print("3. Backdoor Key to the Royal Wing       (1 Royal Badge)")
        print("4. What do you know about the Ghost?    (2000 souls)")
        print("5. Never mind")

        try:
            choice = int(input("\nChoose a service: "))

            if choice == 1:
                if bought_rumor_court:
                    print("Madam: \"You already paid for that.\"")
                elif Status.souls >= 3000:
                    Status.souls -= 3000
                    bought_rumor_court = True
                    print("\nMadam: \"The King has been... unsettled lately.\"")
                    print("Madam: \"They say the blood ceremony will reveal more than anyone expects.\"")
                    print("You obtained information about the Royal Court.")
                else:
                    print("Madam: \"Come back when you can afford it.\"")

            elif choice == 2:
                if bought_milker_info:
                    print("Madam: \"You already know what I told you.\"")
                elif Status.souls >= 5000:
                    Status.souls -= 5000
                    bought_milker_info = True
                    print("\nMadam: \"The man they call the Milker still lives near the old wells.\"")
                    print("Madam: \"He has a child he has no right to keep. That's all I'll say.\"")
                    print("You obtained information about the Milker.")
                else:
                    print("Madam: \"That secret is expensive.\"")

            elif choice == 3:
                if bought_backdoor_key:
                    print("Madam: \"I already gave you the key.\"")
                elif has_item("Royal Badge"):
                    remove_item("Royal Badge")
                    add_item("Backdoor Key")
                    bought_backdoor_key = True
                    print("\nMadam: \"This opens a service door into the Royal Wing.\"")
                    print("Madam: \"Don't tell anyone where you got it.\"")
                    print("You obtained 'BACKDOOR KEY'!")
                else:
                    print("Madam: \"I need a Royal Badge for that. Nothing else will do.\"")

            elif choice == 4:
                if bought_ghost_info:
                    print("Madam: \"I already told you what I know.\"")
                elif Status.souls >= 2000:
                    Status.souls -= 2000
                    bought_ghost_info = True
                    print("\nMadam: \"There's something in the Ballroom that doesn't like to be disturbed.\"")
                    print("Madam: \"The more you touch, the more it remembers you.\"")
                    print("You obtained information about the Ghost.")
                else:
                    print("Madam: \"Even whispers cost money here.\"")

            elif choice == 5:
                print("Madam: \"Don't waste my time.\"")
                return

            else:
                print("Invalid choice.")

        except ValueError:
            print("Choose a valid number.")