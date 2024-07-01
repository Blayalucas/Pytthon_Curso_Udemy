# importar biblioteca 

"""
Para importar uma biblioteca eu posso 
escrever a palavra import + nome da biblioteca 
"""

import math  # biblioteca Matematica

from math import sqrt # chamando  a raiz quadrada da biblioteca matematica

num = int(input("Digite um numero: "))
raiz = math.sqrt(num)  # criando a raiz de num
print(f" A raiz de {num} é {raiz}")

import random    # biblioteca de numero aleatório
num = random.randint (1,10)  # randint = numero aleatório inteiro
print(num)