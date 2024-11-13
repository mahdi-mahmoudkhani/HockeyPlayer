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
