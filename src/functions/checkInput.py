class checkInut:
    def checkInput(px, py, GameMap):
        from commands import commands
        speed = 1
        print(
        "Movement commands: W,A,S,D for movement. Q to exit."
        +
        "\nyou can also add a number between 1 and 9 in front of the movement commands."
        +
        "\nExample: 4w"
        )
        userInput = input(">  ")

        # Check for if there is a number before command
        try:
            ammount = int(userInput[0])*speed
            command = str(userInput[1])
            command.lower()
        except:
            ammount = speed
            command = userInput
            command.lower()

        cordinates = commands.commands(px,py,ammount,command,GameMap)
        return cordinates