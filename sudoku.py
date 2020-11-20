
class Sudoku():

    def __init__(self, puzzle_file):

        self.width = 9
        self.height = 9
        self.blocks = self.define_blocks()

        # get contents from puzzle file
        with open(puzzle_file) as f:
            contents = f.read().splitlines()
        # could check to make sure that it's a 9x9 grid???

        # initialize structure and variables
        # structure has None for variables and value for pre-set numbers
        # I think eventually I can make the "structure" just have the variable at
        # each point vs initializing it with none or value. then set variable to return it's value if called.
        # I'd need to set a value for each variable.
        self.structure = []
        self.variables = set()
        for h in range(self.height):
            row = []
            for w in range(self.width):
                if contents[h][w] == "_":
                    row.append(None)
                    self.variables.add(Variable(h, w, self.identify_block(h, w)))
                else:
                    row.append(contents[h][w])
                    self.variables.add(Variable(h, w, self.identify_block(h, w), contents[h][w]))
            self.structure.append(row)

    def define_blocks(self):
        """Identify coordinates contained in each 3x3 block"""
        blocks = []
        for h in range(0, 9, 3):
            for w in range(0, 9, 3):
                block = []
                for h2 in range(3):
                    for w2 in range(3):
                        block.append((h+h2,w+w2))
                blocks.append(block)
        return blocks

    def identify_block(self, h, w):
        """Identify which block a set of coordinates is part of"""
        for i in range(len(self.blocks)):
            if (h, w) in self.blocks[i]:
                return i

    def arcs(self):
        """Sets self.arcs as a list/set??? of all the arcs contained in the problems.
        1. Each number 1-9 can only appear once in each row, column and block
        """
        raise NotImplementedError

class Variable():
    def __init__(self, h, w, block, domain=None):
        self.h = h
        self.w = w
        self.block = block
        self.domain = [domain] if domain else [i for i in range(1,10)]

    def __str__(self):
        return 'Variable(h='+self.h+', w='+self.w+', block='+self.block+', value='+self.value+')'
