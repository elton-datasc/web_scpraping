from utils import Scrap

def get_data():
    scrap = Scrap()
    url = "https://www.toyshow.com.br/loja/catalogo.php?loja=460977&categoria=25&pg=1"
    merged_df = scrap.merge_scrapes(url)
    print(merged_df)

if __name__ == "__main__":
    get_data()