import requests
from bs4 import BeautifulSoup as bs
from time import sleep


#page = 1
html = requests.get(f'https://www.toyshow.com.br/loja/catalogo.php?loja=460977&categoria=25')
soup = bs(html.content,features="lxml")
pages = soup.find('span',{'class':'page-last'}).find('a')
print(pages)
#num_pages = soup.find('span',{'class':'page-current page-link'}).text
#page += 1
#sleep(5)
#print(num_pages)
  