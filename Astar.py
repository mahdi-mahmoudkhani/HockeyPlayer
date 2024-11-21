from GoalStateChecker import isGoalState
from Successor import Successor
from MapHandler import MapState
from queue import PriorityQueue
from Heuristic import heuristic


def aStarSearch(initialState):
    visited = set()
    frontier = PriorityQueue()
    frontier.put((0, initialState))
    visited.add((initialState.playerLocation,
                tuple(initialState.ballsLocations)))

    expandedNodes = 0

    while not frontier.empty():
        _ , currState = frontier.get()
        expandedNodes += 1

        if isGoalState(currState):
            return currState

        successors = Successor(currState, visited)

        for successor in successors:
            if ((successor.playerLocation, tuple(successor.ballsLocations), tuple(successor.obstacles))) not in visited:
                visited.add((successor.playerLocation,
                            tuple(successor.ballsLocations),
                            tuple(successor.obstacles)))
                totalCost = heuristic(successor) + successor.cost
                frontier.put((totalCost, successor))

    return None  # If no solution is found
