from bs4 import BeautifulSoup
import requests
import pandas
# URL de la web
url = 'https://elpais.com/noticias/sanidad/'
# Claves del navegador web
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
page = requests.get(url, headers = headers)
# Si el status_code nos da un 200 es que es el request se ha hecho bien y si nos da un 400 es que no existe
print(page.status_code)
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.title.text)
noticias = soup.find_all('h2', {'class': 'c_t' })
pages = []
for url in noticias:
    noticia = "https://elpais.com"+url.find('a')['href']
    pages.append(noticia)
print(pages)
for page in pages:
    noticia = requests.get(page, headers = headers)
    soupNoticia = BeautifulSoup(noticia.text, 'html.parser')
    print(soupNoticia.title.text)
    '''noticias = soup.find_all('h2', {'class': 'c_t' })
    pages = []
    for url in noticias:
        noticia = "https://elpais.com"+url.find('a')['href']
        pages.append(noticia)
    print(pages)'''