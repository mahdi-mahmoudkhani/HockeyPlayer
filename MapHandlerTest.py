from MapHandler import MapState , checkIfBallIsInGoal , PlayerMover , OpstaclesUpdator 

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
print(object.gameMap)
print(object.playerLocation)
print(object.ballsLocations)
print(object.goalLocations)
print(object.obstacles)

object.OpstaclesUpdator()
print(object.gameMap)
print(object.obstacles)

object.PlayerMover('right')
print(object.gameMap)
print(object.playerLocation)
print(object.ballsLocations)

object.checkIfBallIsInGoal()
print(object.gameMap)
print(object.ballsLocations)
print(object.goalLocations)
print(object.obstacles)
