class Players:
	def __init__(self, maxhp, battlehp, attack, coins):
		self.coins = coins
		self.maxhp = maxhp
		self.attack = attack
		self.battlehp = battlehp



class Warrior:
	def __init__(self, hp, attack):
		self.hp = hp
		self.attack = attack



class WildBeast:
	def __init__(self, hp, attack):
		self.hp = hp
		self.attack = attack


########################## - Classes

########################## - Alive stuff
Player = Players(10, 10, 2, 0)
Skeleton = Warrior(5, 1)
Dog = WildBeast(3, 1)
Wolf = WildBeast(6, 2)
########################## - Alive stuff

########################## - Functions
def lvlup():
	if Dog.hp or Wolf.hp or Skeleton.hp < 0:
		Player.maxhp += 1
		Player.attack += 1






print("Welcome to Zork, a text based game")
Choice1 = input("You're facing a forest and there's a note on the ground ; 1. Enter forest ; 2.Grab note")
if Choice1 == 1:
	print ("A wild dog attacked you!")
	print ("Entering Battle Mode")
	while Dog.hp > 0:
		Dog.hp -= Player.attack
		Player.battlehp -= Dog.attack
		print Dog.hp
	lvlup()
	print(Player.maxhp, Player.battlehp, Player.attack, Player.coins)
	print('Done, you defeated the beast and walked North.')
elif Choice1 == 2:
	Player.coins += 20
	print("This is worth 20 coins!")
	print("You walked into the forest where you found a statue, where you could read: 'Someone died here a long time ago and his wealth was barried somewhere around here'.")
	print("By the moment had finished reading, a wolf jumped and atacked you!")








