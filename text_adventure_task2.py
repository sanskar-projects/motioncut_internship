from random import choice
from sys import exit
ways={"N":"north","S":"south","E":"east","W":"west","NE":"north-east","NW":"north-west","SE":"south-east","SW":"south-west"}
d={}
d["living room"]={"N":"bedroom","S":"","E":"kitchen","W":"","NE":"toilet","NW":"","SE":"","SW":"balcony"}
d["kitchen"]={"N":"utility","S":"","E":"","W":"living room","NE":"","NW":"","SE":"","SW":""}
d["utility"]={"N":"","S":"","E":"","W":"","NE":"","NW":"","SE":"","SW":"kitchen"}
d["toilet"]={"N":"","S":"","E":"","W":"","NE":"","NW":"","SE":"","SW":"living room"}
d["bedroom"]={"N":"","S":"","E":"","W":"","NE":"","NW":"","SE":"living room","SW":""}
d["balcony"]={"N":"","S":"","E":"living room","W":"","NE":"","NW":"","SE":"","SW":""}
room=_room=axis=_axis=s=S=""
bit=0
while(room==_room and axis==_axis):
    room=choice(list(d.keys()))
    _room=choice(list(d.keys()))
    axis=choice(list(ways.keys()))
    _axis=choice(list(ways.keys()))
def computer():
    global _room,_axis
    way=choice(list(ways.keys()))
    if(d[_room][way]!=""):
        _axis=""
        _room=d[_room][way]
        print(S,"entered",_room)
    elif(bit==0 and _room=="living room" and way=="SE"):
        print("\nYOU LOSE\n",s,"escaped from",S,"\nGAME OVER")
        exit()
    else:
        _axis=way
        print(S,"is in",ways[_axis],"of",_room)
def user():
    global room,axis
    x=input("\n>>>").split()
    verb=x[0]
    if(verb=="run"):
        way=x[1]
        if(way in list(ways.keys())):
            if(d[room][way]!=""):
                axis=""
                room=d[room][way]
                print(s,"entered",room)
            elif(bit==0 and room=="living room" and way=="SE"):
                print("\nYOU WIN\n",s,"escaped from",S,"\nGAME OVER")
                exit()
            else:
                axis=way
                print(s,"is in",ways[axis],"of",room)
        else:
            ("invalid direction")
    else:
        print("invalid command")
def main():
        print("\tTHE KIDNAPPING(A TEXT ADVENTURE)\n")
        global s,S,bit
        s=input("what is the victim's name?: ")
        S=input("what is the kidnapper's name?: ")
        x=""
        while(x!="victim" and x!="kidnapper"):
                x=input("do you want to help victim or kidnapper?: ")
                if(x=="kidnapper"):
                    s,S=S,s
                    bit=1
                    print('''
STORY:
{1} had been pranked by {0} which annoyed {1} so much that {1} decided to kidnap {0} and keep {0} trapped in some flat for one day
then at night there is a sudden power cut in the building so {1} makes an attempt to catch {0} before {0} reaches the foyer.

HELP KIDNAPPER:
{0} will be caught by {1} if {0} and {1} are in the same room and {0} and {1} reach a common point or if {0} and {1} enter the same room together.
-> YOU WIN

If {0} reaches the foyer then {0} will escape succesfully.
-> YOU LOSE'''.format(S,s))
                if(x=="victim"):
                    print('''
STORY:
{0} has been kidnapped by {1} and brought to some flat because of which {0} is very frightened and does not know about {1}'s further intentions
then at night there is sudden power cut in the building so {0} makes an attempt to reach the foyer before {1} catches {0}.

HELP VICTIM:
If {0} reaches the foyer then {0} will escape succesfully.
-> YOU WIN

{0} will be caught by {1} if {0} and {1} are in the same room and {0} and {1} reach a common point or if {0} and {1} enter the same room together.
-> YOU LOSE'''.format(s,S))
        print('''
RULES:
There are six rooms in the flat,
Living room
Kitchen
Utility
Toilet
Bedroom
Balcony
Each room is connected to at least one other room and there is only one foyer in the south-east of the living room.
At start of the game both player and opponent(computer) may be in the same room at different points or in different rooms.
You can run in any of the eight directions within a room and if you encounter a door you will enter another room.
Whenever you run the opponent may make a move as well.

Commands:
run N
run S
run E
run W
run NE
run NW
run SE
run SW

ALL THE BEST!!!!!
''')
        print(s,"is in",axis,"of",room)
        print(S,"is in",_axis,"of",_room)
        while(True):
            user()
            computer()
            if(room==_room and axis==_axis):
                if(bit==0):
                    print("\nYOU LOSE\n",s,"was captured by",S,"\nGAME OVER")
                else:
                    print("\nYOU WIN\n",S,"was captured by",s,"\nGAME OVER")
                exit()
main()

