x = "Vanta"
place = "Garam"


print(f"{x}: Tell me your name:")
user = input("\nI...I am...")
import Status
Status.user = user

def introduction():

    print("\nIt's been a long time... since the last time."
          "\nit seems like a dream from long ago..."
          "\nso distant yet so clear....everything seems foggy now."
          "\ntime ... time ... there's time ... somehow..."
          "\nEverything seems so quiet, so still."
          "\n")

    print(f"{x}: We were waiting for you, {user}."
          f"Though you're earlier than our estimations...nevertheless, welcome to {place}."
          "\n"
          f"{user}: So...")

    while True:
        print("1. What's this place?"
              "\n2. Am I dreaming?")

        try:
            answer = int(input(""))

            if answer == 1:
                print(
                    f"{x}: This is {place}, a lost place forgotten somewhere between the world of dreams and the waking world.")
                break
            elif answer == 2:
                print(f"{x}: It's curious that you ask such a question."
                      f"What do you think, {user}? Are you dreaming?")
                break
            else:
                print("Select either 1 or 2")
        except ValueError:
            print("Please enter a number.")

    print(f"\n{x}: Well, my dear and beloved wayward wayfarer, "
          f"from now on you're free to explore {place}."
          f"\nRemember that not every door is open to see, "
          f"and not every door has to be opened."
          f"\nI hope you may find interesting memories here."
          f"\nI will come to pick you up when the sun rises."
          f"\nSo... the night is yours.")

introduction()