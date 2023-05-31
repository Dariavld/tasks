class Player:
    def __init__(self, name, health, attack_power):
        self.name = name #имя игрока
        self.health = health #ХП
        self.attack_power = attack_power #сила атаки
        
    def attack(self, monster):
        monster.take_damage(self.attack_power) #после атаки на монстра, понижение ХП

        
    def take_damage(self, damage):
        self.health -= damage
        #количество урона

    def choose_player(self):
        player_type = input("Choose your player type (Wizard or Fighter): ")
        if player_type.lower() == "wizard":
            name = input("Enter your wizard name: ")
            health = 100
            mana = 50
            magic_power = 20
            self.player = Wizard(name, health, mana, magic_power)
        elif player_type.lower() == "fighter":
            name = input("Enter your fighter name: ")
            health = 150
            strength = 30
            defense = 10
            self.player = Fighter(name, health, strength, defense)
        else:
            print("Invalid player type")