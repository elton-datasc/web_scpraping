import requests
from bs4 import BeautifulSoup as bs 
import pandas as pd

html = requests.get('https://www.toyshow.com.br/pop-funko')

soup = bs(html.content,features="lxml")

# Com CSS collectors
'''for item in soup.select_one('li h2'):
    print(item)'''

#df = pd.Series([produtos])

'''print(df[0][:1]),\
print(df[0][1:2])'''

#print(soup.select('li '))

'''price_element = soup.select_one('.product-price .price').text
#print(soup.select('div product-price'))
print(price_element)'''

produto = {
    'nome': soup.select_one('li h2').text,
    'preco_antes': soup.select_one('.product-price .price').text,
    'preco_agora': soup.select_one('.price-off').text.strip().split(' ')[1],
    'preco_avista': soup.select_one('.product-payment').text.strip()[24:30],
    'pag_cartao': soup.select_one('.txt-cadaparcelas').text.replace('\n', '').replace(' ', '').split(' ')[0][2:]
}

print(produto)

