from sys import exit
from random import randint


class Game(object):


    def __init__(self, start):

        self.quips = [

            "You died. You kinda suck at this.",
            "Your mom would be proud. If she were smarter."
            "Such a luster.",
            "I have a small puppy that's beteer at this."
            ]

        self.start = start
        


    def play(self):

        next = self.start


        while True:

            print "\n------"
            room = getattr(self, next)
            next = room()


    def death(self):

        print self.quips[randint(0, len(self.quips)-1)]
                        
        exit(1)
                         

    def central_corridor(self):

        print "The Gothons of Planet Percal #25 have invaded your ship and sestroied"
        print "your entire crew. You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put ot on the bridge, and blow the ship up after getting into an"
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jump out,ref scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filed body. He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."



        action = raw_input(">")


        if action == "shoot!":

            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim. Your  laster hits his costume but misses him entirely. This"
            print "completely ruins his brand new costume his mother bought him, which"
            print "makes him fly into an insane rage and blast you repeatdly in the face until"
            print "you are dead. Then he eats you."

            return 'death'

        elif action == "dodge!":

            print "Like a world class boxer you dodge, weave, slip and slide right"
            print "as the Gothons's blaster cranks a laster past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothons stomps on"
            print "your head and eats you."

            return 'death'

        elif action == "tell a joke":

            print "Lucky for you they learn Gothon insults in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
            print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
            print "While he's lauhing you run up and shoot him square in the head"
            print "putting him down, then jump through the Weapon Armory door."

            return 'laster_weapon_corridor'


    def laster_weapon_armory(self):

        print "You do a dive roll into the Weapom Armory, crouch and scan the room"
        print "for more Gothons that might be hiding. It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container. Ther's a keypad lock on the box"
        print "and you need the code to get the bomb out. If you get the code"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb. The code is 3 digits."

        code = "%d%d%d" % (randint(1,9), randint(1,9),randint(1,9))

        guess = raw_input("[keypad]>")

        guesses = 0

        while guess != code and guesses < 10:

            print "BZZZZEDDD!"

            guesses += 1

            guess = raw_input("[keypad]>")


        if guess == code:

            print "The container clicks open and the seal breaks, letting gas out."
            print "


                  

