from io import StringIO


def readFileIntoList(filename):
    with open(filename) as f:
        somevar = f.readlines()
    somevar = [x.strip() for x in somevar]
    return somevar


def getRowNeighbors(field, columns, data):
    column = field[0]
    row = field[1:]
    rowNeighbors = [x + row for x in columns if x != column]
    rowNeighborValues = [data[x + row] for x in columns if x != column and data[x + row] != '.' and not isinstance(data[x + row], list)]
    return rowNeighborValues

def getColumnNeighbors(field, rows, data):
    column = field[0]
    row = field[1:]
    columnNeighbors = [column + str(x) for x in rows if str(x) != row]
    columnNeighborValues = [data[column + str(x)] for x in rows if str(x) != row and data[column + str(x)] != '.' and not isinstance(data[column + str(x)], list)]
    return columnNeighborValues

def getBlockNeighbors(field, columns, rows, blocksize, data):
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

    neighborValues = [data[x] for x in neighbors if data[x] != '.' and not isinstance(data[x], list)]

    return neighborValues


def prettyprintHexadoku(columns, rows, blocksize, data):
    buf = StringIO()

    header =   "      A B C D  E F G H  I J K L  M N O P"
    splitrow = "     |--------|--------|--------|--------|"

    buf.write(header)
    buf.write("\n")


    #it here
    for row in rows:
        if(row % blocksize == 0):
            buf.write(splitrow)
            buf.write("\n")
        currentRow = ""
        for idx,col in enumerate(columns):
            if (idx == 0):
                buf.write(str(row))
                buf.write("    |" if len(str(row)) == 1 else "   |")
            if (idx % blocksize == 0 and idx != 0):
                buf.write("|")
            buf.write((data[col+str(row)] if not isinstance(data[col+str(row)], list) else '.' )+ " ")
        buf.write("|\n")


    #it here


    buf.write(splitrow)


    tmp = buf.getvalue()
    print(tmp)
    return tmp

def getBlocks(columns, rows, blocksize):
    blocks = []
    rowBoundaries = [(x, x+blocksize-1) for x in range(0, len(rows), blocksize)]
    columnBoundaries = [(columns[x], columns[x+blocksize-1]) for x in range(0, len(columns), blocksize)]
    merged = []
    for row in rowBoundaries:
        for col in columnBoundaries:
            merged.append(((col[0]+str(row[0]),col[1]+str(row[1]))))

    print()





# A0-D3 E0-H3 I0-L3 M0-P3
# A4-D7 E4-H7 I4-L7 M4-P7
# A8-D11 E8-H11 I8-L11 M8-L11
# A12-D15 E12-H15 I12-L15 M11-L15





getBlocks([x for x in "ABCDEFGHIJKLMNOP"], [x for x in range(16)], 4)


#getBlockNeighbors("A1", [x for x in "ABCDEFGHIJKLMNOP"], [x for x in range(16)], 4)
#getBlockNeighbors("E10", [x for x in "ABCDEFGHIJKLMNOP"], [x for x in range(16)], 4)
#getBlockNeighbors("P15", [x for x in "ABCDEFGHIJKLMNOP"], [x for x in range(16)], 4)


