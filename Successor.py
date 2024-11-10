from MapHandler import OpstaclesUpdator , PlayerMover 

def Successor(gameMap: list, playerLocation: tuple, direction: str, obstacles: list, ballsLocations: list , goalLocations: list):
    '''
    This function returns the successor of the current state based on the possible directions of the player.
    '''
    
    possible_moves = []
    x , y = playerLocation
    # update the obstacles location
    gameMap, obstacles = OpstaclesUpdator(gameMap, obstacles)
    
    # Define potential moves with their corresponding locations
    possibleMoves = {
        'up': (playerLocation[0] - 1, playerLocation[1]),
        'down': (playerLocation[0] + 1, playerLocation[1]),
        'left': (playerLocation[0], playerLocation[1] - 1),
        'right': (playerLocation[0], playerLocation[1] + 1)
    }
    
    # Create a list of potential moves, but we need to check various conditions
    for direction , (new_x , new_y) in possibleMoves.items():
        # Check if the new position is within bounds
        if 0<=new_x<=len(gameMap) and 0<=new_y<=len(gameMap):
            # Check if the new position is not an obstacle (at the player's next move)
            if gameMap[new_x][new_y] == 'X':
                # Check if the new position is an obstacle
                continue
            
            