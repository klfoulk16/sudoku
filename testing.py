
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
            #for value in block:
                #print(a[value[0]][value[1]], end=", ")
            #print()
            #print(block)

def optional_arguements(domain=None):
    domain = [domain] if domain else [i for i in range(1,10)]
    print(domain)

optional_arguements(3)
