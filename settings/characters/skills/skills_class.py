class Phisical_basic_stats:
    def __init__(self, damage):
        self.damage = damage


class Normal_phisical_skill(Phisical_basic_stats):
    def __init__(self, name):
        super().__init__(damage=5)
        self.name = name

    def damage_func(self, strengh):
        damage = strengh * self.damage
        return damage
