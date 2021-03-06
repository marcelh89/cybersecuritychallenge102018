import operator

line = "MDEwMTEwMDEgMDExMDEwMDEgMDExMDEwMTEgMDExMDAxMDEgMDExMTAwMTEgMDAxMDExMDAgMDAxMDAwMDAgMDExMTEwMDEgMDExMDExMTEgMDExMTAxMDEgMDAxMDAwMDAgMDExMDAxMDAgMDExMDEwMDEgMDExMDAxMDAgMDAxMDAwMDAgMDExMDEwMDEgMDExMTAxMDAgMDAxMDAwMDEgMDAxMDAwMDAgMDEwMTEwMDEgMDExMDExMTEgMDExMTAxMDEgMDExMTAwMTAgMDAxMDAwMDAgMDExMDAxMTAgMDExMDExMDAgMDExMDAwMDEgMDExMDAxMTEgMDAxMDAwMDAgMDExMDEwMDEgMDExMTAwMTEgMDAxMTEwMTAgMDAxMDAwMDAgMDExMTEwMTEgMDEwMDAxMTAgMDEwMDExMDAgMDEwMDAxMTEgMDAxMTEwMTAgMDEwMTEwMDEgMDExMDExMTEgMDExMTAxMDEgMDEwMDAwMTEgMDExMDAwMDEgMDExMDExMTAgMDEwMDAxMTAgMDExMDEwMDEgMDExMDExMTAgMDExMDAxMDAgMDEwMTAxMDAgMDExMDAwMDEgMDExMTAwMTAgMDExMDAxMTEgMDExMDAxMDEgMDExMTAxMDAgMDEwMDEwMDAgMDExMDExMTEgMDExMTAwMTEgMDExMTAxMDAgMDExMTAwMTEgMDEwMDExMTEgMDExMDExMTAgMDEwMTAxMDAgMDExMDEwMDAgMDExMDAxMDEgMDAxMTAxMDAgMDExMTAxMDAgMDExMDEwMDAgMDEwMDAxMTAgMDExMDExMDAgMDExMDExMTEgMDExMDExMTEgMDExMTAwMTAgMDEwMDExMTEgMDExMDAxMTAgMDEwMTAxMDAgMDExMDEwMDAgMDExMDAxMDEgMDEwMDAwMTAgMDExMTAxMDEgMDExMDEwMDEgMDExMDExMDAgMDExMDAxMDAgMDExMDEwMDEgMDExMDExMTAgMDExMDAxMTEgMDExMTExMDE="
n = 4

chunks = [line[i:i+n] for i in range(0, len(line), n)]

countOfChunks = {}

for chunk in chunks:
    if chunk in countOfChunks.keys():
        countOfChunks[chunk] += 1
    else:
        countOfChunks[chunk] = 1

statistic = "etaonishrlducmwyfgpbvkjxqz"

sorted_x = sorted(countOfChunks.items(), key=operator.itemgetter(1), reverse=True)

for idx, val in enumerate(sorted_x):
    char = statistic[idx]
    line = line.replace(val[0], char);