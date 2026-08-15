from inventory import add_item, remove_item, has_item

def statues():
    print("The garden is overgrown and silent. No birds, no wind. "
          "\nIn the center is a stone fountain that is completely dry."
          "\nAround it are four statues of the same woman in different poses.")

    while True:
        print("\n1. Statue of Vision")
        print("2. Statue of Nature")
        print("3. Statue of Time")
        print("4. Statue of Wisdom")
        print("5. Leave the garden for now")

        try:
            answer = int(input("\nWhich statue would you examine? "))

            if answer == 1:
                print("\nIt's a statue of a woman with eyes closed.")

            elif answer == 2:
                print("\nIt's a statue of a woman holding a silver flower that reads:")
                print("\"When the music stops, the garden sleeps.\"")

                if has_item("Dried Flower"):
                    print("\nIt seems that the flower you're carrying can be swapped...")
                    remove_item("Dried Flower")
                    add_item("Silver Flower")
                else:
                    print("\nYou feel like something is missing...")

            elif answer == 3:
                print("\nIt's a statue of a woman looking at a pocket watch.")

            elif answer == 4:
                print("\nIt's a statue of a woman reading an old book.")

            elif answer == 5:
                print("\nYou step away from the garden for now.")
                return

            else:
                print("Please choose a number between 1 and 5.")

        except ValueError:
            print("Please enter a number.")

statues()