import os 

# obtener los docs con la key concreta dentro del path X 
def indexacion_invertida_path (path, key):
    unique_terms = {term for doc in path for term in doc.split()}
    inverted_index = {}

    for i, doc in enumerate(path): # enumeramos cada documento desde 0 incrementando
        for term in doc.split(): # hacemos el split de los docs
            if term in inverted_index: # si el elemento ya tiene hecha la indexacion 
                inverted_index[term].add(i) # añadimos el id del doc al que pertenece
            else: inverted_index[term] = {i} # sino creamos una nueva key en el dic

    docs_list = inverted_index[key]
    print(docs_list)

# obtener los docs de los 3 docs de ejemplo con la key concreta
def indexacion_invertida_docs (docA, docB, docC, key):
    docs = [docA, docB, docC]
    unique_terms = {term for doc in docs for term in doc.split()}
    inverted_index = {}

    for i, doc in enumerate(docs): # enumeramos cada documento desde 0 incrementando
        for term in doc.split(): # hacemos el split de los docs
            if term in inverted_index: # si el elemento ya tiene hecha la indexacion 
                inverted_index[term].add(i) # añadimos el id del doc al que pertenece
            else: inverted_index[term] = {i} # sino creamos una nueva key en el dic

    docs_list = inverted_index[key]
    print(docs_list)

# obtenemos todos los files del path
data_ElMundo_salud = os.path.join(os.getcwd(), 'ElMundo\salud')

data = []
for root, folders, files in os.walk(data_ElMundo_salud):
    for file in files:
        path = os.path.join(root, file)
        with open(path, 'r', encoding="utf-8") as info:
            data.append(info.read())


# obtenemos 3 files de ejemplo del path
article_1 = open("./ElMundo/salud/ElMundo_salud_2021-12-07_1.txt", 'r', encoding="utf-8")
article_2 = open("./ElMundo/salud/ElMundo_salud_2021-12-02_36.txt", 'r', encoding="utf-8")
article_3 = open("./ElMundo/salud/ElMundo_salud_2021-12-07_2.txt", 'r', encoding="utf-8")

docA = article_1.read()
docB = article_2.read()
docC = article_3.read()

article_1.close()
article_2.close()
article_3.close()

# llamamos a las funciones y probamos. 1. docs con la palabra Omicron en todos los files del path
# y que docs de los 3 docs con la palabra Omicron
indexacion_invertida_path(data, 'Ómicron')
indexacion_invertida_docs(docA, docB, docC, 'Ómicron')