from bs4 import BeautifulSoup
import requests
import pandas as pd
# URL de la web
url = 'https://elpais.com/noticias/sanidad/'
# Claves del navegador web
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
page = requests.get(url, headers = headers)
# Si el status_code nos da un 200 es que es el request se ha hecho bien y si nos da un 400 es que no existe
print(page.status_code)
soup = BeautifulSoup(page.text, 'html.parser')
noticias = soup.find_all('h2', {'class': 'c_t' })
allNoticas = []
pages = []
for url in noticias:
    url = {
        'noticia' : "https://elpais.com"+url.find('a')['href']
    }
    pages.append(url)

df = pd.DataFrame(pages)

for page in range(len(df.index)):
    noticia = requests.get(df.at[page,'noticia'], headers = headers)
    soupNoticia = BeautifulSoup(noticia.text, 'html.parser')
    contenido = soupNoticia.find_all('article', {'class': 'a _g _g-lg _g-o' })
    for i in contenido:
        estructuraTexto = soupNoticia.find('div', {'class': 'clearfix' })
        childrenTexto = estructuraTexto.findChildren("p" , recursive=False)
        texto=""
        for childTexto in childrenTexto:
            texto = texto + childTexto.text
        estructuraEtiquetas = soupNoticia.find('ul', {'class': '_df _ls' })
        childrenEtiquetas = estructuraEtiquetas.findChildren("li" , recursive=False)
        tags=""
        for childEtiquetas in childrenEtiquetas:
            tags = tags + childEtiquetas.text + "|"
        #La fecha esta en formato ISO
        if i.find("a", {"id": "article_date_p"}) is not None:
            fecha = i.find('a', id="article_date_p").attrs['data-date']
        if i.find("a", {"id": "article_date_u"}) is not None:
            fecha = i.find('a', id="article_date_u").attrs['data-date']
        componentes = {
            'titulo' : i.find('h1', {'class': 'a_t'}).text,
            'entradilla' : i.find('h2', {'class':'a_st'}).text,
            'texto' : texto,
            'etiquetas' : tags,
            'fecha' : fecha,
        }
        allNoticas.append(componentes)
dfNoticias = pd.DataFrame(allNoticas)
print(dfNoticias)