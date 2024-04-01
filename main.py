from utils import Data
import logging

if __name__ == "__main__":
    try:
        nome, num_pag, start = Data.get_user_input()
        if nome and num_pag:
            Data.create_output_directory(nome)
            Data.extract_data(nome, num_pag)
            Data.log_execution_time(start)
    except ValueError as err:
        logging.error(f'Digite uma categoria válida: {err}')



