import random
import time
from pprint import pprint #pretty printing
import math
from colorama import Fore, Back, Style

class Hero:
    def __init__(self, Hhealth, Hattack, Hluck, Hranged, Hdefence, Hmagic, Hname):
        self.Health = Hhealth
        self.Attack = Hattack
        self.Luck = Hluck
        self.Ranged = Hranged
        self.Defence = Hdefence
        self.Magic = Hmagic
        self.Name = Hname

    def get_health(self):
        return self.Health
    def get_attack(self):
        return self.Attack
    def get_luck(self):
        return self.Luck
    def get_ranged(self):
        return self.Ranged
    def get_defence(self):
       return self.Defence
    def get_magic(self):
        return self.Magic
    def get_name(self):
        return self.Name


    def set_health(self, new_health):
        self.Health = new_health
    def set_attack(self, new_attack):
        self.Attack = new_attack
    def set_luck(self, new_luck):
        self.Luck = new_luck
    def set_ranged(self, new_ranged):
        self.Ranged = new_ranged
    def set_defence(self, new_defence):
        self.Defence = new_defence
    def set_magic(self, new_magic):
        self.Magic = new_magic
    def set_name(self, new_name):
        self.Name = new_name

def create_class():
    a = input(Fore.CYAN+Back.BLACK+Style.BRIGHT+'Are you more stratergic(1) or more of a warrior(2) ? -> ')

    while a != '1' and a != '2':
        print('Invalid Selection')
        a = input(Fore.CYAN+Back.BLACK+Style.BRIGHT+'Are you more stratergic(1) or more of a warrior(2) ? -> ')

    if a == '1':
        hero_attack = 50
        hero_defence = 100
    elif a == '2':
        hero_attack = 100
        hero_defence = 50

    b = input('Press Enter to roll a Dice....')
    time.sleep(0.2)
    print('Rolling Dice....')
    hero_luck = random.randint(0, 10)
    print('Your luck value is', hero_luck, 'out of 10')

    c = input("Are you more a Bow and Arrow(1) wielder or more of a Magic wielder(2) -> ")
    while c != '1' and c != '2':
        print('Invalid Selection')
        c = input("Are you more of a Bow and Arrow(1) wielder or more of a Magic wielder(2) -> ")

    if c == '1':
        hero_ranged = 100
        hero_magic = 50
    elif c == '2':
        hero_ranged = 50
        hero_magic = 100

    hero_name = input("What is your name Hero ?? ")
    print('Welcome', hero_name, '!!!!')

    return (hero_attack, hero_luck, hero_ranged, hero_defence, hero_magic, hero_name)


class Enemy:
    def __init__(self, Ehealth, Eattack, Especial, Echance, Ename):
        self.Health = Ehealth
        self.Attack = Eattack
        self.Special = Especial
        self.Chance = Echance
        self.Name = Ename

    def get_health(self):
        return self.Health
    def get_attack(self):
        return self.Attack
    def get_special(self):
        return self.Special
    def get_chance(self):
        return self.Chance
    def get_name(self):
        return self.Name

    def set_health(self, new_health):
        self.Health = new_health
    def set_attack(self, new_attack):
        self.Attack = new_attack
    def set_special(self, new_special):
        self.Special = new_special
    def set_chance(self, new_chance):
        self.Chance = new_chance
    def set_name(self, new_name):
        self.Name = new_name


class Boss(Enemy):
    def __init__(self, Ehealth, Eattack, Especial, Echance, Ename, EsuperMove):
        super().__init__(Ehealth, Eattack, Especial, Echance, Ename)

        self.SuperMove = EsuperMove

    def get_superM(self):
        return self.SuperMove
    def set_superM(self, new_supeMove):
        self.SuperMove = new_supeMove

def Enemy_Generator(level_boss):
    temp = []
    file = open('adjective.txt','r')
    lines = file.readlines()
    adjective = lines[random.randint(0, len(lines)-1)][:-1]
    file.close()
    file = open('animal.txt', 'r')
    lines = file.readlines()
    animal = lines[random.randint(0, len(lines) - 1)][:-1]
    file.close()

    if level_boss == False:
        health = random.randint(50, 100)
        attack = random.randint(10, 15)
        special = random.randint(10, 20)
        chance = random.randint(1, 10)

        return Enemy(health, attack, special, chance, adjective + ' ' + animal)

    else:
        health = random.randint(200, 250)
        attack = random.randint(20, 40)
        special = random.randint(50, 60)
        chance = random.randint(1, 8)
        superMove = random.randint(100, 200)

        return Boss(health, attack, special, chance, adjective + ' ' + animal, superMove)

def Enemy_Attack(chance, attack_value, name, defence):
    print(name, 'is winding up for an attack....')
    hit = random.randint(0, 10)
    if chance >= hit:
        print('Hero is hit!!!!')
        loss = abs(attack_value - defence)
        print('You stagger losing....', loss, 'health')
        return math.ceil(loss)
    else:
        print('The Enemy Missed!!')
        return 0

