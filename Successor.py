from MapHandler import OpstaclesUpdator , PlayerMover 

def Successor(gameMap, playerLocation, ballsLocations, obstacles, visited):
    
    '''
    This function returns the successor of the current state based on the possible directions of the player.
    '''
    
    possible_moves = []
    x , y = playerLocation
    # update the obstacles location
    gameMap, obstacles = OpstaclesUpdator(gameMap, obstacles)
    
    # Define potential moves with their corresponding locations
    possibleMoves = [("up", -1, 0), ("down", 1, 0), ("left", 0, -1), ("right", 0, 1)]
    
    # Create a list of potential moves, but we need to check various conditions
    for direction , dx , dy in possibleMoves.items():
        new_x = x + dx
        new_y = y + dy
        
        # Check if the new position is within bounds
        if not( 0<=new_x<len(gameMap) and 0<= new_y< len(gameMap)):
            continue
        
        # Check if the new position is not an obstacle (at the player's next move)
        if gameMap[new_x][new_y] == 'X':
            continue
        #check if it was seen before
        if (new_x , new_y) in visited :
            continue
        #if its not seen then add this step 
        visitedNew = visited.copy()
        visitedNew.add((new_x , new_y))
        
        
        if (new_x , new_y) in ballsLocations :
            new_xBall = new_x + (new_x-playerLocation[0])
            new_yBall = new_y + (new_y - playerLocation[1])
            if gameMap[new_xBall][new_yBall] != 'X':
                possible_moves.append(gameMap[new_x][new_y])
                    
                    
    
            
            