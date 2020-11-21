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

        Choose a **random unassigned variable, then it'll iteratively check every value in the domain of the variable to see if the value is arc consistent with the current assignment. If it is, then {variable= value} is added to the assignment dictionary. Then call backtrack on that assignment. If the result was not failure, then return the result assignment. Otherwise, remove {variable=value} from the assignment and try the next value in the variable's domain.

        If we reach the end of the values in the variable's domain return failure. Thus we will back up a step in the backtracking heirarchy because some earlier assignment is causing issues.
        """

        if not assignment:
            assignment = self.original_assignment

        var = self.choose_unassigned_variable(assignment)
        for value in var.domain:
            if self.check_arc_consistency(assignment, var):
                assignment[var] = value
                if backtrack(assignment):
                    return assignment
                else:
                    del assignment[var]
        return None

    def choose_unassigned_variable(self, assignment):
        """For now this will just return a random variable. Eventually we will use a heuristic to return the hopefully best variable to check given the current assignment."""

        for var in self.sudoku.variables:
            if var not in assignment.keys():
                return var

    def check_arc_consistency(self, assignment, var):
        """For any given assignment check to see if all the values are arc-consistent with each other.

        This is necessary. If we called arc3 instead of this, we would be removing numbers from each variable's domain with each backtrack call, which would cause a problem if we had to "un"backtrack. The numbers wouldn't be readded and the domain would be inaccurate."""
        # see if all blocks, rows and columns do not have duplicates

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
    manager.solve()

if __name__ == "__main__":
    main()
