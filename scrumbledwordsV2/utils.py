def readFileIntoList(filename):
    with open(filename) as f:
        somevar = f.readlines()
    somevar = [x.strip() for x in somevar]
    return somevar

def writeListIntoFileLineByLine(filename, list):
    with open(filename, 'w') as f:
        for item in list:
            f.write("%s\n" % item)