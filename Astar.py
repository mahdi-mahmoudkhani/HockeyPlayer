from GoalStateChecker import isGoalState
from Successor import Successor
from MapHandler import MapState
from queue import PriorityQueue
def aStarSearch(initialState: MapState):
    visited  = set()
    frontier = PriorityQueue()
    frontier.put((0,initialState))
    visited.add(initialState.playerLocation)
    
    expandedNodes = 0
    
    while not frontier.empty():
        cost , currState = frontier.get()
        expandedNodes += 1
        if isGoalState(currState):
            currState.cost += int(currState.gameMap[currState.playerLocation[0]][currState.playerLocation[1]][0])
            currState.depth += 1
            return currState
        
        successors = Successor(currState,visited)
        
        for Successor in successors:
            if Successor.playerLocation not in visited:
                visited.add(Successor.playerLocation)
                totalCost = Heuristic(Successor) + Successor.cost
                frontier.put(totalCost,Successor)
            
            
        
    return None