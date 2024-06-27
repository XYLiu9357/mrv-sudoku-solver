"""
File: test_backtrack.py 
Author: XYLiu9357
Description: Unit tests for backtrack solver. 
"""

import pandas as pd
import backtrack

"""
Naive backtrack tests 
"""


def test_naive_backtrack_easy():
    puzzle = backtrack.parse_puzzle("puzzle_easy.txt")
    solution = backtrack.naive_backtrack(puzzle)
    assert backtrack.validate(solution)


def test_naive_backtrack_medium():
    puzzle = backtrack.parse_puzzle("puzzle_medium.txt")
    solution = backtrack.naive_backtrack(puzzle)
    assert backtrack.validate(solution)


def test_naive_backtrack_hard():
    puzzle = backtrack.parse_puzzle("puzzle_hard.txt")
    solution = backtrack.naive_backtrack(puzzle)
    assert backtrack.validate(solution)


def test_naive_backtrack_no_solution():
    puzzle = backtrack.parse_puzzle("puzzle_no_sol.txt")
    solution = backtrack.naive_backtrack(puzzle)
    assert solution == None


"""
MRV backtrack tests 
"""


def test_mrv_backtrack_easy():
    puzzle = backtrack.parse_puzzle("puzzle_easy.txt")
    solution = backtrack.mrv_backtrack(puzzle)
    assert backtrack.validate(solution)


def test_mrv_backtrack_medium():
    puzzle = backtrack.parse_puzzle("puzzle_medium.txt")
    solution = backtrack.mrv_backtrack(puzzle)
    assert backtrack.validate(solution)


def test_mrv_backtrack_hard():
    puzzle = backtrack.parse_puzzle("puzzle_hard.txt")
    solution = backtrack.mrv_backtrack(puzzle)
    assert backtrack.validate(solution)


def test_mrv_backtrack_no_solution():
    puzzle = backtrack.parse_puzzle("puzzle_no_sol.txt")
    solution = backtrack.mrv_backtrack(puzzle)
    assert solution == None
