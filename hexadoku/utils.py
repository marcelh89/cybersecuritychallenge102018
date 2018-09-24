from io import StringIO


def readFileIntoList(filename):
    with open(filename) as f:
        somevar = f.readlines()
    somevar = [x.strip() for x in somevar]
    return somevar


class Hexadoku:
    def __init__(self, filename):
        self.filecontent = []
        self.data = {}
        self.columns = []
        self.rows = []
        self.loadFromDataFile(filename);

    def loadFromDataFile(self, filename):
        self.filecontent = readFileIntoList(filename)

        self.possiblecontents = self.filecontent[0]
        self.columns = [x for x in self.filecontent[1]]
        self.blocksize = int(self.filecontent[2])
        del self.filecontent[0]
        del self.filecontent[0]
        del self.filecontent[0]

        self.rows = [x for x in range(len(self.filecontent))]

        for idx, row in enumerate(self.filecontent):
            rowkey = str(idx)
            for idx, entry in enumerate(row):
                key = str(self.columns[idx]) + rowkey
                self.data[key] = entry  # if entry != "." else possiblecontents

        self.emptyfields = {k: self.data.get(k) for k in self.data if self.data.get(k) == "."}


    def getRowNeighbors(self, field):

        data = self.data
        columns = self.columns

        column = field[0]
        row = field[1:]
        rowNeighbors = [x + row for x in columns if x != column]
        rowNeighborValues = [data[x + row] for x in columns if x != column and data[x + row] != '.' and not isinstance(data[x + row], list)]

        rowNeighborValuesFromLists = [data[x + row] for x in columns if x != column and data[x + row] != '.' and isinstance(data[x + row], list)]
        flatList = [item for sublist in rowNeighborValuesFromLists for item in sublist]

        rowNeighborValues.extend(x for x in flatList if x not in rowNeighborValues)

        return rowNeighborValues

    def getColumnNeighbors(self, field):
        data = self.data
        rows = self.rows

        column = field[0]
        row = field[1:]
        columnNeighbors = [column + str(x) for x in rows if str(x) != row]
        columnNeighborValues = [data[column + str(x)] for x in rows if str(x) != row and data[column + str(x)] != '.' and not isinstance(data[column + str(x)], list)]

        columnNeighborValuesFromLists = [data[column + str(x)] for x in rows if str(x) != row and data[column + str(x)] == '.' and isinstance(data[column + str(x)], list)]
        flatList = [item for sublist in columnNeighborValuesFromLists for item in sublist]

        columnNeighborValues.extend(x for x in flatList if x not in columnNeighborValues)

        return columnNeighborValues

    def getBlockNeighbors(self, field):
        data = self.data
        rows = self.rows
        columns = self.columns
        blocksize = self.blocksize

        column = field[0]
        row = field[1:]

        columnindex = columns.index(column)
        rowindex = rows.index(int(row))

        endindices = [x+(blocksize-1) for x in rows if x % blocksize == 0]
        startindices = [x for x in rows if x % blocksize == 0]

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

        neighborValuesFromLists = [data[x] for x in neighbors if data[x] == '.' and isinstance(data[x], list)]

        flatList = [item for sublist in neighborValuesFromLists for item in sublist]

        neighborValuesFromLists.extend(x for x in flatList if x not in neighborValuesFromLists)

        return neighborValues


    def prettyprint(self):
        buf = StringIO()

        header =   "      A B C D  E F G H  I J K L  M N O P"
        splitrow = "     |--------|--------|--------|--------|"

        buf.write(header)
        buf.write("\n")

        for row in self.rows:
            if(row % self.blocksize == 0):
                buf.write(splitrow)
                buf.write("\n")
            currentRow = ""
            for idx,col in enumerate(self.columns):
                if (idx == 0):
                    buf.write(str(row))
                    buf.write("    |" if len(str(row)) == 1 else "   |")
                if (idx % self.blocksize == 0 and idx != 0):
                    buf.write("|")
                buf.write((self.data[col+str(row)] if not isinstance(self.data[col+str(row)], list) else '.' )+ " ")
            buf.write("|\n")

        buf.write(splitrow)
        tmp = buf.getvalue()

        print(tmp)
        return tmp

    def getBlocks(self, data):
        columns = self.columns

        rows = self.rows
        blocksize = self.blocksize

        rowBoundaries = [(x, x+blocksize-1) for x in range(0, len(rows), blocksize)]
        columnBoundaries = [(columns[x], columns[x+blocksize-1]) for x in range(0, len(columns), blocksize)]
        mergedBlocks = []
        for row in rowBoundaries:
            for col in columnBoundaries:
                name = col[0]+str(row[0])+col[1]+str(row[1])
                coordinates = (col[0],str(row[0]), col[1], str(row[1]))
                block = Block(name, coordinates, data)
                mergedBlocks.append(block)

        return mergedBlocks


    def getBlockWithLeastEmptyFields(self):
        blocks = self.getBlocks(self.data)

        blocks.sort(key=lambda x: len(x.emptyFields))

        if len(blocks) > 0 :
            return blocks[0]
        else:
            return None


    def calculate(self):

        for field in self.emptyfields.keys():

            # fill with all possible values
            fieldvalues = [x for x in self.possiblecontents]

            # get all neighbors
            rowNeighborValues = self.getRowNeighbors(field)
            columnNeighborValues = self.getColumnNeighbors(field)
            blockNeighborValues = self.getBlockNeighbors(field)

            # merge neighbors
            overallNeighbors = list(set(rowNeighborValues + columnNeighborValues + blockNeighborValues))

            # reduce possible items

            tmp = list(set(fieldvalues) - set(overallNeighbors))

            if (len(tmp) == 1):
                self.data[field] = field[0]
            else:
                self.data[field] = tmp

        while(True):
            block = self.getBlockWithLeastEmptyFields()

            self.prettyprint()

            if(block == None):
                break
            else:
                self.iterate(block)


    def iterate(self, block):

        for field in block.emptyFields:

            # fill with all possible values
            fieldvalues = [x for x in self.possiblecontents]

            # get all neighbors
            rowNeighborValues = self.getRowNeighbors(field)
            columnNeighborValues = self.getColumnNeighbors(field)
            blockNeighborValues = self.getBlockNeighbors(field)

            # merge neighbors
            overallNeighbors = list(set(rowNeighborValues + columnNeighborValues + blockNeighborValues))

            # reduce possible items

            tmp = list(set(fieldvalues) - set(overallNeighbors))

            if (len(tmp) == 1):
                self.data[field] = field[0]
            else:
                self.data[field] = tmp



