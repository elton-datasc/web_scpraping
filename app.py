import streamlit as st
from utils import Data
import logging
import time


start = time.time()
# Configuração do logger
logging.basicConfig(level=logging.INFO)

def main():
    st.title("Extração de preços de site")
    
    # Supondo que você tenha uma lista de categorias disponíveis
    categorias = [' ','025 - funko pop' ,'023 - presentes criativos', '033 - colecionáveis' , '133 - camisetas' ,'171 - almofadas', '159 - canecas criativas','161 - luminárias']

    # Solicitação de entrada do usuário usando um menu de seleção
    nome = st.selectbox("Escolha uma categoria:", categorias, index=None,placeholder='Categoria do produto')
    num_pag = st.number_input("Digite o número de páginas:", min_value=1, value=1)  
    
    if st.button("Extrair Dados"):
        if nome and num_pag:
            try:
                with st.status("Downloading data...", expanded=True) as status:
                    Data.create_output_directory(nome)
                    st.write("Searching for data...")
                    time.sleep(2)
                    st.write("Found URL.")
                    Data.extract_data(nome, num_pag)
                    time.sleep(1)
                    st.write("Downloading data...")
                    Data.log_execution_time(start)
                    time.sleep(1)
                    status.update(label="Download complete!", state="complete", expanded=False)
                    time.sleep(1)
                st.success("Dados extraídos com sucesso!")
            except ValueError as err:
                st.error(f'Digite uma categoria válida: {err}')
                logging.error(f'Digite uma categoria válida: {err}')
        else:
            st.error("Por favor, preencha todos os campos.")

if __name__ == "__main__":
    main()
