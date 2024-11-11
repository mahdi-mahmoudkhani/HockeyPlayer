class MapState:
    def __init__(self, numberOfRows, numberOfColumns, inputMapString):
        '''
        This function initializes the map of the game and sets the locations of the player, balls, goals and obstacles.
        '''
        # get the number of rows and columns of the map of the game
        self.numberOfRows, self.numberOfColumns = numberOfRows, numberOfColumns
        # get the map of the game as a 2D list
        self.gameMap = [inputMapString.split()[i:i + self.numberOfColumns] for i in range(
            0, len(inputMapString.split()), self.numberOfColumns)]
        # get the locations of the player (P)
        self.playerLocation = [(rowIndex, colIndex) for rowIndex, row in enumerate(self.gameMap) for colIndex, cell in
                               enumerate(row) if 'P' in cell][0]
        # get the locations of the balls (B)
        self.ballsLocations = [(rowIndex, colIndex) for rowIndex, row in enumerate(
            self.gameMap) for colIndex, cell in enumerate(row) if 'B' in cell]
        # get the locations of the goals (G)
        self.goalLocations = [(rowIndex, colIndex) for rowIndex, row in enumerate(
            self.gameMap) for colIndex, cell in enumerate(row) if 'G' in cell]
        # get the locations of the obstacles (X)
        self.obstacles = [(rowIndex, colIndex, 'left') for rowIndex, row in enumerate(
            self.gameMap) for colIndex, cell in enumerate(row) if 'X' in cell]

    def OpstaclesUpdator(self):
        '''
        This function updates the location of obstacles in the map based on the direction of the obstacles. and returns the updated map and obstacles.
        '''
        for obstacle in self.obstacles:
            rowIndex, colIndex, direction = obstacle
            # update the location of the obstacle based on its direction
            # update the direction of the obstacle
            if direction == 'left':
                self.gameMap[rowIndex][colIndex] = '0'
                self.gameMap[rowIndex][colIndex - 1] = 'X'
                self.obstacles[self.obstacles.index(obstacle)] = (
                    rowIndex, colIndex - 1, 'down')
            elif direction == 'down':
                self.gameMap[rowIndex][colIndex] = '0'
                self.gameMap[rowIndex + 1][colIndex] = 'X'
                self.obstacles[self.obstacles.index(obstacle)] = (
                    rowIndex + 1, colIndex, 'right')
            elif direction == 'right':
                self.gameMap[rowIndex][colIndex] = '0'
                self.gameMap[rowIndex][colIndex + 1] = 'X'
                self.obstacles[self.obstacles.index(obstacle)] = (
                    rowIndex, colIndex + 1, 'up')
            elif direction == 'up':
                self.gameMap[rowIndex][colIndex] = '0'
                self.gameMap[rowIndex - 1][colIndex] = 'X'
                self.obstacles[self.obstacles.index(obstacle)] = (
                    rowIndex - 1, colIndex, 'left')

    def PlayerMover(self, direction: str):
        '''
        This function moves the player in the map based on the direction and returns the updated map, player location and balls locations.
        '''
        rowIndex, colIndex = self.playerLocation
        # move the player based on the direction
        if direction == 'up':
            self.gameMap[rowIndex][colIndex] = self.gameMap[rowIndex][colIndex][0]
            if 'B' in self.gameMap[rowIndex - 1][colIndex]:
                self.gameMap[rowIndex -
                             1][colIndex] = self.gameMap[rowIndex - 1][colIndex][0]
                self.gameMap[rowIndex - 2][colIndex] += 'B'
                self.ballsLocations[self.ballsLocations.index(
                    (rowIndex - 1, colIndex))] = (rowIndex - 2, colIndex)
            self.gameMap[rowIndex - 1][colIndex] += 'P'
            self.playerLocation = (rowIndex - 1, colIndex)

        elif direction == 'down':
            self.gameMap[rowIndex][colIndex] = self.gameMap[rowIndex][colIndex][0]
            if 'B' in self.gameMap[rowIndex + 1][colIndex]:
                self.gameMap[rowIndex +
                             1][colIndex] = self.gameMap[rowIndex + 1][colIndex][0]
                self.gameMap[rowIndex + 2][colIndex] += 'B'
                self.ballsLocations[self.ballsLocations.index(
                    (rowIndex + 1, colIndex))] = (rowIndex + 2, colIndex)
            self.gameMap[rowIndex + 1][colIndex] += 'P'
            self.playerLocation = (rowIndex + 1, colIndex)
        elif direction == 'left':
            self.gameMap[rowIndex][colIndex] = self.gameMap[rowIndex][colIndex][0]
            if 'B' in self.gameMap[rowIndex][colIndex - 1]:
                self.gameMap[rowIndex][colIndex -
                                       1] = self.gameMap[rowIndex][colIndex - 1][0]
                self.gameMap[rowIndex][colIndex - 2] += 'B'
                self.ballsLocations[self.ballsLocations.index(
                    (rowIndex, colIndex - 1))] = (rowIndex, colIndex - 2)
            self.gameMap[rowIndex][colIndex - 1] += 'P'
            self.playerLocation = (rowIndex, colIndex - 1)
        elif direction == 'right':
            self.gameMap[rowIndex][colIndex] = self.gameMap[rowIndex][colIndex][0]
            if 'B' in self.gameMap[rowIndex][colIndex + 1]:
                self.gameMap[rowIndex][colIndex +
                                       1] = self.gameMap[rowIndex][colIndex + 1][0]
                self.gameMap[rowIndex][colIndex + 2] += 'B'
                self.ballsLocations[self.ballsLocations.index(
                    (rowIndex, colIndex + 1))] = (rowIndex, colIndex + 2)
            self.gameMap[rowIndex][colIndex + 1] += 'P'
            self.playerLocation = (rowIndex, colIndex + 1)

    def checkIfBallIsInGoal(self):
        '''
        This function checks if a ball is in a goal and returns the updated map, balls locations and goal locations.
        '''
        for ball in self.ballsLocations:
            if ball in self.goalLocations:
                self.ballsLocations.remove(ball)
                self.goalLocations.remove(ball)
                self.gameMap[ball[0]][ball[1]] = 'X'
                self.obstacles.append((ball[0], ball[1], None))

    def __copy__(self):
        '''
        This function returns a copy of the current state of the game.
        '''
        copiedMapState = MapState(self.numberOfRows, self.numberOfColumns, " ".join([" ".join(row) for row in self.gameMap]))
        copiedMapState.obstacles = self.obstacles.copy()
    
        return copiedMapState
    

def convertToInputMapString(userInput):
    map = userInput.split()
    numberOfRows = int(map[0])
    numberOfColumns = int(map[1])
    inputMapString = " ".join(map[2:])

    return numberOfRows, numberOfColumns, inputMapString
