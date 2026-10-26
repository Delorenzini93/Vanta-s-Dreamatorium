from inventory import add_item, remove_item, has_item
import Status
import os

is_knight_at_table = False
is_knight_down = False
is_bar_puzzle_done = False

def bar():
    global is_knight_at_table, is_knight_down, is_bar_puzzle_done
    os.system('cls')
    Status.current_room = "gardens"

    print("\nThe bar is very crowded and what sounds like Far-Eastern music is in the air")

    while True:
        print("1. Go talk to the bartender")
        print("2. Sit on an empty table")
        print("3. Go upstairs")
        print("4. Leave the Bar")
        print("5. Check inventory")

        try:
            answer = int(input("> "))
            if answer ==1:
                if is_knight_down:
                    print("I should leave this place as soon as possible before I get caught")
                    return
                elif is_knight_at_table:
                    print("I should hurry and take advantage of that drunk Knight right now")
                    return
                elif not is_knight_at_table:
                    print("The bartender is serving a tall, loud-talking Knight")
                    print("Knight:-Hey you! Im sure I could crush you in a fist fight, you wimp!")
                    while True:
                        print("1. Bring it on!")
                        print("2. You seem pretty inebriated, why dont we sit and talk over that table?")
                        try:
                            answer=int(input("> "))
                            if answer==1:
                                print("Waiter:-Hey, this is no place for fights!")
                                print("Why dont you go and sit CALMLY at the table over there?")
                                is_knight_at_table = True
                                return
                            elif answer==2:
                                print(" yeah....wa...waaa..waaa (knight mumbles incomprehensible words)")
                                is_knight_at_table = True
                                return
                        except ValueError:
                            print("Choose a valid action")
            elif answer==2:
                if is_knight_down:
                    print("I should leave this place as soon as possible before I get caught")
                    return
                elif is_knight_at_table:
                    print("Knight:-Sooooo.....you were telling me about.....ABOUT WHAT, YOU PUNK??")
                    while True:
                        print("1. I don't like your face. Let's have a fight right now!")
                        print("2. That guy over there thinks you're a chicken. Let's pick a fight with him!")
                        print("3. Don't you hate this Eastern-sounding music? Let's destroy the jukebox!")
                        print("4. Tell him a fictional story in which you are a heaven-sent messiah")
                        print("5. Tell him about space time travels")
                        print("6. Ask the waiter to serve the Knight more alcohol")
                        try:
                            answer=int(input("> "))
                            if answer==1:
                                print("Nice try.")
                                print("No, don't do it.")
                                print("It'll be the stupidest action you have taken so far.")
                            elif answer==2:
                                print("No. Don't do that.")
                                print("This is not GTA and doing that is not going to help you on your way to the Royal Court")
                            elif answer==3:
                                print("Though disliking this particular kind of music is completely understandable")
                                print("Do you actually think this action is going to help you get into the Royal Court?")
                            elif answer == 4:
                                print("What's your problem with telling people you're a Messiah?")
                                print("You're not a Messiah, you're not drunk and the guy in front of you is...use it at your advantage")
                            elif answer==5:
                                print("Dude, just choose option 6 and knock it off!")
                            elif answer==6:
                                print("The knight gets even more drunk (which is quite remarkable, judging his previous inebriated state)")
                                print("Knight: Ehhh....waaaaa.....waaaaa (it's a medical miracle this guys still manages to exist in this state)")
                                print("Waiter:-Why dont you take him upstairs? Seems about to lose consciousness")
                                is_knight_down = True
                                return
                        except ValueError:
                            print("Choose a valid action")
                elif not is_knight_at_table:
                    print("Seems a little awkward to sit alone at a table, isn't it?")
            elif answer==3:
                if is_bar_puzzle_done:
                    print("Let's better leave this place soon")
                    return
                if is_knight_down:
                    print("You leave the unconscious Knight in a dinghy bed")
                    while True:
                        print("1. Yes")
                        print("2. No, it's not morally or ethical acceptable")
                        try:
                            answer=int(input("Do you want to steal his ROYAL BADGE?"))
                            if answer==1:
                                add_item('Royal Badge')
                                print("You obtain ROYAL BADGE!")
                                print("You can now access the Royal Court!")
                                is_bar_puzzle_done = True
                                return
                            elif answer==2:
                                print("You just intentionally got unconscious an innocent in order to steal his badge")
                                print("No time for morals right now")
                                add_item('Royal Badge')
                                print("You obtain ROYAL BADGE!")
                                print("You can now access the Royal Court!")
                                is_bar_puzzle_done = True
                                return
                        except ValueError:
                            print("Choose a valid action")
                else:
                    print("This room is empty.")
                    print("Seems like a good place to put an inebriated knight in order to steal his badge in order to access the Royal Court, isn't it?")
                    return
            elif answer==4:
                print("You go back to the Plaza")
                return
            elif answer==5:
                from inventory import show_inventory
                show_inventory()
        except ValueError:
            print("Choose a valid action.")