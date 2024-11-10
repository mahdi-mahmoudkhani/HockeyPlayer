from MapHandler import OpstaclesUpdator , PlayerMover 

def Successor(gameMap: list, playerLocation: tuple, direction: str, obstacles: list, ballsLocations: list , goalLocations: list):
    '''
    This function returns the successor of the current state based on the possible directions of the player.
    '''
    # update the obstacles location
    gameMap, obstacles = OpstaclesUpdator(gameMap, obstacles)
    
    # Define potential moves with their corresponding locations
    possibleMoves = {
        'up': (playerLocation[0] - 1, playerLocation[1]),
        'down': (playerLocation[0] + 1, playerLocation[1]),
        'left': (playerLocation[0], playerLocation[1] - 1),
        'right': (playerLocation[0], playerLocation[1] + 1)
    }
    
    