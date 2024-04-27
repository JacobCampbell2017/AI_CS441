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

import random
import time

SOLVED_STATE1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

###############################
### Non-essential functions ###
###############################


def randomize_state(state):
    '''randomizes the state of the puzzle'''
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(nums)
    for i in range(3):
        for j in range(3):
            state[i][j] = nums.pop()
    return state


def display_state(state):
    print("-------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(state[i][j], end="|")
        print("\n-------")

###############################
##### Essential Functions #####
###############################


def is_solvable(state):
    '''determines if the puzzle is solvable'''
    inversions = 0


def main():
    '''main function'''
    random.seed(time.time())

    state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    state = randomize_state(state)

    is_solvable(state)
    display_state(state)


if __name__ == "__main__":
    main()
