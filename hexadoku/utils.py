import copy
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


    def getEmptyFields(self):
        return {k: self.data.get(k) for k in self.data if
                            self.data.get(k) == "." or isinstance(self.data.get(k), list)}

    def getRowNeighbors(self, field):

        data = self.data
        columns = self.columns

        column = field[0]
        row = field[1:]
        rowNeighbors = [x + row for x in columns if x != column]
        rowNeighborValues = [data[x] for x in rowNeighbors if data[x] != '.' and not isinstance(data[x], list)]

        # TODO remove this
        notallowed = ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
        notallowedForColumns = [x for x in rowNeighborValues if x in notallowed]

        #rowNeighborValuesFromLists = [data[x] for x in rowNeighbors if data[x] != '.' and isinstance(data[x], list)]
        #flatList = [item for sublist in rowNeighborValuesFromLists for item in sublist]

        #rowNeighborValues.extend(x for x in flatList if x not in rowNeighborValues)

        return rowNeighborValues

    def getColumnNeighbors(self, field):
        data = self.data
        rows = self.rows

        column = field[0]
        row = field[1:]
        columnNeighbors = [column + str(x) for x in rows if str(x) != row]
        columnNeighborValues = [data[x] for x in columnNeighbors if data[x] != '.' and not isinstance(data[x], list)]

        #columnNeighborValuesFromLists = [data[x] for x in columnNeighbors if data[x] != '.' and isinstance(data[x], list)]
        #flatList = [item for sublist in columnNeighborValuesFromLists for item in sublist]

        #columnNeighborValues.extend(x for x in flatList if x not in columnNeighborValues)

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

        endindices = [x + (blocksize - 1) for x in rows if x % blocksize == 0]
        startindices = [x for x in rows if x % blocksize == 0]

        startrow = [x for x in startindices if x <= rowindex][-1]
        endrow = [x for x in endindices if x >= rowindex][0]

        startcolumn = [columns[x] for x in startindices if x <= columnindex][-1]
        endcolumn = [columns[x] for x in endindices if x >= columnindex][0]

        neighbors = []
        for itcol in range(ord(startcolumn), ord(endcolumn) + 1):
            for itrow in range(startrow, endrow + 1):
                neighbors.append(chr(itcol) + str(itrow))
        neighbors.remove(field)

        neighborValues = [data[x] for x in neighbors if data[x] != '.' and not isinstance(data[x], list)]

        #neighborValuesFromLists = [data[x] for x in neighbors if data[x] == '.' and isinstance(data[x], list)]
        #flatList = [item for sublist in neighborValuesFromLists for item in sublist]
        #neighborValues.extend(x for x in flatList if x not in neighborValuesFromLists)

        return neighborValues

    def prettyprint(self):
        buf = StringIO()

        header = "      A B C D  E F G H  I J K L  M N O P"
        splitrow = "     |--------|--------|--------|--------|"

        buf.write(header)
        buf.write("\n")

        for row in self.rows:
            if (row % self.blocksize == 0):
                buf.write(splitrow)
                buf.write("\n")
            currentRow = ""
            for idx, col in enumerate(self.columns):
                if (idx == 0):
                    buf.write(str(row))
                    buf.write("    |" if len(str(row)) == 1 else "   |")
                if (idx % self.blocksize == 0 and idx != 0):
                    buf.write("|")
                buf.write((self.data[col + str(row)] if not isinstance(self.data[col + str(row)], list) else '.') + " ")
            buf.write("|\n")

        buf.write(splitrow)
        tmp = buf.getvalue()

        print(tmp)
        return tmp

    def getBlocks(self, data):
        columns = self.columns

        rows = self.rows
        blocksize = self.blocksize

        rowBoundaries = [(x, x + blocksize - 1) for x in range(0, len(rows), blocksize)]
        columnBoundaries = [(columns[x], columns[x + blocksize - 1]) for x in range(0, len(columns), blocksize)]
        mergedBlocks = []
        for row in rowBoundaries:
            for col in columnBoundaries:
                name = col[0] + str(row[0]) + col[1] + str(row[1])
                coordinates = (col[0], str(row[0]), col[1], str(row[1]))
                block = Block(name, coordinates, data)
                mergedBlocks.append(block)

        return mergedBlocks

    def getBlockWithLeastEmptyFields(self):
        blocks = self.getBlocks(self.data)

        blocks.sort(key=lambda x: len(x.getEmptyFields()))

        if len(blocks) > 0:
            return blocks[0]
        else:
            return None

    def initialcCalculation(self):

        tmpdata = copy.deepcopy(self.data)

        """
            initial calculation
        """
        for field in self.getEmptyFields().keys():

            # fill with all possible values
            fieldvalues = [x for x in self.possiblecontents]

            # get all neighbors
            rowNeighborValues = self.getRowNeighbors(field)
            rowNeighborValues.sort()
            columnNeighborValues = self.getColumnNeighbors(field)
            columnNeighborValues.sort()
            blockNeighborValues = self.getBlockNeighbors(field)
            blockNeighborValues.sort()

            """ only for debug
            notallowed = ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
            notallowedForColumns = [x for x in columnNeighborValues if x in notallowed]
            notallowedForRows = [x for x in rowNeighborValues if x in notallowed]
            notallowedForBlocks = [x for x in blockNeighborValues if x in notallowed]
            """

            # merge neighbors
            overallNeighbors = list(set(rowNeighborValues) | set(columnNeighborValues) | set(blockNeighborValues))

            # reduce possible items

            tmp = list(set(fieldvalues) - set(overallNeighbors))

            if (len(tmp) == 1):
                tmpdata[field] = tmp[0]
                print("filled " + field + " with " + tmp[0])
            else:
                tmpdata[field] = tmp
                print("filled " + field + " with " + str(tmp))

        self.data = tmpdata

    def solve(self):
        """
           further calculation
        """
        counter = 0
        while (True):

            if counter == 14:
                print()

            block = self.getBlockWithLeastEmptyFields()
            print()

            counter += 1

            if (block == None):
                break
            else:
                self.initialcCalculation()

            if counter == 15:
                break

    """
    def solveBlock(self, block):

        tmpdata = copy.deepcopy(self.data)

        for field in block.emptyFields:

            # fill with all possible values
            fieldvalues = [x for x in self.possiblecontents]

            # get all neighbors
            rowNeighborValues = self.getRowNeighbors(field)
            columnNeighborValues = self.getColumnNeighbors(field)
            blockNeighborValues = self.getBlockNeighbors(field)

            # merge neighbors
            overallNeighbors = list(set(rowNeighborValues) | set(columnNeighborValues) | set(blockNeighborValues))

            # reduce possible items

            tmp = list(set(fieldvalues) - set(overallNeighbors))

            if (len(tmp) == 1):
                tmpdata[field] = tmp[0]
                print("filled " + field + " with " + tmp[0])
            else:
                tmpdata[field] = tmp
                print("filled " + field + " with " + str(tmp))

    """

