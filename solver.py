import numpy as np
from collections import deque

# Function to calculate the current location of the empty tile
def empty_tile(state):
    state_array = np.array(state)
    indices = np.where(state_array == 0)
    i, j = indices[0][0], indices[1][0]
    return (i, j)

# Action to Move Left
def move_left(current_node):
    i, j = empty_tile(current_node)
    if j == 0:
        return None  # Cannot Move Left
    else:
        new_node = np.array([row.copy() for row in current_node])
        new_node[i][j], new_node[i][j-1] = new_node[i][j-1], new_node[i][j]
        return new_node
    
# Action to Move Right
def move_right(current_node):
    i, j = empty_tile(current_node)
    if j == 2:
        return None  # Cannot Move Right
    else:
        new_node = np.array([row.copy() for row in current_node])
        new_node[i][j], new_node[i][j+1] = new_node[i][j+1], new_node[i][j]
        return new_node

# Action to Move Up
def move_up(current_node):
    i, j = empty_tile(current_node)
    if i == 0:
        return None  # Cannot Move Up
    else:
        new_node = np.array([row.copy() for row in current_node])
        new_node[i][j], new_node[i-1][j] = new_node[i-1][j], new_node[i][j]
        return new_node    

# Action to Move Down
def move_down(current_node):
    i, j = empty_tile(current_node)
    if i == 2:
        return None  # Cannot Move Down
    else:
        new_node = np.array([row.copy() for row in current_node])
        new_node[i][j], new_node[i+1][j] = new_node[i+1][j], new_node[i][j]
        return new_node    

# Function to check if a state is the goal state
def is_goal_state(state):
    return np.array_equal(state, np.array([[1, 4, 7], [2, 5, 8], [3, 6, 0]]))

# Breadth First Search algorithm with modifications to track explored states and additional information
def bfs(initial_state, ):
    visited = set()  # Set to store visited states
    explored_states = []  # List to store all explored states
    nodes_info = []  # List to store information about all nodes explored
    queue = deque([(initial_state, [], None)])  # Modified queue to include parent node

    while queue:
        state, path, parent = queue.popleft()  # Get the state, path, and parent from the front of the queue
        state_array = np.array(state)  # Convert state to a NumPy array
        state_tuple = tuple(state_array.reshape(1, 9)[0])  # Convert state to tuple
        visited.add(state_tuple)
        explored_states.append(state_tuple)  # Record explored state
        nodes_info.append((len(explored_states) - 1, explored_states.index(tuple(parent.reshape(1, 9)[0])) if parent is not None else None, state_array)) # Record information about the node 

        if is_goal_state(state_array):
            node_path = [state_array]
            while parent is not None:
                node_path.append(parent)
                parent = path.pop() if path else None
            node_path.reverse()
            return path, nodes_info, explored_states, node_path

        for move in [move_left, move_right, move_up, move_down]:
            new_state = move(state_array)
            if new_state is not None:
                if tuple(new_state.reshape(1, 9)[0]) not in visited:
                    queue.append((new_state, path + [state_array], state_array))

    return None, None, None, None  # If no solution is found, return None for all outputs

# Implementation 

initial_state = np.array([[6, 8, 3], [4, 5, 2], [7, 0, 1]])
path, nodes_info, explored_states, node_path = bfs(initial_state)
print("Puzzle Not Solved" )

# Writing results to text files
if path is not None:
    print("Solving")
    with open('nodes.txt', 'w') as f:
        for state in explored_states:
            f.write(' '.join(map(str, state)) + '\n')

    with open('nodesinfo.txt', 'w') as f:
        for index, parent_index, state in nodes_info:
            f.write(f"{index} {parent_index if parent_index is not None else -1} {' '.join(map(str, state.reshape(1, 9)[0]))}\n")

    with open('nodePath.txt', 'w') as f:
        for state in node_path:
            for row in state:
                f.write(' '.join(map(str, row))+ ' ')
            f.write('\n')
else:
    print("No solution found.")
