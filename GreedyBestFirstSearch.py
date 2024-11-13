from MapHandler import MapState
from Successor import Successor
from GoalStateChecker import isGoalState
from queue import PriorityQueue
from Heuristic import Heuristic

def greedyBestFirstSearch(initialState: MapState):
    visited  = set()
    frontier = PriorityQueue()
    frontier.put((0,initialState))
    visited.add(initialState.playerLocation)
    
    
    while not frontier.empty():
        cost , currState = frontier.get()
        if isGoalState(currState):
            currState.cost += int(currState.gameMap[currState.playerLocation[0]][currState.playerLocation[1]][0])
            currState.depth += 1
            return currState
        
        successors = Successor(currState,visited)
        
        for Successor in successors :
            if Successor.playerLocation not in visited:
                visited.add(Successor.playerLocation)
                frontier.put(Heuristic(Successor) ,Successor)
        
    return None
               
        

