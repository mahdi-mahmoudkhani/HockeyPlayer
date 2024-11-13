from manhattanDist import manhattanDistance
from MapHandler import MapState

def heuristic(mapState: MapState):
    '''
    This function returns the heuristic value of the current
    state based on the manhattan distance between the player and the closest ball + the ball and the closest goal.
    '''
    
     # get the manhattan distance between the player and the closest ball
    playerToBall = min([manhattanDistance(mapState.playerLocation, ball) for ball in mapState.ballsLocations
                         if ball not in mapState.goalLocations], default=None)
    ballToGoal = min([manhattanDistance(ball, mapState.goal) for ball in mapState.ballsLocations
        if ball not in mapState.goalLocations], default=None)
    return playerToBall + ballToGoal