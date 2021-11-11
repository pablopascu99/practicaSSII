from bs4 import BeautifulSoup
import requests
import pandas

url="https://elpais.com/tecnologia/"
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
lista_urls = []
urls = soup.find_all('div', {'class': 'c c-d c--m-n'})

for i in urls:
    ElPais = {
        'url' : i.find('h2', {'class': 'c_t'}).text,
    }
    lista_urls.append(ElPais)
    
productosDataFrame = pandas.DataFrame(data=lista_urls)
fichero_txt = productosDataFrame.to_csv('./urls.txt', index = False)