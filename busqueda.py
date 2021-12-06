import re
# Abrimos los archivos de texto y los leemos
fileA = open("./ElPais/ciencia/ElPais_ciencia_2021-11-29_22.txt", 'r', encoding="utf-8")
fileB = open("./ElPais/ciencia/ElPais_ciencia_2021-11-29_23.txt", 'r', encoding="utf-8")
docA = fileA.read()
docB = fileB.read()
fileA.close()
fileB.close()
# Separamos el texto de los archivos por palabras
bagOfWordsA = re.split('\n######\n|\|| |\(|\)|\.|\,|\”|\“|\[|\]',docA) 
bagOfWordsB = re.split('\n######\n|\|| |\(|\)|\.|\,|\”|\“|\[|\]',docB)
# Pasamos las palabras a un mismo conjunto para evitar duplicidades
uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))
# Creamos un diccionario y contamos las ocurrencias de palabras en cada archivo
numOfWordsA = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsA:
    numOfWordsA[word] += 1
print(len(numOfWordsA.keys()))
del numOfWordsA['']
print(len(numOfWordsA.keys()))
numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsB:
    numOfWordsB[word] += 1
del numOfWordsB['']
#print(numOfWordsA)