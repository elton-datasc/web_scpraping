from utils import Scrap, get_info
from time import sleep
from pathlib import Path
from handler import logging
import time

def get_num_pages():
        #verificar separar as ações em mais funções
        #cabe um try na parte do nome
        start = time.time()
        categoria = int(input('Escolha categoria para a extração :\n 25 - funko pop\n 23 - presentes criativos \n 33 - colecionáveis\n 133 - camisetas , 171 - almofadas \n 159 - canecas criativas, 161 - luminárias :'))
        num_pag = int(input('Qtde de páginas da extração: '))
        nome_categoria = {25:'funko', 23:'presentes',33: 'colecionáveis', 133: 'camisetas', 171: 'almofadas', 159: 'canecas', 161:'luminárias'}
        nome = None
        if categoria in nome_categoria.keys():
                nome = nome_categoria[categoria]
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
                logging.info(f'Iniciando a página {page}')
                scrap = Scrap()
                merged_df = scrap.merge_scrapes(url)
                merged_df.to_csv(f'produtos_{nome}/produtos_pag_{page}.csv', index=False, header=False, sep=';')
                logging.info(f'Finalizando a página {page}')
                pages.append(page)
                page += 1
        logging.info(f'Extração de {pages[0]} página(s) feita(s) com sucesso!')
        end = time.time()
        logging.info(f'Tempo de execução: {end - start} segundos')


if __name__ == "__main__":
    get_num_pages()



