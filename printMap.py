class printMap:
    def printMap(px,py,GameMap,mapSx,mapSy):
        import os
        os.system("cls")
        output = ""
        for x in range(mapSx):
            for y in range(mapSy):
                if(px == x and py == y): output += "P"
                elif GameMap[x][y] == 1: output += "x"
                elif GameMap[x][y] == 0: output += " "
            print(output)
            output = ""