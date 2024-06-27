# Sudoku Solver

Author: XYLiu9357

Python: version 3.8+

Dependencies: `numpy`, `pandas`

## Description

This project aims to solve a 9x9 Sudoku puzzle from a file. The program parses the puzzle and solves it, printing the results to the terminal.

A GUI wiill be made at some later time...

## Naive backtrack

To run the naive backtracking algorithm, use the following command:

```
python main.py -n <file-name>.txt
```

## MRV-guided backtracking

To run the MRV-guided backtracking algorithm, use the following command:

```
python main.py -m <file-name>.txt
```

## Minimum Remaining Value (MRV) Heuristic

The Minimum Remaining Value (MRV) heuristic is a powerful strategy used in constraint satisfaction problems, such as Sudoku. The primary goal of this heuristic is to choose the next variable to be assigned a value in a way that is most likely to lead to a solution quickly. It is based on the idea of minimizing future constraints, which makes it easier to identify contradictions early and avoid fruitless paths in the search tree.

1. Identify Unassigned Variables: In the context of Sudoku, unassigned variables are the empty cells in the grid.
2. Count Valid Guesses: For each unassigned variable, count the number of possible values (guesses) that can be legally assigned to it, considering the current state of the puzzle.
3. Select Variable with Minimum Remaining Values: Choose the variable (cell) with the fewest legal values remaining. This cell is the most constrained and, therefore, the most likely to cause a failure sooner if it is not handled correctly.
4. Backtrack: If assigning a value to the chosen cell leads to a contradiction, backtrack and try the next possible value. Repeat the process until the puzzle is solved or all possibilities are exhausted.
