import pickle
import Monster
import Human
import os
from random import randint

class SignUp(object):
    global check
    check = False
    
    #check the name that's been entered is at least not numbers
    def __init__(self, name):
        good_input = check
        while not good_input:
            self.name = raw_input(">")
            if self.name.isalpha() == True:
                good_input = True

            elif self.name.isalpha() == False:
                print "You can't use numbers for a name. Please type in your name"
                good_input = False


    #pick room to enter either gold or silver
    def enter(self):
        good_input = check
        while not good_input:
            self.pick = raw_input(">")
            if self.pick == 'gold':
                good_input = True
                return 'silver'
            elif self.pick =='silver':

                good_input = True
                return 'gold'
            else:
                print "There are only two rooms to choose from "
                good_input = False

    #picks if the the person want to battle as a fighter or wizard
    def style(self):
        good_input = check
        while not good_input:
            self.choice = raw_input(">")
            if self.choice == 'fighter':
                good_input = True

            elif self.choice == 'wizard':
                good_input = True
            else:
                print "You can only choose 'fighter' or 'wizard'"
                good_input = False

# Not used
class Jason(object):
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)


#sign = SignUp()
#print sign.word, sign.fighting_style, sign.room_change

print "Hi There, an welcome to 'Battle Pen'"
print "What's you name so we can put it on your grave stone"



name = ""
new_player = SignUp(name)


print "Hahaha very good. %s Let's not beat around the bush" % new_player.name
print "it is time for someone to die"
print "I'll need to write in the books if you are a 'fighter' or 'wizard'"
new_player.style()

print "I'll put in the books, 'died trying to be a %s'" % new_player.choice
print "Only kidding my friend, don't look so sad, take a seat while I write you up."
print "Ok, here's the deal, you pick either a 'gold' or 'silver' room to fight"
print "a random monster. It's now or never, which room do you choose?"

new_player.enter()
print "excellent, you have chosen room %s" % new_player.pick

print new_player.name, new_player.choice
data = (new_player.name, new_player.choice, new_player.choice)
filename =  'game.pickle'
print filename

with open(filename, 'wb') as f:
	pickle.dump(data, f)
import Battle
