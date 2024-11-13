
from MapHandler import MapState
from Successor import Successor
from GoalStateChecker import isGoalState
from Heuristic import heuristic


def IDAstarSearch(initialState: MapState):
    visited = set()

    def Search(currState, cost, limit):
        if isGoalState(currState):
            currState.cost += int(
                currState.gameMap[currState.playerLocation[0]][currState.playerLocation[1]][0])
            return currState, True
        if cost > limit:
            return None, False  # not found
        newCost = float('inf')
        successors = Successor(currState, visited)
        for successor in successors:
            if successor not in visited:
                visited.add((successor.playerLocation,
                            tuple(successor.ballsLocations)))
                newCost = cost + heuristic(successor) + successor.cost
                result, found = Search(successor, newCost, limit)
            if found:
                return result, True
        return None, False  # not found

    limit = heuristic(initialState)
    while True:
        print("Searching with limit: ", limit, "using IDA*")
        result, found = Search(initialState, 0, limit)
        if found:
            return result
        limit += 1
    return None
