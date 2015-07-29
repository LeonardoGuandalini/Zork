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

########################## - 'Alive stuff'
Player = Players(10, 10, 2, 0)
Skeleton = Warrior(5, 1)
Dog = WildBeast(3, 1)
Wolf = WildBeast(6, 2)
GiantSpider = WildBeast(20, 2)
########################## - Alive stuff
########################## - Functions
def lvlup():
	if Dog.hp or Wolf.hp or Skeleton.hp < 0:
		Player.maxhp += 1
		Player.attack += 1


def usePotion():
	if Player.battlehp != Player.maxhp:
		playerInventory['potion'] -= 1
		print playerInventory
		Player.battlehp = Player.maxhp





playerInventory = {'potion': 1}


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
	print("MAXHP, CURRENT HP, ATTACK, COINS")
	print(Player.maxhp, Player.battlehp, Player.attack, Player.coins)
	print('Done, you defeated the beast and walked North.')
	print("After that, you entered a cave, where there was an old man. You couldn't see him very, because of the fog. ")
	Choice2 = input("Your options are: 1.Explore cave and use potion ; 2.Talk to old  ")
	if Choice2 == 1:
		usePotion()
		chestChoice1 = input("Open chest?: 1.Yes 2.No")
		if chestChoice1 == 1:
			Player.attack += 3
			print('You found a sword! +3 attack; You went back to the cave and  you talked to the old man, and he started to transform into a giant spider, and attacked you!')
			while GiantSpider.hp >= 0 and Player.battlehp >= 0:
				GiantSpider.hp -= Player.attack
				Player.battlehp -= GiantSpider.attack
				if Player.battlehp <= 0:
					print("Game Over -- You might consider using that potion you got next time!")
				print GiantSpider.hp
				print Player.battlehp	


		else:
			print('You went back to the cave, where the old man is. You talked to him, and he started to transform into a giant spider, and attacked you!')

	elif Choice2 == 2:
		print("You talked to the old man, and he started to transform into a giant spider, and attacked you!'")
#################################################################################################### ~ Other path		
elif Choice1 == 2:
	Player.coins += 20
	print("This is worth 20 coins!")
	print("You walked into the forest where you found a statue, where you could read: 'Someone died here a long time ago and his wealth was barried somewhere around here'.")
	print("By the moment had finished reading, a wolf jumped and atacked you!")
	while Dog.hp > 0:
		Dog.hp -= Player.attack
		Player.battlehp -= Dog.attack
		print Dog.hp
	lvlup()
	print("MAXHP, CURRENT HP, ATTACK, COINS")
	print(Player.maxhp, Player.battlehp, Player.attack, Player.coins)
	print('Done, you defeated the beast and walked North.')
	print("After that, you entered a cave, where there was an old man. You couldn't see him very, because of the fog. ")
	Choice2 = input("Your options are: 1.Explore cave; 2.Talk to old ")
	if Choice2 == 1:
		chestChoice1 = input("Open chest?: 1.Yes 2.No")
		if chestChoice1 == 1:
			Player.attack += 3
			print('You found a sword! +3 attack; You went back to the cave and  you talked to the old man, and he started to transform into a giant spider, and attacked you!')
					


		else:
			print('You went back to the cave, where the old man is. You talked to him, and he started to transform into a giant spider, and attacked you!')







