from MapHandler import MapState
from Successor import Successor
from GoalStateChecker import isGoalState
from queue import PriorityQueue
from Heuristic import heuristic


def greedyBestFirstSearch(initialState: MapState):
    visited = set()
    frontier = PriorityQueue()
    frontier.put((0, initialState))
    visited.add((initialState.playerLocation, tuple(initialState.ballsLocations), tuple(initialState.obstacles)))

    while not frontier.empty():
        cost, currState = frontier.get()

        if isGoalState(currState):

            currState.cost += int(
                currState.gameMap[currState.playerLocation[0]][currState.playerLocation[1]][0])
            currState.depth
            return currState

        successors = Successor(currState, visited)

        for successor in successors:
            if successor.playerLocation not in visited:
                visited.add((successor.playerLocation, tuple(successor.ballsLocations), tuple(successor.obstacles)))
                totalCost = heuristic(successor)
                successor.parent = currState
                successor.cost = currState.cost + \
                    int(currState.gameMap[currState.playerLocation[0]]
                        [currState.playerLocation[1]][0])
                successor.depth = currState.depth + 1

                frontier.put((totalCost, successor))

    return None
