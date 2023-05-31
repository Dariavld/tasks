from player import Player

class Fighter(Player):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=45)
