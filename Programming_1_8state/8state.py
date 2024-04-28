'''
Jacob Campbell - CS441 - Spring2024

A simple 8 state machine

Heuristic_1: Number of misplaced tiles
Heuristic_2: Manhattan distance
Heuristic_3: Manhattan distance + Number of misplaced tiles

input: list of 8 integers from 1-8 and a tile "b" is the blank tile. Another list
         of 8 integers from 1-8 and a tile "b" is the goal state.

output: The solution path to the goal state.

The agent will determine if the puzzle is solvable by counting the number of inversions in the puzzle.
If the number of inversions is even, the puzzle is solvable. If the number of inversions is odd, the puzzle is not solvable.

The agent will solve the puzzle by using the A* algorithm with the heuristic that achieves the highest accuracy.

The solution can be saved in a txt file named after the initial_state-goal_state-Heuristic.txt
There is an option to save the visual representation of the puzzle in the file by ending the input with "v"

If the user doesn't toggle the file output, the solution will be printed to the terminal by default.
'''

import random
import time
import os

#################################################
# Class for State of the puzzle and its methods #
#################################################


class State:
    def __init__(self, state, parent=None, g=0, h=0, c=0):
        self.state = state
        self.parent = parent
        self.goal = g
        self.heuristic = h
        self.next_states = []
        self.cost = c

    def find_next_states(self):
        '''Finds the next possible states from the current state'''
        blank = self.state.index(0)
        if blank % 3 != 0:
            self.next_states.append(self.move_left(blank))
        if blank % 3 != 2:
            self.next_states.append(self.move_right(blank))
        if blank // 3 != 0:
            self.next_states.append(self.move_up(blank))
        if blank // 3 != 2:
            self.next_states.append(self.move_down(blank))

    def move_left(self, blank):
        '''Moves the blank tile left'''
        new_state = self.state.copy()
        new_state[blank] = new_state[blank-1]
        new_state[blank-1] = 0
        return State(new_state, parent=self, g=self.goal, c=self.cost + 1)

    def move_right(self, blank):
        '''Moves the blank tile right'''
        new_state = self.state.copy()
        new_state[blank] = new_state[blank+1]
        new_state[blank+1] = 0
        return State(new_state, parent=self, g=self.goal, c=self.cost + 1)

    def move_up(self, blank):
        '''Moves the blank tile up'''
        new_state = self.state.copy()
        new_state[blank] = new_state[blank-3]
        new_state[blank-3] = 0
        return State(new_state, parent=self, g=self.goal, c=self.cost + 1)

    def move_down(self, blank):
        '''Moves the blank tile down'''
        new_state = self.state.copy()
        new_state[blank] = new_state[blank+3]
        new_state[blank+3] = 0
        return State(new_state, parent=self, g=self.goal, c=self.cost + 1)

    def display_possible_states(self):
        '''
        Displays the Current state and the possible next states. As well as the possible states heuristic.
        Used for debugging, testing, and demonstration purposes.
        '''
        print('Current State:')
        print_state(self.state)
        print('heuristic: ', heuristic_1(self.state, self.goal))
        print('')
        print('Possible States:')
        for i in range(0, len(self.next_states)):
            print_state(self.next_states[i].state)
            print('heuristic: ', heuristic_1(
                self.next_states[i].state, self.goal))
            print('')

    def best_search_solve(self, heuristic_func: int, steps: int) -> list:
        '''
        Solves the puzzle using the best search algorithm
        The heuristic function is determined based on the parameter heuristic_func
        1: heuristic_1 -> Number of misplaced tiles
        2: heuristic_2 -> Manhattan distance
        3: heuristic_3 -> Manhattan distance + Number of misplaced tiles
        '''
        max_steps = steps
        path = []
        open_list = []
        closed_list = []

        if heuristic_func == 1:
            self.heuristic = heuristic_1(self.state, self.goal)
        elif heuristic_func == 2:
            self.heuristic = heuristic_2(self.state, self.goal)
        else:
            self.heuristic = heuristic_3(self.state, self.goal)

        open_list.append(self)

        while open_list and max_steps > 0:
            max_steps -= 1
            current_state = open_list.pop(0)
            closed_list.append(current_state.state)

            if current_state.state == current_state.goal:
                path.append(current_state)
                while current_state.parent:
                    path.append(current_state.parent)
                    current_state = current_state.parent
                path.reverse()
                return path

            current_state.find_next_states()

            for next_state in current_state.next_states:
                if next_state.state not in closed_list:
                    if heuristic_func == 1:
                        next_state.heuristic = heuristic_1(
                            next_state.state, next_state.goal)
                    elif heuristic_func == 2:
                        next_state.heuristic = heuristic_2(
                            next_state.state, next_state.goal)
                    else:
                        next_state.heuristic = heuristic_3(
                            next_state.state, next_state.goal)
                    open_list.append(next_state)

            open_list.sort(key=lambda x: x.heuristic)

        return None

    def A_star_solve(self, heuristic_func: int, steps: int) -> list:
        '''
        Solves the puzzle using the A* algorithm
        The heuristic function is determined based on the parameter heuristic_func
        1: heuristic_1 -> Number of misplaced tiles
        2: heuristic_2 -> Manhattan distance
        3: heuristic_3 -> Manhattan distance + Number of misplaced tiles
        '''
        max_steps = steps
        path = []
        open_list = []
        closed_list = []

        # Set the initial state's heuristic value based on the selected heuristic function
        if heuristic_func == 1:
            self.heuristic = heuristic_1(self.state, self.goal)
        elif heuristic_func == 2:
            self.heuristic = heuristic_2(self.state, self.goal)
        else:
            self.heuristic = heuristic_3(self.state, self.goal)

        open_list.append(self)

        while open_list and max_steps > 0:
            max_steps -= 1
            current_state = open_list.pop(0)
            closed_list.append(current_state.state)

            if current_state.state == current_state.goal:
                path.append(current_state)
                while current_state.parent:
                    path.append(current_state.parent)
                    current_state = current_state.parent
                path.reverse()
                return path

            current_state.find_next_states()

            for next_state in current_state.next_states:
                next_state_cost = current_state.cost + 1

                if next_state.state not in closed_list or next_state_cost < next_state.cost:
                    next_state.cost = next_state_cost
                    if heuristic_func == 1:
                        next_state.heuristic = heuristic_1(
                            next_state.state, next_state.goal)
                    elif heuristic_func == 2:
                        next_state.heuristic = heuristic_2(
                            next_state.state, next_state.goal)
                    else:
                        next_state.heuristic = heuristic_3(
                            next_state.state, next_state.goal)
                    next_state.f_value = next_state.cost + next_state.heuristic
                    open_list.append(next_state)

            # Sort the open list based on the f(n) value
            open_list.sort(key=lambda x: x.f_value)

        return None


