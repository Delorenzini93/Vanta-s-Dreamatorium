from inventory import add_item, remove_item, has_item
import Status

is_Vanta_spoken = False

def west_hall():
    global is_Vanta_spoken
    if not is_Vanta_spoken:
        print("Vanta: Well {user}, you've come a long way from the castle!")
        print("You'll see that not every dream is what it really is, sin't it?")
        print("Always remember the SONG OF EPITAPHS......")
        print("*Vanta disappears into a thick fog leaving something shiny on the floor*")
        add_item('Autumn Anima')
        print("You obtain AUTUMN ANIMA!")
        is_Vanta_spoken = True
    else:
        print("this seems like a peaceful, slightly out of place corridor in comparison to the rest of the castle")

        while True:
            print("1. Go to the Botanical Classroom")
            print("2. Go to the Weather Forecast Room")
            print("3. Go to the Factory Sabotage Room")
            print("4. Go to the World Heritage Room")
            print("5. Go upstairs")
            print("6. Go back to the Corridor with Many Windows")
            print("7. Check inventory")

            try:
                answer = int(input("Where do we go?"))

                if answer == 1:
                    import Botanical_Classroom
                    Botanical_Classroom.botanical_classroom()
                elif answer == 2:
                    import Weather_Forecast_Room
                    Weather_Forecast_Room.weather_forecast_room()
                elif answer == 3:
                    import Factory_Sabotage_Room
                    Factory_Sabotage_Room.factory_sabotage_room()
                elif answer == 4:
                    import World_Heritage_Room
                    World_Heritage_Room.world_heritage_room()
                elif answer == 5:
                    import West_Hall_2F
                    West_Hall_2F.west_hall_2F()
                elif answer == 6:
                    print("You went to the Corridor with Many Windows")
                    import Corridor_With_Many_Windows
                    Corridor_With_Many_Windows.corridor_with_many_windows()
                elif answer == 7:
                    from inventory import show_inventory
                    show_inventory()

            except ValueError:
                print("Choose a valid action")

west_hall()