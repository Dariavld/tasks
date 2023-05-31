from player import Player

class Wizard(Player):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=34)
