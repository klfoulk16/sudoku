# Sudoku Solver

Sudoku solver is a simple python application that takes a .txt file represetnation of a sudoku puzzle and solves it. It also prints out a rough visual of the unsolved and solved puzzle.

## Set Up:

'''bash
# Clone this repository
git clone https://github.com/klfoulk16/sudoku.git

# Use the package manager pip to install the requirements.
pip install -r requirements.txt
'''

## Usage

'''python
python3 solve.py <puzzle.txt>
'''

<puzzle.txt> should link to a txt file that contain's a representation of 9x9 sudoku puzzle as below. <i>The puzzle should have "_" for blank boxes and numbers for boxes that are pre-defined</i>

'''txt
___26_7_1
68__7__9_
19___45__
82_1___4_
__46_29__
_5___3_28
__93___74
_4__5__36
7_3_18___
'''

## Looking for feedback about:
1. My project structure and whether it is readable/efficient.
2. How to make my code more pythonic.
3. How to print out a prettier picture of the sudoku puzzles
(the thick black borders are not attractive.)

This was only my second time creating a project from scratch and I know I have
a long way to go.

## Road Map:
1. I will generate sudoku puzzles to solve.
2. I will finish the test.py file. I did not know about these until I was finished.
3. I will create a pygame version of this project allowing users to solve the
puzzle and ask the AI for advice.
