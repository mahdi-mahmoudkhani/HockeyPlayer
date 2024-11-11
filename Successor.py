from MapHandler import OpstaclesUpdator , PlayerMover , checkIfBallIsInGoal

def Successor(gameMap, playerLocation, ballsLocations, obstacles, visited):
    
    '''
    This function returns the successor of the current state based on the possible directions of the player.
    '''
    
    successors = []
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
      
        # Check if the new position is a ball
        new_gameMap, new_playerLocation, new_ballsLocations = PlayerMover(next_gameMap, playerLocation, direction, ballsLocations)
        #check if in the next move the ball is in the goal
        new_gameMap, new_ballsLocations, goalLocations, new_obstacles = checkIfBallIsInGoal(new_gameMap, new_ballsLocations, goalLocations, new_obstacles)
        
        if isValidState(new_gameMap, new_playerLocation, new_ballsLocations, next_obstacles):
            successors.append((new_gameMap, new_playerLocation, new_ballsLocations, next_obstacles, new_visited))
        
        return successors

        
def isValidState(gameMap: list, playerLocation: tuple, ballsLocations: list, obstacles: list):
    '''
    This function checks if the state of the game is valid by checking wether the balls hit x or not 
    '''
    for ball in ballsLocations:
        if ball in obstacles:
            return False
        if ballsLocations.count(ball) > 1:
            return False
    return True
            
            