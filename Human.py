class Human(object):
    attack_moves = {
        'fighter': {'sword': 8, 'punch': 4,'kick': 5},
        'Wizard': {'fire ball': 7,'staff': 6},
        }

    def __init__(self, name,
                 present_human_hit_points, max_human_hit_points):

        self.name = name
        self.present_human_hit_points = present_human_hit_points
        self.max_human_hit_points = max_human_hit_points

    def decrease_health(self, amount):
        self.amount = amount
        self.present_human_hit_points -= amount
        return amount

class Fighter(Human):

    def __init__(self, name,
                 present_human_hit_points, max_human_hit_points):

        Human.__init__(self, name,
                       present_human_hit_points, max_human_hit_points)
        self.attack_moves_one = Human.attack_moves['fighter']['sword']
        self.attack_moves_two = Human.attack_moves['fighter']['punch']

fighter = Human("bob", 50, 100)
