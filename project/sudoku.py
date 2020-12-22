class Variable:
    def __init__(self, row, column, block, domain=None):
        """
        Create a new variable with row, column, block and domain.
        """
        self.row = row
        self.column = column
        self.block = block
        self.domain = [domain] if domain else [str(i) for i in range(1, 10)]

    def __str__(self):
        return f"Variable(row={self.row}, column={self.column}, block={self.block}, domain={self.domain})"

    def __repr__(self):
        return f"Variable(row={self.row}, column={self.column})"


class Sudoku:
    def __init__(self, puzzle_file):
        """
        Create a new sudoku puzzle with a master set of variables and arcs,
        and subsets of which variables are in each row, column and block.
        """
        with open(puzzle_file) as f:
            contents = f.read().splitlines()
        self.check_dimensions(contents)
        self.width = 9
        self.height = 9
        # define self.variables, self.rows, self.columns, self.blocks
        self.define_variables(contents)
        self.neighbors = self.define_neighbors()

    def check_dimensions(self, contents):
        """
        Checks to make sure the puzzle is a 9x9 grid.
        """
        if len(contents) != 9:
            raise ValueError("The sudoku puzzle should be a 9x9 grid.")
        for row in contents:
            if len(row) != 9:
                raise ValueError("The sudoku puzzle should be a 9x9 grid.")

    def define_variables(self, contents):
        """
        Initializes the set of variables contained in the puzzle. Also
        creates lists of which variables are in which row, column and block so
        we can easily identify arcs.
        """
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
        """
        Returns list of lists filled with (row, column) pairs that are part of
        each block in the puzzle.
        """
        blocks = []
        for h in range(0, 9, 3):
            for w in range(0, 9, 3):
                block = []
                for h2 in range(3):
                    for w2 in range(3):
                        block.append((h + h2, w + w2))
                blocks.append(block)
        return blocks

    def identify_block(self, row, column, block_map):
        """
        Figures out which block a pair of (row, column) coordinates is in.
        """
        for i in range(9):
            if (row, column) in block_map[i]:
                return i
        else:
            raise ValueError("This coordinate pair is not in a block.")

    def define_neighbors(self):
        """
        Creates a dictionary defining the set of binary constraints affecting
        each variable. Maps each variable to a set containing variables that
        are in the same row, column or block (ie the variable's neighbors).
        The variables value cannot be the same as any of the variables in its
        set of neighbors.
        """
        all_neighbors = dict()
        for var in self.variables:
            vars_neighbors = set()
            # add all of the variables that are in that variable's column
            for var2 in self.columns[var.column]:
                if var2 != var:
                    vars_neighbors.add(var2)
            # add all of the variables that are in that variable's row
            for var2 in self.rows[var.row]:
                if var2 != var:
                    vars_neighbors.add(var2)
            # """ block
            for var2 in self.blocks[var.block]:
                if var2 != var:
                    vars_neighbors.add(var2)
            all_neighbors[var] = vars_neighbors
        return all_neighbors