def Hero_Attack(luck):
    hit = random.randint(0, 4)
    if luck < hit:
        #print('MISSED !!')
        return False
    else:
        #print('You have hit the Enemy !!')
        return True

def is_dead(health):
    if health < 1:
        return True
    else:
        return False

def loot(luck, character):
    loot_chance = random.randint(0, 4)

    if luck < loot_chance:
        print('NO LOOT FOR YOU !!')
    else:
        table_num = random.randint(0,4)
        loot_table = ['items', 'ranged', 'defence', 'magic', 'attack']
        item_type = loot_table[table_num]
        file = open(item_type+'.txt','r')
        lines = file.readlines()

        #print('The Enemy dropped a ....')

        item = random.randint(0,len(lines)-1)

        item_line = lines[item]
        split_itemline = item_line.split(',')
        name = split_itemline[0]
        value = int(split_itemline[1])

        print(Fore.YELLOW+Back.BLACK+Style.DIM+'The Enemy dropped a ....',name+Style.RESET_ALL)

        if item_type == 'attack':
            character.set_attack(character.get_attack() + value)
            print(Fore.LIGHTMAGENTA_EX+Back.BLACK+Style.BRIGHT+'Your new Attack Power is ...')
            print(character.get_attack())
        elif item_type == 'ranged':
            character.set_ranged(character.get_ranged() + value)
            print(Fore.LIGHTMAGENTA_EX+Back.BLACK+Style.BRIGHT+'Your new Ranged Power is ...')
            print(character.get_ranged())
        elif item_type == 'defence':
            character.set_defence(character.get_defence() + value)
            print(Fore.LIGHTMAGENTA_EX+Back.BLACK+Style.BRIGHT+'Your new Defence Power is ...')
            print(character.get_defence())
        elif item_type == 'magic':
            character.set_magic(character.get_magic() + value)
            print(Fore.LIGHTMAGENTA_EX+Back.BLACK+Style.BRIGHT+'Your new Magic Power is ...')
            print(character.get_magic())
        else:
            if split_itemline[2] == 'luck':
                character.set_luck(character.get_luck() + value)
                print(Fore.LIGHTMAGENTA_EX+Back.BLACK+Style.BRIGHT+'Your new Luck Value is ...')
                print(character.get_luck())
            elif split_itemline[2] == 'health':
                character.set_health(character.get_health() + value)
                print(Fore.LIGHTMAGENTA_EX+Back.BLACK+Style.BRIGHT+'Your new Health Value is ...')
                print(character.get_health())

def check_over(enemy_dead):
    if enemy_dead == True:
        print(Fore.GREEN+Back.BLACK+Style.BRIGHT+'\n\nTime for Another Battle !!!')
    else:
        print(Fore.BLUE+Back.BLACK+Style.BRIGHT+'You are out of health')
        print(Fore.BLUE+Back.BLACK+Style.BRIGHT+'Better Luck Next Time!!')
        exit()

