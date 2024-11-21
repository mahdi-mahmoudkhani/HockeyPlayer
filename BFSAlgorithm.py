from MapHandler import MapState
from GoalStateChecker import isGoalState
from Successor import Successor


def BFSAlgorithm(initialState: MapState):
    '''
    This function implements the Breadth-First Search algorithm to solve the game.
    '''
    # Initialize the frontier with the initial state
    frontier = [initialState]
    # Initialize the explored set as an empty set
    explored = set()

    # Check if the initial state is the goal state
    if isGoalState(initialState):
        return initialState

    # While the frontier is not empty
    while frontier:
        # Get the first state from the frontier
        currentState = frontier.pop(0)
        # Add the current state to the explored set
        explored.add((currentState.playerLocation,
                     tuple(currentState.ballsLocations),
                     tuple(currentState.obstacles)))

        # Get the successors of the current state
        successors = Successor(currentState, explored)

        # For each successor
        for successor in successors:
            # Check if the successor is the goal state
            if isGoalState(successor):
                successor.cost += int(
                    successor.gameMap[successor.playerLocation[0]][successor.playerLocation[1]][0])
                return successor
            # Add the successor to the frontier
            frontier.append(successor)

    return None
