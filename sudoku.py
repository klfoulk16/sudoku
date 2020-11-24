from itertools import combinations
import time

class Sudoku():

    def __init__(self, puzzle_file):

        with open(puzzle_file) as f:
            contents = f.read().splitlines()
        self.check_dimensions(contents)
        self.width = 9
        self.height = 9
        # define self.variables, self.rows, self.columns, self.blocks
        self.define_variables(contents)
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
        """Initializes the set of variables contained in the puzzle. Also categorizes them into rows, columns and blocks so that we can easily identify arcs."""

        self.variables = set()
        self.rows = [[] for _ in range(self.height)]
        self.columns = [[] for _ in range(self.width)]
        self.blocks = [[] for _ in range(9)]

        block_map = self.define_block_map()
        for row in range(self.height):
            for column in range(self.width):
                block = self.identify_block(row, column, block_map)
                if contents[row][column] == "_":
                    var = Variable(row, column, block)
                    self.variables.add(var)
                    self.rows[row].append(var)
                    self.columns[column].append(var)
                    self.blocks[block].append(var)
                else:
                    var = Variable(row, column, block, contents[row][column])
                    self.variables.add(var)
                    self.rows[row].append(var)
                    self.columns[column].append(var)
                    self.blocks[block].append(var)


    def define_block_map(self):
        """Maps out which array coordinates are part of which block."""
        blocks = []
        for h in range(0, 9, 3):
            for w in range(0, 9, 3):
                block = []
                for h2 in range(3):
                    for w2 in range(3):
                        block.append((h+h2, w+w2))
                blocks.append(block)
        return blocks

    def identify_block(self, row, column, block_map):
        """Figures out which block a pair of coordinates is in"""
        for i in range(9):
            if (row, column) in block_map[i]:
                return i
        else:
            raise ValueError("This coordinate pair is not in a block.")

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
            for var2 in self.blocks[var.block]:
                if var2 != var:
                    neighbors.add(var2)
            self.neighbors[var] = neighbors

class Variable():
    def __init__(self, row, column, block, domain=None):
        self.row = row
        self.column = column
        self.block = block
        self.domain = [domain] if domain else [str(i) for i in range(1,10)]

    def __str__(self):
        return f'Variable(row={self.row}, column={self.column}, block={self.block}, domain={self.domain})'

    def __repr__(self):
        return f"Variable(row={self.row}, column={self.column})"
