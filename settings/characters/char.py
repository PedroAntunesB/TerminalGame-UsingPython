class Basic_functions: 
    def __init__(self, level=1, hp=50, acuracia=10, phisical_atack=10, speed=20, magic=0,name='None', player_class= 'None'):
        self.level = level
        self.max_hp = hp
        self.hp = (self.level * hp)*0.5
        self.minus_hp = 0
        self.acuracia = (self.level * acuracia)*0.5
        self.speed = (self.level * speed)*0.5
        self.phisical_atack = (self.level * phisical_atack)*0.5
        self.magic = magic
        self.name = name
        self.player_class = player_class
        
    def action_atack(self):
        normal_atack = self.phisical_atack
        return normal_atack

    def damage(self, atack):
        self.hp = self.hp - atack

    def __str__(self):
        return f'Name: {self.name}\nClasse: {self.player_class}\nLevel: {self.level}\nVida: {self.hp}\nForça: {self.phisical_atack}\nPoder Magico: {self.magic}\nVelocidade: {self.speed}\n'

    
class Player(Basic_functions):
    def __init__(self,name, player_class):
        super().__init__(name=name, player_class=player_class)
        self.list_atacks = list()
        
    def player_register_atacks(self, atack):
        self.list_atacks.append(atack)

    def print_atacks(self):
        count = 1
        for atack in self.list_atacks:
            print(f'{count}-{atack.name}')
            count += 1

    def use_atack(self, index):
        index -= 1
        return self.list_atacks[index]

    
class Monster(Basic_functions):
    def __init__(self, level_monster):
        super().__init__(level=level_monster)
        self.max_hp = self.hp * 3
        self.hp = self.max_hp
