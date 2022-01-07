import nltk
from nltk.tokenize import word_tokenize
import Stemmer
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import os
import math
import textdistance
import re
# actualizamos la lista de parada cada vez que ejecutamos, pues es necesario para utilizarla
nltk.download('stopwords')

'''
Funcion que pasa el contenido del fichero de texto a tokens o palabras añadidas a una lista
'''
def txt_toTokens(file):
    # Abrimos el fichero de texto
    noticia_texto = open(file, "r", encoding="utf8").read()
    # Pasamos a minusculas el texto y lo tokenizamos
    noticia_tokenizada = word_tokenize(noticia_texto.lower(), language="spanish")
    return noticia_tokenizada

'''
Funcion que aplica una lista de parada y convierte a stems los tokens o palabras
'''
def procesamiento_lenguaje_noticia(noticia):   
    stop_word = []
    # importamos una lista de parada que tiene la libreria nltk en espanol
    stopword_es = nltk.corpus.stopwords.words('spanish')
    # añadimos a la lista de parada tambien los caracteres especiales
    stop_word =stopword_es + ['“','”','’', '‘','!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    # creamos una copia de la noticia tokenizada donde anadiremos solamente los tokens que
    # no pertenezcan a la lista de parada
    noticia_tokenizada_copy=[]
    for i in noticia:
        if i not in stop_word:
            noticia_tokenizada_copy.append(i)
    # aplicamos el stemmer en espanol de la libreria PyStemmer
    noticia_stem=[]
    stemmer = Stemmer.Stemmer('spanish')
    for palabra in noticia_tokenizada_copy:
        s = stemmer.stemWord(palabra)
        noticia_stem = noticia_stem + [s]
    return noticia_stem

'''
Funcion que calcula el TF
'''
def calculateTF (diccionario, bolsa_palabras):
    # Comenzamos con el TF, es decir, la frecuencia de una palabra en un documento concreto. 
    # Si por ejemplo quisiéramos saber la TF de una palabra X en el documento A 
    # simplemente dividimos las ocurrencias entre el número de palabras con las que el doc cuenta.
    diccionario_TF = {}
    cont_bolsa_palabras = len(bolsa_palabras)
    for palabra, count in diccionario.items():
        diccionario_TF[palabra] = count / float(cont_bolsa_palabras)
    return diccionario_TF

'''
Funcion que calcula el IDF
'''
def calculateIDF (noticias):
    # Ahora hacemos exactamente lo mismo pero con el IDF, que correspondera con el registro del 
    # número de documentos dividido por el número de documentos que contienen la palabra 'w'.
    n = len(noticias)
    diccionario_IDF = dict.fromkeys(noticias[0].keys(),0)
    for noticia in noticias:
        for w, val in noticia.items():
            if val > 0:
                diccionario_IDF[w] += 1
    
    for w, val in diccionario_IDF.items():
        diccionario_IDF[w] = math.log(n / float(val)) 
    return diccionario_IDF

'''
Funcion que calcula el TF-IDF
'''
def calculateTFIDF(TF, IDF):
    # El TF-IDF simplemente sera multiplicar el TF por el IDF
    TFIDF = {}
    for w, val in TF.items():
        TFIDF[w] = val * IDF[w]
    return TFIDF

'''
Funcion coge como argumentos una lista con la ruta de noticias y una consulta y las agrupará en una lista conjunta 
'''
def pathToNoticias(noticias,query):
    noticiasProcesadas=[]
    for noticia in noticias:
        noticiasProcesadas.append(procesamiento_lenguaje_noticia(txt_toTokens(noticia)))  
    noticiasProcesadas.append(procesamiento_lenguaje_noticia(query.split(" ")))
    return noticiasProcesadas

'''
Funcion donde ponderamos los stem mediante TF-IDF, creando un dataframe con esas ponderaciones y
el numero de noticia al que pertenecen
'''
def TFIDF(noticiasProcesadas):
    # Pasamos las palabras a un mismo conjunto para evitar duplicidades
    tabla=[]
    for noticia in noticiasProcesadas:
        tabla = set(tabla).union(set(noticia))
        
    # Creamos un diccionario y contamos las ocurrencias de palabras en cada archivo
    diccionarios=[]
    for noticia in noticiasProcesadas:
        palabras = dict.fromkeys(tabla, 0)
        for p in noticia:
            palabras[p] += 1
        diccionarios.append(palabras)
    
    # calculamos el TF del termino en las noticias
    cont=0
    list_TF=[]
    for noticia in noticiasProcesadas:
        TF = calculateTF(diccionarios[cont], noticia)
        list_TF.append(TF)
        cont=cont+1

    # calculamos el IDF
    IDF = calculateIDF(diccionarios)

    # calculamos el TF-IDF
    list_TFIDF=[]
    for i in range(len(list_TF)):
        TFIDF = calculateTFIDF(list_TF[i], IDF)
        list_TFIDF.append(TFIDF)
    # pasamos la lista a un dataframe de Pandas con el TF-IDF realizado
    df = pd.DataFrame(list_TFIDF)
    return df

'''
Funcion donde obtenemos la similitud del coseno de cada noticia respecto a la consulta
'''
def similitud_coseno(lista: list, nombres_ficheros: list):
    # calculamos la similitud del coseno de la lista con las noticias y query aplicando el TF-IDF
    similitud_coseno = cosine_similarity(TFIDF(lista))
    # obtenemos los nombres con los que relacionaremos las ponderaciones de la similitud en funcion del coseno
    nombres_ficheros = nombres_ficheros + ["query"]
    # obtenemos una matriz de similitud
    matriz_similitud = pd.DataFrame(similitud_coseno, index=nombres_ficheros, columns=nombres_ficheros)
    # devolvemos el los valores de similitud del ultimo nombre de fichero(que en realidad es la query)
    return matriz_similitud.loc[nombres_ficheros[len(nombres_ficheros) - 1]]

'''
Funcion que devuelve una lista con las rutas del periodico seleccionado
'''   
def localizar_directorio(periodico): 
    lista_rutas = []
    periodico_nombre = os.scandir("./" + periodico)
    for carpeta in periodico_nombre:
        carpeta_tipo = os.scandir(carpeta)
        for ruta in carpeta_tipo:
            lista_rutas.append(ruta.path)
    return lista_rutas 

'''
Funcion que devuelve las etiquetas de la noticia 
''' 
def obtener_etiquetas(document):
    regex_1_doc_1 = re.match('(?:[^######]*\######){3}([^######]*)', document).group(1)
    regex_2_doc_1 = re.sub('((?: \| )+),?',' ', regex_1_doc_1)
    regex_3_doc_1 = re.sub('\n', '', regex_2_doc_1)
    return regex_3_doc_1

'''
Funcion que calcula el coeficiente de sorensen dice de dos noticias
''' 
def calculo_sorensen_dice(etiquetas_doc_1, etiquetas_doc_2):
    tokens_1= etiquetas_doc_1.split(" ")
    tokens_2 = etiquetas_doc_2.split(" ")
    print('Etiquetas doc 1: ',tokens_1)
    print('Etiquetas doc 2: ',tokens_2)
    sd = textdistance.sorensen(tokens_1, tokens_2)
    print(sd)
    return sd

def main():
    l=localizar_directorio("ElPais")
    m=localizar_directorio("ElMundo")
    #Texto de la noticia ciencia_2021-12-08_38 de ElMundo
    similitud_coseno(pathToNoticias(l,"Se cumplen 80 dias de actividad para un volcán que será, salvo que se pare por sorpresa esta semana, el más largo desde que hay registros en La Palma. Aún le superan las dos primeras erupciones con duración conocida: la de Tehuya, en 1585, se prolongó 84 días; y la de Tigalate, en 1646, 82 días. Por desgracia, todo indica que el próximo domingo se igualará el récord.Si la evolución de un volcán resulta siempre impredecible, el de Cumbre Vieja nos ha dado ya todas las muestras imaginables para confirmar esta máxima. Ha atravesado ciclos en los que parecía perder fuerza para enseguida volver a reactivarse, minando así las esperanzas de los palmeros; ha sorprendido con un parón insólito, al detenerse durante horas tras una sola semana de erupción; y ha asombrado a los expertos al expular, al mismo tiempo, ceniza por una boca y lava por otra, como si hubiera dos volcanes en uno.«Estos procesos geológicos, tanto los terremotos como los volcanes e, incluso, las inundaciones son muy dinámicos, muy cambiantes. Podemos prevenir, pero no predecir. La predicción no existe», comenta Pablo Gabriel Silva, catedrático de Geomorfología y Riesgos Geológicos de la Universidad de Salamanca. «Y menos con el vulcanismo. El vulcanismo depende de muchos factores que hay en el interior de la Tierra y que se desconocen», añade.«El volcán igual continúa cinco meses que se para mañana», ilustra. Es más: no sólo hay incógnitas sobre lo que ocurre en las entrañas de la isla, sino que también está cambiando el suelo de La Palma, lo que acentúa la incertidumbre sobre por dónde caerá la lava y qué construcciones o cultivos seguirá destruyendo a su paso. Es lo que ocurrió, por ejemplo, con el cementerio de Las Manchas, que parecía haberse salvado hasta que la colada 10 se desbordó y acabó arrasando el camposanto.«El volcán ha generado coladas que han cambiado la topografía. Se han rellenado los valles y han desaparecido los barrancos por los que podían discurrir las coladas», indica Silva. Las nuevas coladas, explica, bajan al mar sobre las anteriores, a veces a unos 20 metros de altura sobre el terreno original. «A la mínima que hay un obstáculo, se produce un desbordamiento y se genera otra colada». Por eso, cada vez es más difícil prever por dónde irá el magma. «Cualquier mapa de peligrosidad que existiera antes de la erupción está obsoleto, no nos podemos fiar de él».Una peculiaridad del actual volcán es que ha generado numerosas plumas de ceniza y priroclastos y, a la vez, ha expulsado inmensas cantidades de lava. En contraste, las dos anteriores erupciones en La Palma se decantaron mayoritariamente por un tipo de actividad u otra: el Teneguía, en 1971, fue más explosivo, con pocas coladas, mientras que el de San Juan, en 1949, expulsó mucha lava, pero poco material sólido, sin dejar apenas edificio volcánico.La nueva erupción, sin embargo, ha combinado lo peor de las dos anteriores: «En la misma grieta está saliendo magma, se supone que del mismo reservorio, la misma cámara, pero por unas zonas está saliendo con actividad explosiva y por las bocas de más abajo está saliendo con actividad efusiva, que es la que alimenta las coladas, detalla Silva. «Es casi la primera vez que se ve eso».También causó confusión la extraña pausa de siete horas que se tomó el volcán el 27 de septiembre. «Creó un desconcierto enorme, porque era muy pronto. Representaba el escenario peor de todos los posibles: que se produjese una reapertura o una reactivación del proceso volcánico, pero no en este volcán, sino en otro nuevo, que podría estar a kilómetros de distancia; era lo peor que podía pasar», recuerda Vicente Soler, representante del CSIC en el Comité Científico Asesor del Pevolca.«Por fortuna, no fue así», continúa este experto, pero el caso ilustra a la perfección que «nos movemos en un ambiente de hipótesis permanente». En contraste con las rocas y gases que expulsa el volcán, que pueden analizarse al detalle, «los procesos del interior de la Tierra no son directamente accesibles, de ninguna de las maneras», expone Soler.«Cuando hablamos de las medidas de superficie, se tiene gran precisión, hay todo tipo de instrumentación. Cuando hablamos de los procesos en profundidad, auscultamos indirectamente con la sísmica, las ondas sísmicas que atraviesan el subsuelo, y la deformación que se produce por el empuje magmático», detalla Soler. «Pero poco más es lo que se puede decir. La dificultad de hablar de estas cosas es grande y la capacidad de equivocarnos, también», añade.¿Estamos únicamente a expensas de lo que quiera el volcán? «A expensas de lo que el volcán quiera y a expensas del lento progreso de las ciencias del interior de la Tierra», responde Soler, quien concluye con la siguiente comparación: «Los astrofísicos, como analizan la luz... pues se sabe más de una estrella en los confines de la galaxia que del interior de nuestro propio planeta».")
        ,l).sort_values( axis=0,ascending=False).to_csv('similitud.txt')
    
    #Cogemos dos noticias
    article_1 = open("./ElMundo/salud/ElMundo_salud_2021-12-27_46.txt", 'r', encoding="utf-8")
    article_2 = open("./ElMundo/salud/ElMundo_salud_2021-12-27_47.txt", 'r', encoding="utf-8")
    docA = article_1.read()
    docB = article_2.read()
    article_1.close()
    article_2.close()
    
    #Obtenemos las etiquetas de las noticias
    etiquetas_doc_1 = obtener_etiquetas(docA)
    etiquetas_doc_2 = obtener_etiquetas(docB)
    #calculamos el sorensen dice
    calculo_sorensen_dice(etiquetas_doc_1, etiquetas_doc_2)
    pathToNoticias(m, 'Un grupo de científicos chinos, canadienses y británicos publicaron en la revista Science un artículo sobre un huevo de dinosaurio fosilizado hallado en la provincia central china de Jiangxi que contiene un embrión de 27 centímetros, recoge hoy la cadena estatal CCTV.El huevo fosilizado, de una forma alargada y de 17 centímetros de longitud, tiene alrededor de 70 millones de años y contiene uno de los fósiles de embrión de dinosaurio mejor conservados, según CCTV.El embrión pertenece a la suborden de los terópodos, del período Triásico, y se halla acurrucado dentro del huevo en una postura, con la cabeza entre las patas, que hasta ahora solo se había detectado en dinosaurios aviares, según el estudio."Esta postura es muy similar a la de las aves actuales cuando sus huevos están a punto de eclosionar y pensamos que los dinosaurios habrían salido de sus huevos de una forma similar a la de las aves de nuestra era", apuntó una de los científicos, Fion Ma Wai-sum, al periódico hongkonés South China Morning Post.Ma explicó al diario que el fósil es una prueba más de que las aves actuales proceden de los dinosaurios terópodos.Según Ma, el embrión tenía unos 17 días de vida y su huevo habría eclosionado a los 21 días.La zona en la que se encontró el huevo, en el término municipal de Ganzhou, destaca por los numerosos fósiles, tanto de dinosaurios como de huevos y plantas, que alberga.El huevo se compró en el año 2000 y pasó 10 años almacenado hasta que se comenzó a investigarlo con motivo de la fundación del Museo de Historia Natural de la Piedra en la ciudad suroriental china de Xiamen, de cuya colección forma parte.Este equipo de científicos ha pasado tres años estudiando el fósil y, según Ma, los investigadores continuarán los análisis, que incluirán técnicas de rayos X para saber más acerca de la anatomía del embrión y de otras partes de su cuerpo cubiertas por piedra.')
    
main()