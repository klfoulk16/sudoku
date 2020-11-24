import itertools

def define_block():
    """Used this to figure out how to divide up sudoku grid into 3x3 blocks"""
    a = [
              [5, 3, 4, 6, 7, 8, 9, 1, 2],
              [6, 7, 2, 1, 9, 5, 3, 4, 8],
              [1, 9, 8, 3, 4, 2, 5, 6, 7],
              [8, 5, 9, 7, 6, 1, 4, 2, 3],
              [4, 2, 6, 8, 5, 3, 7, 9, 1],
              [7, 1, 3, 9, 2, 4, 8, 5, 6],
              [9, 6, 1, 5, 3, 7, 2, 8, 4],
              [2, 8, 7, 4, 1, 9, 6, 3, 5],
              [3, 4, 5, 2, 8, 6, 1, 7, 9],
            ]

    #blocks = []
    #for i in range(0, 9, 3):
        #for j in range(0, 9, 3):
            #blocks.append(a[i][j:j+3] + a[i+1][j:j+3] + a[i+2][j:j+3])
    blocks = []
    for h in range(0, 9, 3):
        for w in range(0, 9, 3):
            block = []
            for h2 in range(3):
                for w2 in range(3):
                    block.append((h+h2,w+w2))
            blocks.append(block)
            print(block)
            for value in block:
                print(value)
            #for value in block:
                #print(a[value[0]][value[1]], end=", ")
            #print()
            #print(block)

def optional_arguements(domain=None):
    domain = [domain] if domain else [i for i in range(1,10)]
    print(domain)

def define_arcs(self):
    """Deprecated version...explanation: This is a wonderful setup I had created in the beginning so that all of the pairings would be unique and if (x,y) is present (y,x) will not be. However the way I have set up the other algorithms in PuzzleManager demains that an arc only points one way. Aka saying that X is connected to Y not that PLUS Y is connected to X. When queueing arcs to revise/check if only (x,y) is in the queue, but (y,x) is not, then we will only ever check that all of X's domain is consistent with at least something in Y's, but not vice versa.

    Sets self.arcs as a list/set??? of all the arcs contained in the problems.
    1. Each number 1-9 can only appear once in each row, column and block
    """
    # arcs is a set to eliminate duplicate values // print it out with this and see
    # I will initialize this as a set because I don't need duplicate values
    arcs = set()
    for block in self.blocks:
        if block == self.blocks[0]:
            new_arcs = list(combinations(block, 2))
            for item in new_arcs:
                arcs.add(item)

    # mark arcs for all variables in the same row
    # we could essentially add both width and height by duplicating line 75 and changing it a bit
    for row in range(self.height):
        if row == 0:
            row_items = list((row, w) for w in range(self.width))
            new_arcs = list(combinations(row_items, 2))
            for item in new_arcs:
                arcs.add(item)

    # mark arcs for all variables in same column
    for column in range(self.width):
        if column == 0:
            column_items = list((h, column) for h in range(self.height))
            print(column_items)
            print()
            new_arcs = list(combinations(row_items, 2))
            for item in new_arcs:
                arcs.add(item)
    print(arcs)

def arc3():
    """Testing to see if 'while queue' works"""
    queue = {1,2}

    while queue:
        print(queue)
        queue.pop()

def testing_intertools_with_replacement():
    test_list = [0, 1, 2, 3]

    result = list(itertools.combinations_with_replacement(test_list, 2))
    print(result)

def pairs():
    test_list = [0, 1, 2, 3]
    result = set()

    for var1 in test_list:
        for var2 in test_list:
            if var1 != var2:
                result.add((var1, var2))
    print(result)

def revise():
    x = [0, 1, 2]
    y = [2, 3, 4]

    for value in y:
        if value in x:
            x.remove(value)

    print(x)

def integer():
    i = 9
    print(i%3)

integer()
