entity = "Vanta"
trust_points = 0

 # ====================== T R U S T ==================
def introduccion():
    print("Welcome to T_R_U_S_T, a game in which you answer questions and gain trust points from your answers.")
    print("Gather as much trust points as possible in order to escape the eternal limbo!")
    print("")
    print("               * * * * *                ")
    print("")
    print(f"{entity}: - Hello distant wayfarer, tell me your name:...")
    username = input("Enter your name: ")
    print(f"{entity}: - So you're that {username} every soul is talkin' about latelly, I see...")
    print(f"Tell me {username}, what brings you here?")
    return username

################################################################################
def pregunta_A(username):
    global trust_points

    while True:
        print("1 - I probably just died, I guess")
        print("2 - I really don't know")
        print("3 - None of your business")
        print("4 - What's this place, exactly?")

        try:
            answer_A = int(input("your answer: "))

            if answer_A == 1:
                print(f"{entity}: You may be right...")
                trust_points += 2
                break
            elif answer_A == 2:
                print(f"{entity}: I see...")
                break
            elif answer_A == 3:
                print(f"{entity}: I would be cautious if I were you...")
                trust_points -= 1
                break
            elif answer_A == 4:
                print(f"{entity}: Don't worry, you've come to the right place...")
                trust_points += 1
                break
            else:
                print("please choose a valid option")
        except ValueError:
            print("Please enter a number.")

####################################################################################
def pregunta_B(username):
    global trust_points
    print(f"{entity}: How've come a long way to get here, where do you come from {username}?")

    while True:
        print("1 - I come from Earth")
        print("2 - I come from Mars")
        print("3 - I come in peace")
        print("4 - I wanna go home")

        try:
            answer_B = int(input("your answer is: "))

            if answer_B == 1:
                print(f"{entity}: You do, you do...")
                trust_points += 1
                break
            elif answer_B == 2:
                print(f"{entity}: I see Elon Musk finally acomplished his goals...")
                break
            elif answer_B == 3:
                print(f"{entity}: Don't worry, you're safe {username}...")
                trust_points += 2
                break
            elif answer_B == 4:
                print(f"{entity}: You've made too much mistakes in the past to simply walk away like this.")
                trust_points -= 1
                break
            else:
                print("please choose a valid option")
        except ValueError:
                print("Please enter a number.")

####################################################################################
def intermezzo(username):
    print(f"{entity}: It's time to listen to the ancient wisdom of a song, {username}")
    while True:
        print("1 - Ice")
        print("2 - Fire")

        try:
            answer_intermezzo = int(input("Iwant to hear the song of..."))

            if answer_intermezzo == 1:
                print("You hear the Song of Ice")
                break
            elif answer_intermezzo == 2:
                print("You hear the Song of Fire")
                break
            else:
                print("please choose a valid option")
        except ValueError:
            print("Please enter a number.")
######################################################################################
def pregunta_C(username):
    global trust_points
    print(f"{entity}: Finally, are you afraid of death?")

    while True:
        print("1 - I certainly am")
        print("2 - I do not")
        print("3 - Am I already dead?")
        print("4 - I don't care at this point, to be honest...")

        try:
            answer_C = int(input("your answer is: "))

            if answer_C == 1:
                print(f"{entity}: That proves you're human after all")
                trust_points += 2
                break
            elif answer_C == 2:
                print(f"{entity}: Dishonesty will not get you far {username}")
                trust_points -= 1
                break
            elif answer_C == 3:
                print(f"{entity}: Probably")
                trust_points += 1
                break
            elif answer_C == 4:
                print(f"{entity}: You should, believe me you really should")
                break
            else:
                print("please choose a valid option")
        except ValueError:
                print("Please enter a number.")

#################################################################
def ending():
        if -3 <= trust_points <= 0:
            print("You die in a gruesome way")
        elif 0 <= trust_points <= 5:
            print("You've been ascended to the high heavens")
        else:
            print("You become a GOD")
##################################################################
username = introduccion()
pregunta_A(username)
pregunta_B(username)
intermezzo(username)
pregunta_C(username)
ending()

print("Thanx 4 playin'!")