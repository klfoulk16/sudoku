import sys
from sudoku import *

class PuzzleManager():
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.original_assignment = {variable: variable.domain[0] for variable in self.sudoku.variables if len(variable.domain) == 1}

    def solve(self):
        """Call Your Big Bad Boy Solving Algorithms Here."""
        self.revise_domains()
        return self.backtrack()

    def revise_domains(self):
        """Instead of a big Arc3 algorithm with the revise function, we can just go through the list of variables that have been preassigned and remove those numbers from all of the unassigned variable's domains."""

        for var in self.original_assignment:
            for var2 in self.sudoku.neighbors[var]:
                if self.original_assignment[var] in var2.domain:
                    var2.domain.remove(self.original_assignment[var])

    def backtrack(self, assignment=None):
        """Takes an assignment as an arguement. To start the assignment will be the origin mapping of the pre-set variables (specify this). Later it will be the assignment that the algorithm determines. If the assignment contains every single variable in the problem, then it returns the assignment. Otherwise...

        If the assignment is complete, return assignment.

        Else, Choose a **random unassigned variable, then it'll iteratively check every value in the domain of the variable to see if the value is arc consistent with the current assignment. If it is, then {variable= value} is added to the assignment dictionary. Then call backtrack on that assignment. If the result was not failure, then return the result assignment. Otherwise, remove {variable=value} from the assignment and try the next value in the variable's domain.

        If we reach the end of the values in the variable's domain return failure. Thus we will back up a step in the backtracking heirarchy because some earlier assignment is causing issues.
        """

        if not assignment:
            assignment = self.original_assignment

        if self.assignment_complete(assignment):
            return assignment

        var = self.choose_unassigned_variable(assignment)
        for value in var.domain:
            if self.check_arc_consistency(assignment):
                assignment[var] = value
                if self.backtrack(assignment):
                    return assignment
                else:
                    del assignment[var]
        return None

    def choose_unassigned_variable(self, assignment):
        """For now this will just return a random variable. Eventually we will use a heuristic to return the hopefully best variable to check given the current assignment."""

        for var in self.sudoku.variables:
            if var not in assignment.keys():
                return var

    def check_arc_consistency(self, assignment):
        """For any given assignment check to see if all the values are arc-consistent with each other.

        This is necessary. If we called arc3 instead of this, we would be removing numbers from each variable's domain with each backtrack call, which would cause a problem if we had to "un"backtrack. The numbers wouldn't be readded and the domain would be inaccurate."""
        # see if all blocks, rows and columns do not have duplicates
        for block in self.sudoku.blocks:
            values = []
            for var in block:
                if var in assignment.keys():
                    if assignment[var] in values:
                        return False
                    else:
                        values.append(assignment[var])
        for row in self.sudoku.rows:
            values = []
            for var in self.sudoku.rows[row]:
                if var in assignment.keys():
                    if assignment[var] in values:
                        return False
                    else:
                        values.append(assignment[var])
        for column in self.sudoku.columns:
            values = []
            for var in self.sudoku.columns[column]:
                if var in assignment.keys():
                    if assignment[var] in values:
                        return False
                    else:
                        values.append(assignment[var])
        return True

    def assignment_complete(self, assignment):
        """Checks to see if the assignment is complete."""

        if len(assignment) == len(self.sudoku.variables):
            return True
        else:
            return False

    def grid(self, assignment):
        """Returns a 2d grid of the current assignment."""
        #grid = [[] for row in range(11)]
        grid = []
        for row in self.sudoku.rows:
            new_row = []
            if row == 3 or row == 6:
                grid.append(["border" for _ in range(11)])
            for i in range(9):
                if i == 3 or i == 6:
                    new_row.append("border")
                if self.sudoku.rows[row][i] in assignment.keys():
                    new_row.append(assignment[self.sudoku.rows[row][i]])
                else:
                    new_row.append(None)
            grid.append(new_row)
        return grid

    def print_img(self, assignment):
        """Prints crossword out as an image."""
        from PIL import Image, ImageDraw, ImageFont

        cell_size = 100
        cell_border = 2
        divider = 2
        interior_size = cell_size - 2 * cell_border
        grid = self.grid(assignment)
        # Create a blank canvas.
        img = Image.new(
            "RGBA",
            (self.sudoku.width * cell_size + 200,
             self.sudoku.height * cell_size + 200),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(11):
            for j in range(11):
                #print(grid[i])
                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if not grid[i][j] or grid[i][j] != "border":
                    #print(grid[i][j])
                    draw.rectangle(rect, fill="white")
                    if grid[i][j]:
                        w, h = draw.textsize(grid[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            grid[i][j], fill="black", font=font
                        )
                else:
                    draw.rectangle(rect, fill="black")

        img.show()

    def depricated_revise_domains(self, x, y):
        """DEPRECATED Revise X's domain to enforce arc consistency between X and Y. For each value in X's domain, check to see if there is a variable in Y's domain that satisfies constraint (X,Y). If not remove variable. If no variables were removed from X's domain return False, else return True.

        Basically if there's a variable that has only one value, remove that value from it's arcs.
        """

        if len(x.domain) == 1:
            if x.domain[0] in y.domain:
                y.domain.remove(x.domain[0])

        raise NotImplementedError

    def depricated_arc3(self):
        """DEPRECATED Maintain a queue of all arcs in puzzle (or arcs that need checking). As long as the queue is not empty, remove (X,Y) from the queue and run Revise().

        If revise is true, check to see if the domain of X is 0. If so return false because it's not possible to solve the problem. Otherwise, add every arc including X (aside from the one we just checked) to the queue.

        If revise is false (or after the above), move to the next item in the queue.

        If the queue is empty, return true.

        Unlike in the crossword generator, we are going to check both X and Y in the revise, not just X. So we will add arcs attached to both X and Y. We will also see if either X or Y's domain is 0 not just X's.
        """

        queue = self.sudoku.arcs
        while queue:
            (x, y) = queue.pop()
            if self.depricated_revise_domains(x, y):
                if x.domain == 0:
                    return false
                #queue.add()
            if self.depricated_revise_domains(y, x):
                if y.domain == 0:
                    return false
                #queue.add()
        raise NotImplementedError
        return true

def main():
    # check usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 sudoku.py puzzle_file")

    # parse sys args
    puzzle_file = sys.argv[1]

    # initialize sudoku board and variables
    sudoku = Sudoku(puzzle_file)
    manager = PuzzleManager(sudoku)
    manager.print_img(manager.original_assignment)
    assignment = manager.solve()

    if assignment:
        print("Everything worked and we found a solution.")
        manager.print_img(assignment)
    else:
        print("Something went wrong.")

if __name__ == "__main__":
    main()
