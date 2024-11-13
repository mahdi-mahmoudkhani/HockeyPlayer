### Overview

This program aims to solve the Sokoban game using a set of AI search algorithms, including **BFS**, **DFS**, **UCS**, **IDS**, **A\***, **IDA\***, and **BFS**.

### Getting Started

1. **Load the Initial Map:**
  - Open the `main.py` file.
  - Define the initial game map within a docstring. The map layout should start with the number of rows and columns separated by a space on the **first line**.

2. **Map Layout Format:**
  - Each **subsequent line** represents a row in the map.
  - Each element in a row, separated by a space, represents a column entry.

3. **Map Symbols and Their Meanings:**
  - `X`: Obstacle
  - `G`: Goal
  - `B`: Box
  - `P`: Player
  - Numeric values in each cell denote **energy costs** for movement.

4. **Execution Process:**
  - When you run the program, the input map is initially converted into a string.
  - The program then calculates the number of rows and columns in the map and creates an instance of the `MapState` class.
  - Using this instance, each algorithm is invoked sequentially, returning specific solution results.

### `MapState` Class

The `MapState` class represents the current state of the Sokoban game, including the positions of the player, balls, goals, and obstacles. It includes methods for updating the game state based on player movements, obstacle movements, and checking if a ball is in a goal.

#### `__init__(self, numberOfRows, numberOfColumns, inputMapString, move="", depth=0, cost=0, parent=None)`

Initializes the map of the game and sets the locations of the player, balls, goals, and obstacles.

#### `OpstaclesUpdator(self)`

Updates the location of obstacles in the map based on their direction and returns the updated map and obstacles.

#### `PlayerMover(self, direction: str)`

Moves the player in the map based on the specified direction and returns the updated map, player location, and ball locations.

#### `checkIfBallIsInGoal(self)`

Checks if any ball is in a goal and returns the updated map, ball locations, and goal locations.

#### `__copy__(self, move="", depth=0, cost=0)`

Creates and returns a copy of the current game state.

#### `__lt__(self, other)`

Compares two states based on their costs.

### `Successor` Function

Generates and returns the successor states of the current Sokoban game state based on possible player movements.

#### `Successor(currentMapState: MapState, visited)`

Generates successor states by moving the player in all possible directions and checking for valid game states.

#### `isValidState(currentMapState: MapState)`

Verifies the validity of a given game state.

### `PathReconstructor`

Reconstructs the sequence of moves that led to the goal state, starting from the current state and following the parent states backwards.

### `GoalStateChecker`

Checks if the current state of the game is the goal state, meaning all balls have been placed on their corresponding goal locations.

### `manhattanDistance` Function

Calculates the **Manhattan Distance** between two points on a grid.

### `Heuristic` Function

Computes a heuristic value for the current state based on the Manhattan distance between the player and the closest ball, as well as between the ball and the closest goal.

### Algorithms

- **BFSAlgorithm:** Implements Breadth-First Search (BFS) to explore game states level by level.
- **DFSAlgorithm:** Implements Depth-First Search (DFS) using a stack to explore game states.
- **DLSAlgorithm:** Implements Depth-Limited Search (DLS) with a specified depth limit.
- **IDSAlgorithm:** Implements Iterative Deepening Search (IDS) by calling DLS iteratively.
- **aStarSearch:** Implements A* search using a priority queue and heuristic values.
- **greedyBestFirstSearch:** Implements Greedy Best-First Search (GBFS) prioritizing states with the lowest heuristic value.
- **IDAstarSearch:** Implements Iterative Deepening A* (IDA*) combining depth-first search with A* heuristic and iterative deepening.

