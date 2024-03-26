from utils import Scrap
from time import sleep
from pathlib import Path
from handler import logging
import time

def get_num_pages():
        start = time.time()
        num_pag = int(input('Qtde de páginas da extração: '))
        dir_path = Path("produtos_funko")
        dir_path.mkdir(exist_ok=True)
        page = 1
        while page <= num_pag:
                pages = []
                url = f'https://httpbin.org/status/404'
                logging.info(f'Iniciando a página {page}')
                scrap = Scrap()
                merged_df = scrap.merge_scrapes(url)
                merged_df.to_csv(f'produtos_funko/produtos_pag_{page}.csv', index=False, header=False, sep=';')
                logging.info(f'Finalizando a página {page}')
                page += 1
                pages.append(page)
        logging.info(f'Extração de {len(pages)} página(s) feita(s) com sucesso!')
        end = time.time()
        logging.info(f'Tempo de execução: {end - start} segundos')


if __name__ == "__main__":
    get_num_pages()



