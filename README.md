
# Zork-2-with-classes
Usando as classes, consegui fazer um sistema de ataque e um ruinzinho de level up. Não consegui fazer usando o código que voce fez, mas consegui desse jeito:

class Players:
	def __init__(self, maxhp, battlehp, attack, coins):
		self.coins = coins
		self.maxhp = maxhp
		self.attack = attack
		self.battlehp = battlehp
Player = Players(10, 10, 2, 0)

