import requests

headers = {
    'Referer': 'https://www.toyshow.com.br/loja/catalogo.php?loja=460977&categoria=25&pg=1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'loja': '460977',
    'categoria': '25',
    'pg': '1',
}

response = requests.get('https://www.toyshow.com.br/loja/catalogo.php', params=params, headers=headers)