import requests
from handler import logging

#categorias : 25 funko pop, 23 presentes criativos, 33 colecionáveis, camisetas 133, almofadas 171, canecas criativas 159,luminárias 161 ]

def get_header():

    headers = {
        'Referer': 'https://www.toyshow.com.br/loja/catalogo.php?loja=460977&categoria=25&pg=1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    return headers

def get_params():
    categoria = input('insira a categoria:')
    pg = input('insira a páginas:')
    
    params = {
        'loja': '460977',
        'categoria': categoria,
        'pg': pg }
    return params

#print(get_header())

#print(get_params())

#print(categoria, pagina)

response = requests.get('https://www.toyshow.com.br/loja/catalogo.php', params=get_params(), headers=get_header(), timeout= 5)

logging.info(response)