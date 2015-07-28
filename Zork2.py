class Weapon:
    # The weapon code. Used to select the weapon
    def get_code(self):
        return self.code
    # The damage the weapon can inflict
    def get_damage(self):
        return self.damage
    # The weapon durability. When the user uses the weapon it will loose durability
    def get_durability(self):
        return self.durability
    # The magical damage the weapon can inflict
    def get_magical_damage(self):
        return self.magical_damage
    # The maximum range the weapon can reach (in meters)
    def get_attack_range(self):
        return self.attack_range



class Nothing(Weapon):
    def __init__(self):
        self.code = 0
        self.damage = 1
        self.durability = 99999
        self.magical_damage = 0
        self.attack_range = 0.5


class Dagger(Weapon):
    def __init__(self):
        self.code = 1
        self.damage = 5
        self.durability = 300
        self.magical_damage = 0
        self.attack_range = 1.5
class LongSword(Weapon):
    def __init__(self):
        self.code = 3
        self.damage = 12
        self.durability = 700
        self.magical_damage = 0
        self.attack_range = 2.5
class Sword(Weapon):
    def __init__(self):
        self.code = 2
        self.damage = 10
        self.durability = 1000
        self.magical_damage = 0
        self.attack_range = 2
class DivineSword(Weapon):
    def __init__(self):
        self.code = 2
        self.damage = 10
        self.durability = 400
        self.magical_damage = 5
        self.attack_range = 1.5

class HealingItem:
    def get_healing_points(self):
        return self.healing_points
class SmallPotion(HealingItem):
    def __init__(self):
        self.healing_points = 20
class MediumPotion(HealingItem):
    def __init__(self):
        self.healing_points = 60
class LargePotion(HealingItem):
    def __init__(self):
        self.healing_points = 120
class GreatPotion(HealingItem):
    def __init__(self):
        self.healing_points = 200
########################################### Item section ---> char section
class Character:
    def get_life(self):
        return self.life
    def get_righthand(self):
        return self.righthand
    def get_lefthand(self):
        return self.lefthand
    def get_inventory(self):
        return self.inventory

class Player(Character):
    def __init__(self):
        self.life = 100
        self.righthand = Dagger
        self.lefthand = Nothing
        self.inventory = {}



def Status():
    print("You have %s HP, %s equipped in your RH, %s equipped in your LF and %s in your inventory.") % (Player().life, Player().righthand, Player().lefthand, Player().inventory)





print("Welcome to Zork, a text based game.")
Status()
