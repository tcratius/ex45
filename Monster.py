class Monster(object):
    attack_moves = {
        'fire': 6,
        'slash': 4
        }

    def __init__(self, name, monster_hit_points):
        self.name = name
        self.monster_hit_points = monster_hit_points

    def decrease_health(self, amount):
        self.amount = amount
        self.monster_hit_points -= amount
        return amount

class Bat(Monster):

    def __init__(self, name, monster_hit_points):
        Monster.__init__(self, name, monster_hit_points)
        self.attack_moves = Monster.attack_moves['fire']
