
---

# 8 Puzzle Solver

This Python program solves the classic 8 Puzzle problem using two different heuristics: **Manhattan Distance** and **Misplaced Count**.

## Heuristics

### Manhattan Distance

The `manhattan_distance` function calculates the Manhattan distance between the initial state and the goal state. It sums up the distances of each tile from its current position to its goal position in terms of row and column movements.

### Misplaced Count

The `count_misplaced` function calculates the number of misplaced tiles in the initial state compared to the goal state.

## Usage

1. Run the program.

2. Input the 3x3 matrix for the initial state. Use '0' to represent the blank tile.

3. Input the 3x3 matrix for the goal state. Use '0' to represent the blank tile.

4. Program will run and output with both the heuristics:
   - For **Misplaced Count**, the program will use the A* algorithm with the Misplaced Count heuristic to solve the puzzle.
   - For **Manhattan Distance**, the program will use the A* algorithm with the Manhattan Distance heuristic to solve the puzzle.

## Example

Here's an example of how to use the program:

```python
###### Welcome to 8 Puzzle Solver ######

Enter 9 Elements for Initial State Board.
NOTE: Use '0' for Blank Tile.

1 2 3
4 5 6
7 0 8

Enter Goal State Elements for 9 Board.
NOTE: Use '0' for Blank Tile.

1 2 3
4 5 6
7 8 0

Misplaced
[(['1', '2', '3'], ['4', '5', '6'], ['7', '0', '8']), 1]

Manhattan
[(['1', '2', '3'], ['4', '5', '6'], ['7', '0', '8']), 1]
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

You can replace `[Your Name]` with the actual author's name if needed. This README provides an overview of the code, usage instructions, and a brief example of how to run it.