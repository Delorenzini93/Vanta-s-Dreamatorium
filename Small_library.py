Book_of_Vision = False
Book_of_Nature = False
Book_of_Time = False
Book_of_Wisdom = False
read_all_books = False
has_dried_flower = False


def reading_of_books():
    global Book_of_Vision, Book_of_Nature, Book_of_Time, Book_of_Wisdom
    global read_all_books, has_dried_flower

    print("\n\"Time is still, yet it moves when you are not looking.\"\n")

    while not read_all_books:
        print("1. Book of Vision")
        print("2. Book of Nature")
        print("3. Book of Time")
        print("4. Book of Wisdom")
        print("5. Leave the books for now")

        try:
            answer = int(input("\nWhich book should you take a look at? "))

            if answer == 1:
                print("\n'She closed her eyes and the world went quiet.'")
                Book_of_Vision = True
            elif answer == 2:
                print("\n'The garden remembers what the house forgot.'")
                Book_of_Nature = True
            elif answer == 3:
                print("\n'The clock stopped at the moment the music began.'")
                Book_of_Time = True
            elif answer == 4:
                print("\n'Every story ends the same way if you read it backwards.'")
                Book_of_Wisdom = True
            elif answer == 5:
                print("\nYou step away from the shelves for now.")
                return
            else:
                print("Please choose a number between 1 and 5.")
                continue


            if Book_of_Vision and Book_of_Nature and Book_of_Time and Book_of_Wisdom:
                read_all_books = True
                print("\nAs you close the last book, something shifts on the shelf...")
                print("There's an old and rusty volume that wasn't there before.")
                print("Its title is barely legible: 'Book of the Forgotten'.")
                print("Inside, a dried flower is pressed between two yellowed pages.")
                print("\nNew item obtained: DRIED FLOWER")
                has_dried_flower = True

        except ValueError:
            print("Please enter a number.")

    print("\nYou have found everything the library is willing to give you... for now.")

reading_of_books()