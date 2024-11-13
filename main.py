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


