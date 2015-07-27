

def intro():
    print("Player, in the sections RH and LH, the numbers 0 - 4 are the amount of damage your weapon does. Nothing = 0; Dagger = 1; Sword = 2; Longsword = 3; Divine sword = 4; Double dagger = 3.")
    nothing = 0
    dagger = 1
    sword = 2
    longsword = 3
    divine_sword = 4
    double_dagger = 3

    one = nothing
    two = dagger
    three = sword
    four = longsword
    five = divine_sword
    six = double_dagger




    HP = 100
    Coins = 0
    RH = one
    LH = one
    #START OF COMMENT - SHOWS HOW MANY HP AND COINS YOU HAVE
    def Status():
        print "You have %s HP and %s Coins!" % (HP, Coins)
        print "Items currently equiped: RH = %s & LH = %s" % (RH, LH)
    print "Do you wanna see your status?"
    answer = raw_input("Y or N? ")
    if answer == "Y":
        Status()
    else:
        print "Ok"
    #END OF COMMENT
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
            answer3 = input("1. Give water or 2. Walk away: ")
            if answer3 == 1:
                print("The old man said: Thanks! It's dangerous to go alone. Take this. RECEIVED 1 DAGGER")
                RH = two
                Status()
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
