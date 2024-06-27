"""
File: generator.py 
Author: XYLiu9357
Description: generates a random sudoku puzzle. 

Background: it has been proven that any sudoku with less than 17 clues 
will not have a unique solution. However, having 17 clues does not 
guarantee that a unique solution exists. 
"""

import numpy as np
import pandas as pd


class SudokuGenerator:
    def __init__(self, dim: int = 9) -> None:
        self.n = dim
        self.puzzle = pd.DataFrame(np.zeros((self.n, self.n)))

    def generate(self) -> None:
        pass

    def get_puzzle(self) -> pd.DataFrame:
        return self.puzzle
