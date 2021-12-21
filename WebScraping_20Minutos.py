from bs4 import BeautifulSoup
import requests
import re

#Creamos lista con las url que queremos
listaURLs20min = ['https://www.20minutos.es/ciencia/', 'https://www.20minutos.es/tecnologia/', 'https://www.20minutos.es/salud/']

#Claves del navegador web
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

#Creamos un fro que recorre las distintas urls del 20minutos
for link in range(len(listaURLs20min)):
    page = requests.get(listaURLs20min[link], headers=headers)

    print(page.status_code)
    soup = BeautifulSoup(page.text, 'html.parser')

    #Buscamos la etiqueta de media content debido
    #a que son las que contienen la url de las noticias
    noticias = soup.find_all('div', {'class': 'media-content'})

    #Creamos urls para almacenar las url obtenidas
    #despues mediante un for obtenemos dichas urls
    urls = []
    for url in noticias:
        noticia = url.find('a')['href']
        urls.append(noticia)

    #Mediante un for iteramos entre cada url de noticia
    for page in range(len(urls)):

        noticia = requests.get(urls[page], headers=headers)    
        soupNoticia = BeautifulSoup(noticia.text, 'html.parser')
        
        try:
            #Buscamos las etiquetas de clase "page-article" para obtener
            #la info que necesitamos
            contenido = soupNoticia.find_all('main', {'class':'page-article'})

            #Primero obtenemos el titulo de las noticias
            estructuraTitulo = soupNoticia.find('h1', {'class':'article-title'}).text
            print("Titulo: " + estructuraTitulo)

            #Cogeremos ahora el texto de los diferentes noticias
            #para ello filtraremos mas de cerca lo que necesitamos
            #posteriormente cogeremos los diferentes parrafos de las noticias
            estructuraTexto = soupNoticia.find('div', {'class':'article-text'}).text

            ####TERMINAR ESTO ABAJO LO DE LOS HIJOS
            estructuraEtiquetas = soupNoticia.find('div', {'class' : 'module module-related'})
            tags=""
            if estructuraEtiquetas is not None:
                try:
                    childrenEtiquetas = estructuraEtiquetas.findChildren("ul" , recursive=False)
                    for childEtiquetas in childrenEtiquetas:
                        tags = tags + childEtiquetas.text + "|"

                except: 
                    tags = "Noticia sin etiquetas"
            if estructuraEtiquetas is None:
                tags = "Noticia sin etiquetas"
            
            print(tags)

            #Cogemos la fecha de cada noticia
            estructuraDate = soupNoticia.find('span', {'class':'article-date'}).text
            regExDate1 = re.sub('\s-.*', "", estructuraDate)
            regExDate2 = re.sub('\.', "-", regExDate1)
            print("Fecha: " + regExDate2)

        except:
            contenido=""
