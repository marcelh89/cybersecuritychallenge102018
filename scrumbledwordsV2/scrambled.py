from scrumbledwords.utils import readFileIntoList, writeListIntoFileLineByLine

#define vars
encryptedwords = []
possibleUnscrambled = {}

# read 2 files into variables
scrambledwords = readFileIntoList("scrambled-words.txt")
dictionary = readFileIntoList("dictionary.txt")

## create a dict with length of words as key and list as value which contains all the dictionary words by length
dictPerLength = dict()
for word in dictionary:
    if len(word)-1 in dictPerLength:
        dictPerLength[len(word) - 1].append(word)
    else:
        dictPerLength[len(word)-1] = [word]

## create a mapping of scrambled words and possible solution of dictionary mapped by same length
for word in scrambledwords:
    possibleUnscrambled[word] = dictPerLength[len(word)-1]
    tmp = possibleUnscrambled[word]

    charcount = {}

    for char in word:
        charcount[char] = word.count(char);
        tmp = [x for x in tmp if char in x and word.count(char) == x.count(char)]

    possibleUnscrambled[word] = tmp

uncrambled = [possibleUnscrambled[key] for key in possibleUnscrambled.keys()]
flat_list = [item for sublist in uncrambled for item in sublist]

writeListIntoFileLineByLine("unscrambled-words.txt", flat_list)

