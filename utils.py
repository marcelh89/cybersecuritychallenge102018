def readFileIntoList(filename):
    with open(filename) as f:
        somevar = f.readlines()
    somevar = [x.strip() for x in somevar]
    return somevar

def shiftLeft(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]

def createAllMutationsOfWord(word):
    wordAsChars = list(word)

    # every used mutation goes here for checking if already mutated
    mutations = {}

    # init empty list for all keys
    for key in wordAsChars:
        mutations[key] = []

    #fill list of possible mutations for each character
    for key in wordAsChars:
        leftover = wordAsChars.copy()
        leftover.remove(key);
        elements = []
        counter = 1

        # add the leftover once, then start to mutate / shift array contents
        #elements.append(leftover)
        elements.append("".join(leftover))

        while(counter < len(leftover)):

            # to add leftover as splitted char array
            # elements.append(shift(leftover, counter))

            ### to add leftover as string
            leftoverAsString = "".join(leftover)
            elements.append(shiftLeft(leftoverAsString, counter))

            counter+=1
        mutations[key] = elements

    return mutations

def createAllMutationsOfWord2(word):
    wordAsChars = list(word)

    # every used mutation goes here for checking if already mutated
    mutations = {}

    # init empty list for all keys
    for key in wordAsChars:
        mutations[key] = []

    #fill list of possible mutations for each character
    for key in wordAsChars:
        leftover = wordAsChars.copy()
        leftover.remove(key);
        elements = []
        start = 0
        end = len(leftover) - 1
        print(leftover, start, end)
        break

    return mutations

print(createAllMutationsOfWord2("rsuf"))

def mergeAllMutationsAsList(word):
    mutationsAsList = []
    mutations = createAllMutationsOfWord(word)
    #print(mutations)

    #prefix all lists in the mutations with the keys (and turn out a list of lists with key prefixes)
    for key in mutations:
        mutationsAsList.append(list(key + x for x in mutations[key]))
    #print(mutationsAsList)

    #make a flat list out of list of lists
    flat_list = [item for sublist in mutationsAsList for item in sublist]
    #print(flat_list)
    return flat_list