# API get 

"""
API get = Fazer uma requisição para um site especifico, ou seja, 
pedi algo ao site.

Para fazer API basta entrar no site: https://docs.awesomeapi.com.br/


"""
import requests  # importando uma requisição

# criando um get  " get é um pedido " estou "pedindo" para o site.
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
print(requisicao)  # se der certo vai aparecer 200
# requisição json - json é um dicionario {}, ou seja a informação vai vim em forma de dicionario
print(requisicao.json())  

# criando uma variavel para o receber o json
dicionario_requisicao = requisicao.json()

# pedindo a cotação do Dollar com  Bid "bid é exatamento a cotação atual, no momento"
print(dicionario_requisicao["USDBRL"]["bid"])

