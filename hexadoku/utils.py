from bisect import bisect_left, bisect_right


def readFileIntoList(filename):
    with open(filename) as f:
        somevar = f.readlines()
    somevar = [x.strip() for x in somevar]
    return somevar


def getRowNeighbors(field, columns):
    column = field[0]
    row = field[1:]
    leftovercolumns = [x + row for x in columns if x != column]
    return [leftovercolumns]

def getColumnNeighbors(field, rows):
    column = field[0]
    row = field[1:]
    leftoverrows = [column + str(x) for x in rows if str(x) != row]
    return [leftoverrows]

def getBlockNeighbors(field, columns, rows, blocksize):
    column = field[0]
    row = field[1:]

    columnindex = columns.index(column)
    rowindex = rows.index(int(row))

    endindices = [x+(blocksize-1) for x in rows if x % blocksize==0 ]
    startindices = [x for x in rows if x % blocksize==0 ]

    startrow = [x for x in startindices if x <= rowindex][-1]
    endrow = [x for x in endindices if x >= rowindex][0]

    startcolumn = [columns[x] for x in startindices if x <= columnindex][-1]
    endcolumn = [columns[x] for x in endindices if x >= columnindex][0]

    neighbors = []
    for itcol in range(ord(startcolumn), ord(endcolumn)+1):
        for itrow in range(startrow, endrow+1):
            neighbors.append(chr(itcol) + str(itrow))
    neighbors.remove(field)

    return neighbors


#getBlockNeighbors("A1", [x for x in "ABCDEFGHIJKLMNOP"], [x for x in range(16)], 4)
#getBlockNeighbors("E10", [x for x in "ABCDEFGHIJKLMNOP"], [x for x in range(16)], 4)
#getBlockNeighbors("P15", [x for x in "ABCDEFGHIJKLMNOP"], [x for x in range(16)], 4)

