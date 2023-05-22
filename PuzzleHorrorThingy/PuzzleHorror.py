import sys
import time

"""So the basic idea for the storyline right now is to make a manor, with secret 
rooms and codes to get through to each room, untill you reach the dungeon which will 
act like the real horror part of the storyline"""


"""
References
------------------------------
Grandmother's Name - Margret


Goals
-----------------------------
create secrets that require things like ciphers to solve
create lots of rooms upstairs and downstairs to create a frame for the world


Puzzle Answers
-----------------------------
in the very first input box if you write, "Margret" a secret text blob is released


Monster/demon
-----------------------------




"""



name = "placeholder"
gender = "placeholder"

class room:
      def __init__(self, name, description):
        self.name = name
        self.description = description

Grand_Hall = room("Grand Hall", "Around you is a beautiful marble-based manor, with only a few cobwebs, you are reminded to hire some cleaning staff, looking up you see a portrait of your grandmother, Margret, and every other family head before her. Your grand hall is a grand room, and you must be sure it is well kept for your guests.")

U_Main_Hall = room("Upstairs Main Hall", "You are in the upstairs hallway, this connects to many rooms, including your bedroom, the office, a restroom, and ")
Up_Main_hall_Name = str(U_Main_Hall.name)
Up_Main_hall_Desc = str(U_Main_Hall.description)
Kitchen = room("Kitchen", "You enter the tile-floored kitchen and remeber visiting your family with your father and mother, ")

diningRoom = room("Dining Room", "This room, is covered in a long beautiful carpet with a table long as the room, a chair at the head of the table lies empty, your grandma's old seat")

#slowprint function
def sp(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.06)

#create a loading bars for the game
def loading():
    for i in range(10):
        text = str('|' * i)
        print(f'[{text.ljust(9, "-")}]', end='\r')
        time.sleep(0.5)
    sp('Game Starting...'.ljust(11))

def loading2():
    for i in range(10):
        text = str('|' * i)
        print(f'[{text.ljust(9, "-")}]', end='\r')
        time.sleep(0.5)
    sp('---------------------------------------------------------------------'.ljust(11))


#the start of the game, retieve things like the player name and etc.
def start():
    global name
    global gender
    name = input("Unknown: What is your first name young one? ")
    sp(f"Unknown: {name}... That is a name I haven't heard in a long time")
    
    
    global HeShe
    global him
    #define gender
    chosen = False
    while chosen == False:
        gender = input("Unknown: pick an option do you identify as 1. Male (he/him), 2. Female (she/her), 3. Other (they/them) ")
        #male
        if gender == "1":
            HeShe = "he"
            himHer = "him"
            chosen = True
        #female    
        elif gender == "2":
            HeShe = "she"
            himHer = "her"
            chosen = True
        #non-binary    
        elif gender == "3":
            HeShe = "they"
            himHer = "them"
            chosen = True
        else:
            sp("Unknown: Try again!")

    
    sp(f"Unknown: Thank you, enjoy the game!")

#the start of the game
def exploration():
    sp("You have entered your new home")
    sp("Since your grandmother Margret's passing, you have inherited the family manor")
    sp(f"Since the disappearances of the entire rest of your family, you {name} are the sole survivor.")
    sp("In front of you is the grand hall, a beautiful golden laced blue carpet lays out around you ")
    sp("You hear a whisper, 'Welcome,' however you are alone.")
    chosen = False
    #
    def Grand_Hall_room():
        chosen = False
        while chosen == False:
            sp("What do you want to do, 1. look around, 2. go upstairs, 3. enter the kithcen 4. Enter the dining room")                
            choice = input("")
            global kitchen1_or_dine2
            kitchen1_or_dine2 = 0
            global up_or_no
            up_or_no = "placeholder"
            #look around
            if choice == "1":
                chosen = False
                sp("You are in the " + Grand_Hall.name + " " + Grand_Hall.description)
                #upstairs
            elif choice == "2":
                chosen = True
                up_or_no = True
                sp("You walk upstairs...")
                #continue
                #secret option
            elif choice == "Margret":
                chosen = False
                #make this lead to something if some other criteria is met
                sp("Your grandma was not a terrible person, she had a nack for getting good buisness deals... it seems like she always had a way of knowing who the higher ups are...")
                
            #kitchen
            elif choice == "3":
                up_or_no = False
                kitchen1_or_dine2 = 1
                chosen = True
            #dining room
            elif choice == "4":
                up_or_no = False
                kitchen1_or_dine2 = 2
                chosen = True
            #idk
            else:
                chosen = False
                sp("not sure what you meant by that...")
    Grand_Hall_room()
    #upstairs, Dining Room, or Kitchen
    if up_or_no == True:
        sp(f"You are in " + {Up_Main_hall_Name} + ", " + {Up_Main_hall_Desc})
    elif kitchen1_or_dine2 == 1:
        sp(f"You are in " + {Kitchen.name} + ", " + {Kitchen.description})
    elif kitchen1_or_dine2 == 2:
        sp(f"You are in " + {diningRoom.name} + ", " + {diningRoom.description})
    else:
        sp()


#when releasing the game un-comment the loading section
#loading()
start()
#loading2()
exploration()
