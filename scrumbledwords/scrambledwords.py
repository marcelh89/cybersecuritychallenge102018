import hashlib
from scrumbledwords.utils import readFileIntoList, mergeAllMutationsAsList, writeListIntoFileLineByLine

#define vars
encryptedwords = []


# read 2 files into variables
scrambledwords = readFileIntoList("scrambled-words.txt")
dict = readFileIntoList("dictionary.txt")

print(scrambledwords)
print(dict)

# create all mutations of each scrambled word
print()

unscrambledwords = []

for word in scrambledwords:
    #print(word)
    mutations = mergeAllMutationsAsList(word)

    for mutation in mutations:
        if mutation in dict:
            unscrambledwords.append(mutation)
            #print(word + " --> " +mutation)

writeListIntoFileLineByLine("unscrambled-words.txt",unscrambledwords)
unscrambledconcatenatedstring = "".join(unscrambledwords).lower()
print(unscrambledconcatenatedstring)
hashedUnscrambled = hashlib.sha256(unscrambledconcatenatedstring.encode('utf-8'))
print(hashedUnscrambled.hexdigest())