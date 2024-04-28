# 8 State Puzzle Solver

This Python script provides a solution for the 8 state puzzle, a variant of the classic 8-puzzle problem. The solver utilizes two algorithms: Best Search and A\* Algorithm, along with three heuristic functions to determine the next moves.

## Features

- Solves the 8 state puzzle using two algorithms: Best Search and A\* Algorithm.
- Three heuristic functions available:
  1. Number of misplaced tiles
  2. Manhattan distance
  3. Manhattan distance + Number of misplaced tiles
- Determines if the puzzle is solvable based on the number of inversions.
- Provides an option to save the solution path to a text file.
- Visualization of the puzzle can be included in the saved file.

## Usage

1. Run the script.
2. Choose the algorithm: Best Search (1) or A\* Algorithm (2).
3. Enter the initial state and goal state of the puzzle, along with the desired heuristic function (1, 2, or 3).
4. Optionally, include "v" at the end of the input to save the visual representation of the puzzle in the file.
5. The solution will be displayed in the terminal or saved to a text file, based on the chosen output mode.
6. 'q' will exit from algorithm loops to main menu, and will exit program if in main menu.
7. 'f' inside the algorithm will switch solutions from being displayed in the terminal to displayed in .txt files.

## Input Format

- Initial state and goal state: Two lists of 8 integers from 1 to 8, where "b" represents the blank tile.
- Heuristic function: Choose 1, 2, or 3.
- If you want a better visual representation of the puzzle state and the solutions, append 'v' to the end of the input.

Example inputs:

```bash
(1,3,4,6,7,8,2,5,b) (1,2,3,4,5,6,7,8,b) 1
(7,2,4,5,b,6,8,3,1) (b,1,2,3,4,5,6,7,8) 2 v
(1,3,4,6,7,8,2,5,b) (1,2,3,4,5,6,7,8,b) 3
```

## Output

- The solution path will be displayed in the terminal or saved to a text file.
- If saved to a file, the filename format is: `initial_state-goal_state-Heuristic.txt`.

## Note

By default, the maximum number of iterations is set to 3000. This can be changed by modifying the `MAX_ITERATIONS` constant in the script.

## Author

Jacob Campbell
Spring 2024 - CS441
