from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

html = urlopen('https://www.toyshow.com.br/pop-funko')

bs = BeautifulSoup(html, 'html.parser')

categoria = bs.find('li', {'class':'product-item'})
#nome = bs.find('ul', {'class':'product-tabs-list inline-block'}).find('li',{'class':'product-name'})

lista = categoria.text.strip().split('\n')
lista_filtrada = list(filter(lambda x: x.strip() != '', lista))

produto = {
    'nome': lista_filtrada[1],
    'preco_antes': lista_filtrada[2][3:],
    'preco_agora': lista_filtrada[4],
    'preco_avista': lista_filtrada[6],
    'pag_cartao': (lista_filtrada[10] + " " + lista_filtrada[12] + " " + lista_filtrada[13] + lista_filtrada[14]).strip()
}

print(produto)

#df = pd.DataFrame([produto])

#print(df)
