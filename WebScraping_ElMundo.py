# imports 
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Cogemos las urls de la web El Mundo: Sanidad, tecnologia y ciencia
url_sanidad = 'https://www.elmundo.es/ciencia-y-salud/salud.html'
url_tecnologia = 'https://www.elmundo.es/tecnologia.html'
url_ciencia = 'https://www.elmundo.es/ciencia-y-salud/ciencia.html'

# Creamos una lista con las urls
listaURLsElMundo = [url_sanidad, url_tecnologia, url_ciencia]

# creamos una funcion para hacer el web scraping de los contenidos de cada url
def getFieldsFromPages (listaURLs):
    for link in range(len(listaURLs)):
        # Hacemos la solicitud de requests a la url
        page = requests.get(listaURLs[link])
        # Accedemos al contenido especifico de la página
        soup = BeautifulSoup(page.text, 'html.parser')
        # Buscamos todos los container a que tengan esa clase, que es la que guarda los href de cada noticia
        containers = soup.find_all('div', {'class':'ue-l-cover-grid__unit ue-l-cover-grid__unit--no-grow'})
        # Lista para almacenar los enlaces
        hrefs = []
        # obtenemos ya una lista con todos los hrefs de cada articulo
        for enlace in containers:
            noticia = enlace.find('a')['href']
            hrefs.append(noticia)
        # Contador para identificar el numero de archivo creado
        cont = 1
        # usamos la lista con los href anteriores para hacer el web scraping de los campos de cada noticia
        for href in range(len(hrefs)):
            # Pillamos cada noticia mediante su href individual
            noticia = requests.get(hrefs[href])
            # Accedemos al contenido especifico de cada noticia
            soupNoticia = BeautifulSoup(noticia.text, 'html.parser')
            # cogemos el container principal que es el tiene todos los fields que nos interesan
            fields = soup.find_all('article', {'class' : 'ue-c-article has-image'})
            # Lista para almacenar los enlaces
            noticias = []
            # miramos si la noticia es premium, en caso de que la sea no podremos coger los campos
            premium = soupNoticia.find('div', {'class':'ue-c-article__premium-tag'})
            if premium is None: 
                # Cogemos el titulo
                estructuraTitulo = soupNoticia.find('h1', {'class': 'ue-c-article__headline js-headline'})
                if estructuraTitulo is not None:  
                   titulo = estructuraTitulo.text
                else: 
                    titulo = "Noticia sin titulo"
                # Cogemos la entradilla
                estructuraEntradilla = soupNoticia.find('p', {'class':'ue-c-article__standfirst'})
                if estructuraEntradilla is not None: 
                    entradilla = estructuraEntradilla.text
                else: 
                    entradilla = "Noticia sin entradilla"
                # cogemos el field para coger el texto
                estructuraTexto = soupNoticia.find('div', {'class': 'ue-l-article__body ue-c-article__body'})
                if estructuraTexto is not None: 
                    # Cogemos los p de la estructura de texto que conformaran todo el texto que necesitamos
                    childrenTexto = estructuraTexto.findChildren("p" , recursive=False)
                    texto=""
                    for childTexto in childrenTexto:
                        texto = texto + childTexto.text
                        texto = re.sub('#',' ', texto)
                else: 
                    texto = "Noticia premium, sin texto"
                # Cogemos las etiquetas
                tags = " "
                if soupNoticia.find('ul', {'class' : 'ue-c-article__tags'}) is not None:
                    estructuraEtiquetas = soupNoticia.find('ul', {'class' : 'ue-c-article__tags'})
                    try:
                        childrenEtiquetas = estructuraEtiquetas.findChildren("li" , recursive=False)
                        for childEtiquetas in childrenEtiquetas:
                            tags = tags + childEtiquetas.text + " | "
                    except: 
                        tags = "Noticia sin etiquetas"
                if soupNoticia.find('ul', {'class' : 'ue-c-article__tags'}) is None:
                    tags = "Noticia sin etiquetas"
                if tags == " ":
                    tags = "Noticia sin etiquetas"
                # Cogemos las fechas
                containerFecha = str(soupNoticia.find('div', {'class':'ue-c-article__publishdate'}))
                delTime = re.sub('.+datetime="|T[.\s\S\n]+',"", containerFecha)
            if estructuraEtiquetas is None and estructuraTitulo is None and estructuraTexto is None and estructuraEntradilla is None:
                return 
            else: 
                # Todo el string que meteremos al archivo de texto
                noticiaElMundo = titulo + "\n######\n" + entradilla + "\n######\n" + texto + "\n######\n" + tags + "\n######\n" + delTime + "\n\n"
                delDir_v1 = re.sub('.*\/',"", listaURLsElMundo[link])
                delDir = re.sub('.html', "", delDir_v1)
                file = open("./ElMundo/" + delDir + "/ElMundo_" + delDir + "_" + delTime + "_" + str(cont) + ".txt", "w", encoding="utf-8")
                file.write(noticiaElMundo)
                file.close()
                cont=cont+1
                #print(noticiaElMundo)

# llamamos a la funcion con nuestra lista de enlaces creadas
noticiasElMundo = getFieldsFromPages(listaURLsElMundo)