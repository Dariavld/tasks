from player import Player
from wizard import Wizard
from fighter import Fighter
from monster import Monster
from weapon import Weapon
from sword import Sword
from posoh import Posoh

class Game:
    def __init__(self):
        self.player = None
        self.monster = None
        self.weapon = None
        self.experience_points = 0
        
    def choose_player(self, player_wants_to_be, name):
        if player_wants_to_be == "wizard":
            self.player = Wizard(name)
        elif player_wants_to_be == "fighter":
            self.player = Fighter(name)
        else:
            raise ValueError("Выбирать можно только из двух типов игроков:)")

            
    def choose_monster(self, monster_wants_to_be):
        if monster_wants_to_be == "panochka":
            self.monster = Monster(name="panochka", health=35, attack_power=10)
        elif monster_wants_to_be == "viy":
            self.monster = Monster(name="viy", health=100, attack_power=30)
        else:
            raise ValueError("Только такие монстры есть:)")
            
    def choose_weapon(self, weapon_is):
        if weapon_is == "sword":
            self.weapon = Sword()
        elif weapon_is == "posoh":
            self.weapon = Posoh()
        else:
            raise ValueError("Только такие виды оружия")

            
    def fight(self):
        if not all([self.player, self.monster, self.weapon]):
            raise ValueError("Не все выбрано")
        
        self.player.attack(self.monster)
        
        if self.monster.health <= 0:
            self.experience_points += 13
            print("K.O!")
            return
        
        self.monster.attack(self.player)
        

        if self.player.health <= 0:
            print("Вы мертвы, начать сначала->")
            return


    def gamestart(self):
        self.choose_player()

        self.choose_monster()

        self.choose_weapon()
        
        self.fight()
        
    
