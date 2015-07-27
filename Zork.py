

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
                print ("You arrived the village at 10:56 pm and it was raining. There's a (hotel?) to your left, a store towards you and a tavern by your right.")
                print ("Where would you like to go?: ")
                answer4 = input("1. Hotel; 2.Store; 3.Tavern")
                if answer4 == 1:
                    print("There was a woman inside. She says: Would you like to rest? 10 coins.")
                    answer_Hotel1 = raw_input("Would you like to rest? (Recovers 10HP): ")
                    if answer_Hotel1 == "Yes":
                        if Coins > 10:
                            if HP < 100:
                                print("You rested and recovered 10 HP")
                                Coins -= 10
                                HP += 10
                                Status()
                            else:
                                print("You don't need to rest.")
                        else:
                            print("Sorry, you need more money!")
                    else:
                        print("Ok then.")

                elif answer4 == 2:
                    print("There was a man inside. He says: Hay mate. Would you like to buy some gear?")





                elif answer4 == 3:
                    print("It was crowded. There was a paper hanging on the wall that said that the beer was 2 coins. Drink one?")




        elif answer2 == 2:
            print("You found a chest with 20 coins in it and you followed a path to a village.")
            Coins += 20
            Status()
            print ("You arrived the village at 10:56 pm and it was raining. There's a (hotel?) to your left, a store towards you and a tavern by your right.")
            print ("Where would you like to go?: ")
            answer4 = input("1. Hotel; 2.Store; 3.Tavern")
            if answer4 == 1:
                print("There was a woman inside. She says: Would you like to rest? 10 coins.")
                answer_Hotel1 = raw_input("Would you like to rest? (Recovers 10HP): ")
                if answer_Hotel1 == "Yes":
                    if Coins > 10:
                        if HP < 100:
                            print("You rested and recovered 10 HP")
                            Coins -= 10
                            HP += 10
                            Status()
                        else:
                            print("ERROR: FULL HP")
                    else:
                        print("Sorry, you need more money!")
                else:
                    print("Ok then.")

            elif answer4 == 2:
                print("There was a man inside. He says: Hay mate. Would you like to buy some gear?")





            elif answer4 == 3:
                print("It was crowded. There was a paper hanging on the wall that said that the beer was 2 coins. Drink one?")

        else:
            print("Do something!")
































    elif answer == 2:
        print("Nothing happened.")
        intro()
    else:
        print("...")
        intro()

intro()
