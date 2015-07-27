from inventory import Sword, Dagger, SmallPotion, GreatPotion

class Hero:
    def get_weapon(self):
        return self.weapon
    def get_inventory_item(self):
        return self.inventory_item
    def get_life(self):
        return self.life
    def shout(self):
        print(self.shout_phrase)

class Warrior(Hero):
    def __init__(self):
        self.weapon = Sword()
        self.inventory_item = SmallPotion()
        self.life = 5000
        self.shout_phrase = "I am Krull!! The mighty hero"

class Bard(Hero):
    def __init__(self):
        self.weapon = Dagger()
        self.inventory_item = GreatPotion()
        self.life = 3000
        self.shout_phrase = "I am Zig. I am smart and tuned. Care to hear my story?"
