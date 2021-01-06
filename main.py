#######
# Project:      Simple 2D Console Movement System
# Creator:      Martin
# Date:         5th January 2021
# Last Updated: 6th January 2021
#######
def printMap(px, py, GameMap):
    import os
    os.system("cls")
    output = ""
    mapSx = 8
    mapSy = 15
    for x in range(mapSx):
        for y in range(mapSy):
            if(px == x and py == y): output += "P"
            elif GameMap[x][y] == 1: output += "x"
            elif GameMap[x][y] == 0: output += " "
        print(output)
        output = ""
        
def colission(x,y):
    if(GameMap[x][y] == 1): return True
    else: return False

def checkInput(px, py, GameMap):
    import sys
    speed = 1
    print(
    "Movement commands: W,A,S,D for movement. Q to exit."
    +
    "\nyou can also add a number between 1 and 9 in front of the movement commands."
    +
    "\nExample: 4w "
    )
    userInput = input(">  ")

    try:
        ammount = int(userInput[0])*speed
        command = str(userInput[1])
        command.lower()

        if command == 'w': 
            if not colission(px-ammount, py): px-=ammount

        elif command == 's': 
            if not colission(px+ammount,py): px+=ammount

        elif command == 'a': 
            if not colission(px,py-ammount): py-=ammount

        elif command == 'd': 
            if not colission(px,py+ammount): py+=ammount

    except:
        userInput.lower()
        if userInput == 'q': sys.exit()

        elif userInput == 'w': 
            if not colission(px-speed, py): px-=speed

        elif userInput == 's': 
            if not colission(px+speed,py): px+=speed

        elif userInput == 'a': 
            if not colission(px,py-speed): py-=speed

        elif userInput == 'd': 
            if not colission(px,py+speed): py+=speed

    cordinates = [px, py]
    return cordinates

px = 3
py = 3
GameMap = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
""" Walls = 1 = x       Floor = 0 = (space)   Player = P   map size x=5 y=8 5*8
xxxxxxxxxxxxxxx
x           x x
x           x x
x P     x   x x
x  x    x     x
x  x          x
x  x          x
xxxxxxxxxxxxxxx
"""

while True:
    printMap(px, py, GameMap)
    cordinates = checkInput(px, py, GameMap)
    px = cordinates[0]
    py = cordinates[1]
