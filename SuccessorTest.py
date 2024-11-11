from MapHandlerTest import *
from Successor import *

userInput = '''
            6 10
            1P 1B 1G 1 0 X 1 1 1 1
            0 X 1 1 0 0 0 1 0 X
            0 0 1 2B 2 2 2B 1 0 0
            1 1 0 X X 2 2 1 1G 1
            1 1 0 0 0 2 1 1 1 1
            1 1 1 1 1 1G 1 1 1 1
            '''
numberOfRows, numberOfColumns, inputMapString = convertToInputMapString(
    userInput)
object = MapState(numberOfRows, numberOfColumns, inputMapString)

firstsuccessors = Successor(object, set())
print(firstsuccessors[0].gameMap)
print(firstsuccessors[0].playerLocation)
print(firstsuccessors[0].ballsLocations)
print(firstsuccessors[0].goalLocations)
print(firstsuccessors[0].obstacles)
print("\n\n------------------------------\n\n")

secondsuccessors = Successor(firstsuccessors[0], set())
print(secondsuccessors[0].gameMap)
print(secondsuccessors[0].playerLocation)
print(secondsuccessors[0].ballsLocations)
print(secondsuccessors[0].goalLocations)
print(secondsuccessors[0].obstacles)
print("\n\n------------------------------\n\n")

print(secondsuccessors[1].gameMap)
print(secondsuccessors[1].playerLocation)
print(secondsuccessors[1].ballsLocations)
print(secondsuccessors[1].goalLocations)
print(secondsuccessors[1].obstacles)