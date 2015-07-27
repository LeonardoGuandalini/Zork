from heroes import Warrior, Bard

def select_hero():
    print('Time to choose your hero')
    print('1 - Warrior')
    print('2 - Bard')
    hero_choice = -1
    while (hero_choice != 1 and hero_choice != 2):
        hero_choice = input('Choose your hero:')
    if hero_choice == 1:
        return Warrior()
    if hero_choice == 2:
        return Bard()

def greetings():
    hero = select_hero()
    hero.shout();

greetings()
