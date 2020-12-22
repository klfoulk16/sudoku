"""
Module for testing various aspects of the Sudoku project
"""

import unittest
from sudoku import *


class Test(unittest.TestCase):
    def testSudokuParameters(self):

        sudoku = Sudoku("puzzle1.txt")

        for r in range(len(sudoku.rows)):
            self.assertEqual(
                len(sudoku.rows[r]), 9, f"There should be 9 variables in row {r}"
            )

        for c in range(len(sudoku.columns)):
            self.assertEqual(
                len(sudoku.columns[c]), 9, f"There should be 9 variables in column {c}"
            )

        for b in range(len(sudoku.blocks)):
            self.assertEqual(
                len(sudoku.blocks[b]), 9, f"There should be 9 variables in block {b}"
            )

        block_map = sudoku.define_block_map()
        self.assertEqual(
            len(block_map), 9, f"There should be 9 blocks in the block_map."
        )
        for b in block_map:
            self.assertEqual(
                len(b), 9, f"There should be 9 coordinate pairs in block {b}"
            )


if __name__ == "__main__":
    unittest.main()
