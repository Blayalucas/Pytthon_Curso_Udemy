# Criando meu proprio Decorador 

"""
Para eu criar meu proprio decorator 
tenho que fazer uma função dentro de função

def calcular_tempo ():  
    def wrapper ():             
"""

"""
criar um decorator calcular_tempo 

Que diz quanto tempo aquela função demora para rodar

@calcular_tempo

e recebe outra função dentro de uma def, ou seja def dentro de def
chamada wrapper

Wrapper faz executar a funcao e a variavel do DEF

"""

import requests

# Função decorator calcular tempo
def calcular_tempo (funcao):  # criando um def com variavel
    def wrapper ():            # criando um wrapper 
        print("Vou pegar a cotação") # dando uma ordem - para o DEF calcular
        funcao()  # executando a função e variavel
        print(" Peguei a cotação do dolar")
    return wrapper   # por fim returnar o wrapper


@calcular_tempo
def pegar_cotacao_dolar():
    link =  f"https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao["USDBRL"]["bid"])


pegar_cotacao_dolar()