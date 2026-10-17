from inventory import add_item, remove_item, has_item
import Status
import os

def weather_forecast_room():
    os.system('cls')
    Status.current_room = "west_hall"

    print("\nYou enter the Weather Forecast Room.")
    print("The walls are covered in old charts, broken barometers, and dials that spin for no reason.")
    print("In the center stands a large, absurd machine covered in copper pipes and glass globes.")
    print("A faded sign reads: \"RAIN MAKER – AUTHORIZED PERSONNEL ONLY\"")
    print("Someone has handwritten underneath: \"or very bored people\"")

    while True:
        print("\n1. Examine the Rain Machine")
        print("2. Look at the forecast boards")
        print("3. Check the current weather status")
        print("4. Leave the room")

        try:
            answer = int(input("\nThe dials keep spinning... "))

            if answer == 1:
                print("\nThe Rain Machine is a mess of pipes, levers, and a large red button.")
                print("It looks both dangerous and slightly stupid.")

                if Status.is_raining:
                    print("\nThe machine is currently running. You can hear distant rain outside.")
                    print("1. Turn it off")
                    print("2. Leave it alone")
                    choice = int(input("> "))
                    if choice == 1:
                        print("\nYou pull the main lever. The machine shudders and stops.")
                        print("The sound of rain slowly fades.")
                        Status.is_raining = False
                else:
                    print("\n1. Activate the Rain Machine")
                    print("2. Better not touch it")
                    choice = int(input("> "))
                    if choice == 1:
                        print("\nYou press the large red button.")
                        print("The machine coughs, sparks, and starts humming loudly.")
                        print("Through the window, you see dark clouds gathering unnaturally fast...")
                        print("It begins to rain over the castle.")
                        Status.is_raining = True

            elif answer == 2:
                print("\nThe forecast boards show mostly impossible predictions:")
                print("- \"Light blood drizzle over the throne room\"")
                print("- \"Fog of mild regret in the afternoon\"")
                print("- \"Clear skies with a chance of consequences\"")
                print("- \"Thunderstorm of unwanted memories (overnight)\"")
                print("- \nROYAL GUARDS DONT WORK WHEN IT RAINS")
                print("\nNone of them seem trustworthy.")

            elif answer == 3:
                if Status.is_raining:
                    print("\nCurrent status: It is raining over the castle.")
                    print("Some people might have sought shelter...")
                else:
                    print("\nCurrent status: The sky is clear (for now).")

            elif answer == 4:
                print("You leave the strange weather station.")
                return

        except ValueError:
            print("Choose a valid action.")