#################################################
# Helper functions (eg. parsing input, printing)#
#################################################


def parse_input(user_input):
    '''
    Takes users input and returns a tuple of two lists
    EX: (1,2,3,4,5,6,7,8,b) (1,3,4,6,7,8,5,2,b) -> ([1,2,3,4,5,6,7,8,b], [1,3,4,6,7,8,5,2,b])

    also checks if the input is valid
    '''

    inital_state = []
    goal_state = []
    flag = False
    # Check if the input is valid
    try:
        user_input1, user_input2, heuristic_val, check = user_input.split(' ')
    except:
        user_input1, user_input2, heuristic_val = user_input.split(' ')
        check = 'n'
    if len(user_input1) != 19 or len(user_input2) != 19:
        print('Invalid length, ensure no spaces between numbers and commas.')
        return None
    for i in range(0, len(user_input1)):
        if user_input1[i] == '(' or user_input1[i] == ')' or user_input1[i] == ',':
            continue
        if user_input1[i] == 'b':
            inital_state.append(0)
        else:
            try:
                inital_state.append(int(user_input1[i]))
            except:
                print('Invalid input')
                return None
    for i in range(0, len(user_input2)):
        if user_input2[i] == '(' or user_input2[i] == ')' or user_input2[i] == ',':
            continue
        if user_input2[i] == 'b':
            goal_state.append(0)
        else:
            try:
                goal_state.append(int(user_input2[i]))
            except:
                print('Invalid input')
                return None
    if int(heuristic_val) < 1 or int(heuristic_val) > 3:
        print('Invalid heuristic value. Must be 1, 2, or 3.')
        return None
    if check == 'v':
        flag = True
    return (inital_state, goal_state, int(heuristic_val), flag)


