def MapCreator():
    '''
    This function creates a map of the game and returns the map as a list of lists of strings and also the locations of the player, balls, goals and obstacles.
    '''
    # input number of rows and columns of the map
    numberOfRows, numberOfColumns = map(int, input().split())
    # input the map of the game as a list of lists of strings (each string is a cell)
    gameMap = [list(input().split(' ')) for _ in range(numberOfRows)]
    # get the locations of the player (P)
    playerLocation = [(rowIndex, colIndex) for rowIndex, row in enumerate(gameMap) for colIndex, cell in
     enumerate(row) if 'P' in cell][0]
    # get the locations of the balls (B)
    ballsLocations = [(rowIndex, colIndex) for rowIndex, row in enumerate(gameMap) for colIndex, cell in enumerate(row) if 'B' in cell]
    # get the locations of the goals (G)
    goalLocations = [(rowIndex, colIndex) for rowIndex, row in enumerate(gameMap) for colIndex, cell in enumerate(row) if 'G' in cell]
    # get the locations of the obstacles (X)
    obstacles = [(rowIndex, colIndex, 'left') for rowIndex, row in enumerate(gameMap) for colIndex, cell in enumerate(row) if 'X' in cell]

    return gameMap, playerLocation, ballsLocations, goalLocations, obstacles
