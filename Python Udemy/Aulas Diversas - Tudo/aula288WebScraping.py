# web Scraping 

"""
Raspagem de Dados ou Web Scraping é um método automatizado de extração de dados de sites., 
ou seja, vai buscar dados na internet e reverter esses dados 

usando o bs4 BeautifullSoup
    
"""
# 1 Passo - importar a biblioteca requests com bs4 e BeautifulSoup

import requests

from bs4 import BeautifulSoup

# 2 Passo: instanciar uma URL 

url = 'https://www.youtube.com/'

# 3 Passo: Criar uma get leitura 
response = requests.get(url)

# 4 Passo : Criar um " HTML" Puro, ou seja codigo puro 

raw_html = response.text

# 5 passo: Fazer a conversao do HTML
parsed_html = BeautifulSoup(raw_html, 'html.parser' )


# 6 Print 
print(parsed_html)


