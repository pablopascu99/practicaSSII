from bs4 import BeautifulSoup
import requests
import re

url_ciencia = 'https://www.20minutos.es/ciencia/'
url_tecnologia = 'https://www.20minutos.es/tecnologia/'
url_sanidad = 'https://www.20minutos.es/salud/'

listaURLs20Min = [url_sanidad, url_tecnologia, url_ciencia]

def getFieldsFromPages (listaURLs):
    for link in range(len(listaURLs)):
        # Hacemos la solicitud de requests a la url
        page = requests.get(listaURLs[link])
        # Accedemos al contenido especifico de la página
        soup = BeautifulSoup(page.text, 'html.parser')
        noticias = soup.find_all('div', {'class': 'media-content'})
        # primera prueba: print(noticias)
        hrefs = []
        for enlace in noticias:
            noticia = enlace.find('a')['href']
            hrefs.append(noticia)
        # segunda prueba : print(hrefs)
        cont = 1
        for page in range(len(hrefs)):
            noticia = requests.get(hrefs[page])    
            soupNoticia = BeautifulSoup(noticia.text, 'html.parser')
            contenido = soupNoticia.find_all('main', {'class':'page-article'})
            # tercera prueba: print(contenido)
            try: 
                estructuraTitulo = soupNoticia.find('h1', {'class':'article-title'})
                titulo = estructuraTitulo.text
            except: 
                titulo = "Noticia sin titulo"
            # cuarta prueba: print(titulo)
            try: 
                estructuraEntradilla = soupNoticia.find('div', {'id':'m35-34-36'})
                entradilla = estructuraEntradilla.text
            except: 
                entradilla = "Noticia sin entradilla"
           # quinta prueba:  print(entradilla)
            try: 
                estructuraTexto = soupNoticia.find('div', {'class':'article-text'})
                childrenTexto = estructuraTexto.findChildren("p", recursive=False)
                for childTexto in childrenTexto:
                    texto = childTexto.text
            except: 
                texto = "Noticia sin texto"
            # sexta prueba: print(texto)     
            try: 
                estructuraEtiquetas = soupNoticia.find('li', {'class' : 'tag'})
                etiquetas = estructuraEtiquetas.text
                etiquetas_re = re.sub('\n\s+', '', etiquetas)
                tags = etiquetas_re + " | "
                #tags_f = re.sub('\s\n', '', tags)
            except: 
                tags = "Noticia sin etiquetas"     
            # septima prueba : print(tags)
            try:
                estructuraFecha = soupNoticia.find('span', {'class':'article-date'}).text
                regExDate1 = re.sub('\s-.*', "", estructuraFecha)
                fecha = re.sub('\.', "-", regExDate1)
            except: 
                fecha = "Noticia sin fecha"
            # octava prueba: print(fecha)
            
            noticia20Min = titulo + "\n######\n" + entradilla + "\n######\n" + texto + "\n######\n" + tags + "\n######\n" + fecha + "\n\n"
            print(noticia20Min)
noticias20Min = getFieldsFromPages(listaURLs20Min)