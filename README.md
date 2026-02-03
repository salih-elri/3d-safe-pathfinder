# 3D Safe Pathfinder

This project implements a stack-based depth-first search (DFS) algorithm
to find a safe path in a 3D grid environment with obstacles and safety constraints.

The project is written in Python and focuses on algorithmic problem-solving,
grid navigation, and constraint-based movement.

## Problem Description
- The environment is represented as a 3D grid.
- The agent starts from a given position and must reach a target location.
- Certain cells are blocked or forbidden.
- The agent cannot move to cells that violate neighborhood safety constraints.

## Approach
- Iterative depth-first search (DFS)
- Stack-based backtracking (no recursion)
- Visited-state tracking to prevent loops
- Constraint checks before each move

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/salih-elri/3d-safe-pathfinder.git

2. Run the Python Script:
```bash
python src/safe_path_3d.py

 ``` 
## Example Output
This is an example path returned by the algorithm for a simple 3D grid input.
```
Path: ['east', 'east', 'east', 'south', 'south', 'south']
```
## Notes

This project is an extended and cleaned-up version of an academic coursework problem,
developed to demonstrate problem-solving and algorithmic thinking in Python.

## Author
Salih Elri — Computer Engineering student at METU
