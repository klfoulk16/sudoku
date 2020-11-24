from itertools import combinations
import time

class Sudoku():

    def __init__(self, puzzle_file):

        with open(puzzle_file) as f:
            contents = f.read().splitlines()
        self.check_dimensions(contents)
        self.width = 9
        self.height = 9
        # define variable set, rows, columns
        self.define_variables(contents)
        self.blocks = self.define_blocks()
        self.arcs = self.define_arcs()

    def __str__(self):
        return "Hi I'm a sudoku puzzle, nice to meet you!"

    def check_dimensions(self, contents):
        if len(contents) != 9:
            raise ValueError("The sudoku puzzle should be a 9x9 grid.")
        for row in contents:
            if len(row) != 9:
                raise ValueError("The sudoku puzzle should be a 9x9 grid.")

    def define_variables(self, contents):

        # initialize variables
        # I think rows and columns could be a list of lsits because the indexing will be the same
        self.variables = set()
        self.rows = [[] for _ in range(self.height)]
        self.columns = [[] for _ in range(self.width)]
        self.blocks
        for row in range(self.height):
            for column in range(self.width):
                if contents[row][column] == "_":
                    var = Variable(row, column)
                    self.variables.add(var)
                    self.rows[row].append(var)
                    self.columns[column].append(var)
                else:
                    var = Variable(row, column, contents[row][column])
                    self.variables.add(var)
                    self.rows[row].append(var)
                    self.columns[column].append(var)

    def define_blocks(self):
        """Identify variables contained in each 3x3 block"""
        blocks = []
        for h in range(0, 9, 3):
            for w in range(0, 9, 3):
                block = []
                for h2 in range(3):
                    for w2 in range(3):
                        var = next((x for x in self.variables if x.row == h+h2 and x.column == w+w2))
                        block.append(var)
                blocks.append(block)
        return blocks

    def define_arcs(self):
        """What if for each variable, we created a dictionary that contains all of the neighbors for that variable."""

        self.neighbors = dict()
        for var in self.variables:
            neighbors = set()
            # add all of the variables that are in that variable's column
            for var2 in self.columns[var.column]:
                if var2 != var:
                    neighbors.add(var2)
            # add all of the variables that are in that variable's row
            for var2 in self.rows[var.row]:
                if var2 != var:
                    neighbors.add(var2)
            # """ block
            for var2 in self.identify_block(var):
                if var != var2:
                    neighbors.add(var2)
            self.neighbors[var] = neighbors


class Variable():
    def __init__(self, row, column, domain=None):
        self.row = row
        self.column = column
        self.block = block
        self.domain = [domain] if domain else [str(i) for i in range(1,10)]

    def __str__(self):
        return f'Variable(h={self.h}, w={self.w}, domain={self.domain})'

    def __repr__(self):
        return f"Variable(h={self.h}, w={self.w})"
