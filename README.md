
# Tile Puzzle Solver using Breadth-First Search

This project implements a solver for the classic 8-tile puzzle using the Breadth-First Search (BFS) algorithm. It also includes an animation script to visualize the steps taken to solve the puzzle. The project consists of two main Python files: `project1.py` and `Animate.py`.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [project1.py](#project1py)
  - [Animate.py](#animatepy)
- [How It Works](#how-it-works)
- [Example](#example)
- [Acknowledgments](#acknowledgments)

## Introduction
The 8-tile puzzle is a sliding puzzle that consists of a 3x3 grid with eight numbered tiles and one blank space. The objective is to rearrange the tiles to match a target configuration by sliding the tiles into the blank space.

In this project, we use the Breadth-First Search algorithm to find the shortest path from the initial configuration to the goal configuration. The steps are then visualized using the `Animate.py` script.

## Requirements
- Python 3.x
- NumPy
- Pygame

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/tile-puzzle-solver.git
   ```
2. Navigate to the project directory:
   ```bash
   cd tile-puzzle-solver
   ```
3. Install the required Python packages:
   ```bash
   pip install numpy pygame
   ```

## Usage

### project1.py
This script contains functions to move the blank tile and to identify its location. It simulates the movements of the tiles based on user-defined actions.

#### Key Functions:
1. **find_blank_tile_location(state)**: Finds the coordinates of the blank tile in the puzzle.
2. **action_move_left(current_node)**: Moves the blank tile left if possible.
3. **action_move_right(current_node)**: Moves the blank tile right if possible.
4. **action_move_up(current_node)**: Moves the blank tile up if possible.
5. **action_move_down(current_node)**: Moves the blank tile down if possible.

To run this script, use:
```bash
python project1.py
```

### Animate.py
This script reads the solution path from a file named `nodePath.txt` and animates the movement of tiles on a Pygame window.

#### Key Features:
- Reads the solution steps from `nodePath.txt`.
- Uses Pygame to display the 8-tile puzzle and animate the movements.

#### Usage:
Ensure that you have a file named `nodePath.txt` in the same directory, containing the sequence of puzzle states. Each state should be a single line with 9 numbers separated by spaces, representing the 3x3 grid.

To run the animation script, use:
```bash
python Animate.py
```

## How It Works
1. **Breadth-First Search (BFS) Algorithm**: `project1.py` uses the BFS algorithm to explore all possible configurations of the puzzle until it finds the solution.
2. **Action Functions**: These functions (`action_move_left`, `action_move_right`, etc.) generate new states by moving the blank tile in the specified direction.
3. **Animation**: `Animate.py` reads the solution steps from `nodePath.txt` and animates the transitions between states, providing a visual representation of the solving process.

## Example
### Initial Configuration:
```
1 2 3
4 0 5
6 7 8
```

### Goal Configuration:
```
1 2 3
4 5 0
6 7 8
```

### Output:
After running `project1.py`, the solution will be printed in the console. Running `Animate.py` will visualize the sequence of moves.

## Acknowledgments
- This project was inspired by the classic 8-tile puzzle problem.
- Special thanks to the developers of Python, NumPy, and Pygame for providing powerful libraries that made this project possible.
