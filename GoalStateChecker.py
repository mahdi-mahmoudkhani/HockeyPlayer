from MapHandler import MapState


def isGoalState(currentMapState: MapState):
    '''
    This function checks if the current state is the goal state.
    '''
    return currentMapState.ballsLocations == []
