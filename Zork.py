def intro():
    print("West Side")
    print("You're in a house and there's a path to your left")
    print("1. Follow Path")
    print("2.Shout")
    answer = input("You will: ")
    if answer == 1:
        print("You followed the path and found an old man sitting next to a rock. He seems tired")
        print("1. Talk to man")
        print("2. Keep walking")
        answer2 = input("Chose a valid option: ")
    elif answer == 2:
        print("Nothing happened.")
    else:
        print("...")




intro()
