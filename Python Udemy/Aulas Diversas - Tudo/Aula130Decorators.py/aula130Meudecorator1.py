# Criando meu proprio Decorador 

"""
Aqui é esta buscando a cotação atual do dollar

OBS: todo decorator é uma função DEF lembrar disso SEMPRE



"""

import requests

def pegar_cotacao_dolar():
    link =  f"https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao["USDBRL"]["bid"])


pegar_cotacao_dolar()
