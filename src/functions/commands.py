class commands:
    def moveCommands(px,py,ammount,command,GameMap):
        from colission import  colission

        # Exit
        if command == "q": 
            from sys import exit
            exit()

        # Movement if statements
        ###### Move UP ########################################
        elif command == 'w': 
            if not colission.colission(px-ammount,py,GameMap): 
                px-=ammount
        ###### Move DOWN ######################################
        elif command == 's': 
            if not colission.colission(px+ammount,py,GameMap): 
                px+=ammount
        ###### Move LEFT ######################################
        elif command == 'a': 
            if not colission.colission(px,py-ammount,GameMap): 
                py-=ammount
        ###### Move RIGHT #####################################
        elif command == 'd': 
            if not colission.colission(px,py+ammount,GameMap): 
                py+=ammount
        #######################################################

        # Atempt on patching the out of bounds glitch
        #######################
        if ( px < 0 ):      # w
            px = 1          # w
        #######################
        if ( px >  8 ):     # s
            px = 7          # s
        #######################
        if ( py < 0 ):      # a
            py = 1          # a
        #######################
        if ( py >  15 ):    # d 
            py = 14         # d
        #######################

        cordinates = [px, py]
        return cordinates