from inventory import add_item, remove_item, has_item
import Status


def vantas_diary():
    print("...It looks like Vanta's diary....it's risky but should I leave something?")

    while True:
        print("\n1. Write something")
        print("2. Leave the diary as it is")

        try:
            answer = int(input("\nWhat should I do?"))

            if answer == 1:
                match input(f"Mmmm let's see...").strip().lower():
                    case "kron":
                        print("A sudden breeze echoes thru the room...")
                        add_item("KRON Sword!")
                    case _:
                        print("What am I doing here? Im wasting my time!")

            elif answer == 2:
                print("Yeah, better leave it there")
                break

            else:
                print("Choose either 1 or 2")
                continue

        except ValueError:
            print("Choose a valid action")

def wardrobe():
    print(f"There are many strange garments here...(currently wearing: {Status.current_outfit})")

    while True:
        print("\n1. Dress as King Ethios")
        print("2. Dress as Harry Mason")
        print("3. Dress as Vanta")
        print("4. Dress as Beach clothes")
        print("5. Dress as NFL clothes")
        print("6. Dress as Psychedelic clothes")
        print("7. Dress as David Bowie")
        print("8. Dress as Shadow")
        print("9. Leave the wardrobe")

        try:
            answer = int(input("\nShould I pick..."))

            outfits = {
                1: "King Ethios",
                2: "Harry Mason",
                3: "Vanta",
                4: "Baywatch",
                5: "Joe Montana",
                6: "Jimi Hendrix",
                7: "David Bowie",
                8: "Shadow"
            }
            if answer in outfits:
                Status.current_outfit = outfits[answer]
                print(f"\nYou're now dressed as {Status.current_outfit}!")

            elif answer == 9:
                print("Those garments definitely look weird")
                break
            else:
                print("Please choose a number between 1 and 9.")

        except ValueError:
            print("Please enter a valid action")


def vantas_room():
    print("WOW Vanta's room is very colorful! I've never have thought it was like this!")

    while True:
        print("\n1. Inspect the diary")
        print("2. Inspect the wardrobe")
        print("3. Leave Vanta's Room")

        try:
            answer = int(input("\naction: "))

            if answer == 1:
                vantas_diary()
            elif answer == 2:
                wardrobe()
            elif answer == 3:
                print("Leaving Vanta's Room")
                break
            else:
                print("Choose between 1 and 3.")
        except ValueError:
            print("Enter a valid action")

vantas_room()