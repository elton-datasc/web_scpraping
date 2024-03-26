import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from requests.exceptions import HTTPError
import logging
import os
import sys

class Scrap:
    def __init__(self):
        self.session = requests.Session()
        logging.basicConfig(level=logging.INFO)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)

    def get_page(self, url):
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return bs(response.content, features="lxml")
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            raise sys.exit(logging.error(f"HTTP error occurred: {http_err}"))
        except requests.exceptions.RequestException as err:
            logging.error(f"Request error occurred: {err}")
            raise sys.exit(1)
        except Exception as err:
            logging.error(f"Unexpected error occurred: {err}")
            raise sys.exit(1)


    def scrape_names(self, url):
        soup = self.get_page(url)
        if soup:
            return pd.DataFrame([item.text for item in soup.select('li h2')], columns=['product_name'])
        return pd.DataFrame()

    def scrape_prices(self, url):
        soup = self.get_page(url)
        if soup:
            return pd.DataFrame([price.text[6:] for price in soup.select('.product-price .price')], columns=['prices'])
        return pd.DataFrame()

    def scrape_promo_prices(self, url):
        soup = self.get_page(url)
        if soup:
            return pd.DataFrame([price.text.strip().split(' ')[1] for price in soup.select('.price-off')], columns=['promo_prices'])
        return pd.DataFrame()

    def scrape_spot_price(self, url):
        soup = self.get_page(url)
        if soup:
            return pd.DataFrame([cash_prices.text.strip().replace('\n', '')[22:28] for cash_prices in soup.select('.product-payment')], columns=['spot_price'])
        return pd.DataFrame()

    def merge_scrapes(self, url):
        dfs = [self.scrape_names(url), self.scrape_prices(url), self.scrape_promo_prices(url), self.scrape_spot_price(url)]
        return pd.concat(dfs, axis=1)
    
    


