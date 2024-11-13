from MapHandler import MapState
from BFSAlgorithm import BFSAlgorithm
from DFSAlgorithm import DFSAlgorithm
from UCSAlgorithm import UCSAlgorithm
from IDSAlgorithm import IDSAlgorithm
from Astar import aStarSearch
from GreedyBestFirstSearch import greedyBestFirstSearch
from IDAstar import IDAstarSearch
from PathReconstructor import reconstruct_path

def convertToInputMapString(userInput):
    map = userInput.split()
    numberOfRows = int(map[0])
    numberOfColumns = int(map[1])
    inputMapString = " ".join(map[2:])

    return numberOfRows, numberOfColumns, inputMapString

if __name__ == "__main__":

    givenGameMap = '''
                    6 10
                    1P 1B 1G 1 0 X 1 1 1 1
                    0 X 1 1 0 0 0 1 0 X
                    0 0 1 2B 2 2 2B 1 0 0
                    1 1 0 X X 2 2 1 1G 1
                    1 1 0 0 0 2 1 1 1 1
                    1 1 1 1 1 1G 1 1 1 1
                    '''
   
    numberOfRows, numberOfColumns, inputMapString = convertToInputMapString(
        givenGameMap)
    object = MapState(numberOfRows, numberOfColumns, inputMapString)

 # Breadth First Search Algorithm output
    finalState = BFSAlgorithm(object)
    print("Breath First Search answer:\nsteps: {}\ntotal_cost: {}\ntotal_depth: {}".format(
        reconstruct_path(finalState)[:50], finalState.cost, finalState.depth))
    print("\n-----------------------------\n")

# Depth First Search Algorithm output
    finalState = DFSAlgorithm(object)
    print("Depth First Search answer:\nsteps: {}\ntotal_cost: {}\ntotal_depth: {}".format(
        reconstruct_path(finalState)[:50], finalState.cost, finalState.depth))
    print("\n-----------------------------\n")
    
# Uniform Cost Search Algorithm output
    finalState = UCSAlgorithm(object)
    print("Uniform Cost Search answer:\nsteps: {}\ntotal_cost: {}\ntotal_depth: {}".format(
        reconstruct_path(finalState)[:50], finalState.cost, finalState.depth))
    print("\n-----------------------------\n")

# Iterative Deepening Search Algorithm output
    finalState = IDSAlgorithm(object)
    print("Iterative Deepening Search answer:\nsteps: {}\ntotal_cost: {}\ntotal_depth: {}".format(
        reconstruct_path(finalState)[:50], finalState.cost, finalState.depth))
    print("\n-----------------------------\n")
    
# A* Search Algorithm output
    finalState = aStarSearch(object)
    print("A* Search answer:\nsteps: {}\ntotal_cost: {}\ntotal_depth: {}".format(
        reconstruct_path(finalState)[:50], finalState.cost, finalState.depth))
    print("\n-----------------------------\n")
    
    # Greedy Best First Search Algorithm output
    finalState = greedyBestFirstSearch(object)
    print("Greedy Best First Search answer:\nsteps: {}\ntotal_cost: {}\ntotal_depth: {}".format(
        reconstruct_path(finalState)[:50], finalState.cost, finalState.depth))
    print("\n-----------------------------\n")

    # Iterative Deepening A* Search Algorithm output
    finalState = IDSAlgorithm(object, True)
    print("Iterative Deepening A* Search answer:\nsteps: {}\ntotal_cost: {}\ntotal_depth: {}".format(
         reconstruct_path(finalState)[:50], finalState.cost, finalState.depth))
    print("\n-----------------------------\n")