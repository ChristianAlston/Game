import random


class Character():
    def __init__(self,move,position):
        self.move = move
        self.position = position
        
    
class Player(Character):
    def __init__(self, name = input('What is your name? \n'), ship = input('Choose your ship name \n'), health = 200, speed = 20, attack = 15):
        self.name = name
        self.ship = ship
        self.health = health
        self.speed = speed 
        self.attack = attack
        
    def attack(self):
        print('----------')
        
    def hax(self):
        while True:
            if self.health < 300:
                self.health += 25
                if self.health == 300:
                    break


class Enemy(Character):
    def __init__(self):
        self.name = 'Stormtrooper Pilot' 
        self.ship = 'Tie-Fighter'
        self.health = 60
        self.speed = 5
        self.attack = 5
        
    def attack(self):
        print('----------')
        print('attack! (but missed!)')
        
    def cant_pilot(self):
        print('Oh no! I can\'t shoot the main character because of plot protection!')
    
    


class Enemy2(Character):
    def __init__(self,move, position):
        self.name = 'Commander'
        self.ship = 'Carrier Transport / Gunship'
        self.health = 150
        self.speed = 8
        self.attack = 10
    
    def attack(self):
        print('We might stand a chance against the protagonist if we..')
        print('----------')
    
    def abort(self):
        if self.health == 50:
            print('ABORT! WE CANNOT FIGHT THEM! THE FORCE IS TOO STRONG WITH THEM!')
    
    def crash_somewhere_Idk(self):
        if self.health == 0:
            print('-Crashed!-')
            
                

class Boss():
    def __init__(self, move = 1, position = 10):
        self.name = 'Boss'
        self.ship = 'Frigate'
        self.health = 400
        self.speed = 15
        self.attack = 25
        self.move = move
        self.position = position
    
    
    
# player_1 = Player()
# print(player_1.name, player_1.attack)
    
# enemy = Enemy()
# print(enemy.name, enemy.ship)

# enemy2 = Enemy2()
# print(enemy2.name, enemy2.ship)

boss = Boss()
print(boss.move, boss.position)