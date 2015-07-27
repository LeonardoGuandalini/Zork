

def intro():
    HP = 100
    Coins = 0

    def Status():
        print "You have %s HP and %s Coins!" % (HP, Coins)

    print "Do you wanna see your status?"
    answer = raw_input("Y or N? ")
    if answer == "Y":
        Status()
    else:
        print "Ok"
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
        if answer2 == 1:
            print("The man said: There's a small village 40 km from here. Also, could you give me some water?")
        elif answer2 == 2:
            print("You found a chest with 20 coins in it")
            Coins += 20
            Status()
        else:
            print("Do something!")




    elif answer == 2:
        print("Nothing happened.")
        intro()
    else:
        print("...")
        intro()


intro()
