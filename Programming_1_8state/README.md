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
8. 'v' inside the algorithm will switch solutions from being displayed in text format to visual format (3x3 grid).

## Input Format

- Initial state and goal state: Two lists of 8 integers from 1 to 8, where "b" represents the blank tile.
- The lists should be enclosed in parentheses and separated by a space.
- The Initial state is the first list, and the goal state is the second list.
- Heuristic function: Choose 1, 2, or 3.

Example inputs:

```bash
INITIAL              GOAL               HEURISTIC
(1,3,4,6,7,8,2,5,b) (1,2,3,4,5,6,7,8,b) 1
-----------------------------------------
(7,2,4,5,b,6,8,3,1) (b,1,2,3,4,5,6,7,8) 2
-----------------------------------------
(1,3,4,6,7,8,2,5,b) (1,2,3,4,5,6,7,8,b) 3
-----------------------------------------
```

## Output

- The solution path will be displayed in the terminal or saved to a text file.
- In the solution path, the blank tile is represented by 0 rather than "b".
- If saved to a .txt file, the filename depends on the input, output, heuristic function, and algorithm used. In order of precedence (separator is "\-"):

  1. If it A\* Algorithm is used, the filename will be prefixed with "A_STAR".
  2. if it is Visual mode, the filename will be prefixed with "visual".
  3. Input state in continuous format, with the blank tile represented by 0.
  4. Output state in continuous format, with the blank tile represented by 0.
  5. The heuristic function used. (1, 2, or 3)

Example output filenames:
best_search example:

```bash
Currently printing to file ('f' to toggle terminal output) in text mode ('v' to toggle visual mode)
Input: (1,3,4,6,7,8,2,5,b) (1,2,3,4,5,6,7,8,b) 1
Solution found!
Solution saved to 134678250-123456780-1.txt
Solution found in 44 steps.
```

A\* example:

```bash
Currently printing to file ('f' to toggle terminal output) in visual mode ('v' to toggle visual mode)
Input: (1,3,4,6,7,8,2,5,b) (1,2,3,4,5,6,7,8,b) 3
Solution found!
Solution saved to visual-A_STAR-134678250-123456780-3.txt
Solution found in 22 steps.
```

## Visual Mode

When the visual mode is enabled, the puzzle state will be displayed in a 3x3 grid format. The blank tile is represented by "b".

Example:

### Visual Mode Output

```bash
Currently printing to terminal ('f' to toggle file output) in visual mode ('v' to toggle visual mode)
Input: (1,3,4,6,7,8,2,5,b) (1,2,3,4,5,6,7,8,b) 1
Solution found!
+-------+
| 1 3 4 |
| 6 7 8 |
| 2 5 b |
+-------+
+-------+
| 1 3 4 |
| 6 7 b |
| 2 5 8 |
+-------+

...
```

### Text Mode Output

```bash
Currently printing to terminal ('f' to toggle file output) in text mode ('v' to toggle visual mode)
Input: (1,3,4,6,7,8,2,5,b) (1,2,3,4,5,6,7,8,b) 1
Solution found!
[1, 3, 4, 6, 7, 8, 2, 5, 0]
[1, 3, 4, 6, 7, 0, 2, 5, 8]
...
```

**Notice the 0 in the text mode output, this is the blank tile.**

## Note

By default, the maximum number of iterations is set to 3000. This can be changed by modifying the `MAX_ITERATIONS` constant in the script.

## Author

Jacob Campbell
Spring 2024 - CS441
