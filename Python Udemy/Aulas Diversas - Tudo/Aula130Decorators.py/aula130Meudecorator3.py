# Cronometrar o tempo 

"""
importando tempo com 

import time 

e criar uma variavel tempo_inicial = time.time ()
ele pega exatamente o horario que ele executou

e depois da Funcao criar uma outra com 

tempo_final = time.time () tempo depois da duração


"""

import requests

import time

# Função decorator calcular tempo
def calcular_tempo (funcao):  # criando um def com variavel
    def wrapper ():            # criando um wrapper 
        tempo_inicial = time.time () # variavel com time inicial
        funcao()  # executando a função e variavel
        tempo_final = time.time () # variavel com time final 
        print(f"Duração foi de {tempo_final - tempo_inicial} segundos") # chamando o print com o calculo 
    return wrapper   # por fim returnar o wrapper


@calcular_tempo
def pegar_cotacao_dolar():
    link =  f"https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao["USDBRL"]["bid"])