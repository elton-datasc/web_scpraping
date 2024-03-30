import requests
from bs4 import BeautifulSoup as bs 
import pandas as pd

#classes

def getPage(url):
    html = requests.get(url)
    return bs(html.content,features="lxml")

def scrapeNames(url):
    soup = getPage(url)
    desc = []
    for item in soup.select('li h2'):
        desc.append(item.text)
    df_names = pd.DataFrame(desc, columns=['product_name'])
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    return df_names

def scrapePrices(url):
    soup = getPage(url)
    prices = []
    for price in soup.select('.product-price .price'):
        prices.append(price.text[6:])
    df_prices = pd.DataFrame(prices, columns=['prices'])
    return df_prices

def scrapePromoPrices(url):
    soup = getPage(url)
    promo_prices = []
    for price in soup.select('.price-off'):
        promo_prices.append(price.text.strip().split(' ')[1])
    df_promo_prices = pd.DataFrame(promo_prices, columns=['promo_prices'])
    return df_promo_prices

def scrapeSpotPrice(url):
    soup = getPage(url)
    cash_price = []
    for cash_prices in soup.select('.product-payment'):
        cash_price.append(cash_prices.text.strip().replace('\n', '')[22:28])
    df_cash_price = pd.DataFrame(cash_price, columns=['spot_price'])
    return df_cash_price

def mergeScrapes(url):
    merged_df = pd.concat([scrapeNames(url), scrapePrices(url), scrapePromoPrices(url), scrapeSpotPrice(url)], axis=1)
    return merged_df



url = 'https://www.toyshow.com.br/pop-funko'

df = mergeScrapes(url)
print(df)

