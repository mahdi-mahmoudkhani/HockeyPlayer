
def aStarSearch(initialState: MapState):
    visited  = set()
    frontier = PriorityQueue()
    frontier.put((0,initialState))
    visited.add(initialState.playerLocation)
    
    expandedNodes = 0
    
    while not frontier.empty():
        cost , currState = frontier.get()
        expandedNodes += 1
        
        
    return None
    
    
