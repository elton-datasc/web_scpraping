import requests
from bs4 import BeautifulSoup as bs 
import pandas as pd

html = requests.get('https://www.toyshow.com.br/pop-funko')

soup = bs(html.content,features="lxml")

# Com CSS collectors

#DF com o nome do produto
desc = []
for item in soup.select('li h2'):
    desc.append(item.text)

# Convertendo a lista em um DataFrame
df_names = pd.DataFrame(desc, columns=['product_name'])

# Ajustando as configurações para exibir todo o DataFrame
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Exibindo o DataFrame
#print(df_names)


# DF com o preços originais
prices = []
for price in soup.select('.product-price .price'):
    prices.append(price.text[6:])

df_prices = pd.DataFrame(prices, columns=['prices'])

#print(df_prices)

# df com preços da promoção

price_now = []
for price in soup.select('.price-off'):
    price_now.append(price.text.strip().split(' ')[1])

df_price_now = pd.DataFrame(price_now, columns=['promo_prices'])


# df com os preços à vista 
cash_price = []
for cash_prices in soup.select('.product-payment'):
    cash_price.append(cash_prices.text.strip().replace('\n', '')[22:28])

df_cash_price = pd.DataFrame(cash_price, columns=['spot_price'])


# df final
merged_df = pd.concat([df_names, df_prices, df_price_now, df_cash_price], axis=1)

print(merged_df)