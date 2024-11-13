from GoalStateChecker import isGoalState
from Successor import Successor
from MapHandler import MapState
from queue import PriorityQueue
from Heuristic import heuristic
def aStarSearch(initialState):
    visited = set()
    frontier = PriorityQueue()  
    frontier.put((0, initialState)) 
    visited.add((initialState.playerLocation, tuple(initialState.ballsLocations)))
    
    expandedNodes = 0
    
    while not frontier.empty():
        cost, currState = frontier.get()  
        expandedNodes += 1
        
        
        if isGoalState(currState):
            total_cost = currState.cost + int(currState.gameMap[currState.playerLocation[0]][currState.playerLocation[1]][0])
            steps = currState.depth + 1
            
            return currState 
        
        
        successors = Successor(currState, visited)
        
        for successor in successors:
            if (successor.playerLocation, tuple(successor.ballsLocations)) not in visited:
                visited.add((successor.playerLocation, tuple(successor.ballsLocations)))
                totalCost = heuristic(successor) + successor.cost
                frontier.put((totalCost, successor)) 
            
    return None  # If no solution is found