class Block:
    def __init__(self, name, coordinates, data): # e.g. (A,0,D,3) or (A,12,D,15)
        self.name = name
        self.data = data  ## todo we only need the data for the block, not the whole hexadoku!
        self.startcolumn = coordinates[0]
        self.startrow = coordinates[1]
        self.endcolumn = coordinates[2]
        self.endrow = coordinates[3]
        self.emptyFields = self.getEmptyFields()

    def getEmptyFields(self):
        startcolumn = self.startcolumn
        endcolumn = self.endcolumn
        startrow = int(self.startrow)
        endrow = int(self.endrow)

        emptyfields = []

        for itcol in range(ord(startcolumn), ord(endcolumn)+1):
            for itrow in range(startrow, endrow+1):
                if isinstance(self.data[chr(itcol)+str(itrow)], list):
                    emptyfields.append(chr(itcol)+str(itrow))
        return emptyfields

    def __str__(self):
        return self.name + " / " + self.emptyfields



# A0-D3 E0-H3 I0-L3 M0-P3
# A4-D7 E4-H7 I4-L7 M4-P7
# A8-D11 E8-H11 I8-L11 M8-L11
# A12-D15 E12-H15 I12-L15 M11-L15





#getBlocks([x for x in "ABCDEFGHIJKLMNOP"], [x for x in range(16)], 4)


#getBlockNeighbors("A1", [x for x in "ABCDEFGHIJKLMNOP"], [x for x in range(16)], 4)
#getBlockNeighbors("E10", [x for x in "ABCDEFGHIJKLMNOP"], [x for x in range(16)], 4)
#getBlockNeighbors("P15", [x for x in "ABCDEFGHIJKLMNOP"], [x for x in range(16)], 4)


