from manhattanDist import manhattanDistance
def heuristic(gameMap: list, playerLocation: tuple, ballsLocations: list, goalLocations: list):
    '''
    This function returns the heuristic value of the current
    state based on the manhattan distance between the player and the closest ball + the ball and the closest goal.
    '''
    
     # get the manhattan distance between the player and the closest ball
    playerToBall = min([manhattanDistance(playerLocation, ball) for ball in ballsLocations
                         if ball not in goalLocations], default=None)
    ballToGoal = min([manhattanDistance(ball, goal) for ball in ballsLocations
        if ball not in goalLocations], default=None)
    return playerToBall + ballToGoal