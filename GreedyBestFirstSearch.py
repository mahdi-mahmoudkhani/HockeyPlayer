from MapHandler import MapState
from Successor import Successor
from GoalStateChecker import isGoalState
from queue import PriorityQueue

def greedyBestFirstSearch(initialState: MapState):
    visited  = set()
    frontier = PriorityQueue()
    frontier.put((0,initialState))
    visited.add(initialState.playerLocation)
    

