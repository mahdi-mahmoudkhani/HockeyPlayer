
from MapHandler import MapState
from Successor import Successor
from GoalStateChecker import isGoalState
from Heuristic import heuristic


def IDAstarSearch(initialState: MapState):

    def Search(currState, cost, limit):
        if isGoalState(currState):
            currState.cost += int(
                currState.gameMap[currState.playerLocation[0]][currState.playerLocation[1]][0])
            return currState, True
        
        if cost >= limit:
            return None, False  # not found
        
        newCost = float('inf')
        found = False
        successors = Successor(currState, set())
        for successor in successors:
            try:
                if ((successor.playerLocation, tuple(successor.ballsLocations), tuple(successor.obstacles))) != (currState.parent.playerLocation, tuple(currState.parent.ballsLocations), tuple(currState.parent.obstacles)):
                    newCost = cost + heuristic(successor) + successor.cost
                    result, found = Search(successor, newCost, limit)
            except:
                newCost = cost + heuristic(successor) + successor.cost
                result, found = Search(successor, newCost, limit)
            if found:
                return result, True
        return None, False  # not found

    limit = heuristic(initialState)

    while True:
        result, found = Search(initialState, 0, limit)
        if found:
            return result
        limit += 1
    return None