class Block:
    def __init__(self, name, coordinates, data):  # e.g. (A,0,D,3) or (A,12,D,15)
        self.name = name
        self.data = data  ## todo we only need the data for the block, not the whole hexadoku!
        self.startcolumn = coordinates[0]
        self.startrow = coordinates[1]
        self.endcolumn = coordinates[2]
        self.endrow = coordinates[3]

    def getEmptyFields(self):
        startcolumn = self.startcolumn
        endcolumn = self.endcolumn
        startrow = int(self.startrow)
        endrow = int(self.endrow)

        emptyfields = []

        for itcol in range(ord(startcolumn), ord(endcolumn) + 1):
            for itrow in range(startrow, endrow + 1):
                if isinstance(self.data[chr(itcol) + str(itrow)], list):
                    emptyfields.append(chr(itcol) + str(itrow))
        return emptyfields

    def __str__(self):
        return self.name + " / " + self.getEmptyFields()

# A0-D3 E0-H3 I0-L3 M0-P3
# A4-D7 E4-H7 I4-L7 M4-P7
# A8-D11 E8-H11 I8-L11 M8-L11
# A12-D15 E12-H15 I12-L15 M11-L15


# getBlocks([x for x in "ABCDEFGHIJKLMNOP"], [x for x in range(16)], 4)


# getBlockNeighbors("A1", [x for x in "ABCDEFGHIJKLMNOP"], [x for x in range(16)], 4)
# getBlockNeighbors("E10", [x for x in "ABCDEFGHIJKLMNOP"], [x for x in range(16)], 4)
# getBlockNeighbors("P15", [x for x in "ABCDEFGHIJKLMNOP"], [x for x in range(16)], 4)
