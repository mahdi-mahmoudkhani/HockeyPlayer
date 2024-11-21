from MapHandler import MapState


def Successor(currentMapState: MapState, visited):
    '''
    This function returns the successor of the current state based on the possible directions of the player.
    '''

    successors = []
    x, y = currentMapState.playerLocation

    # Define potential moves with their corresponding locations
    possibleMoves = [("right", 0, 1), ("down", 1, 0),
                     ("left", 0, -1), ("up", -1, 0)]

    # Create a list of potential moves, but we need to check various conditions
    for direction, dx, dy in possibleMoves:

        new_x = x + dx
        new_y = y + dy

        # Create a copy of the current state
        try:
            newMapState = currentMapState.__copy__(
                direction, currentMapState.depth + 1, currentMapState.cost + int(currentMapState.gameMap[x][y][0]))
        except:
            newMapState = currentMapState.__copy__(
                direction, currentMapState.depth + 1, currentMapState.cost)
        # Update the obstacles location
        newMapState.OpstaclesUpdator()

        # Check if the new position is within bounds
        if not (0 <= new_x < newMapState.numberOfRows and 0 <= new_y < newMapState.numberOfColumns):
            continue

        # Check if the new position is not an obstacle (at the player's next move)
        if newMapState.gameMap[new_x][new_y] == 'X':
            continue

        # Move the player
        try:
            newMapState.PlayerMover(direction)
        except:
            continue

        # Check if in the next move the ball is in the goal
        newMapState.checkIfBallIsInGoal()

        # If the state is seen before, then we don't need to consider it again
        if (newMapState.playerLocation, tuple(newMapState.ballsLocations), tuple(newMapState.obstacles)) in visited:
            continue

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
    obstaclesLocations = []
    for obstacle in currentMapState.obstacles:
        obstaclesLocations.append(obstacle[:2])

    for ball in currentMapState.ballsLocations:
        if ball in obstaclesLocations:
            return False
        if currentMapState.ballsLocations.count(ball) > 1:
            return False
        if ball[0] < 0 or ball[0] >= currentMapState.numberOfRows:
            return False
        if ball[1] < 0 or ball[1] >= currentMapState.numberOfColumns:
            return False
    return True
