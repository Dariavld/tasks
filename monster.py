class Monster:
    def __init__(self, name, health, attack_power):

        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def attack(self, player):
        
        player.take_damage(self.attack_power)
        
    def take_damage(self, damage):

        self.health -= damage
