# sword.py
from weapon import Weapon

class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword", attack_power=20)
