from queue import Queue
from Successor import Successor

def BFS(gameMap, playerLocation, ballsLocations, goalLocations, obstacles):
    '''
    This function returns the path from the initial state to the goal state using the BFS search algorithm.
    '''
     # initialize the queue with the initial state
    queue = [(gameMap, playerLocation, ballsLocations, obstacles, set([playerLocation]))]
    path = []
    
     # initialize the visited set with the initial state
    visited = set([playerLocation])
    
    # loop until the queue gets empty
    while queue :
        # get the first element in the queue
        current_gameMap, current_playerLocation, current_ballsLocations, current_obstacles, current_visited = queue.pop(0)
        if current_ballsLocations == goalLocations:
            return path
              
        # get the successors of the current state
        successors = Successor(current_gameMap, current_playerLocation, current_ballsLocations, current_obstacles, current_visited)
       
        
    # return None if no path is found
    return None
        
        
     