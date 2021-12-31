import nltk
from nltk.tokenize import word_tokenize
import Stemmer
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')

def procesamiento_lenguaje_noticia(noticia):
    noticia_texto = open(noticia, "r", encoding="utf8")
    noticia_tokenizada = word_tokenize(noticia_texto.read().lower(), language="spanish")
    
    stop_word = []
    stopword_es = nltk.corpus.stopwords.words('spanish')
    stop_word =stopword_es + ['“','”','’', '‘','!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    noticia_tokenizada_copy=[]
    for i in noticia_tokenizada:
        if i not in stop_word:
            noticia_tokenizada_copy.append(i)

    noticia_stem=[]
    stemmer = Stemmer.Stemmer('spanish')
    for palabra in noticia_tokenizada_copy:
        s = stemmer.stemWord(palabra)
        noticia_stem = noticia_stem + [s]
    return noticia_stem

# funcion que calcula el TF
def calculateTF (wordDict, bagOfWords):
    # Comenzamos con el TF, es decir, la frecuencia de una palabra en un documento concreto. 
    # Si por ejemplo quisiéramos saber la TF de una palabra X en el documento A 
    # simplemente dividimos las ocurrencias entre el número de palabras con las que el doc cuenta.
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

# funcion que calcula el IDF
def calculateIDF (docs):
    # Ahora hacemos exactamente lo mismo pero con el IDF. 
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

# funcion que calcula el TF IDF
def calculateTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

def TFIDF(noticias):
    # Pasamos las palabras a un mismo conjunto para evitar duplicidades
    tabla=[]
    for noticia in noticias:
        conjunto=procesamiento_lenguaje_noticia(noticia)
        tabla = set(tabla).union(set(conjunto))

    # Creamos un diccionario y contamos las ocurrencias de palabras en cada archivo
    diccionarios=[]
    for noticia in noticias:
        conjunto=procesamiento_lenguaje_noticia(noticia)
        palabras = dict.fromkeys(tabla, 0)
        for p in conjunto:
            palabras[p] += 1
        diccionarios.append(palabras)
    
    # calculamos el TF. frecuencia básica del termino en los docs
    cont=0
    list_TF=[]
    for noticia in noticias:
        TF = calculateTF(diccionarios[cont], procesamiento_lenguaje_noticia(noticia))
        list_TF.append(TF)
        cont=cont+1

    # calculamos el IDF.
    IDF = calculateIDF(diccionarios)

    # calculamos el TF-IDF completo
    list_TFIDF=[]
    for i in range(len(list_TF)):
        TFIDF = calculateTFIDF(list_TF[i], IDF)
        list_TFIDF.append(TFIDF)

    df = pd.DataFrame(list_TFIDF)

    return df
def main():
    l=["./ElPais/ciencia/ElPais_ciencia_2021-12-25_19.txt","./ElPais/ciencia/ElPais_ciencia_2021-12-25_20.txt","./ElPais/ciencia/ElPais_ciencia_2021-12-24_22.txt"]
    print(TFIDF(l))
main()