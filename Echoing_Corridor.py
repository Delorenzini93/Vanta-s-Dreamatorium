from inventory import add_item, remove_item, has_item
import Status


x = "Gargoyle"
a = "Asmodeus"
b = "Chuculain"
c = "Esthat"

talked_to_gargoyle = False

def echoing_puzzle():
    global talked_to_gargoyle
    print("A small, dead-ended and windowless corridor lies before you.")
    print("By your left there are 3 door each one containig a prisoner soul.")
    print("By your right there's a judging Gargoyle")

    while True:
        print(f"\n1. Speak to the {x}")
        print("2. Speak with closest prisoner")
        print("3. Speak with middle prisoner")
        print("4. Speak with furthest prisoner")
        print("5. Leave the corridor")

        try:
            answer = int(input("\nWhat should I say? "))

            if answer == 1:
                if not talked_to_gargoyle:
                    print(f"{x}: Well, a younger soul, I see...{Status.user}")
                    print("Today you'll be both judge and witness as three wandering souls's fate lie in your hands")
                    print("Talk to them and tell which one of them is the true guilty soul of heinous sins.")
                    talked_to_gargoyle = True

                elif talked_to_gargoyle:
                    print(f"{x}: Who's guilty?")
                    match input("Veredict: ").strip().lower():
                        case "esthat":
                            print("Perfect, I knew it all along")
                            add_item("Signed Veredict")
                        case _:
                            print(f"{x}: You're drifting you're mind away and far from the truth.")
            elif answer == 2:
                print(f"{a}: Long ago there was a fire unintentionally started by one of my brothers.")
                print("He was young and beautiful and attracted a fascination by a peculiar kind of people.")
                print("People from distant villages came to the castle to meet him.")
                print("People could not believe their eyes...nor the fire in his eyes")
                print(f"I, {a} am not guilty of any of this...please spare my soul")
                continue

            elif answer == 3:
                print(f"{b}: He was blind with rage and did heinous things")
                print("So terrible the northern Gods took away his eyes since he didn't see what was before him")
                print("Day after day, my brother fell into a bottomless pit of despite")
                print("He claims to be not guilty....don't believe his lies")
                continue

            elif answer == 4:
                print(f"{c}: I was betrayed just to let people know of his envy, I knew it all along")
                print("Since a young age he was arrogant and envious, I see it crystal clear")
                print("Just as the window from this corridor, his soul was open to all kind of sins")
                print(f"Im not guilty and my name is {c}, I saw {a} starting the fire....the terrible fire")
                continue

            elif answer == 5:
                print("\nYou step away from the echoing corridor for now.")
                return

            else:
                print("Please choose a number between 1 and 5.")
                continue

        except ValueError:
            print("Please enter a number between 1 to 5")

    print("\nYou have found the truth about the Terrible Fire.")

echoing_puzzle()