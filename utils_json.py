import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import logging
import sys
from logging.config import fileConfig
import os
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.environ['APP_PATH'])


fileConfig(f"{os.environ['APP_PATH']}/logging_config.ini")
logger = logging.getLogger()


def get_header():
    # cURL do bash
    headers = {
        'Referer': 'https://www.toyshow.com.br/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    return headers

class Scrap:
    def __init__(self):
        self.session = requests.Session()
        #logging.basicConfig(level=logging.INFO)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)

    def get_page(self, url):
        try:
            response = self.session.get(url,headers=get_header(), timeout=5)
            response.raise_for_status()
            return bs(response.content, 'html.parser')
        except requests.exceptions.HTTPError as http_err:
            raise sys.exit(logging.error(f"HTTP error occurred: {http_err}"))
        except requests.exceptions.RequestException as err:
            raise sys.exit(logging.error(f"Request error occurred: {err}"))
        except Exception as err:
            raise sys.exit(logging.error(f"Unexpected error occurred: {err}"))


    def scrap_json(self, url):
        soup = self.get_page(url)
        product_name = [item.text for item in soup.select('li h2')]
        prices = [price.text[6:] for price in soup.select('.product-price .price')]
        promo_prices = [price.text.strip().split(' ')[1] for price in soup.select('.price-off')]
        spot_price = [cash_prices.text.strip().replace('\n', '')[22:28] for cash_prices in soup.select('.product-payment')]

        products = {
            'product_name': product_name,
            'prices': prices,
            'promo_prices': promo_prices,
        }

        return pd.DataFrame(products)

    
    



# %%
