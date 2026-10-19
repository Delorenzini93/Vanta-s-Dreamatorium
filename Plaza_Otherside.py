import Status
import os

is_barrel_usable = False

def plaza_otherside():
    global is_barrel_usable
    os.system('cls')
    Status.current_room = "gardens"

    print("You jump out of the boat and now the principal door of the castle is facing you")
    print("There's a hanging barrel used to give and receive stuff from the outside and a bell by its side")

    while True:
        print("1. Ring the bell")
        print("2. Use the hanging barrel")
        print("3. Ride the boat")
        print("4. Check inventory")

        try:
            answer = int(input("> "))
            if answer == 1:
                if Status.jesters_dilemma_solved:
                    print("There's no need for ringing the bell right now")
                elif not is_barrel_usable:
                    print("Though you cannot see him, someone speaks from the other side of the door")
                    print("Workingman: -Hello emissary from the castle, I'm so grateful for being so blessed!")
                    print("My recently born baby has been chosen to receive the ROYAL BLESSING!")
                    print("And...some goods for the winter, as I was told hehe...very grateful sir, many thanks")
                    print("I'll put my child in the barrel so he can be blessed!")
                    is_barrel_usable = True
                else:
                    print("Time is running, I shouldn't ring the bell right now!")
                    return
            elif answer == 2:
                if is_barrel_usable and not Status.carrying_blue_blood_baby:
                    print("You swing the lever and the barrel goes back and forth")
                    print("The workingman's baby is sleeping, now's the chance!")
                    print("You're now carrying the baby the Jester's misplaced...be careful with your movements now")
                    Status.carrying_blue_blood_baby = True
                elif is_barrel_usable and Status.carrying_normal_baby:
                    print("You swing the lever and the barrel goes back and forth")
                    print("The workingman's thanks you once again and goes away with his real baby")
                    print("You're solved the Jester's misplaced babies...time to find them now")
                    Status.carrying_normal_baby = False
                    Status.jesters_dilemma_solved = True
                elif not is_barrel_usable:
                    print("I should let the person from the other side know I'm ready")
                    return
            elif answer == 3:
                print("You ride the boat and slowly sail to the other side")
                return
            elif answer == 4:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action")