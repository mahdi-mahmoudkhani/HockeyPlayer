
from MapHandler import *
def Successor(currentMapState: MapState, visited):
    '''
    This function returns the successor of the current state based on the possible directions of the player.
    '''

    successors = []
    x, y = currentMapState.playerLocation

    # Define potential moves with their corresponding locations
    possibleMoves = [("up", -1, 0), ("down", 1, 0),
                     ("left", 0, -1), ("right", 0, 1)]

    # Create a list of potential moves, but we need to check various conditions
    for direction, dx, dy in possibleMoves:

        # Create a copy of the current state
        newMapState = currentMapState.__copy__()
        # Update the obstacles location
        newMapState.OpstaclesUpdator()

        new_x = x + dx
        new_y = y + dy

        # Check if the new position is within bounds
        if not (0 <= new_x < newMapState.numberOfRows and 0 <= new_y < newMapState.numberOfColumns):
            continue

        # Check if the new position is not an obstacle (at the player's next move)
        if newMapState.gameMap[new_x][new_y] == 'X':
            continue

        # Check if it was seen before
        if (new_x, new_y) in visited:
            continue

        # If it's not seen then add this step
        visitedNew = visited.copy()
        visitedNew.add((new_x, new_y))

        # Move the player
        newMapState.PlayerMover(direction)

        # Check if in the next move the ball is in the goal
        newMapState.checkIfBallIsInGoal()
        

        if isValidState(newMapState):
            successors.append(newMapState)

    return successors


def isValidState(currentMapState: MapState):
    """
    Checks if the state of the game is valid.

    This function verifies the validity of the game state by ensuring that no ball is located in an obstacle 
    and that no ball appears more than once in the list of ball locations.

    Parameters:
    mapState (MapState): The current state of the game encapsulated in a MapState object.

    Returns:
    bool: True if the game state is valid, False otherwise.
    """
    for ball in currentMapState.ballsLocations:
        if ball in currentMapState.obstacles:
            return False
        if currentMapState.ballsLocations.count(ball) > 1:
            return False
    return True
