Goals for the project:
1. Constraint Satisfaction.
    a. Work with AC3 algorithm and backtracking.
2. Construct a large(ish) project from scratch.
3. Have fun!!
4. Maybe learn some Pygame or how to translate pictures to arrays (computer vision)

Broad Steps:

Step 1: 20 hours (4 days, 5 hours) 4.25, 5:45 start
1. Given an array that represents a sudoku puzzle, return the solved array.
    i. At this step I will be hard coding the puzzle.
    i. How to describe the problem in an array? Or multiple arrays?
        a. Need to make sure each constraint can be easily checked.
    ii. Use AC3 and backtracking to find solution.
2. Print out image of unsolved and solved puzzle.
3. Generate Sudoku puzzle.
    i. Write code to generate.
    ii. Import puzzle from a photo (computer vision?!)
5. Interactive Pygame version where person can ask for hints
    i. Can either upload photo or generate random one


Step 1:
Print it out in the terminal so I can see it
Objects
    Sudoku:
        1. Defines the puzzle
            i. How do I make sure the set numbers are set...aka they cannot be updated
            ii. How do I divide up squares, lines, rows
    Manager:
        1. Creates
        2. Solves


Variables - each empty square
Domain - 1-9
Constraints - squares that can't be the same

1. Make sure unary constraints are met. I.E. if sudoku puzzle has a number hard coded, get rid of all other numbers for it's domain.
2. Make sure binary contraints are met (Arc Consistency)
    i. Remove hard coded values from the domain of all variables each hard coded varibale is connected with
