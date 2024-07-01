# Funcao Filter 

"""
No Filter  você precisa passar 2 argumentos a Função e lista de items 
para ele percorrer. 

Função  é o que desejo - tipo aumentar_tamanho ou diminuir_preco

exemplo da formula:
variavel = list(filter(função, variavel )
preco_produtos = list(filter(aplicar_aumento, preco_produtos)

"""

preco_produtos = [
    5000,
    9000,
    2000,
    15000,

]

def aplicar_aumento(preco):  # vai iterar #percorrer" a lista
    if preco > 3000: 
        return preco * 1.8
    else:
        return preco

preco_produtos = list(filter(aplicar_aumento, preco_produtos)) # Filter 
print(preco_produtos)