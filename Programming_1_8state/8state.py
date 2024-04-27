'''
Jacob Campbell - CS441 - Spring2024

A simple 8 state machine

Heuristic_1: Number of misplaced tiles
Heuristic_2: Manhattan distance
Heuristic_3: tbd

input: 3x3 grid where a random tile is missing, the rest of the tiles are in random order

output: 3x3 grid where the tiles are in order

Agent must determine if the puzzle is solvable, and if so, solve it.

The agent will determine if the puzzle is solvable by counting the number of inversions in the puzzle. 
If the number of inversions is even, the puzzle is solvable. If the number of inversions is odd, the puzzle is not solvable.

The agent will solve the puzzle by using the A* algorithm with the hueristic that achieves the highest accuracy.
'''