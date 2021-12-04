from bs4 import BeautifulSoup
import requests
import re

# URLs de la web ElPais
listaURLsElPais=['https://elpais.com/noticias/sanidad','https://elpais.com/noticias/tecnologia','https://elpais.com/noticias/ciencia']
# Claves del navegador web
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

for link in range(len(listaURLsElPais)):
    page = requests.get(listaURLsElPais[link], headers = headers)
    # Si el status_code nos da un 200 es que es el request se ha hecho bien y si nos da un 400 es que no existe
    print(page.status_code)
    soup = BeautifulSoup(page.text, 'html.parser')
    # Cogemos todas las etiquetas con clase c_t, que son las que nos interesan
    # porque tienen las url de cada noticia
    noticias = soup.find_all('h2', {'class': 'c_t' })
    # Guardamos todas las noticias con los campos: titulo, entradilla, 
    # fecha, texto y etiquetas
    allNoticas = []
    # Guardamos las url de las noticias
    pages = []
    for url in noticias:
        noticia= "https://elpais.com"+url.find('a')['href']
        
        pages.append(noticia)
    # Contador para identificar el numero de archivo creado
    cont=1
    for page in range(len(pages)):
        # Cogemos el cada noticia mediante su url
        noticia = requests.get(pages[page], headers = headers)
        soupNoticia = BeautifulSoup(noticia.text, 'html.parser')
        # Cogemos todas las etiquetas con clase a _g _g-lg _g-o, que son las que nos interesan
        # porque tienen los campos que queremos de cada noticia
        try:
            contenido = soupNoticia.find_all('article', {'class': 'a _g _g-lg _g-o' })
            noticiaCampos=[]
            # Cogemos la estructura que abarca el campo de texto
            estructuraTexto = soupNoticia.find('div', {'class': 'clearfix' })
            # Cogemos los parrafos hijos de la estructura de texto que conformaran
            # todo el texto que necesitamos
            childrenTexto = estructuraTexto.findChildren("p" , recursive=False)
            texto=""
            for childTexto in childrenTexto:
                texto = texto + childTexto.text
            # Cogemos las etiquetas hijas de la estructura de etiquetas que agruparan
            # todas las etiquetas que necesitamos
            estructuraEtiquetas = soupNoticia.find('ul', {'class': '_df _ls' })
            childrenEtiquetas = estructuraEtiquetas.findChildren("li" , recursive=False)
            tags=""
            for childEtiquetas in childrenEtiquetas:
                tags = tags + childEtiquetas.text + "|"
            # Hay dos estructuras posibles en las fechas por lo que tenemos que 
            # tener en cuenta ambos casos
            if soupNoticia.find("a", {"id": "article_date_p"}) is not None:
                # Guardamos la fecha
                fecha = soupNoticia.find('a', id="article_date_p").attrs['data-date']
                # Eliminamos la parte de la hora
                delTime = re.sub('T.*', "", fecha)
            if soupNoticia.find("a", {"id": "article_date_u"}) is not None:
                # Guardamos la fecha
                fecha = soupNoticia.find('a', id="article_date_u").attrs['data-date']
                # Eliminamos la parte de la hora
                delTime = re.sub('T.*', "", fecha)
            # Guardamos el titulo
            titulo = soupNoticia.find('h1', {'class': 'a_t'}).text
            # Guardamos la entradilla
            entradilla = soupNoticia.find('h2', {'class':'a_st'}).text

            # Todo el string que meteremos al archivo de texto
            noticiaElPais = titulo + "\n######\n" + entradilla + "\n######\n" + texto + "\n######\n" + tags + "\n######\n" + delTime
            delDir = re.sub('.*noticias/', "", listaURLsElPais[link])
            # Situamos y creamos los archivos de texto con los campos extraidos
            file = open("./ElPais/" + delDir + "/ElPais_" + delDir + "_" + delTime + "_" + str(cont) + ".txt", "w", encoding="utf-8")
            file.write(noticiaElPais)
            file.close()
            cont=cont+1
        except:
            contenido=""