fileA = open("./ElPais/ciencia/ElPais_ciencia_2021-11-29_22.txt", 'r', encoding="utf-8")
fileB = open("./ElPais/ciencia/ElPais_ciencia_2021-11-29_23.txt", 'r', encoding="utf-8")
docA = fileA.read()
docB = fileB.read()
print(docA)
fileA.close()
fileB.close()
bagOfWordsA = docA.split(' ') 
bagOfWordsB = docB.split(' ')
print(bagOfWordsA)
uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))
numOfWordsA = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsA:
    numOfWordsA[word] += 1
numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsB:
    numOfWordsB[word] += 1