def best_search_loop():
    '''
    loop for best search algorithm
    '''
    terminal = 'terminal'
    while True:
        # Get user input
        # Wrap explanation text in a box
        print('\n+' + '-'*38 + '+')
        print(
            'Enter the initial state and goal state and Heuristic function (1,2,3): [q to quit to menu] ')
        print('Ex: (1,3,4,6,7,8,2,5,b) (1,2,3,4,5,6,7,8,b) 1')
        print('Ex: (1,3,4,6,7,8,2,5,b) (1,2,3,4,5,6,7,8,b) 2')
        print('If you want the visualization of the puzzle in the saved file, please end input with "v"')
        print(
            f'Currently printing to {terminal} (\'f\' to toggle file output)')
        print('+-' + '-'*36 + '-+')
        user_input = input('Input: ')
        if user_input == 'f':
            if terminal == 'terminal':
                terminal = 'file'
            else:
                terminal = 'terminal'
            continue
        if user_input == 'q':
            return
        states = parse_input(user_input)
        if states == None:
            continue
        goal_state = states[1]
        heuristic_val = states[2]
        flag = states[3]
        initial_state = State(states[0], None, goal_state, None)

        if not is_solvable(initial_state.state, goal_state):
            print('+' + '-'*38 + '+')
            print('|' + ' '*38 + '|')
            print('|' + ' '*14 + 'NOT SOLVABLE' + ' '*12 + '|')
            print('|' + ' '*14 + 'TRY ANOTHER!' + ' '*12 + '|')
            print('+' + '-'*38 + '+')
            continue

        # initial_state.find_next_states()
        # initial_state.display_possible_states()
        # print_state(initial_state.state)

        path = initial_state.best_search_solve(heuristic_val, 3000)
        if path == None:
            print('No solution found.')
            continue
        else:
            '''Save the solution to a txt file'''
            file_name = str(initial_state.state).strip(
                '[]').replace(',', '').replace(' ', '')
            file_name += '-' + \
                str(goal_state).strip('[]').replace(',', '').replace(' ', '')
            file_name += '-' + str(heuristic_val) + '.txt'

            print('Solution found!')
            if terminal == 'file':
                if flag:
                    file_name = 'visual_' + file_name

                    if os.path.exists(file_name):
                        os.remove(file_name)
                    for i in range(len(path)):
                        with open(file_name, 'a') as f:
                            print_state_file(path[i].state, f)
                    with open(file_name, 'a') as f:
                        f.write('Solution found in ' +
                                str(len(path)-1) + ' steps.')
                else:
                    if os.path.exists(file_name):
                        os.remove(file_name)

                    for i in range(len(path)):
                        with open(file_name, 'a') as f:
                            f.write(str(path[i].state) + '\n')
                    with open(file_name, 'a') as f:
                        f.write('Solution found in ' +
                                str(len(path)-1) + ' steps.')
                print('Solution saved to', file_name)
            else:
                for i in range(len(path)):
                    print_state(path[i].state)
            print('Solution found in', len(path)-1, 'steps.')
            print('')


def A_star_loop():
    '''
    loop for A* search algorithm

    Same as best_search_loop but uses A* algorithm. I could have combined the two into one loop and seperated the algorithm calls
    but I got lazy and didn't want to take longer to do it.
    '''
    terminal = 'terminal'
    while True:
        print('\n+' + '-'*38 + '+')
        print(
            'Enter the initial state and goal state and Heuristic function (1,2,3): [q to quit to menu] ')
        print('Ex: (1,3,4,6,7,8,2,5,b) (1,2,3,4,5,6,7,8,b) 1')
        print('Ex: (1,3,4,6,7,8,2,5,b) (1,2,3,4,5,6,7,8,b) 2')
        print('If you want the visualization of the puzzle in the saved file, please end input with "v"')
        print(
            f'Currently printing to {terminal} (\'f\' to toggle file output)')
        print('+-' + '-'*36 + '-+')
        user_input = input('Input: ')
        if user_input == 'f':
            if terminal == 'terminal':
                terminal = 'file'
            else:
                terminal = 'terminal'
            continue
        if user_input == 'q':
            return
        states = parse_input(user_input)
        if states == None:
            continue
        goal_state = states[1]
        heuristic_val = states[2]
        flag = states[3]
        initial_state = State(states[0], None, goal_state, None)

        if not is_solvable(initial_state.state, goal_state):
            print('+' + '-'*38 + '+')
            print('|' + ' '*38 + '|')
            print('|' + ' '*14 + 'NOT SOLVABLE' + ' '*12 + '|')
            print('|' + ' '*14 + 'TRY ANOTHER!' + ' '*12 + '|')
            print('+' + '-'*38 + '+')
            continue

        # initial_state.find_next_states()
        # initial_state.display_possible_states()
        # print_state(initial_state.state)

        path = initial_state.A_star_solve(heuristic_val, 3000)
        if path == None:
            print('No solution found.')
            continue
        else:
            '''Save the solution to a txt file'''
            file_name = 'A_STAR_' + str(initial_state.state).strip(
                '[]').replace(',', '').replace(' ', '')
            file_name += '-' + \
                str(goal_state).strip('[]').replace(',', '').replace(' ', '')
            file_name += '-' + str(heuristic_val) + '.txt'

            print('Solution found!')
            if terminal == 'file':
                if flag:
                    file_name = 'visual_' + file_name

                    if os.path.exists(file_name):
                        os.remove(file_name)
                    for i in range(len(path)):
                        with open(file_name, 'a') as f:
                            print_state_file(path[i].state, f)
                    with open(file_name, 'a') as f:
                        f.write('Solution found in ' +
                                str(len(path)-1) + ' steps.')
                else:
                    if os.path.exists(file_name):
                        os.remove(file_name)

                    for i in range(len(path)):
                        with open(file_name, 'a') as f:
                            f.write(str(path[i].state) + '\n')
                    with open(file_name, 'a') as f:
                        f.write('Solution found in ' +
                                str(len(path)-1) + ' steps.')
                print('Solution saved to', file_name)
            else:
                for i in range(len(path)):
                    print_state(path[i].state)
            print('Solution found in', len(path)-1, 'steps.')
            print('')


