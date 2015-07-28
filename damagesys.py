class Fighter:
    def __init__(self, hp, attack):
        self.hp = hp
        self.attack = attack

fighter1 = Fighter(10, 5)
fighter2 = Fighter(20, 2)



def fight():
    print("//FIGHT//")
    while fighter1.hp > 0 and fighter2.hp > 0:
        fighter1.hp -= fighter2.attack
        fighter2.hp -= fighter1.attack
        print fighter1.hp
        print fighter2.hp

fight()
