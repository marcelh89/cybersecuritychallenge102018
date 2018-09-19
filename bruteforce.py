from utils import readFileIntoList, mergeAllMutationsAsList

#define vars
encryptedwords = []


# read 2 files into variables
scrambledwords = readFileIntoList("scrambled-words.txt")
dict = readFileIntoList("dictionary.txt")

print(scrambledwords)
print(dict)

# create all mutations of each scrambled word
print()

for word in scrambledwords:
    #print(word)
    mutations = mergeAllMutationsAsList(word)

    for mutation in mutations:
        if mutation in dict:
            print(word + " --> " +mutation)