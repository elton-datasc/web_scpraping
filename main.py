from utils import Scrap, num_total_pages
from pathlib import Path
from logging.config import fileConfig
import time
from dotenv import load_dotenv
import logging
import os
import sys

load_dotenv()

sys.path.append(os.environ['APP_PATH'])

fileConfig(f"{os.environ['APP_PATH']}/logging_config.ini")
logger = logging.getLogger()

def get_num_pages():
        scrap = Scrap()
        #verificar separar as ações em mais funções
        #cabe um try na parte do nome
        start = time.time()
        nome_categoria = {25:'funko', 23:'presentes',33: 'colecionáveis', 133: 'camisetas', 171: 'almofadas', 159: 'canecas', 161:'luminárias'}
        categoria = int(input('Escolha categoria para a extração  :\n  \n 025 - funko pop\n 023 - presentes criativos \n 033 - colecionáveis\n 133 - camisetas \n 171 - almofadas \n 159 - canecas criativas\n 161 - luminárias \n  \nCategoria :'))
        if categoria in nome_categoria.keys():
                nome = nome_categoria[categoria]
        else:
                raise sys.exit(logging.error(f"Insira uma categoria válida!'"))   
        total_pages = num_total_pages(categoria)
        num_pag = int(input(f'A categoria {categoria} possui {total_pages} páginas.\nQuantas páginas farão parte da extração? '))
        nome = None 
        if nome is None:
                logging.error('Insira uma categoria válida!')
                print(nome_categoria.keys())
                return
        dir_path = Path(f"produtos_{nome}")
        dir_path.mkdir(exist_ok=True)
        page =1
        while page <= num_pag:
                pages = []
                url = f'https://www.toyshow.com.br/loja/catalogo.php?loja=460977&categoria={categoria}&pg={page}'
                logger.info(f'Iniciando a página {page}')
                merged_df = scrap.merge_scrapes(url)
                merged_df.to_csv(f'produtos_{nome}/produtos_pag_{page}.csv', index=False, header=False, sep=';')
                logger.info(f'Finalizando a página {page}')
                pages.append(page)
                page += 1
        logger.info(f'Extração de {pages[0]} página(s) feita(s) com sucesso!')
        end = time.time()
        logger.info(f'Tempo de execução: {end - start} segundos')


if __name__ == "__main__":
    try:
        get_num_pages()

    except ValueError as err:
        print(f'Digite uma categoria válida: {err}')



