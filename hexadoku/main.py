
"""
    A B C D   E F G H   I J K L   M N O P
   |--------|---------|---------|--------|
0  |3 F . . | . 6 8 9 | 5 2 4 . | . . A B|
1  |B . C 6 | . 5 . 4 | 9 . D . | E 3 . 2|
2  |2 D E . | 0 . . . | . . . 7 | . 9 4 C|
3  |. . 4 . | . A . . | . . F . | . 0 . .|
   |--------|---------|---------|--------|
4  |. . . . | 3 . . 8 | 6 . . D | . . . .|
5  |. . D . | . E 5 6 | A C 7 . | . F . .|
6  |6 . . C | . . 2 7 | F B . . | 8 . . 1|
7  |. 2 3 . | 4 . F . | . 9 . 1 | . D C .|
   |--------|---------|---------|--------|
8  |. B 5 . | 9 . 6 . | . 3 . E | . 1 0 .|
9  |8 . . E | . . B 3 | 7 A . . | C . . 5|
10 |. . 9 . | . 7 E 1 | C 6 5 . | . B . .|
11 |. . . . | 5 . . 0 | 4 . . 9 | . . . .|
   |--------|---------|---------|--------|
12 |. . 6 . | . C . . | . . 9 . | . 8 . .|
13 |0 C F . | 2 . . . | . . . 3 | . E 6 7|
14 |9 . 1 2 | . F . 5 | E . C . | 3 A . D|
15 |D A . . | . 3 7 E | B F 2 . | . . 5 0|
   |--------|---------|---------|--------|

"""
import copy

from hexadoku.utils import readFileIntoList, getRowNeighbors, getColumnNeighbors, getBlockNeighbors

filecontent = readFileIntoList("data.txt")

possiblecontents = filecontent[0]
columns = [x for x in filecontent[1]]
blocksize = int(filecontent[2])
del filecontent[0]
del filecontent[0]
del filecontent[0]

rows = [x for x in range(len(filecontent))]

## get initial data and load it into variable
data = {}
for idx, row in enumerate(filecontent):
    rowkey = str(columns[idx])
    for idx, entry in enumerate(row):
        key = rowkey+str(idx)
        data[key] = entry #if entry != "." else possiblecontents


emptyfields = {k: data.get(k) for k in data if data.get(k) == "."}


for field in emptyfields.keys():

    # fill with all possible values
    fieldvalues = [x for x in possiblecontents]

    #and then reduce...

    #get all neighbors
    rowNeighborValues = getRowNeighbors(field, columns, data)
    columnNeighborValues = getColumnNeighbors(field, rows, data)
    blockNeighborValues = getBlockNeighbors(field, columns, rows, blocksize, data)

    #merge neighbors
    overallNeighbors = list(set(rowNeighborValues + columnNeighborValues + blockNeighborValues))

    #reduce possible items

    tmp = list(set(fieldvalues)-set(overallNeighbors))

    data[field] = tmp

print()
