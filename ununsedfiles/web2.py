from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page3.html')

bs = BeautifulSoup(html, 'html.parser')

'''for child in bs.find('table',{'id':'giftList'}).tr.next_siblings:
    print(child)'''

'''for i in bs.tr:
    print(i) '''

# as duas sintaxe funcionam 
print(bs.img.attrs.get('src'))
print(bs.img.attrs['src'])