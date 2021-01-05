#######
# Project:      Simple 2D Console Movement System
# Creator:      Martus
# Date:         5th January 2021
# Last Updated: 5th January 2021
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
        
def checkInput(px, py, GameMap):
    import sys
    print("Movement commands: W,A,S,D for movement. Q to exit")
    userInput = input(">  ")
    userInput.lower()
    if userInput == 'q': sys.exit()
    elif userInput == 'w': px-=1
    elif userInput == 's': px+=1
    elif userInput == 'a': py-=1
    elif userInput == 'd': py+=1
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
