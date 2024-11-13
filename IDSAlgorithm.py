from MapHandler import MapState
from DLSAlgorithm import DLSAlgorithm

def IDSAlgorithm(mapState: MapState, maxLimit = float('inf')):
    '''
    This function is the implementation of the Iterative Deepening Search Algorithm.
    It will call the DLSAlgorithm function with increasing depth limits until the solution is found or the maxLimit is reached.
    The maxLimit is entered by the user and is the maximum depth the algorithm will search to.
    '''
    depth = 0
    while depth <= maxLimit:
        print("Searching at depth:", depth, "using IDS Algorithm")
        result = DLSAlgorithm(mapState, depth)
        if result is not None:
            return result
        depth += 1

    return None