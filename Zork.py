HP = 90
def intro():
    HP = 100
    print("Player, in the sections RH and LH, the numbers 0 - 4 are the amount of damage your weapon does. Nothing = 0; Dagger = 1; Sword = 2; Longsword = 3; Divine sword = 4; Double dagger = 3.")
    nothing = 0
    dagger = 1
    sword = 2
    longsword = 3
    divine_sword = 4
    double_dagger = 3
    small_potion = HP + 10
    map1 = "It shows the map of the village and a castle towards it."

    one = nothing
    two = dagger
    three = sword
    four = longsword
    five = divine_sword
    six = double_dagger
    seven = small_potion
    eight = map1




    HP = 100
    Coins = 0
    RH = one
    LH = one
    Inventory = {"small_potion" : 0, "maps" : 0}
    #START OF COMMENT - SHOWS HOW MANY HP AND COINS YOU HAVE
    def Status():
        print "You have %s HP and %s Coins!" % (HP, Coins)
        print "Items currently equiped: RH = %s & LH = %s" % (RH, LH)
        print "Items in inventory: %s. " % (Inventory)
    print "Do you wanna see your status?"
    answer = raw_input("Y or N? ")
    if answer == "Y":
        Status()
    else:
        print "Ok"
    #END OF COMMENT
    #Start of new function UseItem
    def UseItem():
        global HP
        print Inventory
        Choice = raw_input("Which item do you want to use?: ")
        if Choice == "small_potion":
            if Inventory["small_potion"] > 0:
                if HP <= 90:
                    HP += 10
                    Inventory["small_potion"] -= 1
                    print Inventory
                    Status()
    #END OF FUNCTION














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
                if answer4 == 1:#Hotel
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

                elif answer4 == 2: #Store
                    print("There was a man inside. He says: Hay mate. Would you like to buy some gear?")
                    answer_Shop1 = input("1.Yes, 2.No: ")
                    items = ["Dagger, Small Potion, Map"]
                    if answer_Shop1 == 1:
                        print items
                        print("What would you like to buy?")
                        buyChoice = input("1. Dagger, 2.Potion, 3.Map: ")
                        if buyChoice == 1:
                            Shop1 = raw_input("So you wanna buy a Dagger. 3 coins.")
                            if Shop1 == "Yes":
                                if Coins >= 3:
                                    handChoice = raw_input("You bought it. In which hand do you want to equip it?: ")
                                    if handChoice == "RH":
                                        RH = two
                                    else:
                                        LF = two
                                        Status()
                        elif buyChoice == 2:
                            Shop2 = raw_input("2 coins: ")
                            if Shop2 == "Yes":
                                if Coins >= 2:
                                    Inventory["small_potion"] = 1
                                    Status()
                                    UseItem()

                        elif buyChoice == 3:
                            print("wait")






                    elif answer4 == 3:#Tavern
                        print("It was crowded. There was a paper hanging on the wall that said that the beer was 2 coins. Drink one?")




        elif answer2 == 2:
            print("You found a chest with 20 coins in it and you followed a path to a village.")
            Coins += 20
            Status()
            print ("You arrived the village at 10:56 pm and it was raining. There's a (hotel?) to your left, a store towards you and a tavern by your right.")
            print ("Where would you like to go?: ")
            answer4 = input("1. Hotel; 2.Store; 3.Tavern")
            if answer4 == 1: #Hotel
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

            elif answer4 == 2:#Store
                print("There was a man inside. He says: Hay mate. Would you like to buy some gear?")
                answer_Shop1 = input("1.Yes, 2.No: ")
                items = ["Dagger, Small Potion, Map"]
                if answer_Shop1 == 1:
                    print items
                    print("What would you like to buy?")
                    buyChoice = input("1. Dagger, 2.Potion, 3.Map: ")
                    if buyChoice == 1:
                        Shop1 = raw_input("So you wanna buy a Dagger. 3 coins.")
                        if Shop1 == "Yes":
                            if Coins >= 3:
                                handChoice = raw_input("You bought it. In which hand do you want to equip it?: ")
                                if handChoice == "RH":
                                    RH = two
                                else:
                                    LF = two
                    elif buyChoice == 2:
                        Shop2 = raw_input("2 coins")
                        if Shop2 == "Yes":
                            if Coins >= 2:
                                Inventory["small_potion"] = 1
                                Coins -= 2
                                Status()
                                UseItem()
                                print Inventory


                    elif buyChoice == 3:
                        print "Gaben"




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