def battle_state(gen_enemy, Character):
    print(Fore.LIGHTRED_EX+Back.BLACK+Style.BRIGHT+"What's that coming over the Hill ??!!?? ")
    print(Fore.LIGHTRED_EX+Back.BLACK+Style.BRIGHT+"It's a ...",gen_enemy.get_name(),"Looking for a Fight")
    print(Fore.LIGHTRED_EX+Back.BLACK+Style.BRIGHT+"Check out it's stats...")
    #pprint(vars(gen_enemy))
    try:
        '''print('Health: ',gen_enemy.Health)
        print('Attack: ',gen_enemy.Attack)
        print('Special Attack Power: ',gen_enemy.Special)
        print('Chance of Hitting You: ',gen_enemy.Chance)'''
        print(Fore.LIGHTRED_EX+Back.BLACK+Style.BRIGHT+"It's a Boss Enemy with Super Move Power: ", gen_enemy.SuperMove)
    except:
        print(Fore.LIGHTRED_EX+Back.BLACK+Style.BRIGHT+'Health: ', gen_enemy.Health)
        print(Fore.LIGHTRED_EX+Back.BLACK+Style.BRIGHT+'Attack: ', gen_enemy.Attack)
        print(Fore.LIGHTRED_EX+Back.BLACK+Style.BRIGHT+'Special Attack Power: ', gen_enemy.Special)
        print(Fore.LIGHTRED_EX+Back.BLACK+Style.BRIGHT+'Chance of Hitting You: ', gen_enemy.Chance)
    '''print('Health: ', gen_enemy.Health)
    print('Attack: ', gen_enemy.Attack)
    print('Special Attack Power: ', gen_enemy.Special)
    print('Chance of Hitting You: ', gen_enemy.Chance)
    print("It's a Boss Enemy with Super Move Power: ", gen_enemy.SuperMove)'''

    battle = True

    while battle:

        print(Fore.MAGENTA+Back.BLACK+Style.BRIGHT+'1. Sword Attack')
        print(Fore.MAGENTA+Back.BLACK+Style.BRIGHT+'2. Ranged Attack')
        print(Fore.MAGENTA+Back.BLACK+Style.BRIGHT+'3. Magic Attack')
        choice = input(Fore.MAGENTA+Back.BLACK+Style.BRIGHT+'Enter your choice of Attack : ')

        while choice != '1' and choice != '2' and choice != '3':
            print(Fore.MAGENTA+Back.BLACK+Style.BRIGHT+'OOPS.....Only Enter 1, 2 or 3.....')
            print(Fore.MAGENTA+Back.BLACK+Style.BRIGHT+'1. Sword Attack')
            print(Fore.MAGENTA+Back.BLACK+Style.BRIGHT+'2. Ranged Attack')
            print(Fore.MAGENTA+Back.BLACK+Style.BRIGHT+'3. Magic Attack')
            choice = input(Fore.MAGENTA+Back.BLACK+Style.BRIGHT+'Enter your choice of Attack : ')

        if choice == '1':
            damage = Character.get_attack()
        elif choice == '2':
            damage = Character.get_attack()
        else:
            damage = Character.get_attack()
        print(Fore.CYAN+Back.BLACK+Style.BRIGHT+'You wind up for the attack...')
        hit = Hero_Attack(Character.get_luck())

        if hit == True:
            gen_enemy.set_health(gen_enemy.get_health() - damage)
            print(Fore.CYAN+Back.BLACK+Style.BRIGHT+"You've Hit the Enemy!!!")
            print(Fore.CYAN+Back.BLACK+Style.BRIGHT+"The Enemy's Health is Now....", gen_enemy.get_health())

        else:
            print(Fore.LIGHTBLUE_EX+Back.BLACK+Style.BRIGHT+'You missed your attack!!!'+Style.RESET_ALL)

        enemy_dead = is_dead(gen_enemy.get_health())

        if enemy_dead == False:
            x = (Character.get_health() - Enemy_Attack(gen_enemy.get_chance(), gen_enemy.get_attack(), gen_enemy.get_name(), Character.get_defence()))
            if x < 0:
                Character.set_health(0)
            else:
                Character.set_health(x)


            character_dead = is_dead(Character.get_health())

            if character_dead == True:
                battle = False
                return False

            else:
                print(Fore.WHITE+Back.BLACK+Style.BRIGHT+"Your remaining health is....", Character.get_health())
        else:
            battle = False
            print(Fore.CYAN+Back.BLACK+Style.BRIGHT+"You've defeated the Enemy!!!!")
            print(Fore.CYAN+Back.BLACK+Style.BRIGHT+'Did you find any loot ???!!!')
            loot(Character.get_luck(), Character)

            return True



print(Fore.GREEN+Back.BLACK+Style.BRIGHT+'''         Hello Adventurer !!
        Welcome to the Game.
        In this Game You will encounter various kinds of Animals with interesting and dangerous 
        qualities.
        They will have but one intent .....
            TO ATTACK AND KILL YOU !!!!!
        You will have to be brave and courageous to fight and survive.
        Choose your attacks wisely as well as your defences!!!!
        
        Now let's begin with the Game
        Enter the choices wisely
        They will affect your Attacks and Defences.                                                                                                                '''+Style.RESET_ALL)

x = input(Fore.GREEN+Back.BLACK+Style.BRIGHT+'\n\n                                             Press Enter to Start.....                                                                                                              ')
#print(Fore.GREEN+Back.BLACK+Style.BRIGHT+'\n')

def levelGenerator(character, level):

    maxNumberOfEnemies = math.ceil(level*5)

    for i in range(maxNumberOfEnemies):
        bossChance = random.randint(1, 10)
        if bossChance > 7:
            levelBoss = True
        else:
            levelBoss = False

        characterDead = battle_state(Enemy_Generator(levelBoss), character)

        check_over(characterDead)

def main():
    classData = create_class()

    character = Hero(100, classData[0], classData[1], classData[2], classData[3], classData[4], classData[5])

    print(Fore.LIGHTCYAN_EX+Back.BLACK+Style.BRIGHT+'Here are your Attack and Weapons\' Power')
    print('Your Health Power: ',character.Health)
    print('Your Attack Power: ',character.Attack)
    print('Your Defence Power:',character.Defence)
    print('Your Luck Power: ', character.Luck)
    print('Your Ranged Power: ', character.Ranged)
    print('Your Magic Power: ', character.Magic)
    print('\n\n')

    print('Level 1 ....')
    levelGenerator(character, 1)

    print('Level 2.....')
    levelGenerator(character, 2)

    print('Level 3.....')
    levelGenerator(character, 3)

    print('Level 4.....')
    levelGenerator(character, 4)

    print('Level 5.....')
    levelGenerator(character, 5)

    print('Level 6.....')
    levelGenerator(character, 6)

    print('Level 7.....')
    levelGenerator(character, 7)

    print('Level 8.....')
    levelGenerator(character, 8)

    print('Level 9.....')
    levelGenerator(character, 9)

    print('Level 10.....')
    levelGenerator(character, 10)

    print('You Won !!!!!!')
    pprint(vars(character))


main()














