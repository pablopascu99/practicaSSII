import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Creamos los dos documentos con los ficheros de noticias extraidos del Mundo, 
# lo abrimos cogemos el texto y lo cerramos. 

fileA = open("./ElMundo/salud/ElMundo_salud_2021-12-01_43.txt", 'r', encoding="utf-8")
docA = fileA.read()
fileA.close()

fileB = open("./ElMundo/salud/ElMundo_salud_2021-12-01_44.txt", 'r', encoding="utf-8")
docB = fileB.read()
fileB.close()

# Usamos la estrategia 'Bag of words': Se usa para crear un vocabulario. 
# Se identifican los términos de los documentos de la colección. D = {d1, d2, ..., dn}  Y si un término aparece en alguno de los documentos, 
# pasa directamente a formar parte del vocabulario. V = {t1, t2, ..., tm}. 

bagA = re.split('\n######\n|\|| |\(|\)|\.|\,|\”|\“|\[|\]',docA)
bagB = re.split('\n######\n|\|| |\(|\)|\.|\,|\”|\“|\[|\]',docB)

# Como vemos obtenemos las palabras de los dos documentos pero desordenadas y repetidas una sola vez.

tabla = set(bagA).union(set(bagB))

# Observamos que ahora si que obtenemos los vectores (repeticiones de las palabras de cada doc), 
# las repeticiones dependerá de cada documento, no es habitual que tengan las mismas.

palabrasA = dict.fromkeys(tabla, 0)
for p in bagA:
    palabrasA[p] += 1
del palabrasA['']
# print(len(palabrasA.keys()))
# print(palabrasA)

palabrasB = dict.fromkeys(tabla, 0)
for p in bagB:
    palabrasB[p] += 1
del palabrasB['']
# print(len(palabrasB.keys()))
# print(palabrasB)

# Comenzamos con el TF, es decir, la frecuencia de una palabra en un documento concreto. 
# Si por ejemplo quisiéramos saber la TF de una palabra X en el documento A 
# simplemente dividimos las ocurrencias entre el número de palabras con las que el doc cuenta.

def calculateTF (wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

tfA = calculateTF(palabrasA, bagA)
tfB = calculateTF(palabrasB, bagB)
# print(tfA)
# print(tfB)

# Ahora hacemos exactamente lo mismo pero con el IDF. 

def calculateIDF (docs):
    import math
    n = len(docs)
    idfDict = dict.fromkeys(docs[0].keys(),0)
    for document in docs:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log(n / float(val))
        
    return idfDict

idfs = calculateIDF([palabrasA, palabrasB])

# print(idfs)

# calculamos el TF IDF
def calculateTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

tfidfA = calculateTFIDF(tfA, idfs)
tfidfB = calculateTFIDF(tfB, idfs)

df = pd.DataFrame([tfidfA, tfidfB])
print(df)