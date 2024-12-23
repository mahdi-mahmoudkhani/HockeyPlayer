from MapHandler import MapState
from GoalStateChecker import isGoalState
from Successor import Successor


def DLSAlgorithm(mapState: MapState, limit):
    # Initialize the stack
    stack = []
    stack.append(mapState)

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

        elif currentState.depth >= limit:
            continue

        # If the current state is not the goal state
        else:
            # Get the successors of the current state
            successors = Successor(currentState, set())

            # For each successor
            for successor in successors[::-1]:
                # If the successor is not visited
                try:
                    if (successor.playerLocation, tuple(successor.ballsLocations), tuple(successor.obstacles)) != (currentState.parent.playerLocation, tuple(currentState.parent.ballsLocations), tuple(successor.parent.obstacles)):
                        # Add the successor to the stack
                        stack.append(successor)
                except:
                    stack.append(successor)

    # If the stack is empty and the goal state is not found
    return None