def is_solvable(i_state, g_state):
    '''If the inversions is even, the puzzle is solvable. If the inversions is odd, the puzzle is not solvable.'''
    inversions1 = 0
    inversions2 = 0

    for i in range(0, len(i_state)):
        for j in range(i+1, len(i_state)):
            if i_state[i] == 0 or i_state[j] == 0 or g_state[i] == 0 or g_state[j] == 0:
                continue
            if i_state[i] > i_state[j]:
                inversions1 += 1
            if g_state[i] > g_state[j]:
                inversions2 += 1
    if inversions1 % 2 == inversions2 % 2:
        return True
    return False


def print_state(state):
    '''Prints the state of the puzzle'''
    print('+' + '-'*7 + '+')
    for i in range(0, 3):
        print('|', end='')
        for j in range(0, 3):
            if state[i*3+j] == 0:
                print(' b', end='')
            else:
                print(' ' + str(state[i*3+j]), end='')
        print(' |')
    print('+' + '-'*7 + '+')


def print_state_file(state, file):
    '''Writes the state of the puzzle to a file'''
    visual_representation = ''
    visual_representation += '+' + '-'*7 + '+\n'
    for i in range(0, 3):
        visual_representation += '|'
        for j in range(0, 3):
            if state[i*3+j] == 0:
                visual_representation += ' b'
            else:
                visual_representation += ' ' + str(state[i*3+j])
        visual_representation += ' |\n'
    visual_representation += '+' + '-'*7 + '+\n'

    file.write(visual_representation)

###########################################################################
# Essential functions (eg. A* algorithm, best-first algorithm, heuristics)#
###########################################################################


def heuristic_1(state, goal):
    '''Number of misplaced tiles'''
    misplaced = 0
    for i in range(0, len(state)):
        if state[i] == 0:
            continue
        if state[i] != goal[i]:
            misplaced += 1
    return misplaced


def heuristic_2(state, goal):
    distance = 0
    for i in range(0, len(state)):
        if state[i] == 0:
            continue
        for j in range(0, len(goal)):
            if state[i] == goal[j]:
                distance += abs(i//3 - j//3) + abs(i % 3 - j % 3)
    return distance


def heuristic_3(state, goal):
    return heuristic_1(state, goal) + heuristic_2(state, goal)


def main():

    user_input = ''
    while user_input != 'q':
        print('Welcome to the 8 state puzzle solver!')
        print('The Heuristic functions are as follows:')
        print('1: Number of misplaced tiles')
        print('2: Manhattan distance')
        print('3: Manhattan distance + Number of misplaced tiles')
        print('')

        print('Choose the Algorithm: [q to quit]')
        print('1: Best Search')
        print('2: A* Algorithm')

        user_input = input('Algorithm: ')

        if user_input == '1':
            best_search_loop()
        elif user_input == '2':
            A_star_loop()
        elif user_input == 'q':
            print('Goodbye!')
            return
        else:
            print('+' + '-'*38 + '+')
            print('|' + ' '*38 + '|')
            print('|' + ' '*12 + 'Invalid input' + ' '*13 + '|')
            print('|' + ' '*12 + 'Please try again' + ' '*10 + '|')
            print('+' + '-'*38 + '+')


if __name__ == '__main__':
    main()
