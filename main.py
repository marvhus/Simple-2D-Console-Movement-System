#######
# Project:      Simple 2D Console Movement System
# Creator:      Martin
# Date:         5th January 2021
# Last Updated: 6th January 2021
#######

from checkInput import checkInput
from printMap import printMap

mapSx = 8
mapSy = 15
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
# Walls = 1 = x       Floor = 0 = (space)   Player = PW

while True:
    printMap.printMap(px, py, GameMap,mapSx,mapSy)
    print(f"PlayerX: {px}\nPlayerY: {py}")
    cordinates = checkInput.checkInput(px, py, GameMap)
    px = cordinates[0]
    py = cordinates[1]
