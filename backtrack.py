"""
File: generator.py 
Author: XYLiu9357
Description: Use backtracking to solve a Sudoku puzzle. 
"""

import numpy as np
import pandas as pd


def parse_puzzle(file_name: str) -> pd.DataFrame:
    """
    parse_puzzle: str, int -> DataFrame
    Description: Parse a Sudoku puzzle from the specified file
    """
    with open(file_name, "r") as puzzle_file:
        puzzle_str = puzzle_file.read(9 * 9)

    # All invalid entries are treated as empty
    digits = (int(char) if char.isdigit() else 0 for char in puzzle_str)
    digits_np = np.array(list(digits))
    digits_np = digits_np.reshape((9, 9))

    puzzle = pd.DataFrame(digits_np)
    return puzzle


def validate(grid: pd.DataFrame) -> bool:
    """
    validate: DataFrame -> bool
    Description: Validate each row, column and block to check if the puzzle is valid
    """
    check_valid = lambda x: max(np.bincount(x[x != 0])) <= 1
    row_valid = np.all(np.apply_along_axis(func1d=check_valid, axis=0, arr=grid))
    col_valid = np.all(np.apply_along_axis(func1d=check_valid, axis=1, arr=grid))

    def check_valid(block):
        non_zero_elements = block[block != 0]
        return len(non_zero_elements) == len(np.unique(non_zero_elements))

    # Reshape the grid to extract 3x3 blocks
    blocks = np.array(grid).reshape((3, 3, 3, 3)).swapaxes(1, 2).reshape(-1, 3, 3)
    block_valid = np.all(
        np.apply_along_axis(
            func1d=check_valid, axis=1, arr=blocks.reshape(blocks.shape[0], -1)
        )
    )

    if row_valid and col_valid and block_valid:
        print("Solution is valid!")
        return True
    else:
        print("Solution is invalid...")
        return False


# def validate_on_update(grid: pd.DataFrame, row: int, col: int) -> bool:
#     """
#     ===DEPRECATED===
#     validate_on_update: DataFrame, int, int -> bool
#     Description: On every update of the grid, check if the affected rows and columns
#     are valid. This is more efficient compared to validating the whole grid.
#     """
#     check_valid = lambda x: max(np.bincount(x[x != 0])) <= 1
#     row_valid = np.all(
#         np.apply_along_axis(func1d=check_valid, axis=0, arr=grid.iloc[row, :])
#     )
#     col_valid = np.all(
#         np.apply_along_axis(func1d=check_valid, axis=0, arr=grid.iloc[:, col])
#     )

#     blocks = np.array(grid.iloc[:3, :3])
#     block_valid = np.all(
#         np.apply_along_axis(func1d=check_valid, axis=0, arr=blocks.reshape(3 * 3, -1))
#     )

#     return row_valid and col_valid and block_valid


def generate_guesses(grid: pd.DataFrame, row: int, col: int) -> np.ndarray:
    """
    generate_guesses: DataFrame, int, int -> ndarray
    Description: Generate a list of valid guesses for grid[row][col].
    """
    choices = np.arange(1, 10)
    cur_row = grid.iloc[row, :].values
    cur_col = grid.iloc[:, col].values

    start_row = row // 3 * 3
    start_col = col // 3 * 3
    cur_block = grid.iloc[
        start_row : start_row + 3, start_col : start_col + 3
    ].values.flatten()

    guesses = np.setdiff1d(choices, np.concatenate((cur_row, cur_col, cur_block)))
    return guesses[guesses != 0]


def _naive_backtrack(grid: pd.DataFrame) -> bool:
    """
    _naive_backtrack: DataFrame, int, int -> bool
    Description: Solve the puzzle by recursive row-wise backtracking. This is the
    easiest to implement but the most inefficient.
    """
    empty_indices = np.argwhere((np.array(grid) == 0))

    # Break case: puzzle solved
    if empty_indices.size < 1:
        return True

    x, y = empty_indices[0]

    # Extract valid list of guesses
    guesses = generate_guesses(grid, x, y)

    for num in guesses:
        # Make a guess
        grid.iloc[x, y] = num
        # Try to solve the rest if it is locally correct
        if _naive_backtrack(grid):
            return True

    # Reset if not found
    grid.iloc[x, y] = 0

    # Break case: puzzle not solved
    return False


def naive_backtrack(grid: pd.DataFrame) -> pd.DataFrame:
    """
    naive_backtrack: DataFrame -> DataFrame
    Description: Given a puzzle grid, solve the puzzle and return the solution. None will
    be returned if there is no solution. Only one solution will be returned if there exists
    multiple valid solutions. This solver uses backtracking.
    """
    # Make a defensive deep copy of the grid
    solution = grid.copy(deep=True)
    success = _naive_backtrack(solution)

    if not success:
        print("Solution does not exist")
        return None

    # Solve the puzzle by backtracking
    return solution


def _mrv_backtrack(grid: pd.DataFrame) -> bool:
    """
    _mrv_backtrack: DataFrame, int, int -> bool
    Description: Solve the puzzle by recursive backtracking following
    the minimum-remaining-value (MRV) heuristic.
    """

    def apply_guesses(row, col):
        return len(generate_guesses(grid, row, col))

    rows, cols = np.where(grid.values == 0)

    # Permit use of argmin to find the MRV entry
    guess_counts = np.full(grid.shape, np.inf)

    for row, col in zip(rows, cols):
        guess_counts[row, col] = apply_guesses(row, col)

    min_pos = np.unravel_index(np.argmin(guess_counts), grid.shape)
    if guess_counts[min_pos] == np.inf:
        return True

    x, y = min_pos
    guesses = generate_guesses(grid, x, y)

    for num in guesses:
        grid.iloc[x, y] = num
        if _mrv_backtrack(grid):
            return True

    grid.iloc[x, y] = 0

    return False


def mrv_backtrack(grid: pd.DataFrame) -> pd.DataFrame:
    """
    mrv_backtrack: DataFrame -> DataFrame
    Description: Given a puzzle grid, solve the puzzle and return the solution. None will
    be returned if there is no solution. Only one solution will be returned if there exists
    multiple valid solutions. This solver uses backtracking following the MRV heuristic.
    """
    # Make a defensive deep copy of the grid
    solution = grid.copy(deep=True)
    success = _mrv_backtrack(solution)

    if not success:
        print("Solution does not exist")
        return None

    # Solve the puzzle by backtracking
    return solution


if __name__ == "__main__":
    grid = parse_puzzle(input("Input puzzle file name > "))
    solution = mrv_backtrack(grid)

    if solution is not None:
        print("Solution found")
        if validate(solution):
            print(solution)
