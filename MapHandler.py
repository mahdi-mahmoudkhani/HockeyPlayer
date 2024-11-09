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

def OpstaclesUpdator(gameMap: list, obstacles: list):
    '''
    This function updates the location of obstacles in the map based on the direction of the obstacles. and returns the updated map and obstacles.
    '''
    for obstacle in obstacles:
        rowIndex, colIndex, direction = obstacle
        # update the location of the obstacle based on its direction
        # update the direction of the obstacle 
        if direction == 'left':
            gameMap[rowIndex][colIndex] = '0'
            gameMap[rowIndex][colIndex - 1] = 'X'
            obstacles[obstacles.index(obstacle)] = (rowIndex, colIndex - 1, 'down')
        elif direction == 'down':
            gameMap[rowIndex][colIndex] = '0'
            gameMap[rowIndex + 1][colIndex] = 'X'
            obstacles[obstacles.index(obstacle)] = (rowIndex + 1, colIndex, 'right')
        elif direction == 'right':
            gameMap[rowIndex][colIndex] = '0'
            gameMap[rowIndex][colIndex + 1] = 'X'
            obstacles[obstacles.index(obstacle)] = (rowIndex, colIndex + 1, 'up')
        elif direction == 'up':
            gameMap[rowIndex][colIndex] = '0'
            gameMap[rowIndex - 1][colIndex] = 'X'
            obstacles[obstacles.index(obstacle)] = (rowIndex - 1, colIndex, 'left')

    return gameMap, obstacles