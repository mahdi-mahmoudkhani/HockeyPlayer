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

def PlayerMover(gameMap: list, playerLocation: tuple, direction: str, ballsLocations: list):
    '''
    This function moves the player in the map based on the direction and returns the updated map, player location and balls locations.
    '''
    rowIndex, colIndex = playerLocation
    # move the player based on the direction
    if direction == 'up':
        gameMap[rowIndex][colIndex] = gameMap[rowIndex][colIndex][0]
        if 'B' in gameMap[rowIndex - 1][colIndex]:
            gameMap[rowIndex - 1][colIndex] = gameMap[rowIndex - 1][colIndex][0]
            gameMap[rowIndex - 2][colIndex] += 'B'
            ballsLocations[ballsLocations.index((rowIndex - 1, colIndex))] = (rowIndex - 2, colIndex)
        gameMap[rowIndex - 1][colIndex] += 'P'
        playerLocation = (rowIndex - 1, colIndex)

    elif direction == 'down':
        gameMap[rowIndex][colIndex] = gameMap[rowIndex][colIndex][0]
        if 'B' in gameMap[rowIndex + 1][colIndex]:
            gameMap[rowIndex + 1][colIndex] = gameMap[rowIndex + 1][colIndex][0]
            gameMap[rowIndex + 2][colIndex] += 'B'
            ballsLocations[ballsLocations.index((rowIndex + 1, colIndex))] = (rowIndex + 2, colIndex)
        gameMap[rowIndex + 1][colIndex] += 'P'
        playerLocation = (rowIndex + 1, colIndex)
    elif direction == 'left':
        gameMap[rowIndex][colIndex] = gameMap[rowIndex][colIndex][0]
        if 'B' in gameMap[rowIndex][colIndex - 1]:
            gameMap[rowIndex][colIndex - 1] = gameMap[rowIndex][colIndex - 1][0]
            gameMap[rowIndex][colIndex - 2] += 'B'
            ballsLocations[ballsLocations.index((rowIndex, colIndex - 1))] = (rowIndex, colIndex - 2)
        gameMap[rowIndex][colIndex - 1] += 'P'
        playerLocation = (rowIndex, colIndex - 1)
    elif direction == 'right':
        gameMap[rowIndex][colIndex] = gameMap[rowIndex][colIndex][0]
        if 'B' in gameMap[rowIndex][colIndex + 1]:
            gameMap[rowIndex][colIndex + 1] = gameMap[rowIndex][colIndex + 1][0]
            gameMap[rowIndex][colIndex + 2] += 'B'
            ballsLocations[ballsLocations.index((rowIndex, colIndex + 1))] = (rowIndex, colIndex + 2)
        gameMap[rowIndex][colIndex + 1] += 'P'
        playerLocation = (rowIndex, colIndex + 1)
    

    return gameMap, playerLocation, ballsLocations

def checkIfBallIsInGoal(gameMap: list, ballsLocations: list, goalLocations: list, obstacles: list):
    '''
    This function checks if a ball is in a goal and returns the updated map, balls locations and goal locations.
    '''
    for ball in ballsLocations:
        if ball in goalLocations:
            ballsLocations.remove(ball)
            goalLocations.remove(ball)
            gameMap[ball[0]][ball[1]] = 'X'
            obstacles.append((ball[0], ball[1], None))
    
    return gameMap, ballsLocations, goalLocations, obstacles
