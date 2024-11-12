from MapHandler import MapState
from GoalStateChecker import isGoalState
from Successor import Successor

def DFSAlgorithm(mapState: MapState):
    # Initialize the stack
    stack = []
    stack.append(mapState)

    # Initialize the visited list
    visited = []

    # While the stack is not empty
    while stack:
        # Pop the last element from the stack
        currentState = stack.pop()

        # If the current state is the goal state
        if isGoalState(currentState):
            # Return the current state
            currentState.cost += int(
                currentState.gameMap[currentState.playerLocation[0]][currentState.playerLocation[1]][0])
            return currentState

        # If the current state is not the goal state
        else:
            # Add the current state to the visited list
            visited.append((currentState.playerLocation,
                           tuple(currentState.ballsLocations)))

            # Get the successors of the current state
            successors = Successor(currentState, visited)

            # For each successor
            for successor in successors:
                # Add the successor to the stack
                stack.append(successor)

    # If the stack is empty and the goal state is not found
    return None
