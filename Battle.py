import pickle
import Monster
import Human
import os
from random import randint





class Battle2(object):


    def battle_stats(self, monster_attack, player_attack):
        os.system("cls")
        print "Animal %s HP %d Attacks you %d point"  % (
                self.monster.name, self.monster.monster_hit_points, self.monster_attack)
        print "Vs "
        print "%s Your HP is %d Damage to %s is %d points " % (
                self.player.name, self.player.present_human_hit_points,
                self.monster.name, self.player_attack)

    def EndGame(self, out_come):
        self.out_come = out_come
        if self.out_come == 'monster':
            print "*" * 10
            print "Game Over"
            print "You beat the %s" % monster.name
        elif self.out_come == 'human':
            print "*" * 10
            print "Game Over"
            print "Looks like I'll be using the coffin for %s after all" % player.name

    def deduct_hp(self, player, monster):
        self.monster_attack = self.player.decrease_health(randint (1, monster.attack_moves))
        self.player_attack = self.monster.decrease_health(randint (1, player.attack_moves_one))
        return self.monster_attack, self.player_attack

    def player_pick(self, name, battle_type):
        self.battle_type = battle_type
        if self.battle_type == 'fighter':
            self.player = Human.Fighter(name, 50, 100)
            return self.player
        elif battle_type == 'wizard':
            self.player = Human.Wizard(name, 40, 90)
            return self.player

    def begin_battle(self, player, monster):
        self.player = player
        self.monster = monster
        print "You are attacked by %s" % monster.name
        print "do you wish to fight? "
        action = raw_input("=> ")
        if action == "yes":
        # Subtracts the attack from the opponents hit point
            self.monster_attack, self.player_attack = self.deduct_hp(self.player, self.monster)
        # Prints out update each opponents HP and Attack
            self.battle_stats(self.monster_attack, self.player_attack)
            death = False
            while not death:
                print "\n"
                print "continue to fight press f "
                action = raw_input("=> ")

                if action == "f":
                    self.monster_attack, self.player_attack = self.deduct_hp(self.player, self.monster)
                    self.battle_stats(self.monster_attack, self.player_attack)

                    if (self.player.present_human_hit_points <= 0 or
                            self.monster.monster_hit_points <= 0):
                        if (self.player.present_human_hit_points == 0 or
                                self.player.present_human_hit_points <= 0):
                            self.EndGame('human')
                            death = True

                        elif (self.monster.monster_hit_points == 0 or
                                self.monster.monster_hit_points <= 0):
                            self.EndGame('monster')
                            death = True
                    elif (self.player.present_human_hit_points) > 0:
                        death = False

        elif action == "no":
            print "leaves room"
        else:
            print "does not compute"


filename = 'game.pickle'
with open(filename, 'rb') as f:
	b = pickle.load(f)

character = Battle2()
go = character.player_pick(b[0], b[1])
bat = Monster.Bat("Fire Bat", 40)
character.begin_battle(go, bat)
