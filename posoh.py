# posoh.py
from weapon import Weapon

class Posoh(Weapon):
    def __init__(self):
        super().__init__(name="Posoh", attack_power=30)
