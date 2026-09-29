from inventory import add_item, remove_item, has_item
import Status

is_figure_approached = False
is_silence_broken = False
is_whisper_heard = False

def silence_room():
    global is_figure_approached, is_silence_broken, is_whisper_heard

    print("\nYou push open a heavy door and step inside.")
    print("The moment the door closes behind you, all sound dies.")
    print("No footsteps. No breathing. Not even the faint crackle of distant torches.")
    print("Dust hangs motionless in the air, as if the room itself is holding its breath.")
    print("In the center sits a single figure, completely still.")

    while True:
        print("\n1. Approach the figure")
        print("2. Listen carefully")
        print("3. Examine the walls")
        print("4. Try to make a sound")
        print("5. Leave the room")

        try:
            answer = int(input("The silence presses against your ears... "))

            if answer == 1:
                if not is_figure_approached:
                    print("\nYou slowly walk toward the center of the room.")
                    print("Your own footsteps make no sound.")
                    print("The figure is a person — or what remains of one — sitting cross-legged.")
                    print("Its eyes are open, but empty. Its mouth is slightly parted, as if mid-sentence.")
                    print("A thin silver chain hangs from its neck, ending in a small, cold medallion.")
                    print("You carefully take the medallion.")
                    add_item("Silent Medallion")
                    print("You obtained 'SILENT MEDALLION'!")
                    is_figure_approached = True
                else:
                    print("\nThe figure remains exactly as you left it.")
                    print("Still. Watching. Silent.")

            elif answer == 2:
                if not is_whisper_heard:
                    print("\nYou close your eyes and listen.")
                    print("At first there is nothing.")
                    print("Then, from somewhere impossibly close, a soft whisper brushes against your mind:")
                    print('"...do not speak here..."')
                    print("The voice fades before you can tell if it was real.")
                    is_whisper_heard = True
                else:
                    print("\nThe silence remains absolute.")
                    print("Whatever spoke before does not speak again.")

            elif answer == 3:
                print("\nThe walls are smooth stone, cold to the touch.")
                print("No carvings. No cracks. No signs of age.")
                print("It feels as if this room was never meant to change.")

            elif answer == 4:
                if not is_silence_broken:
                    print("\nYou clear your throat and speak a single word.")
                    print("The sound feels wrong — too loud, too sharp.")
                    print("For a moment the air seems to thicken.")
                    print("The figure’s head twitches, just slightly.")
                    print("Then the silence returns, heavier than before.")
                    print("You feel as if something is now aware of you.")
                    is_silence_broken = True
                    Status.player_defense -= 5
                    print("You feel strangely exposed... (-5 Defense)")
                else:
                    print("\nYou try again, but the room swallows the sound completely.")
                    print("It is as if the space itself refuses to allow noise anymore.")

            elif answer == 5:
                print("\nYou back away carefully and open the door.")
                print("The moment you step out, ordinary sound rushes back in —")
                print("distant drips, your own breathing, the weight of the dungeons.")
                print("You do not look back.")
                return

        except ValueError:
            print("Choose a valid action.")

silence_room()