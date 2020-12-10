# Sudoku Solver

Sudoku Solver is a simple python application that takes a .txt file representation of a sudoku puzzle and solves it. It also prints out a rough visual of the unsolved and solved puzzle.

### Files:
1. solve.py contains the main function as well as the 'PuzzleManager' class.
2. sudoku.py contains classes that define the sudoku puzzle and its variables.
3. test.py is the start of my testing scripts. It is still in development.

## Set Up:

```bash
# Clone this repository
git clone https://github.com/klfoulk16/sudoku.git

# Use the package manager pip to install the requirements.
pip install -r requirements.txt
```

## Usage

Run the following command in your terminal:
```python
python3 solve.py <puzzle.txt>
```

<puzzle.txt> should link to a txt file that contains a representation of a 9x9 sudoku puzzle like the one below. The puzzle should have "_" for blank boxes and numbers for boxes that are pre-defined.

```txt
___26_7_1
68__7__9_
19___45__
82_1___4_
__46_29__
_5___3_28
__93___74
_4__5__36
7_3_18___
```

## Looking for feedback about:
1. My project structure whether it is readable/efficient.
2. How to make my code more pythonic.
3. How to print out a prettier picture of the sudoku puzzles
(the thick black borders are not attractive).

This was only my second time creating a project from scratch and I know I have
a long way to go.

## Road Map:
1. I will generate sudoku puzzles to solve instead of using .txt files.
2. I will finish the test.py file so that the code is "well-tested."
3. I will create a Pygame version of this project allowing users to solve the
puzzle and ask the AI for advice.
