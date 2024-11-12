from MapHandler import MapState
from GoalStateChecker import isGoalState
from Successor import Successor
import heapq

def UCSAlgorithm(mapState: MapState):
    '''
    This function is the implementation of the Uniform Cost Search Algorithm.
    It will use a priority queue to store the states and their costs.
    The states will be popped from the queue based on their costs.
    The algorithm will continue until the goal state is found.
    '''
    priorityQueue = []
    # Push the initial state to the priority queue with a cost of 0
    heapq.heappush(priorityQueue, (0, mapState))
    visited = []
    while priorityQueue:
        # Pop the mapState with the lowest cost
        currentState = heapq.heappop(priorityQueue)[1]
        # If the current state is the goal state
        if isGoalState(currentState):
            return currentState

        else:
            # Add the current state to the visited list
            visited.append((currentState.playerLocation,
                            tuple(currentState.ballsLocations)))
            # Get the successors of the current state
            successors = Successor(currentState, visited)
            for successor in successors:
                # Add the successor to the priority queue
                heapq.heappush(priorityQueue, (successor.cost, successor))

    return None
