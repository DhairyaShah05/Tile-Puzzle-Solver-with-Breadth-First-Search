import numpy as np

def find_blank_tile_location(state):
    # Convert the state to a numpy array
    state_array = np.array(state)
    
    # Find the indices where the value is 0 (blank tile)
    indices = np.where(state_array == 0)
    
    # Extract the indices of the blank tile
    i, j = indices[0][0], indices[1][0]
    
    return (i, j)

def action_move_left(current_node):
    i, j = find_blank_tile_location(current_node)
    if j == 0:
        return False, None  # Cannot move left
    else:
        new_node = [row.copy() for row in current_node]
        new_node[i][j], new_node[i][j-1] = new_node[i][j-1], new_node[i][j]
        return True, new_node

def action_move_right(current_node):
    i, j = find_blank_tile_location(current_node)
    if j == 2:
        return False, None  # Cannot move right
    else:
        new_node = [row.copy() for row in current_node]
        new_node[i][j], new_node[i][j+1] = new_node[i][j+1], new_node[i][j]
        return True, new_node

def action_move_up(current_node):
    i, j = find_blank_tile_location(current_node)
    if i == 0:
        return False, None  # Cannot move up
    else:
        new_node = [row.copy() for row in current_node]
        new_node[i][j], new_node[i-1][j] = new_node[i-1][j], new_node[i][j]
        return True, new_node

def action_move_down(current_node):
    i, j = find_blank_tile_location(current_node)
    if i == 2:
        return False, None  # Cannot move down
    else:
        new_node = [row.copy() for row in current_node]
        new_node[i][j], new_node[i+1][j] = new_node[i+1][j], new_node[i][j]
        return True, new_node

# Example usage:
current_node = [[1, 2, 3],
                [4, 0, 5],
                [6, 7, 8]]

status, new_node = action_move_left(current_node)
print("Status:", status)
print("New Node after moving left:")
for row in new_node:
    print(row)
